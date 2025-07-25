# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins as _builtins
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

__all__ = [
    'GetZoneResult',
    'AwaitableGetZoneResult',
    'get_zone',
    'get_zone_output',
]

@pulumi.output_type
class GetZoneResult:
    """
    A collection of values returned by getZone.
    """
    def __init__(__self__, account_id=None, id=None, name=None, reverse=None):
        if account_id and not isinstance(account_id, int):
            raise TypeError("Expected argument 'account_id' to be a int")
        pulumi.set(__self__, "account_id", account_id)
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if reverse and not isinstance(reverse, bool):
            raise TypeError("Expected argument 'reverse' to be a bool")
        pulumi.set(__self__, "reverse", reverse)

    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.int:
        return pulumi.get(self, "account_id")

    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.int:
        return pulumi.get(self, "id")

    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        return pulumi.get(self, "name")

    @_builtins.property
    @pulumi.getter
    def reverse(self) -> _builtins.bool:
        return pulumi.get(self, "reverse")


class AwaitableGetZoneResult(GetZoneResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZoneResult(
            account_id=self.account_id,
            id=self.id,
            name=self.name,
            reverse=self.reverse)


def get_zone(name: Optional[_builtins.str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZoneResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('dnsimple:index/getZone:getZone', __args__, opts=opts, typ=GetZoneResult).value

    return AwaitableGetZoneResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        reverse=pulumi.get(__ret__, 'reverse'))
def get_zone_output(name: Optional[pulumi.Input[_builtins.str]] = None,
                    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetZoneResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('dnsimple:index/getZone:getZone', __args__, opts=opts, typ=GetZoneResult)
    return __ret__.apply(lambda __response__: GetZoneResult(
        account_id=pulumi.get(__response__, 'account_id'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        reverse=pulumi.get(__response__, 'reverse')))
