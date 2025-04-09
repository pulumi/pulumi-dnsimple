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

__all__ = [
    'GetRegistrantChangeCheckResult',
    'AwaitableGetRegistrantChangeCheckResult',
    'get_registrant_change_check',
    'get_registrant_change_check_output',
]

@pulumi.output_type
class GetRegistrantChangeCheckResult:
    """
    A collection of values returned by getRegistrantChangeCheck.
    """
    def __init__(__self__, contact_id=None, domain_id=None, extended_attributes=None, id=None, registry_owner_change=None):
        if contact_id and not isinstance(contact_id, str):
            raise TypeError("Expected argument 'contact_id' to be a str")
        pulumi.set(__self__, "contact_id", contact_id)
        if domain_id and not isinstance(domain_id, str):
            raise TypeError("Expected argument 'domain_id' to be a str")
        pulumi.set(__self__, "domain_id", domain_id)
        if extended_attributes and not isinstance(extended_attributes, list):
            raise TypeError("Expected argument 'extended_attributes' to be a list")
        pulumi.set(__self__, "extended_attributes", extended_attributes)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if registry_owner_change and not isinstance(registry_owner_change, bool):
            raise TypeError("Expected argument 'registry_owner_change' to be a bool")
        pulumi.set(__self__, "registry_owner_change", registry_owner_change)

    @property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> builtins.str:
        return pulumi.get(self, "contact_id")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> builtins.str:
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="extendedAttributes")
    def extended_attributes(self) -> Sequence['outputs.GetRegistrantChangeCheckExtendedAttributeResult']:
        return pulumi.get(self, "extended_attributes")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="registryOwnerChange")
    def registry_owner_change(self) -> builtins.bool:
        return pulumi.get(self, "registry_owner_change")


class AwaitableGetRegistrantChangeCheckResult(GetRegistrantChangeCheckResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegistrantChangeCheckResult(
            contact_id=self.contact_id,
            domain_id=self.domain_id,
            extended_attributes=self.extended_attributes,
            id=self.id,
            registry_owner_change=self.registry_owner_change)


def get_registrant_change_check(contact_id: Optional[builtins.str] = None,
                                domain_id: Optional[builtins.str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegistrantChangeCheckResult:
    """
    Get information on the requirements of a registrant change.

    > **Note:** The registrant change API is currently in developer preview and is subject to change.

    Get registrant change requirements for the `dnsimple.com` domain and the contact with ID `1234`:

    ```python
    import pulumi
    import pulumi_dnsimple as dnsimple

    example = dnsimple.get_registrant_change_check(domain_id="dnsimple.com",
        contact_id="1234")
    ```

    The following arguments are supported:

    * `domain_id` - (Required) The name or ID of the domain.
    * `contact_id` - (Required) The ID of the contact you are planning to change to.

    The following additional attributes are exported:

    * `contact_id` - The ID of the contact you are planning to change to.
    * `domain_id` - The name or ID of the domain.
    * `extended_attributes` - (List) A list of extended attributes that are required for the registrant change. (see below for nested schema)
    * `registry_owner_change` - (Boolean) Whether the registrant change is going to result in an owner change at the registry.

    <a id="nestedblock--extended_attributes"></a>
    """
    __args__ = dict()
    __args__['contactId'] = contact_id
    __args__['domainId'] = domain_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('dnsimple:index/getRegistrantChangeCheck:getRegistrantChangeCheck', __args__, opts=opts, typ=GetRegistrantChangeCheckResult).value

    return AwaitableGetRegistrantChangeCheckResult(
        contact_id=pulumi.get(__ret__, 'contact_id'),
        domain_id=pulumi.get(__ret__, 'domain_id'),
        extended_attributes=pulumi.get(__ret__, 'extended_attributes'),
        id=pulumi.get(__ret__, 'id'),
        registry_owner_change=pulumi.get(__ret__, 'registry_owner_change'))
def get_registrant_change_check_output(contact_id: Optional[pulumi.Input[builtins.str]] = None,
                                       domain_id: Optional[pulumi.Input[builtins.str]] = None,
                                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetRegistrantChangeCheckResult]:
    """
    Get information on the requirements of a registrant change.

    > **Note:** The registrant change API is currently in developer preview and is subject to change.

    Get registrant change requirements for the `dnsimple.com` domain and the contact with ID `1234`:

    ```python
    import pulumi
    import pulumi_dnsimple as dnsimple

    example = dnsimple.get_registrant_change_check(domain_id="dnsimple.com",
        contact_id="1234")
    ```

    The following arguments are supported:

    * `domain_id` - (Required) The name or ID of the domain.
    * `contact_id` - (Required) The ID of the contact you are planning to change to.

    The following additional attributes are exported:

    * `contact_id` - The ID of the contact you are planning to change to.
    * `domain_id` - The name or ID of the domain.
    * `extended_attributes` - (List) A list of extended attributes that are required for the registrant change. (see below for nested schema)
    * `registry_owner_change` - (Boolean) Whether the registrant change is going to result in an owner change at the registry.

    <a id="nestedblock--extended_attributes"></a>
    """
    __args__ = dict()
    __args__['contactId'] = contact_id
    __args__['domainId'] = domain_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('dnsimple:index/getRegistrantChangeCheck:getRegistrantChangeCheck', __args__, opts=opts, typ=GetRegistrantChangeCheckResult)
    return __ret__.apply(lambda __response__: GetRegistrantChangeCheckResult(
        contact_id=pulumi.get(__response__, 'contact_id'),
        domain_id=pulumi.get(__response__, 'domain_id'),
        extended_attributes=pulumi.get(__response__, 'extended_attributes'),
        id=pulumi.get(__response__, 'id'),
        registry_owner_change=pulumi.get(__response__, 'registry_owner_change')))
