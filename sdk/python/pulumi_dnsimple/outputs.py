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
from . import outputs
from ._enums import *

__all__ = [
    'RegisteredDomainDomainRegistration',
    'RegisteredDomainRegistrantChange',
    'RegisteredDomainTimeouts',
    'GetCertificateTimeoutsResult',
    'GetRegistrantChangeCheckExtendedAttributeResult',
    'GetRegistrantChangeCheckExtendedAttributeOptionResult',
]

@pulumi.output_type
class RegisteredDomainDomainRegistration(dict):
    def __init__(__self__, *,
                 id: Optional[_builtins.int] = None,
                 period: Optional[_builtins.int] = None,
                 state: Optional[_builtins.str] = None):
        """
        :param _builtins.int id: The ID of this resource.
        :param _builtins.int period: The registration period in years.
        :param _builtins.str state: The state of the domain.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if period is not None:
            pulumi.set(__self__, "period", period)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.int]:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[_builtins.int]:
        """
        The registration period in years.
        """
        return pulumi.get(self, "period")

    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        """
        The state of the domain.
        """
        return pulumi.get(self, "state")


@pulumi.output_type
class RegisteredDomainRegistrantChange(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "accountId":
            suggest = "account_id"
        elif key == "contactId":
            suggest = "contact_id"
        elif key == "domainId":
            suggest = "domain_id"
        elif key == "extendedAttributes":
            suggest = "extended_attributes"
        elif key == "irtLockLiftedBy":
            suggest = "irt_lock_lifted_by"
        elif key == "registryOwnerChange":
            suggest = "registry_owner_change"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RegisteredDomainRegistrantChange. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RegisteredDomainRegistrantChange.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RegisteredDomainRegistrantChange.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 account_id: Optional[_builtins.int] = None,
                 contact_id: Optional[_builtins.int] = None,
                 domain_id: Optional[_builtins.str] = None,
                 extended_attributes: Optional[Mapping[str, _builtins.str]] = None,
                 id: Optional[_builtins.int] = None,
                 irt_lock_lifted_by: Optional[_builtins.str] = None,
                 registry_owner_change: Optional[_builtins.bool] = None,
                 state: Optional[_builtins.str] = None):
        """
        :param _builtins.int account_id: DNSimple Account ID to which the registrant change belongs to
        :param _builtins.int contact_id: The ID of the contact to be used for the domain registration. The contact ID can be changed after the domain has been registered. The change will result in a new registrant change this may result in a [60-day lock](https://support.dnsimple.com/articles/icann-60-day-lock-registrant-change/).
        :param _builtins.str domain_id: DNSimple domain ID for which the registrant change is being performed
        :param Mapping[str, _builtins.str] extended_attributes: A map of extended attributes to be set for the domain registration. To see if there are any required extended attributes for any TLD use our [Lists the TLD Extended Attributes API](https://developer.dnsimple.com/v2/tlds/#getTldExtendedAttributes). The values provided in the `extended_attributes` will also be sent when a registrant change is initiated as part of changing the `contact_id`.
        :param _builtins.int id: The ID of this resource.
        :param _builtins.str irt_lock_lifted_by: Date when the registrant change lock was lifted for the domain
        :param _builtins.bool registry_owner_change: True if the registrant change will result in a registry owner change
        :param _builtins.str state: The state of the domain.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if contact_id is not None:
            pulumi.set(__self__, "contact_id", contact_id)
        if domain_id is not None:
            pulumi.set(__self__, "domain_id", domain_id)
        if extended_attributes is not None:
            pulumi.set(__self__, "extended_attributes", extended_attributes)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if irt_lock_lifted_by is not None:
            pulumi.set(__self__, "irt_lock_lifted_by", irt_lock_lifted_by)
        if registry_owner_change is not None:
            pulumi.set(__self__, "registry_owner_change", registry_owner_change)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.int]:
        """
        DNSimple Account ID to which the registrant change belongs to
        """
        return pulumi.get(self, "account_id")

    @_builtins.property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> Optional[_builtins.int]:
        """
        The ID of the contact to be used for the domain registration. The contact ID can be changed after the domain has been registered. The change will result in a new registrant change this may result in a [60-day lock](https://support.dnsimple.com/articles/icann-60-day-lock-registrant-change/).
        """
        return pulumi.get(self, "contact_id")

    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[_builtins.str]:
        """
        DNSimple domain ID for which the registrant change is being performed
        """
        return pulumi.get(self, "domain_id")

    @_builtins.property
    @pulumi.getter(name="extendedAttributes")
    def extended_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        """
        A map of extended attributes to be set for the domain registration. To see if there are any required extended attributes for any TLD use our [Lists the TLD Extended Attributes API](https://developer.dnsimple.com/v2/tlds/#getTldExtendedAttributes). The values provided in the `extended_attributes` will also be sent when a registrant change is initiated as part of changing the `contact_id`.
        """
        return pulumi.get(self, "extended_attributes")

    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.int]:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @_builtins.property
    @pulumi.getter(name="irtLockLiftedBy")
    def irt_lock_lifted_by(self) -> Optional[_builtins.str]:
        """
        Date when the registrant change lock was lifted for the domain
        """
        return pulumi.get(self, "irt_lock_lifted_by")

    @_builtins.property
    @pulumi.getter(name="registryOwnerChange")
    def registry_owner_change(self) -> Optional[_builtins.bool]:
        """
        True if the registrant change will result in a registry owner change
        """
        return pulumi.get(self, "registry_owner_change")

    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        """
        The state of the domain.
        """
        return pulumi.get(self, "state")


