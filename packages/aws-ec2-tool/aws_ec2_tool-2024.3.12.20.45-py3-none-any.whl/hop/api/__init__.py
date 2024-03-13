""" hop.api
"""

import shil
from ssm import util as ssm_util

from hop import util

from .environment import Environment

LOGGER = util.get_logger(__name__)
SSH_BASE_ARGS = (
    "-tt -o LogLevel=ERROR -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
)

CMD_T = (
    "ps -U `whoami` | grep ssh-agent "
    "| grep -v grep 1> /dev/null 2> /dev/null || eval $(ssh-agent -s) ; "
    "ssm get {secret_path} "
    "| ssh-add -q -t 30 - "
    "&& ssh {SSH_BASE_ARGS} {ssh_user}@{ssh_host} {ssh_command}"
)


def _get_handle(**kwargs):
    """ """
    profile = kwargs.pop("profile", None)
    env = (
        Environment.from_profile(profile)
        if ssm_util.is_string(profile)
        else kwargs.pop("env", None)
    )
    assert env
    env.logger.info("this environment will be used for retrieving secrets")
    return env


def resolve_user(user=None, env=None, instance=None):
    """ """
    if user:
        env.logger.debug(f"user override was passed in: {user}")
        return user
    if instance:
        instance_tags = util.tags_list_to_dict(instance.get("Tags", []))
        if instance_tags and "User" in instance_tags:
            user = instance_tags["User"]
            env.logger.debug(f"hint for `User` found in instance tags: {user}")
            return user
    return env.get_user_from_ami(instance["ImageId"])


def give_up(err="Giving up, could not figure out how to hop"):
    """ """
    LOGGER.critical(err)
    raise RuntimeError(err)


import inquirer


def hop(
    identifier=None,
    command=None,
    key=None,
    debug=False,
    env=None,
    aslib=False,
    user=None,
    **kwargs,
):
    """
    helper for intiating keyless connections to appservers
    """
    assert identifier
    # LOGGER.debug(f"dispatching hop for `{identifier}`..")
    # `command` is nargs=-1, a list, so convert it
    kwargs.update(
        secret_path=key, command=" ".join(command), user=user, env=env, aslib=aslib
    )
    if identifier.startswith("i-"):
        LOGGER.warning("detected instance id")
        kwargs.update(instance_id=identifier)
    elif identifier.startswith("r-"):
        LOGGER.warning("detected reservation id")
        kwargs.update(instance_id=identifier)
    # elif any([identifier.endswith(x) for x in ['.com', ".net", ".local", ".org"]]):
    #     LOGGER.debug("detected host name (fully qualified)")
    #     kwargs.update(dns=identifier)
    # elif identifier.startswith('10.'):
    #     LOGGER.debug("looks like a private IP, passing through")
    #     kwargs.update(dns=identifier)
    elif "." in identifier:
        LOGGER.critical("detected host with external DNS, or partial DNS?")
        return give_up(NotImplemented)
    # elif ',' in identifier:
    #     LOGGER.debug("detected tuple (hopefully of format 'env,stack')")
    #     assert env is None,'cannot pass tuple and --env'
    #     env, stack_name = identifier.split(',')
    #     env = Environment.from_name(env)
    #     LOGGER.debug("resolving stack")
    #     stack = env.stacks[stack_name]
    #     exports = stack.exports
    #     LOGGER.debug("checking stack exports for dns/ip value")
    #     dns = exports.get('PrivateDNS', exports.get('PrivateIP'))
    #     kwargs.update(dns=dns, env=env, stack_name=stack_name)
    else:
        return give_up(f"No strategies found for dispatching on `{identifier}`")

    return hop_partial(**kwargs)


def hop_partial(aslib, **kwargs):
    """ """
    LOGGER.debug(f"hop_partial: {locals()}")
    for secret_meta in find_secrets(aslib=aslib, **kwargs):
        # raise Exception(secret)
        context = kwargs.copy()
        context.update(**secret_meta)
        connection_succeeded = True
        LOGGER.critical(context)
        if not aslib:
            connection_succeeded = hop_connect(**context)
            output = False
        else:
            output = hop_connect(aslib=aslib, **context)
        if connection_succeeded and output:
            return output
        elif connection_succeeded:
            return LOGGER.debug("Exiting after successful connection")
        else:
            LOGGER.debug("Connection failed, trying next option")
    if aslib:
        msg = "failed"
        return msg
    else:
        return give_up()


