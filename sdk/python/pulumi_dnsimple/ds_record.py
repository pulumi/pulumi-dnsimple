# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DsRecordArgs', 'DsRecord']

@pulumi.input_type
class DsRecordArgs:
    def __init__(__self__, *,
                 algorithm: pulumi.Input[str],
                 domain: pulumi.Input[str],
                 digest: Optional[pulumi.Input[str]] = None,
                 digest_type: Optional[pulumi.Input[str]] = None,
                 keytag: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DsRecord resource.
        :param pulumi.Input[str] algorithm: DNSSEC algorithm number as a string.
        :param pulumi.Input[str] domain: The domain name or numeric ID to create the delegation signer record for.
        :param pulumi.Input[str] digest: The hexidecimal representation of the digest of the corresponding DNSKEY record.
        :param pulumi.Input[str] digest_type: DNSSEC digest type number as a string.
        :param pulumi.Input[str] keytag: A keytag that references the corresponding DNSKEY record.
        :param pulumi.Input[str] public_key: A public key that references the corresponding DNSKEY record.
               
               # Attributes Reference
        """
        pulumi.set(__self__, "algorithm", algorithm)
        pulumi.set(__self__, "domain", domain)
        if digest is not None:
            pulumi.set(__self__, "digest", digest)
        if digest_type is not None:
            pulumi.set(__self__, "digest_type", digest_type)
        if keytag is not None:
            pulumi.set(__self__, "keytag", keytag)
        if public_key is not None:
            pulumi.set(__self__, "public_key", public_key)

    @property
    @pulumi.getter
    def algorithm(self) -> pulumi.Input[str]:
        """
        DNSSEC algorithm number as a string.
        """
        return pulumi.get(self, "algorithm")

    @algorithm.setter
    def algorithm(self, value: pulumi.Input[str]):
        pulumi.set(self, "algorithm", value)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Input[str]:
        """
        The domain name or numeric ID to create the delegation signer record for.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def digest(self) -> Optional[pulumi.Input[str]]:
        """
        The hexidecimal representation of the digest of the corresponding DNSKEY record.
        """
        return pulumi.get(self, "digest")

    @digest.setter
    def digest(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "digest", value)

    @property
    @pulumi.getter(name="digestType")
    def digest_type(self) -> Optional[pulumi.Input[str]]:
        """
        DNSSEC digest type number as a string.
        """
        return pulumi.get(self, "digest_type")

    @digest_type.setter
    def digest_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "digest_type", value)

    @property
    @pulumi.getter
    def keytag(self) -> Optional[pulumi.Input[str]]:
        """
        A keytag that references the corresponding DNSKEY record.
        """
        return pulumi.get(self, "keytag")

    @keytag.setter
    def keytag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "keytag", value)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[str]]:
        """
        A public key that references the corresponding DNSKEY record.

        # Attributes Reference
        """
        return pulumi.get(self, "public_key")

    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_key", value)