@pulumi.output_type
class RegisteredDomainTimeouts(dict):
    def __init__(__self__, *,
                 create: Optional[_builtins.str] = None,
                 delete: Optional[_builtins.str] = None,
                 update: Optional[_builtins.str] = None):
        """
        :param _builtins.str create: Create timeout.
        :param _builtins.str delete: Delete timeout (currently unused).
        :param _builtins.str update: Update timeout.
        """
        if create is not None:
            pulumi.set(__self__, "create", create)
        if delete is not None:
            pulumi.set(__self__, "delete", delete)
        if update is not None:
            pulumi.set(__self__, "update", update)

    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        """
        Create timeout.
        """
        return pulumi.get(self, "create")

    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        """
        Delete timeout (currently unused).
        """
        return pulumi.get(self, "delete")

    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        """
        Update timeout.
        """
        return pulumi.get(self, "update")


@pulumi.output_type
class GetCertificateTimeoutsResult(dict):
    def __init__(__self__, *,
                 read: Optional[_builtins.str] = None):
        """
        :param _builtins.str read: (String) - The timeout for the read operation e.g. `5m`
        """
        if read is not None:
            pulumi.set(__self__, "read", read)

    @_builtins.property
    @pulumi.getter
    def read(self) -> Optional[_builtins.str]:
        """
        (String) - The timeout for the read operation e.g. `5m`
        """
        return pulumi.get(self, "read")


@pulumi.output_type
class GetRegistrantChangeCheckExtendedAttributeResult(dict):
    def __init__(__self__, *,
                 description: _builtins.str,
                 name: _builtins.str,
                 options: Sequence['outputs.GetRegistrantChangeCheckExtendedAttributeOptionResult'],
                 required: _builtins.bool):
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "options", options)
        pulumi.set(__self__, "required", required)

    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        return pulumi.get(self, "description")

    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        return pulumi.get(self, "name")

    @_builtins.property
    @pulumi.getter
    def options(self) -> Sequence['outputs.GetRegistrantChangeCheckExtendedAttributeOptionResult']:
        return pulumi.get(self, "options")

    @_builtins.property
    @pulumi.getter
    def required(self) -> _builtins.bool:
        return pulumi.get(self, "required")


@pulumi.output_type
class GetRegistrantChangeCheckExtendedAttributeOptionResult(dict):
    def __init__(__self__, *,
                 description: _builtins.str,
                 title: _builtins.str,
                 value: _builtins.str):
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "title", title)
        pulumi.set(__self__, "value", value)

    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        return pulumi.get(self, "description")

    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        return pulumi.get(self, "title")

    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        return pulumi.get(self, "value")


