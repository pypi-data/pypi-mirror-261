"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  The OpenAPI Specification in YAML format is available on [www](https://www.agilicus.com/www/api/agilicus-openapi.yaml) for importing to other tools.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2024.03.06
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from agilicus_api.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from agilicus_api.exceptions import ApiAttributeError


def lazy_import():
    from agilicus_api.model.http_rule import HttpRule
    from agilicus_api.model.rule_action import RuleAction
    from agilicus_api.model.rule_condition import RuleCondition
    from agilicus_api.model.rule_scope_enum import RuleScopeEnum
    globals()['HttpRule'] = HttpRule
    globals()['RuleAction'] = RuleAction
    globals()['RuleCondition'] = RuleCondition
    globals()['RuleScopeEnum'] = RuleScopeEnum


class RuleConfig(ModelNormal):
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

    allowed_values = {
    }

    validations = {
        ('name',): {
            'regex': {
                'pattern': r'[a-zA-Z0-9-_:]+',  # noqa: E501
            },
        },
        ('comments',): {
            'max_length': 2047,
        },
        ('priority',): {
            'inclusive_maximum': 65535,
            'inclusive_minimum': -65535,
        },
    }

    @property
    def name(self):
       return self.get("name")

    @name.setter
    def name(self, new_value):
       self.name = new_value

    @property
    def roles(self):
       return self.get("roles")

    @roles.setter
    def roles(self, new_value):
       self.roles = new_value

    @property
    def excluded_roles(self):
       return self.get("excluded_roles")

    @excluded_roles.setter
    def excluded_roles(self, new_value):
       self.excluded_roles = new_value

    @property
    def comments(self):
       return self.get("comments")

    @comments.setter
    def comments(self, new_value):
       self.comments = new_value

    @property
    def condition(self):
       return self.get("condition")

    @condition.setter
    def condition(self, new_value):
       self.condition = new_value

    @property
    def scope(self):
       return self.get("scope")

    @scope.setter
    def scope(self, new_value):
       self.scope = new_value

    @property
    def extended_condition(self):
       return self.get("extended_condition")

    @extended_condition.setter
    def extended_condition(self, new_value):
       self.extended_condition = new_value

    @property
    def priority(self):
       return self.get("priority")

    @priority.setter
    def priority(self, new_value):
       self.priority = new_value

    @property
    def actions(self):
       return self.get("actions")

    @actions.setter
    def actions(self, new_value):
       self.actions = new_value

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

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
            'name': (str,),  # noqa: E501
            'roles': ([str],),  # noqa: E501
            'excluded_roles': ([str],),  # noqa: E501
            'comments': (str,),  # noqa: E501
            'condition': (HttpRule,),  # noqa: E501
            'scope': (RuleScopeEnum,),  # noqa: E501
            'extended_condition': (RuleCondition,),  # noqa: E501
            'priority': (int,),  # noqa: E501
            'actions': ([RuleAction],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'name': 'name',  # noqa: E501
        'roles': 'roles',  # noqa: E501
        'excluded_roles': 'excluded_roles',  # noqa: E501
        'comments': 'comments',  # noqa: E501
        'condition': 'condition',  # noqa: E501
        'scope': 'scope',  # noqa: E501
        'extended_condition': 'extended_condition',  # noqa: E501
        'priority': 'priority',  # noqa: E501
        'actions': 'actions',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, name, *args, **kwargs):  # noqa: E501
        """RuleConfig - a model defined in OpenAPI

        Args:
            name (str): The name of the rule.

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
            roles ([str]): The list of roles assigned to this rule.. [optional]  # noqa: E501
            excluded_roles ([str]): The list of roles excluded from this rule.. [optional]  # noqa: E501
            comments (str): A description of the rule. The comments have no functional effect, but can help to clarify the purpose of a rule when the name is not sufficient. . [optional]  # noqa: E501
            condition (HttpRule): [optional]  # noqa: E501
            scope (RuleScopeEnum): [optional]  # noqa: E501
            extended_condition (RuleCondition): [optional]  # noqa: E501
            priority (int): The priority of the rule relative to other rules at the top level: that is, if this rule is not being evaluated as part of a RuleSet, it is assumed to be within a 'global' RuleSet that contains all 'root' rules. In that case, this priority applies.  Rules are evaluated in order of higher priority number to lower priority number. . [optional] if omitted the server will use the default value of 0  # noqa: E501
            actions ([RuleAction]): The actions to take if the rule evaluates to true. At least one of allow or deny must be present in the action list for the system to effectively operate on the request. By default, if neither allow nor deny is present in the list of actions resulting from the rule, the request will be allowed. Some actions may conflict.  If there is a conflict, the first action in the preorder depth-first-search traversal of the rule tree will take precedence. For example, deny and allow are conflicting actions. If the parent rule has deny, and a sub_rule has allow, then the request will be denied. Or, if the parent rule has none, the first sub-rule has allow, and the second sub-rule has deny, the request will be allowed. . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.name = name
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    def __python_set(val):
        return set(val)
 
    required_properties = __python_set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, name, *args, **kwargs):  # noqa: E501
        """RuleConfig - a model defined in OpenAPI

        Args:
            name (str): The name of the rule.

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
            roles ([str]): The list of roles assigned to this rule.. [optional]  # noqa: E501
            excluded_roles ([str]): The list of roles excluded from this rule.. [optional]  # noqa: E501
            comments (str): A description of the rule. The comments have no functional effect, but can help to clarify the purpose of a rule when the name is not sufficient. . [optional]  # noqa: E501
            condition (HttpRule): [optional]  # noqa: E501
            scope (RuleScopeEnum): [optional]  # noqa: E501
            extended_condition (RuleCondition): [optional]  # noqa: E501
            priority (int): The priority of the rule relative to other rules at the top level: that is, if this rule is not being evaluated as part of a RuleSet, it is assumed to be within a 'global' RuleSet that contains all 'root' rules. In that case, this priority applies.  Rules are evaluated in order of higher priority number to lower priority number. . [optional] if omitted the server will use the default value of 0  # noqa: E501
            actions ([RuleAction]): The actions to take if the rule evaluates to true. At least one of allow or deny must be present in the action list for the system to effectively operate on the request. By default, if neither allow nor deny is present in the list of actions resulting from the rule, the request will be allowed. Some actions may conflict.  If there is a conflict, the first action in the preorder depth-first-search traversal of the rule tree will take precedence. For example, deny and allow are conflicting actions. If the parent rule has deny, and a sub_rule has allow, then the request will be denied. Or, if the parent rule has none, the first sub-rule has allow, and the second sub-rule has deny, the request will be allowed. . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.name = name
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

