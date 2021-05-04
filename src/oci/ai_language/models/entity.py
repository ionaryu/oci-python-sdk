# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Entity(object):
    """
    entity object
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Entity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param offset:
            The value to assign to the offset property of this Entity.
        :type offset: int

        :param length:
            The value to assign to the length property of this Entity.
        :type length: int

        :param text:
            The value to assign to the text property of this Entity.
        :type text: str

        :param type:
            The value to assign to the type property of this Entity.
        :type type: str

        :param is_pii:
            The value to assign to the is_pii property of this Entity.
        :type is_pii: bool

        :param score:
            The value to assign to the score property of this Entity.
        :type score: float

        """
        self.swagger_types = {
            'offset': 'int',
            'length': 'int',
            'text': 'str',
            'type': 'str',
            'is_pii': 'bool',
            'score': 'float'
        }

        self.attribute_map = {
            'offset': 'offset',
            'length': 'length',
            'text': 'text',
            'type': 'type',
            'is_pii': 'isPii',
            'score': 'score'
        }

        self._offset = None
        self._length = None
        self._text = None
        self._type = None
        self._is_pii = None
        self._score = None

    @property
    def offset(self):
        """
        Gets the offset of this Entity.
        The number of Unicode code points preceding this entity in the submitted text.


        :return: The offset of this Entity.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this Entity.
        The number of Unicode code points preceding this entity in the submitted text.


        :param offset: The offset of this Entity.
        :type: int
        """
        self._offset = offset

    @property
    def length(self):
        """
        Gets the length of this Entity.
        Length of text


        :return: The length of this Entity.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this Entity.
        Length of text


        :param length: The length of this Entity.
        :type: int
        """
        self._length = length

    @property
    def text(self):
        """
        Gets the text of this Entity.
        Entity text like name of person, location, and so on.


        :return: The text of this Entity.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this Entity.
        Entity text like name of person, location, and so on.


        :param text: The text of this Entity.
        :type: str
        """
        self._text = text

    @property
    def type(self):
        """
        Gets the type of this Entity.
        Type of entity text like PER, LOC, GPE and NOPE.


        :return: The type of this Entity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Entity.
        Type of entity text like PER, LOC, GPE and NOPE.


        :param type: The type of this Entity.
        :type: str
        """
        self._type = type

    @property
    def is_pii(self):
        """
        Gets the is_pii of this Entity.
        This flag is to indicate if it is PII entity or not.


        :return: The is_pii of this Entity.
        :rtype: bool
        """
        return self._is_pii

    @is_pii.setter
    def is_pii(self, is_pii):
        """
        Sets the is_pii of this Entity.
        This flag is to indicate if it is PII entity or not.


        :param is_pii: The is_pii of this Entity.
        :type: bool
        """
        self._is_pii = is_pii

    @property
    def score(self):
        """
        Gets the score of this Entity.
        Score or confidence for prediction.


        :return: The score of this Entity.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this Entity.
        Score or confidence for prediction.


        :param score: The score of this Entity.
        :type: float
        """
        self._score = score

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
