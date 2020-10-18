# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['Record']


class Record(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[float]] = None,
                 ttl: Optional[pulumi.Input[float]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a DNSimple record resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_dnsimple as dnsimple

        # Add a record to the root domain
        foobar = dnsimple.Record("foobar",
            domain=var["dnsimple_domain"],
            name="",
            ttl=3600,
            type="A",
            value="192.168.0.11")
        ```

        ```python
        import pulumi
        import pulumi_dnsimple as dnsimple

        # Add a record to a sub-domain
        foobar = dnsimple.Record("foobar",
            domain=var["dnsimple_domain"],
            name="terraform",
            ttl=3600,
            type="A",
            value="192.168.0.11")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain: The domain to add the record to
        :param pulumi.Input[str] name: The name of the record
        :param pulumi.Input[float] priority: The priority of the record - only useful for some record types
        :param pulumi.Input[float] ttl: The TTL of the record
        :param pulumi.Input[str] type: The type of the record
        :param pulumi.Input[str] value: The value of the record
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if domain is None:
                raise TypeError("Missing required property 'domain'")
            __props__['domain'] = domain
            if name is None:
                raise TypeError("Missing required property 'name'")
            __props__['name'] = name
            __props__['priority'] = priority
            __props__['ttl'] = ttl
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            if value is None:
                raise TypeError("Missing required property 'value'")
            __props__['value'] = value
            __props__['domain_id'] = None
            __props__['hostname'] = None
        super(Record, __self__).__init__(
            'dnsimple:index/record:Record',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            domain: Optional[pulumi.Input[str]] = None,
            domain_id: Optional[pulumi.Input[str]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[float]] = None,
            ttl: Optional[pulumi.Input[float]] = None,
            type: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'Record':
        """
        Get an existing Record resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain: The domain to add the record to
        :param pulumi.Input[str] domain_id: The domain ID of the record
        :param pulumi.Input[str] hostname: The FQDN of the record
        :param pulumi.Input[str] name: The name of the record
        :param pulumi.Input[float] priority: The priority of the record - only useful for some record types
        :param pulumi.Input[float] ttl: The TTL of the record
        :param pulumi.Input[str] type: The type of the record
        :param pulumi.Input[str] value: The value of the record
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["domain"] = domain
        __props__["domain_id"] = domain_id
        __props__["hostname"] = hostname
        __props__["name"] = name
        __props__["priority"] = priority
        __props__["ttl"] = ttl
        __props__["type"] = type
        __props__["value"] = value
        return Record(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        The domain to add the record to
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[str]:
        """
        The domain ID of the record
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        """
        The FQDN of the record
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the record
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[float]:
        """
        The priority of the record - only useful for some record types
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[Optional[float]]:
        """
        The TTL of the record
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the record
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The value of the record
        """
        return pulumi.get(self, "value")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

