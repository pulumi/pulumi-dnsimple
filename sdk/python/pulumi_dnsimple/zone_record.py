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

__all__ = ['ZoneRecordArgs', 'ZoneRecord']

@pulumi.input_type
class ZoneRecordArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[_builtins.str],
                 type: pulumi.Input[_builtins.str],
                 value: pulumi.Input[_builtins.str],
                 zone_name: pulumi.Input[_builtins.str],
                 priority: Optional[pulumi.Input[_builtins.int]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = None,
                 ttl: Optional[pulumi.Input[_builtins.int]] = None):
        """
        The set of arguments for constructing a ZoneRecord resource.
        :param pulumi.Input[_builtins.str] name: The name of the record
        :param pulumi.Input[_builtins.str] type: The type of the record
        :param pulumi.Input[_builtins.str] value: The value of the record
        :param pulumi.Input[_builtins.str] zone_name: The zone name to add the record to
        :param pulumi.Input[_builtins.int] priority: The priority of the record - only useful for some record types
        :param pulumi.Input[Sequence[pulumi.Input[_builtins.str]]] regions: A list of regions to serve the record from. You can find a list of supported values in our [developer documentation](https://developer.dnsimple.com/v2/zones/records/).
        :param pulumi.Input[_builtins.int] ttl: The TTL of the record - defaults to 3600
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)
        pulumi.set(__self__, "zone_name", zone_name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if regions is not None:
            pulumi.set(__self__, "regions", regions)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)

    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        """
        The name of the record
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]):
        pulumi.set(self, "name", value)

    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        """
        The type of the record
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]):
        pulumi.set(self, "type", value)

    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        """
        The value of the record
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]):
        pulumi.set(self, "value", value)

    @_builtins.property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> pulumi.Input[_builtins.str]:
        """
        The zone name to add the record to
        """
        return pulumi.get(self, "zone_name")

    @zone_name.setter
    def zone_name(self, value: pulumi.Input[_builtins.str]):
        pulumi.set(self, "zone_name", value)

    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        """
        The priority of the record - only useful for some record types
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]):
        pulumi.set(self, "priority", value)

    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        """
        A list of regions to serve the record from. You can find a list of supported values in our [developer documentation](https://developer.dnsimple.com/v2/zones/records/).
        """
        return pulumi.get(self, "regions")

    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]):
        pulumi.set(self, "regions", value)

    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        """
        The TTL of the record - defaults to 3600
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.int]]):
        pulumi.set(self, "ttl", value)


