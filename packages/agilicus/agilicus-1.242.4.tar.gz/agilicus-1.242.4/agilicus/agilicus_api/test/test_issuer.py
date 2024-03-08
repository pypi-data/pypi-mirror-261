"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  The OpenAPI Specification in YAML format is available on [www](https://www.agilicus.com/www/api/agilicus-openapi.yaml) for importing to other tools.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2024.03.06
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import agilicus_api
from agilicus_api.model.admin_status import AdminStatus
from agilicus_api.model.application_upstream_identity_provider import ApplicationUpstreamIdentityProvider
from agilicus_api.model.issuer_client import IssuerClient
from agilicus_api.model.issuer_status import IssuerStatus
from agilicus_api.model.k8s_slug import K8sSlug
from agilicus_api.model.kerberos_upstream_identity_provider import KerberosUpstreamIdentityProvider
from agilicus_api.model.local_auth_upstream_identity_provider import LocalAuthUpstreamIdentityProvider
from agilicus_api.model.managed_upstream_identity_provider import ManagedUpstreamIdentityProvider
from agilicus_api.model.oidc_upstream_identity_provider import OIDCUpstreamIdentityProvider
from agilicus_api.model.operational_status import OperationalStatus
from agilicus_api.model.upstream_group_mapping import UpstreamGroupMapping
globals()['AdminStatus'] = AdminStatus
globals()['ApplicationUpstreamIdentityProvider'] = ApplicationUpstreamIdentityProvider
globals()['IssuerClient'] = IssuerClient
globals()['IssuerStatus'] = IssuerStatus
globals()['K8sSlug'] = K8sSlug
globals()['KerberosUpstreamIdentityProvider'] = KerberosUpstreamIdentityProvider
globals()['LocalAuthUpstreamIdentityProvider'] = LocalAuthUpstreamIdentityProvider
globals()['ManagedUpstreamIdentityProvider'] = ManagedUpstreamIdentityProvider
globals()['OIDCUpstreamIdentityProvider'] = OIDCUpstreamIdentityProvider
globals()['OperationalStatus'] = OperationalStatus
globals()['UpstreamGroupMapping'] = UpstreamGroupMapping
from agilicus_api.model.issuer import Issuer


class TestIssuer(unittest.TestCase):
    """Issuer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIssuer(self):
        """Test Issuer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Issuer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
