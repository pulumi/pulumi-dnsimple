# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DomainArgs', 'Domain']

@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str]):
        """
        The set of arguments for constructing a Domain resource.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _DomainState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[int]] = None,
                 auto_renew: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_whois: Optional[pulumi.Input[bool]] = None,
                 registrant_id: Optional[pulumi.Input[int]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 unicode_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Domain resources.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if auto_renew is not None:
            pulumi.set(__self__, "auto_renew", auto_renew)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if private_whois is not None:
            pulumi.set(__self__, "private_whois", private_whois)
        if registrant_id is not None:
            pulumi.set(__self__, "registrant_id", registrant_id)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if unicode_name is not None:
            pulumi.set(__self__, "unicode_name", unicode_name)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "auto_renew")

    @auto_renew.setter
    def auto_renew(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_renew", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="privateWhois")
    def private_whois(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "private_whois")

    @private_whois.setter
    def private_whois(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "private_whois", value)

    @property
    @pulumi.getter(name="registrantId")
    def registrant_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "registrant_id")

    @registrant_id.setter
    def registrant_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "registrant_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="unicodeName")
    def unicode_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "unicode_name")

    @unicode_name.setter
    def unicode_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unicode_name", value)


class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Domain resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Domain resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainArgs.__new__(DomainArgs)

            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["account_id"] = None
            __props__.__dict__["auto_renew"] = None
            __props__.__dict__["private_whois"] = None
            __props__.__dict__["registrant_id"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["unicode_name"] = None
        super(Domain, __self__).__init__(
            'dnsimple:index/domain:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[int]] = None,
            auto_renew: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            private_whois: Optional[pulumi.Input[bool]] = None,
            registrant_id: Optional[pulumi.Input[int]] = None,
            state: Optional[pulumi.Input[str]] = None,
            unicode_name: Optional[pulumi.Input[str]] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DomainState.__new__(_DomainState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["auto_renew"] = auto_renew
        __props__.__dict__["name"] = name
        __props__.__dict__["private_whois"] = private_whois
        __props__.__dict__["registrant_id"] = registrant_id
        __props__.__dict__["state"] = state
        __props__.__dict__["unicode_name"] = unicode_name
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "auto_renew")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateWhois")
    def private_whois(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "private_whois")

    @property
    @pulumi.getter(name="registrantId")
    def registrant_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "registrant_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="unicodeName")
    def unicode_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "unicode_name")

