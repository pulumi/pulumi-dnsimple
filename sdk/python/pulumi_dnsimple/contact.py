# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ContactArgs', 'Contact']

@pulumi.input_type
class ContactArgs:
    def __init__(__self__, *,
                 address1: pulumi.Input[str],
                 city: pulumi.Input[str],
                 country: pulumi.Input[str],
                 email: pulumi.Input[str],
                 first_name: pulumi.Input[str],
                 last_name: pulumi.Input[str],
                 phone: pulumi.Input[str],
                 postal_code: pulumi.Input[str],
                 state_province: pulumi.Input[str],
                 address2: Optional[pulumi.Input[str]] = None,
                 fax: Optional[pulumi.Input[str]] = None,
                 job_title: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 organization_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Contact resource.
        :param pulumi.Input[str] address1: Address line 1
        :param pulumi.Input[str] city: City
        :param pulumi.Input[str] country: Country
        :param pulumi.Input[str] email: Email
               
               # Attributes Reference
        :param pulumi.Input[str] first_name: First name
        :param pulumi.Input[str] last_name: Last name
        :param pulumi.Input[str] phone: Phone
        :param pulumi.Input[str] postal_code: Postal code
        :param pulumi.Input[str] state_province: State province
        :param pulumi.Input[str] address2: Address line 2
        :param pulumi.Input[str] fax: Fax
        :param pulumi.Input[str] job_title: Job title
        :param pulumi.Input[str] label: Label
        :param pulumi.Input[str] organization_name: Organization name
        """
        pulumi.set(__self__, "address1", address1)
        pulumi.set(__self__, "city", city)
        pulumi.set(__self__, "country", country)
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "first_name", first_name)
        pulumi.set(__self__, "last_name", last_name)
        pulumi.set(__self__, "phone", phone)
        pulumi.set(__self__, "postal_code", postal_code)
        pulumi.set(__self__, "state_province", state_province)
        if address2 is not None:
            pulumi.set(__self__, "address2", address2)
        if fax is not None:
            pulumi.set(__self__, "fax", fax)
        if job_title is not None:
            pulumi.set(__self__, "job_title", job_title)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if organization_name is not None:
            pulumi.set(__self__, "organization_name", organization_name)

    @property
    @pulumi.getter
    def address1(self) -> pulumi.Input[str]:
        """
        Address line 1
        """
        return pulumi.get(self, "address1")

    @address1.setter
    def address1(self, value: pulumi.Input[str]):
        pulumi.set(self, "address1", value)

    @property
    @pulumi.getter
    def city(self) -> pulumi.Input[str]:
        """
        City
        """
        return pulumi.get(self, "city")

    @city.setter
    def city(self, value: pulumi.Input[str]):
        pulumi.set(self, "city", value)

    @property
    @pulumi.getter
    def country(self) -> pulumi.Input[str]:
        """
        Country
        """
        return pulumi.get(self, "country")

    @country.setter
    def country(self, value: pulumi.Input[str]):
        pulumi.set(self, "country", value)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        """
        Email

        # Attributes Reference
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Input[str]:
        """
        First name
        """
        return pulumi.get(self, "first_name")

    @first_name.setter
    def first_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "first_name", value)

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Input[str]:
        """
        Last name
        """
        return pulumi.get(self, "last_name")

    @last_name.setter
    def last_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "last_name", value)

    @property
    @pulumi.getter
    def phone(self) -> pulumi.Input[str]:
        """
        Phone
        """
        return pulumi.get(self, "phone")

    @phone.setter
    def phone(self, value: pulumi.Input[str]):
        pulumi.set(self, "phone", value)

    @property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> pulumi.Input[str]:
        """
        Postal code
        """
        return pulumi.get(self, "postal_code")

    @postal_code.setter
    def postal_code(self, value: pulumi.Input[str]):
        pulumi.set(self, "postal_code", value)

    @property
    @pulumi.getter(name="stateProvince")
    def state_province(self) -> pulumi.Input[str]:
        """
        State province
        """
        return pulumi.get(self, "state_province")

    @state_province.setter
    def state_province(self, value: pulumi.Input[str]):
        pulumi.set(self, "state_province", value)

    @property
    @pulumi.getter
    def address2(self) -> Optional[pulumi.Input[str]]:
        """
        Address line 2
        """
        return pulumi.get(self, "address2")

    @address2.setter
    def address2(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address2", value)

    @property
    @pulumi.getter
    def fax(self) -> Optional[pulumi.Input[str]]:
        """
        Fax
        """
        return pulumi.get(self, "fax")

    @fax.setter
    def fax(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fax", value)

    @property
    @pulumi.getter(name="jobTitle")
    def job_title(self) -> Optional[pulumi.Input[str]]:
        """
        Job title
        """
        return pulumi.get(self, "job_title")

    @job_title.setter
    def job_title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job_title", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        Label
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[pulumi.Input[str]]:
        """
        Organization name
        """
        return pulumi.get(self, "organization_name")

    @organization_name.setter
    def organization_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_name", value)


@pulumi.input_type
class _ContactState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[int]] = None,
                 address1: Optional[pulumi.Input[str]] = None,
                 address2: Optional[pulumi.Input[str]] = None,
                 city: Optional[pulumi.Input[str]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 fax: Optional[pulumi.Input[str]] = None,
                 fax_normalized: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 job_title: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 organization_name: Optional[pulumi.Input[str]] = None,
                 phone: Optional[pulumi.Input[str]] = None,
                 phone_normalized: Optional[pulumi.Input[str]] = None,
                 postal_code: Optional[pulumi.Input[str]] = None,
                 state_province: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Contact resources.
        :param pulumi.Input[int] account_id: The account ID for the contact.
        :param pulumi.Input[str] address1: Address line 1
        :param pulumi.Input[str] address2: Address line 2
        :param pulumi.Input[str] city: City
        :param pulumi.Input[str] country: Country
        :param pulumi.Input[str] created_at: Timestamp representing when this contact was created.
        :param pulumi.Input[str] email: Email
               
               # Attributes Reference
        :param pulumi.Input[str] fax: Fax
        :param pulumi.Input[str] fax_normalized: The fax number, normalized.
        :param pulumi.Input[str] first_name: First name
        :param pulumi.Input[str] job_title: Job title
        :param pulumi.Input[str] label: Label
        :param pulumi.Input[str] last_name: Last name
        :param pulumi.Input[str] organization_name: Organization name
        :param pulumi.Input[str] phone: Phone
        :param pulumi.Input[str] phone_normalized: The phone number, normalized.
        :param pulumi.Input[str] postal_code: Postal code
        :param pulumi.Input[str] state_province: State province
        :param pulumi.Input[str] updated_at: Timestamp representing when this contact was updated.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if address1 is not None:
            pulumi.set(__self__, "address1", address1)
        if address2 is not None:
            pulumi.set(__self__, "address2", address2)
        if city is not None:
            pulumi.set(__self__, "city", city)
        if country is not None:
            pulumi.set(__self__, "country", country)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if fax is not None:
            pulumi.set(__self__, "fax", fax)
        if fax_normalized is not None:
            pulumi.set(__self__, "fax_normalized", fax_normalized)
        if first_name is not None:
            pulumi.set(__self__, "first_name", first_name)
        if job_title is not None:
            pulumi.set(__self__, "job_title", job_title)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if last_name is not None:
            pulumi.set(__self__, "last_name", last_name)
        if organization_name is not None:
            pulumi.set(__self__, "organization_name", organization_name)
        if phone is not None:
            pulumi.set(__self__, "phone", phone)
        if phone_normalized is not None:
            pulumi.set(__self__, "phone_normalized", phone_normalized)
        if postal_code is not None:
            pulumi.set(__self__, "postal_code", postal_code)
        if state_province is not None:
            pulumi.set(__self__, "state_province", state_province)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[int]]:
        """
        The account ID for the contact.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def address1(self) -> Optional[pulumi.Input[str]]:
        """
        Address line 1
        """
        return pulumi.get(self, "address1")

    @address1.setter
    def address1(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address1", value)

    @property
    @pulumi.getter
    def address2(self) -> Optional[pulumi.Input[str]]:
        """
        Address line 2
        """
        return pulumi.get(self, "address2")

    @address2.setter
    def address2(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address2", value)

    @property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[str]]:
        """
        City
        """
        return pulumi.get(self, "city")

    @city.setter
    def city(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "city", value)

    @property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[str]]:
        """
        Country
        """
        return pulumi.get(self, "country")

    @country.setter
    def country(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Timestamp representing when this contact was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        Email

        # Attributes Reference
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def fax(self) -> Optional[pulumi.Input[str]]:
        """
        Fax
        """
        return pulumi.get(self, "fax")

    @fax.setter
    def fax(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fax", value)

    @property
    @pulumi.getter(name="faxNormalized")
    def fax_normalized(self) -> Optional[pulumi.Input[str]]:
        """
        The fax number, normalized.
        """
        return pulumi.get(self, "fax_normalized")

    @fax_normalized.setter
    def fax_normalized(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fax_normalized", value)

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[str]]:
        """
        First name
        """
        return pulumi.get(self, "first_name")

    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_name", value)

    @property
    @pulumi.getter(name="jobTitle")
    def job_title(self) -> Optional[pulumi.Input[str]]:
        """
        Job title
        """
        return pulumi.get(self, "job_title")

    @job_title.setter
    def job_title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job_title", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        Label
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[str]]:
        """
        Last name
        """
        return pulumi.get(self, "last_name")

    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_name", value)

    @property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[pulumi.Input[str]]:
        """
        Organization name
        """
        return pulumi.get(self, "organization_name")

    @organization_name.setter
    def organization_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_name", value)

    @property
    @pulumi.getter
    def phone(self) -> Optional[pulumi.Input[str]]:
        """
        Phone
        """
        return pulumi.get(self, "phone")

    @phone.setter
    def phone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "phone", value)

    @property
    @pulumi.getter(name="phoneNormalized")
    def phone_normalized(self) -> Optional[pulumi.Input[str]]:
        """
        The phone number, normalized.
        """
        return pulumi.get(self, "phone_normalized")

    @phone_normalized.setter
    def phone_normalized(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "phone_normalized", value)

    @property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[str]]:
        """
        Postal code
        """
        return pulumi.get(self, "postal_code")

    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "postal_code", value)

    @property
    @pulumi.getter(name="stateProvince")
    def state_province(self) -> Optional[pulumi.Input[str]]:
        """
        State province
        """
        return pulumi.get(self, "state_province")

    @state_province.setter
    def state_province(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state_province", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        Timestamp representing when this contact was updated.
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


class Contact(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address1: Optional[pulumi.Input[str]] = None,
                 address2: Optional[pulumi.Input[str]] = None,
                 city: Optional[pulumi.Input[str]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 fax: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 job_title: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 organization_name: Optional[pulumi.Input[str]] = None,
                 phone: Optional[pulumi.Input[str]] = None,
                 postal_code: Optional[pulumi.Input[str]] = None,
                 state_province: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a DNSimple contact resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_dnsimple as dnsimple

        # Create a contact
        me = dnsimple.Contact("me",
            address1="Level 1, 2 Main St",
            address2="Marsfield",
            city="San Francisco",
            country="US",
            email="apple@contoso.com",
            fax="+1849491024",
            first_name="Apple",
            job_title="Manager",
            label="Apple Appleseed",
            last_name="Appleseed",
            organization_name="Contoso",
            phone="+1401239523",
            postal_code="90210",
            state_province="California")
        ```

        ## Import

        DNSimple contacts can be imported using their numeric ID. bash

        ```sh
         $ pulumi import dnsimple:index/contact:Contact resource_name 5678
        ```

         The ID can be found within [DNSimple Contacts API](https://developer.dnsimple.com/v2/contacts/#listContacts). Check out [Authentication](https://developer.dnsimple.com/v2/#authentication) in API Overview for available options. bash curl -u 'EMAIL:PASSWORD' https://api.dnsimple.com/v2/1234/contacts?label_like=example.com | jq {

         "data"[

         {

         "id"1,

         "account_id"1010,

         "label""Default",

         "first_name""First",

         "last_name""User",

         "job_title""CEO",

         "organization_name""Awesome Company",

         "email""first@example.com",

         "phone""+18001234567",

         "fax""+18011234567",

         "address1""Italian Street, 10",

         "address2\"\"\",

         "city""Roma",

         "state_province""RM",

         "postal_code""00100",

         "country""IT",

         "created_at""2013-11-08T17:23:15Z",

         "updated_at""2015-01-08T21:30:50Z"

         },

         {

         "id"2,

         "account_id"1010,

         "label\"\"\",

         "first_name""Second",

         "last_name""User",

         "job_title\"\"\",

         "organization_name\"\"\",

         "email""second@example.com",

         "phone""+18881234567",

         "fax\"\"\",

         "address1""French Street",

         "address2""c/o Someone",

         "city""Paris",

         "state_province""XY",

         "postal_code""00200",

         "country""FR",

         "created_at""2014-12-06T15:46:18Z",

         "updated_at""2014-12-06T15:46:18Z"

         }

         ],

         "pagination"{

         "current_page"1,

         "per_page"30,

         "total_entries"2,

         "total_pages"1

         } }

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address1: Address line 1
        :param pulumi.Input[str] address2: Address line 2
        :param pulumi.Input[str] city: City
        :param pulumi.Input[str] country: Country
        :param pulumi.Input[str] email: Email
               
               # Attributes Reference
        :param pulumi.Input[str] fax: Fax
        :param pulumi.Input[str] first_name: First name
        :param pulumi.Input[str] job_title: Job title
        :param pulumi.Input[str] label: Label
        :param pulumi.Input[str] last_name: Last name
        :param pulumi.Input[str] organization_name: Organization name
        :param pulumi.Input[str] phone: Phone
        :param pulumi.Input[str] postal_code: Postal code
        :param pulumi.Input[str] state_province: State province
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContactArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a DNSimple contact resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_dnsimple as dnsimple

        # Create a contact
        me = dnsimple.Contact("me",
            address1="Level 1, 2 Main St",
            address2="Marsfield",
            city="San Francisco",
            country="US",
            email="apple@contoso.com",
            fax="+1849491024",
            first_name="Apple",
            job_title="Manager",
            label="Apple Appleseed",
            last_name="Appleseed",
            organization_name="Contoso",
            phone="+1401239523",
            postal_code="90210",
            state_province="California")
        ```

        ## Import

        DNSimple contacts can be imported using their numeric ID. bash

        ```sh
         $ pulumi import dnsimple:index/contact:Contact resource_name 5678
        ```

         The ID can be found within [DNSimple Contacts API](https://developer.dnsimple.com/v2/contacts/#listContacts). Check out [Authentication](https://developer.dnsimple.com/v2/#authentication) in API Overview for available options. bash curl -u 'EMAIL:PASSWORD' https://api.dnsimple.com/v2/1234/contacts?label_like=example.com | jq {

         "data"[

         {

         "id"1,

         "account_id"1010,

         "label""Default",

         "first_name""First",

         "last_name""User",

         "job_title""CEO",

         "organization_name""Awesome Company",

         "email""first@example.com",

         "phone""+18001234567",

         "fax""+18011234567",

         "address1""Italian Street, 10",

         "address2\"\"\",

         "city""Roma",

         "state_province""RM",

         "postal_code""00100",

         "country""IT",

         "created_at""2013-11-08T17:23:15Z",

         "updated_at""2015-01-08T21:30:50Z"

         },

         {

         "id"2,

         "account_id"1010,

         "label\"\"\",

         "first_name""Second",

         "last_name""User",

         "job_title\"\"\",

         "organization_name\"\"\",

         "email""second@example.com",

         "phone""+18881234567",

         "fax\"\"\",

         "address1""French Street",

         "address2""c/o Someone",

         "city""Paris",

         "state_province""XY",

         "postal_code""00200",

         "country""FR",

         "created_at""2014-12-06T15:46:18Z",

         "updated_at""2014-12-06T15:46:18Z"

         }

         ],

         "pagination"{

         "current_page"1,

         "per_page"30,

         "total_entries"2,

         "total_pages"1

         } }

        :param str resource_name: The name of the resource.
        :param ContactArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContactArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address1: Optional[pulumi.Input[str]] = None,
                 address2: Optional[pulumi.Input[str]] = None,
                 city: Optional[pulumi.Input[str]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 fax: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 job_title: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 organization_name: Optional[pulumi.Input[str]] = None,
                 phone: Optional[pulumi.Input[str]] = None,
                 postal_code: Optional[pulumi.Input[str]] = None,
                 state_province: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ContactArgs.__new__(ContactArgs)

            if address1 is None and not opts.urn:
                raise TypeError("Missing required property 'address1'")
            __props__.__dict__["address1"] = address1
            __props__.__dict__["address2"] = address2
            if city is None and not opts.urn:
                raise TypeError("Missing required property 'city'")
            __props__.__dict__["city"] = city
            if country is None and not opts.urn:
                raise TypeError("Missing required property 'country'")
            __props__.__dict__["country"] = country
            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = email
            __props__.__dict__["fax"] = fax
            if first_name is None and not opts.urn:
                raise TypeError("Missing required property 'first_name'")
            __props__.__dict__["first_name"] = first_name
            __props__.__dict__["job_title"] = job_title
            __props__.__dict__["label"] = label
            if last_name is None and not opts.urn:
                raise TypeError("Missing required property 'last_name'")
            __props__.__dict__["last_name"] = last_name
            __props__.__dict__["organization_name"] = organization_name
            if phone is None and not opts.urn:
                raise TypeError("Missing required property 'phone'")
            __props__.__dict__["phone"] = phone
            if postal_code is None and not opts.urn:
                raise TypeError("Missing required property 'postal_code'")
            __props__.__dict__["postal_code"] = postal_code
            if state_province is None and not opts.urn:
                raise TypeError("Missing required property 'state_province'")
            __props__.__dict__["state_province"] = state_province
            __props__.__dict__["account_id"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["fax_normalized"] = None
            __props__.__dict__["phone_normalized"] = None
            __props__.__dict__["updated_at"] = None
        super(Contact, __self__).__init__(
            'dnsimple:index/contact:Contact',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[int]] = None,
            address1: Optional[pulumi.Input[str]] = None,
            address2: Optional[pulumi.Input[str]] = None,
            city: Optional[pulumi.Input[str]] = None,
            country: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            email: Optional[pulumi.Input[str]] = None,
            fax: Optional[pulumi.Input[str]] = None,
            fax_normalized: Optional[pulumi.Input[str]] = None,
            first_name: Optional[pulumi.Input[str]] = None,
            job_title: Optional[pulumi.Input[str]] = None,
            label: Optional[pulumi.Input[str]] = None,
            last_name: Optional[pulumi.Input[str]] = None,
            organization_name: Optional[pulumi.Input[str]] = None,
            phone: Optional[pulumi.Input[str]] = None,
            phone_normalized: Optional[pulumi.Input[str]] = None,
            postal_code: Optional[pulumi.Input[str]] = None,
            state_province: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'Contact':
        """
        Get an existing Contact resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] account_id: The account ID for the contact.
        :param pulumi.Input[str] address1: Address line 1
        :param pulumi.Input[str] address2: Address line 2
        :param pulumi.Input[str] city: City
        :param pulumi.Input[str] country: Country
        :param pulumi.Input[str] created_at: Timestamp representing when this contact was created.
        :param pulumi.Input[str] email: Email
               
               # Attributes Reference
        :param pulumi.Input[str] fax: Fax
        :param pulumi.Input[str] fax_normalized: The fax number, normalized.
        :param pulumi.Input[str] first_name: First name
        :param pulumi.Input[str] job_title: Job title
        :param pulumi.Input[str] label: Label
        :param pulumi.Input[str] last_name: Last name
        :param pulumi.Input[str] organization_name: Organization name
        :param pulumi.Input[str] phone: Phone
        :param pulumi.Input[str] phone_normalized: The phone number, normalized.
        :param pulumi.Input[str] postal_code: Postal code
        :param pulumi.Input[str] state_province: State province
        :param pulumi.Input[str] updated_at: Timestamp representing when this contact was updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ContactState.__new__(_ContactState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["address1"] = address1
        __props__.__dict__["address2"] = address2
        __props__.__dict__["city"] = city
        __props__.__dict__["country"] = country
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["email"] = email
        __props__.__dict__["fax"] = fax
        __props__.__dict__["fax_normalized"] = fax_normalized
        __props__.__dict__["first_name"] = first_name
        __props__.__dict__["job_title"] = job_title
        __props__.__dict__["label"] = label
        __props__.__dict__["last_name"] = last_name
        __props__.__dict__["organization_name"] = organization_name
        __props__.__dict__["phone"] = phone
        __props__.__dict__["phone_normalized"] = phone_normalized
        __props__.__dict__["postal_code"] = postal_code
        __props__.__dict__["state_province"] = state_province
        __props__.__dict__["updated_at"] = updated_at
        return Contact(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[int]:
        """
        The account ID for the contact.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def address1(self) -> pulumi.Output[str]:
        """
        Address line 1
        """
        return pulumi.get(self, "address1")

    @property
    @pulumi.getter
    def address2(self) -> pulumi.Output[str]:
        """
        Address line 2
        """
        return pulumi.get(self, "address2")

    @property
    @pulumi.getter
    def city(self) -> pulumi.Output[str]:
        """
        City
        """
        return pulumi.get(self, "city")

    @property
    @pulumi.getter
    def country(self) -> pulumi.Output[str]:
        """
        Country
        """
        return pulumi.get(self, "country")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Timestamp representing when this contact was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        Email

        # Attributes Reference
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def fax(self) -> pulumi.Output[str]:
        """
        Fax
        """
        return pulumi.get(self, "fax")

    @property
    @pulumi.getter(name="faxNormalized")
    def fax_normalized(self) -> pulumi.Output[str]:
        """
        The fax number, normalized.
        """
        return pulumi.get(self, "fax_normalized")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Output[str]:
        """
        First name
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter(name="jobTitle")
    def job_title(self) -> pulumi.Output[str]:
        """
        Job title
        """
        return pulumi.get(self, "job_title")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[str]:
        """
        Label
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Output[str]:
        """
        Last name
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> pulumi.Output[str]:
        """
        Organization name
        """
        return pulumi.get(self, "organization_name")

    @property
    @pulumi.getter
    def phone(self) -> pulumi.Output[str]:
        """
        Phone
        """
        return pulumi.get(self, "phone")

    @property
    @pulumi.getter(name="phoneNormalized")
    def phone_normalized(self) -> pulumi.Output[str]:
        """
        The phone number, normalized.
        """
        return pulumi.get(self, "phone_normalized")

    @property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> pulumi.Output[str]:
        """
        Postal code
        """
        return pulumi.get(self, "postal_code")

    @property
    @pulumi.getter(name="stateProvince")
    def state_province(self) -> pulumi.Output[str]:
        """
        State province
        """
        return pulumi.get(self, "state_province")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Timestamp representing when this contact was updated.
        """
        return pulumi.get(self, "updated_at")

