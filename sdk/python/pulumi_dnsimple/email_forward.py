# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['EmailForwardArgs', 'EmailForward']

@pulumi.input_type
class EmailForwardArgs:
    def __init__(__self__, *,
                 alias_name: pulumi.Input[str],
                 destination_email: pulumi.Input[str],
                 domain: pulumi.Input[str]):
        """
        The set of arguments for constructing a EmailForward resource.
        """
        pulumi.set(__self__, "alias_name", alias_name)
        pulumi.set(__self__, "destination_email", destination_email)
        pulumi.set(__self__, "domain", domain)

    @property
    @pulumi.getter(name="aliasName")
    def alias_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "alias_name")

    @alias_name.setter
    def alias_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "alias_name", value)

    @property
    @pulumi.getter(name="destinationEmail")
    def destination_email(self) -> pulumi.Input[str]:
        return pulumi.get(self, "destination_email")

    @destination_email.setter
    def destination_email(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination_email", value)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Input[str]:
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain", value)


@pulumi.input_type
class _EmailForwardState:
    def __init__(__self__, *,
                 alias_email: Optional[pulumi.Input[str]] = None,
                 alias_name: Optional[pulumi.Input[str]] = None,
                 destination_email: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering EmailForward resources.
        """
        if alias_email is not None:
            pulumi.set(__self__, "alias_email", alias_email)
        if alias_name is not None:
            pulumi.set(__self__, "alias_name", alias_name)
        if destination_email is not None:
            pulumi.set(__self__, "destination_email", destination_email)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)

    @property
    @pulumi.getter(name="aliasEmail")
    def alias_email(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "alias_email")

    @alias_email.setter
    def alias_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alias_email", value)

    @property
    @pulumi.getter(name="aliasName")
    def alias_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "alias_name")

    @alias_name.setter
    def alias_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alias_name", value)

    @property
    @pulumi.getter(name="destinationEmail")
    def destination_email(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "destination_email")

    @destination_email.setter
    def destination_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_email", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)


class EmailForward(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias_name: Optional[pulumi.Input[str]] = None,
                 destination_email: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a EmailForward resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EmailForwardArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a EmailForward resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param EmailForwardArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EmailForwardArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias_name: Optional[pulumi.Input[str]] = None,
                 destination_email: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EmailForwardArgs.__new__(EmailForwardArgs)

            if alias_name is None and not opts.urn:
                raise TypeError("Missing required property 'alias_name'")
            __props__.__dict__["alias_name"] = alias_name
            if destination_email is None and not opts.urn:
                raise TypeError("Missing required property 'destination_email'")
            __props__.__dict__["destination_email"] = destination_email
            if domain is None and not opts.urn:
                raise TypeError("Missing required property 'domain'")
            __props__.__dict__["domain"] = domain
            __props__.__dict__["alias_email"] = None
        super(EmailForward, __self__).__init__(
            'dnsimple:index/emailForward:EmailForward',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            alias_email: Optional[pulumi.Input[str]] = None,
            alias_name: Optional[pulumi.Input[str]] = None,
            destination_email: Optional[pulumi.Input[str]] = None,
            domain: Optional[pulumi.Input[str]] = None) -> 'EmailForward':
        """
        Get an existing EmailForward resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EmailForwardState.__new__(_EmailForwardState)

        __props__.__dict__["alias_email"] = alias_email
        __props__.__dict__["alias_name"] = alias_name
        __props__.__dict__["destination_email"] = destination_email
        __props__.__dict__["domain"] = domain
        return EmailForward(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aliasEmail")
    def alias_email(self) -> pulumi.Output[str]:
        return pulumi.get(self, "alias_email")

    @property
    @pulumi.getter(name="aliasName")
    def alias_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "alias_name")

    @property
    @pulumi.getter(name="destinationEmail")
    def destination_email(self) -> pulumi.Output[str]:
        return pulumi.get(self, "destination_email")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        return pulumi.get(self, "domain")

