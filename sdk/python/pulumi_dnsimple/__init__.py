# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .contact import *
from .domain import *
from .domain_delegation import *
from .ds_record import *
from .email_forward import *
from .get_certificate import *
from .get_registrant_change_check import *
from .get_zone import *
from .lets_encrypt_certificate import *
from .provider import *
from .registered_domain import *
from .zone_record import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_dnsimple.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_dnsimple.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "dnsimple",
  "mod": "index/contact",
  "fqn": "pulumi_dnsimple",
  "classes": {
   "dnsimple:index/contact:Contact": "Contact"
  }
 },
 {
  "pkg": "dnsimple",
  "mod": "index/domain",
  "fqn": "pulumi_dnsimple",
  "classes": {
   "dnsimple:index/domain:Domain": "Domain"
  }
 },
 {
  "pkg": "dnsimple",
  "mod": "index/domainDelegation",
  "fqn": "pulumi_dnsimple",
  "classes": {
   "dnsimple:index/domainDelegation:DomainDelegation": "DomainDelegation"
  }
 },
 {
  "pkg": "dnsimple",
  "mod": "index/dsRecord",
  "fqn": "pulumi_dnsimple",
  "classes": {
   "dnsimple:index/dsRecord:DsRecord": "DsRecord"
  }
 },
 {
  "pkg": "dnsimple",
  "mod": "index/emailForward",
  "fqn": "pulumi_dnsimple",
  "classes": {
   "dnsimple:index/emailForward:EmailForward": "EmailForward"
  }
 },
 {
  "pkg": "dnsimple",
  "mod": "index/letsEncryptCertificate",
  "fqn": "pulumi_dnsimple",
  "classes": {
   "dnsimple:index/letsEncryptCertificate:LetsEncryptCertificate": "LetsEncryptCertificate"
  }
 },
 {
  "pkg": "dnsimple",
  "mod": "index/registeredDomain",
  "fqn": "pulumi_dnsimple",
  "classes": {
   "dnsimple:index/registeredDomain:RegisteredDomain": "RegisteredDomain"
  }
 },
 {
  "pkg": "dnsimple",
  "mod": "index/zoneRecord",
  "fqn": "pulumi_dnsimple",
  "classes": {
   "dnsimple:index/zoneRecord:ZoneRecord": "ZoneRecord"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "dnsimple",
  "token": "pulumi:providers:dnsimple",
  "fqn": "pulumi_dnsimple",
  "class": "Provider"
 }
]
"""
)
