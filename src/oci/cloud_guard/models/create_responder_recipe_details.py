# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateResponderRecipeDetails(object):
    """
    Details of ResponderRecipe.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateResponderRecipeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateResponderRecipeDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateResponderRecipeDetails.
        :type description: str

        :param source_responder_recipe_id:
            The value to assign to the source_responder_recipe_id property of this CreateResponderRecipeDetails.
        :type source_responder_recipe_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateResponderRecipeDetails.
        :type compartment_id: str

        :param responder_rules:
            The value to assign to the responder_rules property of this CreateResponderRecipeDetails.
        :type responder_rules: list[UpdateResponderRecipeResponderRule]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateResponderRecipeDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateResponderRecipeDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'source_responder_recipe_id': 'str',
            'compartment_id': 'str',
            'responder_rules': 'list[UpdateResponderRecipeResponderRule]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'source_responder_recipe_id': 'sourceResponderRecipeId',
            'compartment_id': 'compartmentId',
            'responder_rules': 'responderRules',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._source_responder_recipe_id = None
        self._compartment_id = None
        self._responder_rules = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateResponderRecipeDetails.
        ResponderRecipe Display Name


        :return: The display_name of this CreateResponderRecipeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateResponderRecipeDetails.
        ResponderRecipe Display Name


        :param display_name: The display_name of this CreateResponderRecipeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateResponderRecipeDetails.
        ResponderRecipe Description


        :return: The description of this CreateResponderRecipeDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateResponderRecipeDetails.
        ResponderRecipe Description


        :param description: The description of this CreateResponderRecipeDetails.
        :type: str
        """
        self._description = description

    @property
    def source_responder_recipe_id(self):
        """
        **[Required]** Gets the source_responder_recipe_id of this CreateResponderRecipeDetails.
        The id of the source responder recipe.


        :return: The source_responder_recipe_id of this CreateResponderRecipeDetails.
        :rtype: str
        """
        return self._source_responder_recipe_id

    @source_responder_recipe_id.setter
    def source_responder_recipe_id(self, source_responder_recipe_id):
        """
        Sets the source_responder_recipe_id of this CreateResponderRecipeDetails.
        The id of the source responder recipe.


        :param source_responder_recipe_id: The source_responder_recipe_id of this CreateResponderRecipeDetails.
        :type: str
        """
        self._source_responder_recipe_id = source_responder_recipe_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateResponderRecipeDetails.
        Compartment Identifier


        :return: The compartment_id of this CreateResponderRecipeDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateResponderRecipeDetails.
        Compartment Identifier


        :param compartment_id: The compartment_id of this CreateResponderRecipeDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def responder_rules(self):
        """
        Gets the responder_rules of this CreateResponderRecipeDetails.
        Responder Rules to override from source responder recipe


        :return: The responder_rules of this CreateResponderRecipeDetails.
        :rtype: list[UpdateResponderRecipeResponderRule]
        """
        return self._responder_rules

    @responder_rules.setter
    def responder_rules(self, responder_rules):
        """
        Sets the responder_rules of this CreateResponderRecipeDetails.
        Responder Rules to override from source responder recipe


        :param responder_rules: The responder_rules of this CreateResponderRecipeDetails.
        :type: list[UpdateResponderRecipeResponderRule]
        """
        self._responder_rules = responder_rules

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateResponderRecipeDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateResponderRecipeDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateResponderRecipeDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateResponderRecipeDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateResponderRecipeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateResponderRecipeDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateResponderRecipeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateResponderRecipeDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