def find_secrets(
    dns=None,
    instance_id=None,
    secret_path=None,
    ami_id=None,
    # secrets_env_name='default',
    env=None,
    user=None,
    aslib=None,
    **kwargs,
):
    """ """
    LOGGER.debug(f"find_secrets: {locals()}")
    if env:
        LOGGER.debug(
            (
                "environment hint `{}` was passed, cascading environment-search "
                "will be short-circuited"
            ).format(env)
        )
        envs = [Environment.from_name(env)] if isinstance(env, str) else [env]
    else:
        global DEFAULT_ENV_SEARCH_ORDER
        msg = "default environment search order: {}"
        LOGGER.debug(msg.format(DEFAULT_ENV_SEARCH_ORDER))
        this_search_order = DEFAULT_ENV_SEARCH_ORDER
        # this_search_order = (
        #     list(
        #         reversed(
        #             sorted(
        #                 DEFAULT_ENV_SEARCH_ORDER,
        #                 key=lambda x: text_util.longest_common_substring(x, dns),
        #             )
        #         )
        #     )
        #     if dns
        #     else DEFAULT_ENV_SEARCH_ORDER
        # )
        #
        # if this_search_order != DEFAULT_ENV_SEARCH_ORDER:
        #     msg = "search-order was changed to {} (longest-common-substring heuristic)"
        #     LOGGER.debug(msg.format(this_search_order))
        missing = []
        for env_name in this_search_order:
            try:
                Environment.from_name(env_name)
            except Exception as exc:
                LOGGER.debug(str(exc))
                err = "Could not load environment from name `{}`, profile missing?"
                LOGGER.critical(err.format(env_name))
                missing.append(env_name)
        this_search_order = [x for x in this_search_order if x not in missing]
        envs = [Environment.from_name(x) for x in this_search_order]
    if instance_id and not dns:
        LOGGER.debug(f"searching for environment with instance {instance_id}")
        for env in envs:
            ec2_metadata = env.get_ec2_metadata_from_id(instance_id)
            if ec2_metadata:
                msg = "found host with instance-id `{}`, derived dns `{}`"
                name_from_tag = util.tags_list_to_dict(
                    ec2_metadata.get("Tags", [])
                ).get("Name")
                dns = name_from_tag or ec2_metadata["PrivateIpAddress"]
                env.logger.debug(msg.format(instance_id, dns))
                break

    # LOGGER.debug("all secrets will come from `{}`".format(secrets_env_name))
    # LOGGER.debug("1st pass: use direct lookup".format())
    # secrets_env = Environment.from_name(secrets_env_name)
    # ssh_secrets = env.secrets.ssh()
    # for secret in ssh_secrets:
    #     if dns and secret.secret_name == dns:
    #         LOGGER.debug("exact match for dns, path is: {}".format(secret.secret_path))
    #         yield secret

    LOGGER.debug(f"2nd pass: searching through environments: {envs}")
    LOGGER.debug(f"env search order is: {[env.name for env in envs]}")
    AMIs = {}
    match = None
    for env in envs:
        if match:
            break
        env.logger.debug("getting reservations")
        reservations = env.ec2.describe_instances()["Reservations"]
        dnscount = 0
        options = []
        if dns:
            for rc in reservations:
                for ic in rc["Instances"]:
                    if ic["State"]["Name"] != "running":
                        continue
                    instance_name = util.tags_list_to_dict(ic.get("Tags", [])).get(
                        "Name"
                    )
                    if dns and instance_name and dns in instance_name:
                        dnscount = dnscount + 1
                        options.append(
                            ic["InstanceId"]
                            + ": "
                            + instance_name
                            + " "
                            + ic.get("PrivateIpAddress")
                            + ", InstanceType: "
                            + ic.get("InstanceType")
                            + ", AvailabilityZone: "
                            + ic["Placement"].get("AvailabilityZone")
                            + ", LaunchTime: "
                            + ic.get("LaunchTime").strftime("%b %d %Y %H:%M:%S")
                        )
        # LOGGER.debug(f"Instance Count: {dnscount}")
        if dnscount > 1:
            instance_choices = [
                inquirer.List(
                    "chosenInstance",
                    message="There are more than one instance with this hostname. Please pick one",
                    choices=options,
                )
            ]
            chosen_instance = inquirer.prompt(instance_choices)["chosenInstance"]
            instance_id = chosen_instance.split(":", 1)[0].strip()
            LOGGER.debug(f"Instance Chosen: {instance_id}")
        for rez in reservations:
            if match:
                break
            for instance in rez["Instances"]:
                if match:
                    break
                if instance["State"]["Name"] in "stopped terminated".split():
                    continue
                # if ami_id and instance['ImageId'] == ami_id:
                #     raise Exception(NotImplemented)
                instance_name = util.tags_list_to_dict(instance.get("Tags", [])).get(
                    "Name"
                )
                tmp = [instance_name]
                tmp += [
                    instance.get(attr)
                    for attr in [
                        "PublicIpAddress",
                        "PublicDnsName",
                        "PrivateIpAddress",
                    ]
                ]
                if instance_id and instance_id == instance["InstanceId"]:
                    match = instance
                    continue
                if dns and dnscount < 2 and dns in tmp:
                    match = instance
                    continue
    if not match:
        if aslib:
            msg = "failed"
            return msg
        else:
            return give_up()
    else:
        LOGGER.debug(f"found match: {instance}")
        keyname = instance["KeyName"]
        ssh_user = resolve_user(user=user, env=env, instance=instance)
        common = dict(
            ami_id=instance["ImageId"],
            ssh_user=ssh_user,
            env=env.name,
            dns=instance.get("PublicIpAddress", instance["PrivateIpAddress"]),
            secret_path=f"{env.ssm_keys_prefix}/{keyname}/{ssh_user}",
        )

        yield common


def hop_connect(
    command="",
    secret_path=None,
    ssh_user=None,
    dns=None,
    secret_name=None,
    aslib=None,
    **kwargs,
):
    """ """
    if any(
        [
            not secret_path,
            not ssh_user,
        ]
    ):
        LOGGER.critical([secret_path, ssh_user])
        give_up(NotImplemented)
    host = util.first(dns, secret_name)
    if not host:
        err = "Could not derive host!"
        LOGGER.critical([err, host, kwargs])
        raise RuntimeError(err)
    cmd = CMD_T.format(
        SSH_BASE_ARGS=SSH_BASE_ARGS,
        ssh_host=host,
        ssh_user=ssh_user,
        ssh_command=command,
        secret_path=secret_path,
    )
    if aslib:
        LOGGER.debug(command)
        result = util.invoke(cmd)
        string_stdout = result.stdout
        return string_stdout
    else:
        result = shil.invoke(cmd, interactive=True)
        return any(
            [
                result.succeeded,  # normal exit
                result.return_code == 130,  # Script terminated by Control-C
            ]
        )
