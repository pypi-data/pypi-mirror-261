#!/usr/bin/env python3
from argparse import Namespace
from base64 import b64decode
from fnmatch import fnmatch
from json import loads, JSONDecodeError
from re import compile
from typing import List, TYPE_CHECKING

from boto3 import client

if TYPE_CHECKING:
    from mypy_boto3_secretsmanager import SecretsManagerClient
else:
    SecretsManagerClient = object


ENV_NAME_RE = compile("[^a-zA-Z0-9_]")
SECRETS_MANAGER: SecretsManagerClient = client("secretsmanager")


def get_secret_list(
    patterns: List[str], client: SecretsManagerClient = SECRETS_MANAGER
) -> dict:
    """
    Generate a list of secrets, organized by the pattern that matched them. A dict containing
    the input patters as the key and a list of matched secret names as the value is returned
    """
    opts = {"MaxResults": 100}
    matches = {}
    secrets_list = []
    parsed_names = []

    # Get all of the secrets in the account
    while True:
        res = client.list_secrets(**opts)
        secrets_list += [x["Name"] for x in res["SecretList"]]
        if token := res.get("NextToken"):
            opts["NextToken"] = token
        else:
            break

    for pattern in patterns:
        # If it's just a name and not a glob match it and move on
        if "*" not in pattern and pattern in res:
            matches[pattern] = [pattern]
            parsed_names.append(pattern)
            continue
        # Get all secret names that match the current pattern
        matches[pattern] = [
            x for x in secrets_list if x not in parsed_names and fnmatch(x, pattern)
        ]
        # Append to the list of parsed names so each secret is only matched once
        parsed_names += [x for x in secrets_list if x in matches[pattern]]

    return matches


def make_secret_name(name: str, config: dict) -> str:
    if config["upper"]:
        name = name.upper()
    if config["lower"]:
        name = name.lower()
    if prefix := config.get("prefix"):
        name = f"{prefix}{name}"
    return name


def handle_secret(secret: dict) -> dict:
    vals = secret.get("SecretString", "SecretBinary")

    # Secret values could be in different formats depending on how they were stored. See the response
    # section of the boto3 docs for `get_secret_value()` for specifics:
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager/client/get_secret_value.html
    if isinstance(vals, bytes):
        vals = b64decode(vals).decode()

    try:
        vals = loads(vals)
    except (TypeError, JSONDecodeError):
        pass

    # If the value wasn't a JSON object then set the name to the name of the secret
    # itself since there will only be one value and no nested keys
    if not isinstance(vals, dict):
        vals = {secret["Name"]: vals}

    return vals


def get_secrets(
    args: Namespace | List[Namespace], client: SecretsManagerClient = SECRETS_MANAGER, env: bool = False
):
    """
    Retreive all of the scret values for the list provided by get_secrets_list()
    """
    configs = {}

    if not isinstance(args, list):
        args = [args]

    # These values would always be the same for all entries, regardless of
    # whether it was commandline args or stdin
    merge = args[0].merge_keys
    env = args[0].env

    # Create a config that allows us to match up patters to their original
    # commandline arguments and store the values from any matching secret names
    for arg in args:
        # Terminal garbage from reading stdin
        if len(arg.secret) == 1 and arg.secret[0] in ("-", ""):
            continue

        configs.update(
            {
                secret: {
                    "prefix": arg.prefix,
                    "upper": arg.upper,
                    "lower": arg.lower,
                    "values": {},
                }
                for secret in arg.secret
            }
        )

    patterns = list(configs.keys())

    secret_list = get_secret_list(patterns, client)

    # Take the patterns and their corresponding matched secret names and retrieve the values
    for pattern, matches in secret_list.items():
        if not matches:
            del configs[pattern]
            continue

        for match in matches:
            try:
                res = client.get_secret_value(SecretId=match)
            except client.exceptions.ResourceNotFoundException:
                res = {"Name": match, "SecretString": None}

            vals = handle_secret(res)

            # If the value wasn't a JSON object then set the name to the name of the secret
            # itself since there will only be one value and no nested keys
            if not isinstance(vals, dict):
                vals = {match: vals}

            # If --merge-keys wasn't set then we will retain the name of the secret as the key.
            # this means the user will have to handle parsing any items out of the secret itself.
            if not merge:
                name = make_secret_name(match, configs[pattern])
                configs[pattern]["values"][name] = vals
                continue
            # If we made it here then the secret is a JSON object and the values dict will contain
            # the keys inside of the secret. In the case of multiple secrets containing the same keys
            # the last one in wins the conflict
            for name, val in vals.items():
                name = make_secret_name(name, configs[pattern])
                configs[pattern]["values"][name] = val

    res = {}

    # Flatten all of the different values dicts. Just like when parsing the values from
    # multiple secrets with the same pattern above, the last key found will win in any conflicts
    for items in configs.values():
        res.update(items["values"])

    if env:
        output = ""
        for k, v in res.items():
            print(k)
            output += f"{ENV_NAME_RE.sub("_", k)}={v}\n"
        res = output

    return res
