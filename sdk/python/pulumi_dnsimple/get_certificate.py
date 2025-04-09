# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetCertificateResult',
    'AwaitableGetCertificateResult',
    'get_certificate',
    'get_certificate_output',
]

@pulumi.output_type
class GetCertificateResult:
    """
    A collection of values returned by getCertificate.
    """
    def __init__(__self__, certificate_chains=None, certificate_id=None, domain=None, id=None, private_key=None, root_certificate=None, server_certificate=None, timeouts=None):
        if certificate_chains and not isinstance(certificate_chains, list):
            raise TypeError("Expected argument 'certificate_chains' to be a list")
        pulumi.set(__self__, "certificate_chains", certificate_chains)
        if certificate_id and not isinstance(certificate_id, int):
            raise TypeError("Expected argument 'certificate_id' to be a int")
        pulumi.set(__self__, "certificate_id", certificate_id)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if private_key and not isinstance(private_key, str):
            raise TypeError("Expected argument 'private_key' to be a str")
        pulumi.set(__self__, "private_key", private_key)
        if root_certificate and not isinstance(root_certificate, str):
            raise TypeError("Expected argument 'root_certificate' to be a str")
        pulumi.set(__self__, "root_certificate", root_certificate)
        if server_certificate and not isinstance(server_certificate, str):
            raise TypeError("Expected argument 'server_certificate' to be a str")
        pulumi.set(__self__, "server_certificate", server_certificate)
        if timeouts and not isinstance(timeouts, dict):
            raise TypeError("Expected argument 'timeouts' to be a dict")
        pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter(name="certificateChains")
    def certificate_chains(self) -> Sequence[builtins.str]:
        """
        A list of certificates that make up the chain
        """
        return pulumi.get(self, "certificate_chains")

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> builtins.int:
        return pulumi.get(self, "certificate_id")

    @property
    @pulumi.getter
    def domain(self) -> builtins.str:
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> builtins.str:
        """
        The corresponding Private Key for the SSL Certificate
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter(name="rootCertificate")
    def root_certificate(self) -> builtins.str:
        """
        The Root Certificate of the issuing CA
        """
        return pulumi.get(self, "root_certificate")

    @property
    @pulumi.getter(name="serverCertificate")
    def server_certificate(self) -> builtins.str:
        """
        The SSL Certificate
        """
        return pulumi.get(self, "server_certificate")

    @property
    @pulumi.getter
    def timeouts(self) -> Optional['outputs.GetCertificateTimeoutsResult']:
        return pulumi.get(self, "timeouts")


class AwaitableGetCertificateResult(GetCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificateResult(
            certificate_chains=self.certificate_chains,
            certificate_id=self.certificate_id,
            domain=self.domain,
            id=self.id,
            private_key=self.private_key,
            root_certificate=self.root_certificate,
            server_certificate=self.server_certificate,
            timeouts=self.timeouts)


def get_certificate(certificate_id: Optional[builtins.int] = None,
                    domain: Optional[builtins.str] = None,
                    timeouts: Optional[Union['GetCertificateTimeoutsArgs', 'GetCertificateTimeoutsArgsDict']] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCertificateResult:
    """
    Provides a DNSimple certificate data source.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_dnsimple as dnsimple

    foobar = dnsimple.get_certificate(domain=dnsimple_domain,
        certificate_id=dnsimple_certificate_id)
    ```


    :param builtins.int certificate_id: The ID of the SSL Certificate
    :param builtins.str domain: The domain of the SSL Certificate
    """
    __args__ = dict()
    __args__['certificateId'] = certificate_id
    __args__['domain'] = domain
    __args__['timeouts'] = timeouts
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('dnsimple:index/getCertificate:getCertificate', __args__, opts=opts, typ=GetCertificateResult).value

    return AwaitableGetCertificateResult(
        certificate_chains=pulumi.get(__ret__, 'certificate_chains'),
        certificate_id=pulumi.get(__ret__, 'certificate_id'),
        domain=pulumi.get(__ret__, 'domain'),
        id=pulumi.get(__ret__, 'id'),
        private_key=pulumi.get(__ret__, 'private_key'),
        root_certificate=pulumi.get(__ret__, 'root_certificate'),
        server_certificate=pulumi.get(__ret__, 'server_certificate'),
        timeouts=pulumi.get(__ret__, 'timeouts'))
def get_certificate_output(certificate_id: Optional[pulumi.Input[builtins.int]] = None,
                           domain: Optional[pulumi.Input[builtins.str]] = None,
                           timeouts: Optional[pulumi.Input[Optional[Union['GetCertificateTimeoutsArgs', 'GetCertificateTimeoutsArgsDict']]]] = None,
                           opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetCertificateResult]:
    """
    Provides a DNSimple certificate data source.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_dnsimple as dnsimple

    foobar = dnsimple.get_certificate(domain=dnsimple_domain,
        certificate_id=dnsimple_certificate_id)
    ```


    :param builtins.int certificate_id: The ID of the SSL Certificate
    :param builtins.str domain: The domain of the SSL Certificate
    """
    __args__ = dict()
    __args__['certificateId'] = certificate_id
    __args__['domain'] = domain
    __args__['timeouts'] = timeouts
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('dnsimple:index/getCertificate:getCertificate', __args__, opts=opts, typ=GetCertificateResult)
    return __ret__.apply(lambda __response__: GetCertificateResult(
        certificate_chains=pulumi.get(__response__, 'certificate_chains'),
        certificate_id=pulumi.get(__response__, 'certificate_id'),
        domain=pulumi.get(__response__, 'domain'),
        id=pulumi.get(__response__, 'id'),
        private_key=pulumi.get(__response__, 'private_key'),
        root_certificate=pulumi.get(__response__, 'root_certificate'),
        server_certificate=pulumi.get(__response__, 'server_certificate'),
        timeouts=pulumi.get(__response__, 'timeouts')))
