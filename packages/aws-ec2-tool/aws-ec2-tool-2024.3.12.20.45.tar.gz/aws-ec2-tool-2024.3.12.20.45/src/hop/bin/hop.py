""" hop.bin.hop:

    Command line entrypoints
"""

from hop import cli, util

LOGGER = util.get_logger(__name__)


@cli.options.optional_user
# @cli.options.command
@cli.options.script
@cli.options.profile
@cli.click.option("--list-only", "-l", is_flag=True, help="list instances")
@cli.click.option(
    "--ssm-prefix",
    "-s",
    help="default SSM prefix to use for key-search",
    default="/keypairs",
)
@cli.click.argument("command", nargs=-1)
@cli.click.argument("identifier", nargs=1, default=None)
@cli.click.command(
    # cls=cli.Group
)
def entry(
    identifier=None,
    ssm_prefix: str = "/",
    list_only: bool = False,
    script=None,
    command=[],
    **kwargs,
):  # noqa
    """
    Tool for SSH'ing in to EC2 with SSM-backed keys.

    Example usage:

        hop <instance_id>
        hop <reservation_id>
        hop <instance_name>
        hop <ip_address>
    """
    assert not (script and command)
    # raise Exception([args, kwargs])
    from hop import api

    env = api._get_handle(env=None, **kwargs)
    ssm_prefix = ssm_prefix[:-1] if ssm_prefix.endswith("/") else ssm_prefix
    env.ssm_keys_prefix = ssm_prefix
    if list_only:
        instances = env.filter_instances(**kwargs)
        print(instances)
    else:
        api.hop(
            identifier=identifier, env=env, script=script, command=command, **kwargs
        )
