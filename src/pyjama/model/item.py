"""
    Jama REST API

    This is the documentation for the Jama REST API.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ..exceptions import ApiAttributeError
from ..model_utils import ApiTypeError  # noqa: F401
from ..model_utils import (
    ModelComposed,
    ModelNormal,
    ModelSimple,
    OpenApiModel,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


def lazy_import():
    from ..model.allowed_resource import AllowedResource
    from ..model.location import Location
    from ..model.lock import Lock

    globals()["AllowedResource"] = AllowedResource
    globals()["Location"] = Location
    globals()["Lock"] = Lock


class Item(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {}

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            none_type,
        )  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            "id": (int,),  # noqa: E501
            "document_key": (str,),  # noqa: E501
            "global_id": (str,),  # noqa: E501
            "project": (int,),  # noqa: E501
            "item_type": (int,),  # noqa: E501
            "child_item_type": (int,),  # noqa: E501
            "created_date": (datetime,),  # noqa: E501
            "modified_date": (datetime,),  # noqa: E501
            "last_activity_date": (datetime,),  # noqa: E501
            "created_by": (int,),  # noqa: E501
            "modified_by": (int,),  # noqa: E501
            "lock": (Lock,),  # noqa: E501
            "location": (Location,),  # noqa: E501
            "resources": ({str: (AllowedResource,)},),  # noqa: E501
            "fields": (
                {str: (bool, date, datetime, dict, float, int, list, str, none_type,)},
            ),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "id": "id",  # noqa: E501
        "document_key": "documentKey",  # noqa: E501
        "global_id": "globalId",  # noqa: E501
        "project": "project",  # noqa: E501
        "item_type": "itemType",  # noqa: E501
        "child_item_type": "childItemType",  # noqa: E501
        "created_date": "createdDate",  # noqa: E501
        "modified_date": "modifiedDate",  # noqa: E501
        "last_activity_date": "lastActivityDate",  # noqa: E501
        "created_by": "createdBy",  # noqa: E501
        "modified_by": "modifiedBy",  # noqa: E501
        "lock": "lock",  # noqa: E501
        "location": "location",  # noqa: E501
        "resources": "resources",  # noqa: E501
        "fields": "fields",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(
        cls,
        id,
        document_key,
        global_id,
        project,
        item_type,
        child_item_type,
        created_date,
        modified_date,
        last_activity_date,
        created_by,
        modified_by,
        lock,
        location,
        resources,
        fields,
        *args,
        **kwargs,
    ):  # noqa: E501
        """Item - a model defined in OpenAPI

        Args:
            id (int):
            document_key (str):
            global_id (str):
            project (int): ID of a project
            item_type (int): ID of an item type
            child_item_type (int): ID of an item type
            created_date (datetime):
            modified_date (datetime):
            last_activity_date (datetime):
            created_by (int): ID of a user
            modified_by (int): ID of a user
            lock (Lock):
            location (Location):
            resources ({str: (AllowedResource,)}): A set of resources and allowed permissions
            fields ({str: (bool, date, datetime, dict, float, int, list, str, none_type,)}): A map of field names to field values e.g. {\"name\":\"Sample Item\", \"status\": 292, \"release\": 2, \"assigned\": 23}

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", True)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                        % (args, self.__class__.__name__,),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.document_key = document_key
        self.global_id = global_id
        self.project = project
        self.item_type = item_type
        self.child_item_type = child_item_type
        self.created_date = created_date
        self.modified_date = modified_date
        self.last_activity_date = last_activity_date
        self.created_by = created_by
        self.modified_by = modified_by
        self.lock = lock
        self.location = location
        self.resources = resources
        self.fields = fields
        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(
        self,
        id,
        document_key,
        global_id,
        project,
        item_type,
        child_item_type,
        created_date,
        modified_date,
        last_activity_date,
        created_by,
        modified_by,
        lock,
        location,
        resources,
        fields,
        *args,
        **kwargs,
    ):  # noqa: E501
        """Item - a model defined in OpenAPI

        Args:
            id (int):
            document_key (str):
            global_id (str):
            project (int): ID of a project
            item_type (int): ID of an item type
            child_item_type (int): ID of an item type
            created_date (datetime):
            modified_date (datetime):
            last_activity_date (datetime):
            created_by (int): ID of a user
            modified_by (int): ID of a user
            lock (Lock):
            location (Location):
            resources ({str: (AllowedResource,)}): A set of resources and allowed permissions
            fields ({str: (bool, date, datetime, dict, float, int, list, str, none_type,)}): A map of field names to field values e.g. {\"name\":\"Sample Item\", \"status\": 292, \"release\": 2, \"assigned\": 23}

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                        % (args, self.__class__.__name__,),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.document_key = document_key
        self.global_id = global_id
        self.project = project
        self.item_type = item_type
        self.child_item_type = child_item_type
        self.created_date = created_date
        self.modified_date = modified_date
        self.last_activity_date = last_activity_date
        self.created_by = created_by
        self.modified_by = modified_by
        self.lock = lock
        self.location = location
        self.resources = resources
        self.fields = fields
        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes."
                )