@pulumi.input_type
class _ZoneRecordState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[_builtins.str]] = None,
                 name_normalized: Optional[pulumi.Input[_builtins.str]] = None,
                 priority: Optional[pulumi.Input[_builtins.int]] = None,
                 qualified_name: Optional[pulumi.Input[_builtins.str]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = None,
                 ttl: Optional[pulumi.Input[_builtins.int]] = None,
                 type: Optional[pulumi.Input[_builtins.str]] = None,
                 value: Optional[pulumi.Input[_builtins.str]] = None,
                 value_normalized: Optional[pulumi.Input[_builtins.str]] = None,
                 zone_id: Optional[pulumi.Input[_builtins.str]] = None,
                 zone_name: Optional[pulumi.Input[_builtins.str]] = None):
        """
        Input properties used for looking up and filtering ZoneRecord resources.
        :param pulumi.Input[_builtins.str] name: The name of the record
        :param pulumi.Input[_builtins.int] priority: The priority of the record - only useful for some record types
        :param pulumi.Input[_builtins.str] qualified_name: The FQDN of the record
        :param pulumi.Input[Sequence[pulumi.Input[_builtins.str]]] regions: A list of regions to serve the record from. You can find a list of supported values in our [developer documentation](https://developer.dnsimple.com/v2/zones/records/).
        :param pulumi.Input[_builtins.int] ttl: The TTL of the record - defaults to 3600
        :param pulumi.Input[_builtins.str] type: The type of the record
        :param pulumi.Input[_builtins.str] value: The value of the record
        :param pulumi.Input[_builtins.str] value_normalized: The normalized value of the record
        :param pulumi.Input[_builtins.str] zone_id: The zone ID of the record
        :param pulumi.Input[_builtins.str] zone_name: The zone name to add the record to
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if name_normalized is not None:
            pulumi.set(__self__, "name_normalized", name_normalized)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if qualified_name is not None:
            pulumi.set(__self__, "qualified_name", qualified_name)
        if regions is not None:
            pulumi.set(__self__, "regions", regions)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)
        if value_normalized is not None:
            pulumi.set(__self__, "value_normalized", value_normalized)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)
        if zone_name is not None:
            pulumi.set(__self__, "zone_name", zone_name)

    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The name of the record
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "name", value)

    @_builtins.property
    @pulumi.getter(name="nameNormalized")
    def name_normalized(self) -> Optional[pulumi.Input[_builtins.str]]:
        return pulumi.get(self, "name_normalized")

    @name_normalized.setter
    def name_normalized(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "name_normalized", value)

    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        """
        The priority of the record - only useful for some record types
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]):
        pulumi.set(self, "priority", value)

    @_builtins.property
    @pulumi.getter(name="qualifiedName")
    def qualified_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The FQDN of the record
        """
        return pulumi.get(self, "qualified_name")

    @qualified_name.setter
    def qualified_name(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "qualified_name", value)

    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        """
        A list of regions to serve the record from. You can find a list of supported values in our [developer documentation](https://developer.dnsimple.com/v2/zones/records/).
        """
        return pulumi.get(self, "regions")

    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]):
        pulumi.set(self, "regions", value)

    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        """
        The TTL of the record - defaults to 3600
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.int]]):
        pulumi.set(self, "ttl", value)

    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The type of the record
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "type", value)

    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The value of the record
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "value", value)

    @_builtins.property
    @pulumi.getter(name="valueNormalized")
    def value_normalized(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The normalized value of the record
        """
        return pulumi.get(self, "value_normalized")

    @value_normalized.setter
    def value_normalized(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "value_normalized", value)

    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The zone ID of the record
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "zone_id", value)

    @_builtins.property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The zone name to add the record to
        """
        return pulumi.get(self, "zone_name")

    @zone_name.setter
    def zone_name(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "zone_name", value)


@pulumi.type_token("dnsimple:index/zoneRecord:ZoneRecord")
class ZoneRecord(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[_builtins.str]] = None,
                 priority: Optional[pulumi.Input[_builtins.int]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = None,
                 ttl: Optional[pulumi.Input[_builtins.int]] = None,
                 type: Optional[pulumi.Input[_builtins.str]] = None,
                 value: Optional[pulumi.Input[_builtins.str]] = None,
                 zone_name: Optional[pulumi.Input[_builtins.str]] = None,
                 __props__=None):
        """
        Provides a DNSimple zone record resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_dnsimple as dnsimple

        # Add a record to the root domain
        foobar = dnsimple.ZoneRecord("foobar",
            zone_name=dnsimple_domain,
            name="",
            value="192.168.0.11",
            type="A",
            ttl=3600)
        ```

        ```python
        import pulumi
        import pulumi_dnsimple as dnsimple

        # Add a record to a sub-domain
        foobar = dnsimple.ZoneRecord("foobar",
            zone_name=dnsimple_domain,
            name="terraform",
            value="192.168.0.11",
            type="A",
            ttl=3600)
        ```

        ## Import

        DNSimple resources can be imported using their parent zone name (domain name) and numeric record ID.

        **Importing record example.com with record ID 1234**

        bash

        ```sh
        $ pulumi import dnsimple:index/zoneRecord:ZoneRecord resource_name example.com_1234
        ```

        **Importing record www.example.com with record ID 1234**

        bash

        ```sh
        $ pulumi import dnsimple:index/zoneRecord:ZoneRecord resource_name example.com_1234
        ```

        The record ID can be found in the URL when editing a record on the DNSimple web dashboard.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[_builtins.str] name: The name of the record
        :param pulumi.Input[_builtins.int] priority: The priority of the record - only useful for some record types
        :param pulumi.Input[Sequence[pulumi.Input[_builtins.str]]] regions: A list of regions to serve the record from. You can find a list of supported values in our [developer documentation](https://developer.dnsimple.com/v2/zones/records/).
        :param pulumi.Input[_builtins.int] ttl: The TTL of the record - defaults to 3600
        :param pulumi.Input[_builtins.str] type: The type of the record
        :param pulumi.Input[_builtins.str] value: The value of the record
        :param pulumi.Input[_builtins.str] zone_name: The zone name to add the record to
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ZoneRecordArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a DNSimple zone record resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_dnsimple as dnsimple

        # Add a record to the root domain
        foobar = dnsimple.ZoneRecord("foobar",
            zone_name=dnsimple_domain,
            name="",
            value="192.168.0.11",
            type="A",
            ttl=3600)
        ```

        ```python
        import pulumi
        import pulumi_dnsimple as dnsimple

        # Add a record to a sub-domain
        foobar = dnsimple.ZoneRecord("foobar",
            zone_name=dnsimple_domain,
            name="terraform",
            value="192.168.0.11",
            type="A",
            ttl=3600)
        ```

        ## Import

        DNSimple resources can be imported using their parent zone name (domain name) and numeric record ID.

        **Importing record example.com with record ID 1234**

        bash

        ```sh
        $ pulumi import dnsimple:index/zoneRecord:ZoneRecord resource_name example.com_1234
        ```

        **Importing record www.example.com with record ID 1234**

        bash

        ```sh
        $ pulumi import dnsimple:index/zoneRecord:ZoneRecord resource_name example.com_1234
        ```

        The record ID can be found in the URL when editing a record on the DNSimple web dashboard.

        :param str resource_name: The name of the resource.
        :param ZoneRecordArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZoneRecordArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[_builtins.str]] = None,
                 priority: Optional[pulumi.Input[_builtins.int]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = None,
                 ttl: Optional[pulumi.Input[_builtins.int]] = None,
                 type: Optional[pulumi.Input[_builtins.str]] = None,
                 value: Optional[pulumi.Input[_builtins.str]] = None,
                 zone_name: Optional[pulumi.Input[_builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZoneRecordArgs.__new__(ZoneRecordArgs)

            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["priority"] = priority
            __props__.__dict__["regions"] = regions
            __props__.__dict__["ttl"] = ttl
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = value
            if zone_name is None and not opts.urn:
                raise TypeError("Missing required property 'zone_name'")
            __props__.__dict__["zone_name"] = zone_name
            __props__.__dict__["name_normalized"] = None
            __props__.__dict__["qualified_name"] = None
            __props__.__dict__["value_normalized"] = None
            __props__.__dict__["zone_id"] = None
        super(ZoneRecord, __self__).__init__(
            'dnsimple:index/zoneRecord:ZoneRecord',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[_builtins.str]] = None,
            name_normalized: Optional[pulumi.Input[_builtins.str]] = None,
            priority: Optional[pulumi.Input[_builtins.int]] = None,
            qualified_name: Optional[pulumi.Input[_builtins.str]] = None,
            regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = None,
            ttl: Optional[pulumi.Input[_builtins.int]] = None,
            type: Optional[pulumi.Input[_builtins.str]] = None,
            value: Optional[pulumi.Input[_builtins.str]] = None,
            value_normalized: Optional[pulumi.Input[_builtins.str]] = None,
            zone_id: Optional[pulumi.Input[_builtins.str]] = None,
            zone_name: Optional[pulumi.Input[_builtins.str]] = None) -> 'ZoneRecord':
        """
        Get an existing ZoneRecord resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[_builtins.str] name: The name of the record
        :param pulumi.Input[_builtins.int] priority: The priority of the record - only useful for some record types
        :param pulumi.Input[_builtins.str] qualified_name: The FQDN of the record
        :param pulumi.Input[Sequence[pulumi.Input[_builtins.str]]] regions: A list of regions to serve the record from. You can find a list of supported values in our [developer documentation](https://developer.dnsimple.com/v2/zones/records/).
        :param pulumi.Input[_builtins.int] ttl: The TTL of the record - defaults to 3600
        :param pulumi.Input[_builtins.str] type: The type of the record
        :param pulumi.Input[_builtins.str] value: The value of the record
        :param pulumi.Input[_builtins.str] value_normalized: The normalized value of the record
        :param pulumi.Input[_builtins.str] zone_id: The zone ID of the record
        :param pulumi.Input[_builtins.str] zone_name: The zone name to add the record to
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZoneRecordState.__new__(_ZoneRecordState)

        __props__.__dict__["name"] = name
        __props__.__dict__["name_normalized"] = name_normalized
        __props__.__dict__["priority"] = priority
        __props__.__dict__["qualified_name"] = qualified_name
        __props__.__dict__["regions"] = regions
        __props__.__dict__["ttl"] = ttl
        __props__.__dict__["type"] = type
        __props__.__dict__["value"] = value
        __props__.__dict__["value_normalized"] = value_normalized
        __props__.__dict__["zone_id"] = zone_id
        __props__.__dict__["zone_name"] = zone_name
        return ZoneRecord(resource_name, opts=opts, __props__=__props__)

    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        """
        The name of the record
        """
        return pulumi.get(self, "name")

    @_builtins.property
    @pulumi.getter(name="nameNormalized")
    def name_normalized(self) -> pulumi.Output[_builtins.str]:
        return pulumi.get(self, "name_normalized")

    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[_builtins.int]:
        """
        The priority of the record - only useful for some record types
        """
        return pulumi.get(self, "priority")

    @_builtins.property
    @pulumi.getter(name="qualifiedName")
    def qualified_name(self) -> pulumi.Output[_builtins.str]:
        """
        The FQDN of the record
        """
        return pulumi.get(self, "qualified_name")

    @_builtins.property
    @pulumi.getter
    def regions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        """
        A list of regions to serve the record from. You can find a list of supported values in our [developer documentation](https://developer.dnsimple.com/v2/zones/records/).
        """
        return pulumi.get(self, "regions")

    @_builtins.property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[_builtins.int]:
        """
        The TTL of the record - defaults to 3600
        """
        return pulumi.get(self, "ttl")

    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        """
        The type of the record
        """
        return pulumi.get(self, "type")

    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Output[_builtins.str]:
        """
        The value of the record
        """
        return pulumi.get(self, "value")

    @_builtins.property
    @pulumi.getter(name="valueNormalized")
    def value_normalized(self) -> pulumi.Output[_builtins.str]:
        """
        The normalized value of the record
        """
        return pulumi.get(self, "value_normalized")

    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[_builtins.str]:
        """
        The zone ID of the record
        """
        return pulumi.get(self, "zone_id")

    @_builtins.property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> pulumi.Output[_builtins.str]:
        """
        The zone name to add the record to
        """
        return pulumi.get(self, "zone_name")

