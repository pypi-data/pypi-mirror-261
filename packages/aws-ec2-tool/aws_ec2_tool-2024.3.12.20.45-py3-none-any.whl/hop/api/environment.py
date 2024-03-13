""" hop.api.environment

Core abstraction for environment-aware boto, which
reduces a lot of boilerplate with boto sessions/profiles
"""

from ssm.api.environment import Environment as BaseEnvironment

from hop import util

LOGGER = util.get_logger(__name__)
DEFAULT_ENV_SEARCH_ORDER = []


class Environment(BaseEnvironment):
    """ """

    def init_session(self):
        """ """
        super(self.__class__, self).init_session()
        self.ec2 = self.session.client("ec2")

    def get_ec2_metadata_from_id(self, id, **kwargs):
        """ """
        return self.get_ec2_metadata_base(
            filters=[
                {"Name": "instance-id", "Values": [id]},
            ],
            **kwargs,
        )

    def get_ami(self, ami_id, strict=True):
        import botocore

        LOGGER.debug(f"looking up ami {ami_id}")
        try:
            response = self.ec2.describe_images(ImageIds=[ami_id])
        except botocore.exceptions.ClientError:
            if not strict:
                return None
            else:
                raise
        else:
            images = response.get("Images", [])
            return util.first(*images)

    def get_user_from_ami(self, ami_id):
        """ """
        LOGGER.debug(f"looking up user for ami {ami_id}")
        result = None
        ami = self.get_ami(ami_id, strict=False)
        ami_name = None
        if ami is not None:
            ami_tags = ami.get("Tags", [])
            tags = util.tags_list_to_dict(ami_tags)
            ami_name = tags.get("Name", "unknown")
            if not ami_tags:
                LOGGER.warning(f"found ami `{ami_id} aka `{ami_name}`; no tags")
            else:
                LOGGER.warning(
                    f"found ami `{ami_id} aka `{ami_name}` with tags: {ami_tags}"
                )
            ami_location = ami.get("ImageLocation", "")
            ami_description = ami.get("Description", "")
            if any(
                [
                    "/ubuntu/" in ami_location,
                    "Ubuntu" or "Canonical" in ami_description,
                    "ubuntu" in ami_name.lower(),
                    "ubuntu" in [t.lower() for t in tags.keys()],
                ]
            ):
                result = "ubuntu"

            # no love for amazon linux version 1.  this is old, breaks half of the ansible
            if any(
                [
                    "amzn2" in ami_name.lower(),
                    "amazon" in [t.lower() for t in tags.keys()],
                ]
            ):
                result = "ec2-user"

            if any(
                ["emr" in ami_name.lower(), "emr" in [t.lower() for t in tags.keys()]]
            ):
                result = "ec2-user"

        if result is None:
            result = "ubuntu"
            msg = "could not guess unix user for ami `{}`, using default `{}` "
            LOGGER.warning(msg.format(ami_id, result))
        else:
            LOGGER.debug(f"guessing user: {result}")
        return result

    def get_ec2_metadata_base(self, filters=[], running=True):
        """ """
        if running:
            filters += [{"Name": "instance-state-name", "Values": ["running"]}]
        result_list = self.ec2.describe_instances(Filters=filters)
        if not result_list:
            msg = "no matching instance for filters `{}` was found running"
            msg = msg.format(filters)
            LOGGER.warning(msg)
            return None
        else:
            try:
                ec2_metadata = result_list["Reservations"][0]["Instances"][0]
            except IndexError:
                LOGGER.warning(f"cannot get ec2_metadata for filter `{filters}`")
                return None
            else:
                return ec2_metadata
