""" hop.cli.options (boilerplate for click)

    Common CLI arguments for reuse
"""

import click

from ssm.cli.options import profile  # noqa

required_key = click.option(
    "--key",
    required=True,
    help="Key name to use",
)

optional_user = user = click.option(
    "--user",
    help="username (default will attempt auto-detect)",
    required=False,
    default="",
)
required_user = click.option(
    "--user", help="username to use", required=True, default=""
)

command = click.option(
    "--command",
    "-c",
    required=False,
    default="",
    help="Command to run (like bash -c)",
)
required_command = click.option(
    "--command",
    "-c",
    default="",
    help="Command to run (like bash -c)",
)

script = click.option("--script", "-s", help="Script to run", default="")

# optional_arn = click.option(
#     "--arn",
#     required=False,
#     default="",
#     help="ARN",
# )
# optional_role_name = click.option(
#     "--role-name",
#     required=False,
#     default="",
#     help="Role name",
# )
