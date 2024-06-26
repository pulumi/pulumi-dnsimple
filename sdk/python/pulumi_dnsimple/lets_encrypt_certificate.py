# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['LetsEncryptCertificateArgs', 'LetsEncryptCertificate']

@pulumi.input_type
class LetsEncryptCertificateArgs:
    def __init__(__self__, *,
                 auto_renew: pulumi.Input[bool],
                 name: pulumi.Input[str],
                 contact_id: Optional[pulumi.Input[int]] = None,
                 domain_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LetsEncryptCertificate resource.
        :param pulumi.Input[bool] auto_renew: Set to true if the certificate will auto-renew
        :param pulumi.Input[str] name: The certificate name
        :param pulumi.Input[int] contact_id: The contact id for the certificate
        :param pulumi.Input[str] domain_id: The domain to be issued the certificate for
        """
        pulumi.set(__self__, "auto_renew", auto_renew)
        pulumi.set(__self__, "name", name)
        if contact_id is not None:
            warnings.warn("""contact_id is deprecated and has no effect. The attribute will be removed in the next major version.""", DeprecationWarning)
            pulumi.log.warn("""contact_id is deprecated: contact_id is deprecated and has no effect. The attribute will be removed in the next major version.""")
        if contact_id is not None:
            pulumi.set(__self__, "contact_id", contact_id)
        if domain_id is not None:
            pulumi.set(__self__, "domain_id", domain_id)

    @property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> pulumi.Input[bool]:
        """
        Set to true if the certificate will auto-renew
        """
        return pulumi.get(self, "auto_renew")

    @auto_renew.setter
    def auto_renew(self, value: pulumi.Input[bool]):
        pulumi.set(self, "auto_renew", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The certificate name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="contactId")
    @_utilities.deprecated("""contact_id is deprecated and has no effect. The attribute will be removed in the next major version.""")
    def contact_id(self) -> Optional[pulumi.Input[int]]:
        """
        The contact id for the certificate
        """
        return pulumi.get(self, "contact_id")

    @contact_id.setter
    def contact_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "contact_id", value)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[str]]:
        """
        The domain to be issued the certificate for
        """
        return pulumi.get(self, "domain_id")

    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_id", value)


@pulumi.input_type
class _LetsEncryptCertificateState:
    def __init__(__self__, *,
                 authority_identifier: Optional[pulumi.Input[str]] = None,
                 auto_renew: Optional[pulumi.Input[bool]] = None,
                 contact_id: Optional[pulumi.Input[int]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 csr: Optional[pulumi.Input[str]] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 expires_on: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
                 years: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering LetsEncryptCertificate resources.
        :param pulumi.Input[str] authority_identifier: The identifying certification authority (CA)
        :param pulumi.Input[bool] auto_renew: Set to true if the certificate will auto-renew
        :param pulumi.Input[int] contact_id: The contact id for the certificate
        :param pulumi.Input[str] csr: The certificate signing request
        :param pulumi.Input[str] domain_id: The domain to be issued the certificate for
        :param pulumi.Input[str] name: The certificate name
        :param pulumi.Input[str] state: The state of the certificate
        :param pulumi.Input[int] years: The years the certificate will last
        """
        if authority_identifier is not None:
            pulumi.set(__self__, "authority_identifier", authority_identifier)
        if auto_renew is not None:
            pulumi.set(__self__, "auto_renew", auto_renew)
        if contact_id is not None:
            warnings.warn("""contact_id is deprecated and has no effect. The attribute will be removed in the next major version.""", DeprecationWarning)
            pulumi.log.warn("""contact_id is deprecated: contact_id is deprecated and has no effect. The attribute will be removed in the next major version.""")
        if contact_id is not None:
            pulumi.set(__self__, "contact_id", contact_id)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if csr is not None:
            pulumi.set(__self__, "csr", csr)
        if domain_id is not None:
            pulumi.set(__self__, "domain_id", domain_id)
        if expires_on is not None:
            pulumi.set(__self__, "expires_on", expires_on)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)
        if years is not None:
            pulumi.set(__self__, "years", years)

    @property
    @pulumi.getter(name="authorityIdentifier")
    def authority_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The identifying certification authority (CA)
        """
        return pulumi.get(self, "authority_identifier")

    @authority_identifier.setter
    def authority_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authority_identifier", value)

    @property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[pulumi.Input[bool]]:
        """
        Set to true if the certificate will auto-renew
        """
        return pulumi.get(self, "auto_renew")

    @auto_renew.setter
    def auto_renew(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_renew", value)

    @property
    @pulumi.getter(name="contactId")
    @_utilities.deprecated("""contact_id is deprecated and has no effect. The attribute will be removed in the next major version.""")
    def contact_id(self) -> Optional[pulumi.Input[int]]:
        """
        The contact id for the certificate
        """
        return pulumi.get(self, "contact_id")

    @contact_id.setter
    def contact_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "contact_id", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def csr(self) -> Optional[pulumi.Input[str]]:
        """
        The certificate signing request
        """
        return pulumi.get(self, "csr")

    @csr.setter
    def csr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "csr", value)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[str]]:
        """
        The domain to be issued the certificate for
        """
        return pulumi.get(self, "domain_id")

    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_id", value)

    @property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "expires_on")

    @expires_on.setter
    def expires_on(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_on", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The certificate name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state of the certificate
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)

    @property
    @pulumi.getter
    def years(self) -> Optional[pulumi.Input[int]]:
        """
        The years the certificate will last
        """
        return pulumi.get(self, "years")

    @years.setter
    def years(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "years", value)


class LetsEncryptCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_renew: Optional[pulumi.Input[bool]] = None,
                 contact_id: Optional[pulumi.Input[int]] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a DNSimple Let's Encrypt certificate resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_dnsimple as dnsimple

        foobar = dnsimple.LetsEncryptCertificate("foobar",
            domain_id=dnsimple["domainId"],
            auto_renew=False,
            name="www")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_renew: Set to true if the certificate will auto-renew
        :param pulumi.Input[int] contact_id: The contact id for the certificate
        :param pulumi.Input[str] domain_id: The domain to be issued the certificate for
        :param pulumi.Input[str] name: The certificate name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LetsEncryptCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a DNSimple Let's Encrypt certificate resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_dnsimple as dnsimple

        foobar = dnsimple.LetsEncryptCertificate("foobar",
            domain_id=dnsimple["domainId"],
            auto_renew=False,
            name="www")
        ```

        :param str resource_name: The name of the resource.
        :param LetsEncryptCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LetsEncryptCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_renew: Optional[pulumi.Input[bool]] = None,
                 contact_id: Optional[pulumi.Input[int]] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LetsEncryptCertificateArgs.__new__(LetsEncryptCertificateArgs)

            if auto_renew is None and not opts.urn:
                raise TypeError("Missing required property 'auto_renew'")
            __props__.__dict__["auto_renew"] = auto_renew
            __props__.__dict__["contact_id"] = contact_id
            __props__.__dict__["domain_id"] = domain_id
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["authority_identifier"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["csr"] = None
            __props__.__dict__["expires_on"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["updated_at"] = None
            __props__.__dict__["years"] = None
        super(LetsEncryptCertificate, __self__).__init__(
            'dnsimple:index/letsEncryptCertificate:LetsEncryptCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authority_identifier: Optional[pulumi.Input[str]] = None,
            auto_renew: Optional[pulumi.Input[bool]] = None,
            contact_id: Optional[pulumi.Input[int]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            csr: Optional[pulumi.Input[str]] = None,
            domain_id: Optional[pulumi.Input[str]] = None,
            expires_on: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None,
            years: Optional[pulumi.Input[int]] = None) -> 'LetsEncryptCertificate':
        """
        Get an existing LetsEncryptCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authority_identifier: The identifying certification authority (CA)
        :param pulumi.Input[bool] auto_renew: Set to true if the certificate will auto-renew
        :param pulumi.Input[int] contact_id: The contact id for the certificate
        :param pulumi.Input[str] csr: The certificate signing request
        :param pulumi.Input[str] domain_id: The domain to be issued the certificate for
        :param pulumi.Input[str] name: The certificate name
        :param pulumi.Input[str] state: The state of the certificate
        :param pulumi.Input[int] years: The years the certificate will last
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LetsEncryptCertificateState.__new__(_LetsEncryptCertificateState)

        __props__.__dict__["authority_identifier"] = authority_identifier
        __props__.__dict__["auto_renew"] = auto_renew
        __props__.__dict__["contact_id"] = contact_id
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["csr"] = csr
        __props__.__dict__["domain_id"] = domain_id
        __props__.__dict__["expires_on"] = expires_on
        __props__.__dict__["name"] = name
        __props__.__dict__["state"] = state
        __props__.__dict__["updated_at"] = updated_at
        __props__.__dict__["years"] = years
        return LetsEncryptCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authorityIdentifier")
    def authority_identifier(self) -> pulumi.Output[str]:
        """
        The identifying certification authority (CA)
        """
        return pulumi.get(self, "authority_identifier")

    @property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> pulumi.Output[bool]:
        """
        Set to true if the certificate will auto-renew
        """
        return pulumi.get(self, "auto_renew")

    @property
    @pulumi.getter(name="contactId")
    @_utilities.deprecated("""contact_id is deprecated and has no effect. The attribute will be removed in the next major version.""")
    def contact_id(self) -> pulumi.Output[Optional[int]]:
        """
        The contact id for the certificate
        """
        return pulumi.get(self, "contact_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def csr(self) -> pulumi.Output[str]:
        """
        The certificate signing request
        """
        return pulumi.get(self, "csr")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[Optional[str]]:
        """
        The domain to be issued the certificate for
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> pulumi.Output[str]:
        return pulumi.get(self, "expires_on")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The certificate name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the certificate
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def years(self) -> pulumi.Output[int]:
        """
        The years the certificate will last
        """
        return pulumi.get(self, "years")

