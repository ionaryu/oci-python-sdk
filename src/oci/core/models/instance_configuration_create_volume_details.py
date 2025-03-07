# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationCreateVolumeDetails(object):
    """
    Creates a new block volume. Please see :class:`CreateVolumeDetails`
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationCreateVolumeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this InstanceConfigurationCreateVolumeDetails.
        :type availability_domain: str

        :param backup_policy_id:
            The value to assign to the backup_policy_id property of this InstanceConfigurationCreateVolumeDetails.
        :type backup_policy_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this InstanceConfigurationCreateVolumeDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this InstanceConfigurationCreateVolumeDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this InstanceConfigurationCreateVolumeDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this InstanceConfigurationCreateVolumeDetails.
        :type freeform_tags: dict(str, str)

        :param kms_key_id:
            The value to assign to the kms_key_id property of this InstanceConfigurationCreateVolumeDetails.
        :type kms_key_id: str

        :param vpus_per_gb:
            The value to assign to the vpus_per_gb property of this InstanceConfigurationCreateVolumeDetails.
        :type vpus_per_gb: int

        :param size_in_gbs:
            The value to assign to the size_in_gbs property of this InstanceConfigurationCreateVolumeDetails.
        :type size_in_gbs: int

        :param source_details:
            The value to assign to the source_details property of this InstanceConfigurationCreateVolumeDetails.
        :type source_details: oci.core.models.InstanceConfigurationVolumeSourceDetails

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'backup_policy_id': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'kms_key_id': 'str',
            'vpus_per_gb': 'int',
            'size_in_gbs': 'int',
            'source_details': 'InstanceConfigurationVolumeSourceDetails'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'backup_policy_id': 'backupPolicyId',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'kms_key_id': 'kmsKeyId',
            'vpus_per_gb': 'vpusPerGB',
            'size_in_gbs': 'sizeInGBs',
            'source_details': 'sourceDetails'
        }

        self._availability_domain = None
        self._backup_policy_id = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._kms_key_id = None
        self._vpus_per_gb = None
        self._size_in_gbs = None
        self._source_details = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this InstanceConfigurationCreateVolumeDetails.
        The availability domain of the volume.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this InstanceConfigurationCreateVolumeDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this InstanceConfigurationCreateVolumeDetails.
        The availability domain of the volume.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this InstanceConfigurationCreateVolumeDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def backup_policy_id(self):
        """
        Gets the backup_policy_id of this InstanceConfigurationCreateVolumeDetails.
        If provided, specifies the ID of the volume backup policy to assign to the newly
        created volume. If omitted, no policy will be assigned.


        :return: The backup_policy_id of this InstanceConfigurationCreateVolumeDetails.
        :rtype: str
        """
        return self._backup_policy_id

    @backup_policy_id.setter
    def backup_policy_id(self, backup_policy_id):
        """
        Sets the backup_policy_id of this InstanceConfigurationCreateVolumeDetails.
        If provided, specifies the ID of the volume backup policy to assign to the newly
        created volume. If omitted, no policy will be assigned.


        :param backup_policy_id: The backup_policy_id of this InstanceConfigurationCreateVolumeDetails.
        :type: str
        """
        self._backup_policy_id = backup_policy_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this InstanceConfigurationCreateVolumeDetails.
        The OCID of the compartment that contains the volume.


        :return: The compartment_id of this InstanceConfigurationCreateVolumeDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this InstanceConfigurationCreateVolumeDetails.
        The OCID of the compartment that contains the volume.


        :param compartment_id: The compartment_id of this InstanceConfigurationCreateVolumeDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this InstanceConfigurationCreateVolumeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this InstanceConfigurationCreateVolumeDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this InstanceConfigurationCreateVolumeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this InstanceConfigurationCreateVolumeDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this InstanceConfigurationCreateVolumeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this InstanceConfigurationCreateVolumeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstanceConfigurationCreateVolumeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this InstanceConfigurationCreateVolumeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this InstanceConfigurationCreateVolumeDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this InstanceConfigurationCreateVolumeDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this InstanceConfigurationCreateVolumeDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this InstanceConfigurationCreateVolumeDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this InstanceConfigurationCreateVolumeDetails.
        The OCID of the Key Management key to assign as the master encryption key
        for the volume.


        :return: The kms_key_id of this InstanceConfigurationCreateVolumeDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this InstanceConfigurationCreateVolumeDetails.
        The OCID of the Key Management key to assign as the master encryption key
        for the volume.


        :param kms_key_id: The kms_key_id of this InstanceConfigurationCreateVolumeDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def vpus_per_gb(self):
        """
        Gets the vpus_per_gb of this InstanceConfigurationCreateVolumeDetails.
        The number of volume performance units (VPUs) that will be applied to this volume per GB,
        representing the Block Volume service's elastic performance options.
        See `Block Volume Elastic Performance`__ for more information.

        Allowed values:

          * `0`: Represents Lower Cost option.

          * `10`: Represents Balanced option.

          * `20`: Represents Higher Performance option.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeelasticperformance.htm


        :return: The vpus_per_gb of this InstanceConfigurationCreateVolumeDetails.
        :rtype: int
        """
        return self._vpus_per_gb

    @vpus_per_gb.setter
    def vpus_per_gb(self, vpus_per_gb):
        """
        Sets the vpus_per_gb of this InstanceConfigurationCreateVolumeDetails.
        The number of volume performance units (VPUs) that will be applied to this volume per GB,
        representing the Block Volume service's elastic performance options.
        See `Block Volume Elastic Performance`__ for more information.

        Allowed values:

          * `0`: Represents Lower Cost option.

          * `10`: Represents Balanced option.

          * `20`: Represents Higher Performance option.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeelasticperformance.htm


        :param vpus_per_gb: The vpus_per_gb of this InstanceConfigurationCreateVolumeDetails.
        :type: int
        """
        self._vpus_per_gb = vpus_per_gb

    @property
    def size_in_gbs(self):
        """
        Gets the size_in_gbs of this InstanceConfigurationCreateVolumeDetails.
        The size of the volume in GBs.


        :return: The size_in_gbs of this InstanceConfigurationCreateVolumeDetails.
        :rtype: int
        """
        return self._size_in_gbs

    @size_in_gbs.setter
    def size_in_gbs(self, size_in_gbs):
        """
        Sets the size_in_gbs of this InstanceConfigurationCreateVolumeDetails.
        The size of the volume in GBs.


        :param size_in_gbs: The size_in_gbs of this InstanceConfigurationCreateVolumeDetails.
        :type: int
        """
        self._size_in_gbs = size_in_gbs

    @property
    def source_details(self):
        """
        Gets the source_details of this InstanceConfigurationCreateVolumeDetails.

        :return: The source_details of this InstanceConfigurationCreateVolumeDetails.
        :rtype: oci.core.models.InstanceConfigurationVolumeSourceDetails
        """
        return self._source_details

    @source_details.setter
    def source_details(self, source_details):
        """
        Sets the source_details of this InstanceConfigurationCreateVolumeDetails.

        :param source_details: The source_details of this InstanceConfigurationCreateVolumeDetails.
        :type: oci.core.models.InstanceConfigurationVolumeSourceDetails
        """
        self._source_details = source_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
