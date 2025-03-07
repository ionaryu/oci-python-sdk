# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetDetectorDetails(object):
    """
    Overriden settings of a Detector Rule applied on target
    """

    #: A constant which can be used with the risk_level property of a TargetDetectorDetails.
    #: This constant has a value of "CRITICAL"
    RISK_LEVEL_CRITICAL = "CRITICAL"

    #: A constant which can be used with the risk_level property of a TargetDetectorDetails.
    #: This constant has a value of "HIGH"
    RISK_LEVEL_HIGH = "HIGH"

    #: A constant which can be used with the risk_level property of a TargetDetectorDetails.
    #: This constant has a value of "MEDIUM"
    RISK_LEVEL_MEDIUM = "MEDIUM"

    #: A constant which can be used with the risk_level property of a TargetDetectorDetails.
    #: This constant has a value of "LOW"
    RISK_LEVEL_LOW = "LOW"

    #: A constant which can be used with the risk_level property of a TargetDetectorDetails.
    #: This constant has a value of "MINOR"
    RISK_LEVEL_MINOR = "MINOR"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetDetectorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this TargetDetectorDetails.
        :type is_enabled: bool

        :param risk_level:
            The value to assign to the risk_level property of this TargetDetectorDetails.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type risk_level: str

        :param configurations:
            The value to assign to the configurations property of this TargetDetectorDetails.
        :type configurations: list[oci.cloud_guard.models.DetectorConfiguration]

        :param condition_groups:
            The value to assign to the condition_groups property of this TargetDetectorDetails.
        :type condition_groups: list[oci.cloud_guard.models.ConditionGroup]

        :param labels:
            The value to assign to the labels property of this TargetDetectorDetails.
        :type labels: list[str]

        :param is_configuration_allowed:
            The value to assign to the is_configuration_allowed property of this TargetDetectorDetails.
        :type is_configuration_allowed: bool

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'risk_level': 'str',
            'configurations': 'list[DetectorConfiguration]',
            'condition_groups': 'list[ConditionGroup]',
            'labels': 'list[str]',
            'is_configuration_allowed': 'bool'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'risk_level': 'riskLevel',
            'configurations': 'configurations',
            'condition_groups': 'conditionGroups',
            'labels': 'labels',
            'is_configuration_allowed': 'isConfigurationAllowed'
        }

        self._is_enabled = None
        self._risk_level = None
        self._configurations = None
        self._condition_groups = None
        self._labels = None
        self._is_configuration_allowed = None

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this TargetDetectorDetails.
        Enables the control


        :return: The is_enabled of this TargetDetectorDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this TargetDetectorDetails.
        Enables the control


        :param is_enabled: The is_enabled of this TargetDetectorDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def risk_level(self):
        """
        **[Required]** Gets the risk_level of this TargetDetectorDetails.
        The Risk Level

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The risk_level of this TargetDetectorDetails.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """
        Sets the risk_level of this TargetDetectorDetails.
        The Risk Level


        :param risk_level: The risk_level of this TargetDetectorDetails.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR"]
        if not value_allowed_none_or_none_sentinel(risk_level, allowed_values):
            risk_level = 'UNKNOWN_ENUM_VALUE'
        self._risk_level = risk_level

    @property
    def configurations(self):
        """
        Gets the configurations of this TargetDetectorDetails.
        Configuration details


        :return: The configurations of this TargetDetectorDetails.
        :rtype: list[oci.cloud_guard.models.DetectorConfiguration]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """
        Sets the configurations of this TargetDetectorDetails.
        Configuration details


        :param configurations: The configurations of this TargetDetectorDetails.
        :type: list[oci.cloud_guard.models.DetectorConfiguration]
        """
        self._configurations = configurations

    @property
    def condition_groups(self):
        """
        Gets the condition_groups of this TargetDetectorDetails.
        Condition group corresponding to each compartment


        :return: The condition_groups of this TargetDetectorDetails.
        :rtype: list[oci.cloud_guard.models.ConditionGroup]
        """
        return self._condition_groups

    @condition_groups.setter
    def condition_groups(self, condition_groups):
        """
        Sets the condition_groups of this TargetDetectorDetails.
        Condition group corresponding to each compartment


        :param condition_groups: The condition_groups of this TargetDetectorDetails.
        :type: list[oci.cloud_guard.models.ConditionGroup]
        """
        self._condition_groups = condition_groups

    @property
    def labels(self):
        """
        Gets the labels of this TargetDetectorDetails.
        user defined labels for a detector rule


        :return: The labels of this TargetDetectorDetails.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this TargetDetectorDetails.
        user defined labels for a detector rule


        :param labels: The labels of this TargetDetectorDetails.
        :type: list[str]
        """
        self._labels = labels

    @property
    def is_configuration_allowed(self):
        """
        Gets the is_configuration_allowed of this TargetDetectorDetails.
        configuration allowed or not


        :return: The is_configuration_allowed of this TargetDetectorDetails.
        :rtype: bool
        """
        return self._is_configuration_allowed

    @is_configuration_allowed.setter
    def is_configuration_allowed(self, is_configuration_allowed):
        """
        Sets the is_configuration_allowed of this TargetDetectorDetails.
        configuration allowed or not


        :param is_configuration_allowed: The is_configuration_allowed of this TargetDetectorDetails.
        :type: bool
        """
        self._is_configuration_allowed = is_configuration_allowed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
