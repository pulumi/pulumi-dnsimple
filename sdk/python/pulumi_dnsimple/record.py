# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Record(pulumi.CustomResource):
    domain: pulumi.Output[str]
    """
    The domain to add the record to
    """
    domain_id: pulumi.Output[str]
    """
    The domain ID of the record
    """
    hostname: pulumi.Output[str]
    """
    The FQDN of the record
    """
    name: pulumi.Output[str]
    """
    The name of the record
    """
    priority: pulumi.Output[float]
    """
    The priority of the record - only useful for some record types
    """
    ttl: pulumi.Output[float]
    """
    The TTL of the record
    """
    type: pulumi.Output[str]
    """
    The type of the record
    """
    value: pulumi.Output[str]
    """
    The value of the record
    """
    def __init__(__self__, resource_name, opts=None, domain=None, name=None, priority=None, ttl=None, type=None, value=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a DNSimple record resource.



        > This content is derived from https://github.com/terraform-providers/terraform-provider-dnsimple/blob/master/website/docs/r/record.html.markdown.

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
            opts.version = utilities.get_version()
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
    def get(resource_name, id, opts=None, domain=None, domain_id=None, hostname=None, name=None, priority=None, ttl=None, type=None, value=None):
        """
        Get an existing Record resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
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
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

