"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  The OpenAPI Specification in YAML format is available on [www](https://www.agilicus.com/www/api/agilicus-openapi.yaml) for importing to other tools.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2024.03.06
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from agilicus_api.api_client import ApiClient, Endpoint as _Endpoint
from agilicus_api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from agilicus_api.model.error_message import ErrorMessage
from agilicus_api.model.launcher import Launcher
from agilicus_api.model.list_launchers_response import ListLaunchersResponse


class LaunchersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_launcher(
            self,
            launcher,
            **kwargs
        ):
            """Create a launcher  # noqa: E501

            Create a launcher  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_launcher(launcher, async_req=True)
            >>> result = thread.get()

            Args:
                launcher (Launcher):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Launcher
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['launcher'] = \
                launcher
            return self.call_with_http_info(**kwargs)

        if self.create_launcher is None:
            self.create_launcher = _Endpoint(
                settings={
                    'response_type': (Launcher,),
                    'auth': [
                        'token-valid'
                    ],
                    'endpoint_path': '/v1/launchers',
                    'operation_id': 'create_launcher',
                    'http_method': 'POST',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'launcher',
                    ],
                    'required': [
                        'launcher',
                    ],
                    'nullable': [
                    ],
                    'enum': [
                    ],
                    'validation': [
                    ]
                },
                root_map={
                    'validations': {
                    },
                    'allowed_values': {
                    },
                    'openapi_types': {
                        'launcher':
                            (Launcher,),
                    },
                    'attribute_map': {
                    },
                    'location_map': {
                        'launcher': 'body',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [
                        'application/json'
                    ],
                    'content_type': [
                        'application/json'
                    ]
                },
                api_client=api_client,
                callable=__create_launcher
            )

        def __delete_launcher(
            self,
            launcher_id,
            **kwargs
        ):
            """Delete a Launcher  # noqa: E501

            Delete a Launcher  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_launcher(launcher_id, async_req=True)
            >>> result = thread.get()

            Args:
                launcher_id (str): Launcher unique identifier

            Keyword Args:
                org_id (str): Organisation Unique identifier. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['launcher_id'] = \
                launcher_id
            return self.call_with_http_info(**kwargs)

        if self.delete_launcher is None:
            self.delete_launcher = _Endpoint(
                settings={
                    'response_type': None,
                    'auth': [
                        'token-valid'
                    ],
                    'endpoint_path': '/v1/launchers/{launcher_id}',
                    'operation_id': 'delete_launcher',
                    'http_method': 'DELETE',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'launcher_id',
                        'org_id',
                    ],
                    'required': [
                        'launcher_id',
                    ],
                    'nullable': [
                    ],
                    'enum': [
                    ],
                    'validation': [
                        'launcher_id',
                    ]
                },
                root_map={
                    'validations': {
                        ('launcher_id',): {

                            'regex': {
                                'pattern': r'^[a-zA-Z0-9-]+$',  # noqa: E501
                            },
                        },
                    },
                    'allowed_values': {
                    },
                    'openapi_types': {
                        'launcher_id':
                            (str,),
                        'org_id':
                            (str,),
                    },
                    'attribute_map': {
                        'launcher_id': 'launcher_id',
                        'org_id': 'org_id',
                    },
                    'location_map': {
                        'launcher_id': 'path',
                        'org_id': 'query',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [],
                    'content_type': [],
                },
                api_client=api_client,
                callable=__delete_launcher
            )

        def __get_launcher(
            self,
            launcher_id,
            **kwargs
        ):
            """Get a single launcher  # noqa: E501

            Get a single launcher  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_launcher(launcher_id, async_req=True)
            >>> result = thread.get()

            Args:
                launcher_id (str): Launcher unique identifier

            Keyword Args:
                org_id (str): Organisation Unique identifier. [optional]
                expand_resource_members (bool): On resource requests, when True will populate member_resources with its full Resource object. . [optional] if omitted the server will use the default value of False
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Launcher
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['launcher_id'] = \
                launcher_id
            return self.call_with_http_info(**kwargs)

        if self.get_launcher is None:
            self.get_launcher = _Endpoint(
                settings={
                    'response_type': (Launcher,),
                    'auth': [
                        'token-valid'
                    ],
                    'endpoint_path': '/v1/launchers/{launcher_id}',
                    'operation_id': 'get_launcher',
                    'http_method': 'GET',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'launcher_id',
                        'org_id',
                        'expand_resource_members',
                    ],
                    'required': [
                        'launcher_id',
                    ],
                    'nullable': [
                    ],
                    'enum': [
                    ],
                    'validation': [
                        'launcher_id',
                    ]
                },
                root_map={
                    'validations': {
                        ('launcher_id',): {

                            'regex': {
                                'pattern': r'^[a-zA-Z0-9-]+$',  # noqa: E501
                            },
                        },
                    },
                    'allowed_values': {
                    },
                    'openapi_types': {
                        'launcher_id':
                            (str,),
                        'org_id':
                            (str,),
                        'expand_resource_members':
                            (bool,),
                    },
                    'attribute_map': {
                        'launcher_id': 'launcher_id',
                        'org_id': 'org_id',
                        'expand_resource_members': 'expand_resource_members',
                    },
                    'location_map': {
                        'launcher_id': 'path',
                        'org_id': 'query',
                        'expand_resource_members': 'query',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [
                        'application/json'
                    ],
                    'content_type': [],
                },
                api_client=api_client,
                callable=__get_launcher
            )

        def __list_launchers(
            self,
            **kwargs
        ):
            """Get all launchers  # noqa: E501

            Get all launchers  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_launchers(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                limit (int): limit the number of rows in the response. [optional] if omitted the server will use the default value of 500
                org_id (str): Organisation Unique identifier. [optional]
                expand_resource_members (bool): On resource requests, when True will populate member_resources with its full Resource object. . [optional] if omitted the server will use the default value of False
                org_ids ([str]): The list of org ids to search for. Each org will be searched for independently.. [optional]
                resource_id (str): The id of the resource to query for. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ListLaunchersResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        if self.list_launchers is None:
            self.list_launchers = _Endpoint(
                settings={
                    'response_type': (ListLaunchersResponse,),
                    'auth': [
                        'token-valid'
                    ],
                    'endpoint_path': '/v1/launchers',
                    'operation_id': 'list_launchers',
                    'http_method': 'GET',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'limit',
                        'org_id',
                        'expand_resource_members',
                        'org_ids',
                        'resource_id',
                    ],
                    'required': [],
                    'nullable': [
                    ],
                    'enum': [
                    ],
                    'validation': [
                        'limit',
                    ]
                },
                root_map={
                    'validations': {
                        ('limit',): {

                            'inclusive_maximum': 500,
                            'inclusive_minimum': 1,
                        },
                    },
                    'allowed_values': {
                    },
                    'openapi_types': {
                        'limit':
                            (int,),
                        'org_id':
                            (str,),
                        'expand_resource_members':
                            (bool,),
                        'org_ids':
                            ([str],),
                        'resource_id':
                            (str,),
                    },
                    'attribute_map': {
                        'limit': 'limit',
                        'org_id': 'org_id',
                        'expand_resource_members': 'expand_resource_members',
                        'org_ids': 'org_ids',
                        'resource_id': 'resource_id',
                    },
                    'location_map': {
                        'limit': 'query',
                        'org_id': 'query',
                        'expand_resource_members': 'query',
                        'org_ids': 'query',
                        'resource_id': 'query',
                    },
                    'collection_format_map': {
                        'org_ids': 'multi',
                    }
                },
                headers_map={
                    'accept': [
                        'application/json'
                    ],
                    'content_type': [],
                },
                api_client=api_client,
                callable=__list_launchers
            )

        def __replace_launcher(
            self,
            launcher_id,
            **kwargs
        ):
            """Create or update a launcher  # noqa: E501

            Create or update a launcher  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.replace_launcher(launcher_id, async_req=True)
            >>> result = thread.get()

            Args:
                launcher_id (str): Launcher unique identifier

            Keyword Args:
                org_id (str): Organisation Unique identifier. [optional]
                launcher (Launcher): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Launcher
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['launcher_id'] = \
                launcher_id
            return self.call_with_http_info(**kwargs)

        if self.replace_launcher is None:
            self.replace_launcher = _Endpoint(
                settings={
                    'response_type': (Launcher,),
                    'auth': [
                        'token-valid'
                    ],
                    'endpoint_path': '/v1/launchers/{launcher_id}',
                    'operation_id': 'replace_launcher',
                    'http_method': 'PUT',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'launcher_id',
                        'org_id',
                        'launcher',
                    ],
                    'required': [
                        'launcher_id',
                    ],
                    'nullable': [
                    ],
                    'enum': [
                    ],
                    'validation': [
                        'launcher_id',
                    ]
                },
                root_map={
                    'validations': {
                        ('launcher_id',): {

                            'regex': {
                                'pattern': r'^[a-zA-Z0-9-]+$',  # noqa: E501
                            },
                        },
                    },
                    'allowed_values': {
                    },
                    'openapi_types': {
                        'launcher_id':
                            (str,),
                        'org_id':
                            (str,),
                        'launcher':
                            (Launcher,),
                    },
                    'attribute_map': {
                        'launcher_id': 'launcher_id',
                        'org_id': 'org_id',
                    },
                    'location_map': {
                        'launcher_id': 'path',
                        'org_id': 'query',
                        'launcher': 'body',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [
                        'application/json'
                    ],
                    'content_type': [
                        'application/json'
                    ]
                },
                api_client=api_client,
                callable=__replace_launcher
            )

    create_launcher = None 
    delete_launcher = None 
    get_launcher = None 
    list_launchers = None 
    replace_launcher = None 