@pulumi.input_type
class _DsRecordState:
    def __init__(__self__, *,
                 algorithm: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 digest: Optional[pulumi.Input[str]] = None,
                 digest_type: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 keytag: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DsRecord resources.
        :param pulumi.Input[str] algorithm: DNSSEC algorithm number as a string.
        :param pulumi.Input[str] created_at: The time the DS record was created at.
        :param pulumi.Input[str] digest: The hexidecimal representation of the digest of the corresponding DNSKEY record.
        :param pulumi.Input[str] digest_type: DNSSEC digest type number as a string.
        :param pulumi.Input[str] domain: The domain name or numeric ID to create the delegation signer record for.
        :param pulumi.Input[str] keytag: A keytag that references the corresponding DNSKEY record.
        :param pulumi.Input[str] public_key: A public key that references the corresponding DNSKEY record.
               
               # Attributes Reference
        :param pulumi.Input[str] updated_at: The time the DS record was last updated at.
        """
        if algorithm is not None:
            pulumi.set(__self__, "algorithm", algorithm)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if digest is not None:
            pulumi.set(__self__, "digest", digest)
        if digest_type is not None:
            pulumi.set(__self__, "digest_type", digest_type)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if keytag is not None:
            pulumi.set(__self__, "keytag", keytag)
        if public_key is not None:
            pulumi.set(__self__, "public_key", public_key)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter
    def algorithm(self) -> Optional[pulumi.Input[str]]:
        """
        DNSSEC algorithm number as a string.
        """
        return pulumi.get(self, "algorithm")

    @algorithm.setter
    def algorithm(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "algorithm", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time the DS record was created at.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def digest(self) -> Optional[pulumi.Input[str]]:
        """
        The hexidecimal representation of the digest of the corresponding DNSKEY record.
        """
        return pulumi.get(self, "digest")

    @digest.setter
    def digest(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "digest", value)

    @property
    @pulumi.getter(name="digestType")
    def digest_type(self) -> Optional[pulumi.Input[str]]:
        """
        DNSSEC digest type number as a string.
        """
        return pulumi.get(self, "digest_type")

    @digest_type.setter
    def digest_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "digest_type", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The domain name or numeric ID to create the delegation signer record for.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def keytag(self) -> Optional[pulumi.Input[str]]:
        """
        A keytag that references the corresponding DNSKEY record.
        """
        return pulumi.get(self, "keytag")

    @keytag.setter
    def keytag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "keytag", value)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[str]]:
        """
        A public key that references the corresponding DNSKEY record.

        # Attributes Reference
        """
        return pulumi.get(self, "public_key")

    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_key", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time the DS record was last updated at.
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


class DsRecord(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 algorithm: Optional[pulumi.Input[str]] = None,
                 digest: Optional[pulumi.Input[str]] = None,
                 digest_type: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 keytag: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a DNSimple domain delegation signer record resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_dnsimple as dnsimple

        foobar = dnsimple.DsRecord("foobar",
            domain=var["dnsimple"]["domain"],
            algorithm="8",
            digest="6CEEA0117A02480216EBF745A7B690F938860074E4AD11AF2AC573007205682B",
            digest_type="2",
            key_tag="12345")
        ```

        ## Import

        DNSimple DS record resources can be imported using their domain ID and numeric record ID. bash

        ```sh
         $ pulumi import dnsimple:index/dsRecord:DsRecord resource_name example.com_5678
        ```

         The record ID can be found within [DNSimple DNSSEC API](https://developer.dnsimple.com/v2/domains/dnssec/#listDomainDelegationSignerRecords). Check out [Authentication](https://developer.dnsimple.com/v2/#authentication) in API Overview for available options. bash curl -u 'EMAIL:PASSWORD' https://api.dnsimple.com/v2/1010/domains/example.com/ds_records | jq {

         "data"[

         {

         "id"24,

         "domain_id"1010,

         "algorithm""8",

         "digest""C1F6E04A5A61FBF65BF9DC8294C363CF11C89E802D926BDAB79C55D27BEFA94F",

         "digest_type""2",

         "keytag""44620",

         "public_key"null,

         "created_at""2017-03-03T13:49:58Z",

         "updated_at""2017-03-03T13:49:58Z"

         }

         ],

         "pagination"{

         "current_page"1,

         "per_page"30,

         "total_entries"1,

         "total_pages"1

         } }

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] algorithm: DNSSEC algorithm number as a string.
        :param pulumi.Input[str] digest: The hexidecimal representation of the digest of the corresponding DNSKEY record.
        :param pulumi.Input[str] digest_type: DNSSEC digest type number as a string.
        :param pulumi.Input[str] domain: The domain name or numeric ID to create the delegation signer record for.
        :param pulumi.Input[str] keytag: A keytag that references the corresponding DNSKEY record.
        :param pulumi.Input[str] public_key: A public key that references the corresponding DNSKEY record.
               
               # Attributes Reference
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DsRecordArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a DNSimple domain delegation signer record resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_dnsimple as dnsimple

        foobar = dnsimple.DsRecord("foobar",
            domain=var["dnsimple"]["domain"],
            algorithm="8",
            digest="6CEEA0117A02480216EBF745A7B690F938860074E4AD11AF2AC573007205682B",
            digest_type="2",
            key_tag="12345")
        ```

        ## Import

        DNSimple DS record resources can be imported using their domain ID and numeric record ID. bash

        ```sh
         $ pulumi import dnsimple:index/dsRecord:DsRecord resource_name example.com_5678
        ```

         The record ID can be found within [DNSimple DNSSEC API](https://developer.dnsimple.com/v2/domains/dnssec/#listDomainDelegationSignerRecords). Check out [Authentication](https://developer.dnsimple.com/v2/#authentication) in API Overview for available options. bash curl -u 'EMAIL:PASSWORD' https://api.dnsimple.com/v2/1010/domains/example.com/ds_records | jq {

         "data"[

         {

         "id"24,

         "domain_id"1010,

         "algorithm""8",

         "digest""C1F6E04A5A61FBF65BF9DC8294C363CF11C89E802D926BDAB79C55D27BEFA94F",

         "digest_type""2",

         "keytag""44620",

         "public_key"null,

         "created_at""2017-03-03T13:49:58Z",

         "updated_at""2017-03-03T13:49:58Z"

         }

         ],

         "pagination"{

         "current_page"1,

         "per_page"30,

         "total_entries"1,

         "total_pages"1

         } }

        :param str resource_name: The name of the resource.
        :param DsRecordArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DsRecordArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 algorithm: Optional[pulumi.Input[str]] = None,
                 digest: Optional[pulumi.Input[str]] = None,
                 digest_type: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 keytag: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DsRecordArgs.__new__(DsRecordArgs)

            if algorithm is None and not opts.urn:
                raise TypeError("Missing required property 'algorithm'")
            __props__.__dict__["algorithm"] = algorithm
            __props__.__dict__["digest"] = digest
            __props__.__dict__["digest_type"] = digest_type
            if domain is None and not opts.urn:
                raise TypeError("Missing required property 'domain'")
            __props__.__dict__["domain"] = domain
            __props__.__dict__["keytag"] = keytag
            __props__.__dict__["public_key"] = public_key
            __props__.__dict__["created_at"] = None
            __props__.__dict__["updated_at"] = None
        super(DsRecord, __self__).__init__(
            'dnsimple:index/dsRecord:DsRecord',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            algorithm: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            digest: Optional[pulumi.Input[str]] = None,
            digest_type: Optional[pulumi.Input[str]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            keytag: Optional[pulumi.Input[str]] = None,
            public_key: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'DsRecord':
        """
        Get an existing DsRecord resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] algorithm: DNSSEC algorithm number as a string.
        :param pulumi.Input[str] created_at: The time the DS record was created at.
        :param pulumi.Input[str] digest: The hexidecimal representation of the digest of the corresponding DNSKEY record.
        :param pulumi.Input[str] digest_type: DNSSEC digest type number as a string.
        :param pulumi.Input[str] domain: The domain name or numeric ID to create the delegation signer record for.
        :param pulumi.Input[str] keytag: A keytag that references the corresponding DNSKEY record.
        :param pulumi.Input[str] public_key: A public key that references the corresponding DNSKEY record.
               
               # Attributes Reference
        :param pulumi.Input[str] updated_at: The time the DS record was last updated at.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DsRecordState.__new__(_DsRecordState)

        __props__.__dict__["algorithm"] = algorithm
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["digest"] = digest
        __props__.__dict__["digest_type"] = digest_type
        __props__.__dict__["domain"] = domain
        __props__.__dict__["keytag"] = keytag
        __props__.__dict__["public_key"] = public_key
        __props__.__dict__["updated_at"] = updated_at
        return DsRecord(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def algorithm(self) -> pulumi.Output[str]:
        """
        DNSSEC algorithm number as a string.
        """
        return pulumi.get(self, "algorithm")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time the DS record was created at.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def digest(self) -> pulumi.Output[Optional[str]]:
        """
        The hexidecimal representation of the digest of the corresponding DNSKEY record.
        """
        return pulumi.get(self, "digest")

    @property
    @pulumi.getter(name="digestType")
    def digest_type(self) -> pulumi.Output[Optional[str]]:
        """
        DNSSEC digest type number as a string.
        """
        return pulumi.get(self, "digest_type")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        The domain name or numeric ID to create the delegation signer record for.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def keytag(self) -> pulumi.Output[Optional[str]]:
        """
        A keytag that references the corresponding DNSKEY record.
        """
        return pulumi.get(self, "keytag")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[Optional[str]]:
        """
        A public key that references the corresponding DNSKEY record.

        # Attributes Reference
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The time the DS record was last updated at.
        """
        return pulumi.get(self, "updated_at")

