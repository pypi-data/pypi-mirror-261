# Fetch secrets from AWS Secrets Manager similar to env-consul

## Usage
```shell
usage: secrets-env [-h] [-p PREFIX] [-m] [--stdin STDIN] [-e] [-u | -l] secret [secret ...]

Return one or more secrets by either name or pattern, using Unix style glob matching. When using glob style matches then all secret names that
match the pattern will be returned. When using stdin and specifying options per pattern the options will be applied to the first match whereas multiple secrets
supplied as positional args will have the options provided as commandline arguments applied to all of them.

positional arguments:
  secret

options:
  -h, --help            show this help message and exit
  -p PREFIX, --prefix PREFIX
                        Prepend a prefix to each value
  -m, --merge-keys      Merge all secrets into one object. Secrets that are simple strings will have the last segment of their name (characters following the last /) as they key.
  --stdin STDIN         Read secret options from stdin. See details below for more info.

                        When using stdin, a subset of arguments are taken as lowercase strings matching the long version of argument names and separated by a pipe. You don't actually have to use this argument to use stdin.
                        Technically just passing data on stdin is enough.
                        Example:

                        echo 'myvar | upper | prefix TF_VAR_;' | secrets-env -

                        This is the equivalent of passing -u -p TF_VAR_ myvar as commandline arguments. Note the ending '-'. Multiple secrets are supported, with each
                        one taking its own set of arguments and separated by a semi-colon.

  -e, --env             Format output as env vars for a shell to consume
  -u, --upper           Cast secret names to upper case. Does not apply to prefixes.
  -l, --lower           Cast secret names to lower case. Does not apply to prefixes.
```

## Examples

### Basic example
```shell
~  > secrets-env -m mmoon-test/1 mmoon-test/2
{
  "test1": "test1val",
  "test2": "test2val"
}
```

### Returning TF input variables
```shell
~  > secrets-env -m -e -p TF_VAR_  mmoon-test/1 mmoon-test/2
TF_VAR_test1=test1val
TF_VAR_test2=test2val
```

### Passing args on stdin
You can pass multiple secrets on stdin, each with their own flags for `--upper`, `--lower`, or `--prefix`. `--merge-keys` and `--env` are always set os commandline flags and will be ignored if set on stdin. Note the `-` delimiting the end of arg input. This tells secrets-env that commandline args have ended and to start reading from stdin.
```shell
echo '
mmoon-test/1 | upper | prefix MY_PREFIX_;
mmoon-test/2 | lower | prefix stay_lower_prefix_;
' | secrets-env -me -

MY_PREFIX_MMOON_TEST_1=test1val
stay_lower_prefix_test=test2val
```
