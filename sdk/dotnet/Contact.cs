// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.DNSimple
{
    /// <summary>
    /// Provides a DNSimple contact resource.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using DNSimple = Pulumi.DNSimple;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     // Create a contact
    ///     var me = new DNSimple.Contact("me", new()
    ///     {
    ///         Label = "Apple Appleseed",
    ///         FirstName = "Apple",
    ///         LastName = "Appleseed",
    ///         OrganizationName = "Contoso",
    ///         JobTitle = "Manager",
    ///         Address1 = "Level 1, 2 Main St",
    ///         Address2 = "Marsfield",
    ///         City = "San Francisco",
    ///         StateProvince = "California",
    ///         PostalCode = "90210",
    ///         Country = "US",
    ///         Phone = "+1401239523",
    ///         Fax = "+1849491024",
    ///         Email = "apple@contoso.com",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// DNSimple contacts can be imported using their numeric ID.
    /// 
    /// bash
    /// 
    /// ```sh
    /// $ pulumi import dnsimple:index/contact:Contact resource_name 5678
    /// ```
    /// 
    /// The ID can be found within [DNSimple Contacts API](https://developer.dnsimple.com/v2/contacts/#listContacts). Check out [Authentication](https://developer.dnsimple.com/v2/#authentication) in API Overview for available options.
    /// 
    /// bash
    /// 
    /// curl -u 'EMAIL:PASSWORD' https://api.dnsimple.com/v2/1234/contacts?label_like=example.com | jq
    /// 
    /// {
    /// 
    ///   "data": [
    /// 
    ///     {
    ///     
    ///       "id": 1,
    ///     
    ///       "account_id": 1010,
    ///     
    ///       "label": "Default",
    ///     
    ///       "first_name": "First",
    ///     
    ///       "last_name": "User",
    ///     
    ///       "job_title": "CEO",
    ///     
    ///       "organization_name": "Awesome Company",
    ///     
    ///       "email": "first@example.com",
    ///     
    ///       "phone": "+18001234567",
    ///     
    ///       "fax": "+18011234567",
    ///     
    ///       "address1": "Italian Street, 10",
    ///     
    ///       "address2": "",
    ///     
    ///       "city": "Roma",
    ///     
    ///       "state_province": "RM",
    ///     
    ///       "postal_code": "00100",
    ///     
    ///       "country": "IT",
    ///     
    ///       "created_at": "2013-11-08T17:23:15Z",
    ///     
    ///       "updated_at": "2015-01-08T21:30:50Z"
    ///     
    ///     },
    ///     
    ///     {
    ///     
    ///       "id": 2,
    ///     
    ///       "account_id": 1010,
    ///     
    ///       "label": "",
    ///     
    ///       "first_name": "Second",
    ///     
    ///       "last_name": "User",
    ///     
    ///       "job_title": "",
    ///     
    ///       "organization_name": "",
    ///     
    ///       "email": "second@example.com",
    ///     
    ///       "phone": "+18881234567",
    ///     
    ///       "fax": "",
    ///     
    ///       "address1": "French Street",
    ///     
    ///       "address2": "c/o Someone",
    ///     
    ///       "city": "Paris",
    ///     
    ///       "state_province": "XY",
    ///     
    ///       "postal_code": "00200",
    ///     
    ///       "country": "FR",
    ///     
    ///       "created_at": "2014-12-06T15:46:18Z",
    ///     
    ///       "updated_at": "2014-12-06T15:46:18Z"
    ///     
    ///     }
    /// 
    ///   ],
    /// 
    ///   "pagination": {
    /// 
    ///     "current_page": 1,
    ///     
    ///     "per_page": 30,
    ///     
    ///     "total_entries": 2,
    ///     
    ///     "total_pages": 1
    /// 
    ///   }
    /// 
    /// }
    /// </summary>
    [DNSimpleResourceType("dnsimple:index/contact:Contact")]
    public partial class Contact : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The account ID for the contact.
        /// </summary>
        [Output("accountId")]
        public Output<int> AccountId { get; private set; } = null!;

        /// <summary>
        /// Address line 1
        /// </summary>
        [Output("address1")]
        public Output<string> Address1 { get; private set; } = null!;

        /// <summary>
        /// Address line 2
        /// </summary>
        [Output("address2")]
        public Output<string> Address2 { get; private set; } = null!;

        /// <summary>
        /// City
        /// </summary>
        [Output("city")]
        public Output<string> City { get; private set; } = null!;

        /// <summary>
        /// Country
        /// </summary>
        [Output("country")]
        public Output<string> Country { get; private set; } = null!;

        /// <summary>
        /// Timestamp representing when this contact was created.
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// Email
        /// 
        /// # Attributes Reference
        /// </summary>
        [Output("email")]
        public Output<string> Email { get; private set; } = null!;

        /// <summary>
        /// Fax
        /// </summary>
        [Output("fax")]
        public Output<string> Fax { get; private set; } = null!;

        /// <summary>
        /// The fax number, normalized.
        /// </summary>
        [Output("faxNormalized")]
        public Output<string> FaxNormalized { get; private set; } = null!;

        /// <summary>
        /// First name
        /// </summary>
        [Output("firstName")]
        public Output<string> FirstName { get; private set; } = null!;

        /// <summary>
        /// Job title
        /// </summary>
        [Output("jobTitle")]
        public Output<string> JobTitle { get; private set; } = null!;

        /// <summary>
        /// Label
        /// </summary>
        [Output("label")]
        public Output<string> Label { get; private set; } = null!;

        /// <summary>
        /// Last name
        /// </summary>
        [Output("lastName")]
        public Output<string> LastName { get; private set; } = null!;

        /// <summary>
        /// Organization name
        /// </summary>
        [Output("organizationName")]
        public Output<string> OrganizationName { get; private set; } = null!;

        /// <summary>
        /// Phone
        /// </summary>
        [Output("phone")]
        public Output<string> Phone { get; private set; } = null!;

        /// <summary>
        /// The phone number, normalized.
        /// </summary>
        [Output("phoneNormalized")]
        public Output<string> PhoneNormalized { get; private set; } = null!;

        /// <summary>
        /// Postal code
        /// </summary>
        [Output("postalCode")]
        public Output<string> PostalCode { get; private set; } = null!;

        /// <summary>
        /// State province
        /// </summary>
        [Output("stateProvince")]
        public Output<string> StateProvince { get; private set; } = null!;

        /// <summary>
        /// Timestamp representing when this contact was updated.
        /// </summary>
        [Output("updatedAt")]
        public Output<string> UpdatedAt { get; private set; } = null!;


        /// <summary>
        /// Create a Contact resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Contact(string name, ContactArgs args, CustomResourceOptions? options = null)
            : base("dnsimple:index/contact:Contact", name, args ?? new ContactArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Contact(string name, Input<string> id, ContactState? state = null, CustomResourceOptions? options = null)
            : base("dnsimple:index/contact:Contact", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Contact resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Contact Get(string name, Input<string> id, ContactState? state = null, CustomResourceOptions? options = null)
        {
            return new Contact(name, id, state, options);
        }
    }

    public sealed class ContactArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Address line 1
        /// </summary>
        [Input("address1", required: true)]
        public Input<string> Address1 { get; set; } = null!;

        /// <summary>
        /// Address line 2
        /// </summary>
        [Input("address2")]
        public Input<string>? Address2 { get; set; }

        /// <summary>
        /// City
        /// </summary>
        [Input("city", required: true)]
        public Input<string> City { get; set; } = null!;

        /// <summary>
        /// Country
        /// </summary>
        [Input("country", required: true)]
        public Input<string> Country { get; set; } = null!;

        /// <summary>
        /// Email
        /// 
        /// # Attributes Reference
        /// </summary>
        [Input("email", required: true)]
        public Input<string> Email { get; set; } = null!;

        /// <summary>
        /// Fax
        /// </summary>
        [Input("fax")]
        public Input<string>? Fax { get; set; }

        /// <summary>
        /// First name
        /// </summary>
        [Input("firstName", required: true)]
        public Input<string> FirstName { get; set; } = null!;

        /// <summary>
        /// Job title
        /// </summary>
        [Input("jobTitle")]
        public Input<string>? JobTitle { get; set; }

        /// <summary>
        /// Label
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// Last name
        /// </summary>
        [Input("lastName", required: true)]
        public Input<string> LastName { get; set; } = null!;

        /// <summary>
        /// Organization name
        /// </summary>
        [Input("organizationName")]
        public Input<string>? OrganizationName { get; set; }

        /// <summary>
        /// Phone
        /// </summary>
        [Input("phone", required: true)]
        public Input<string> Phone { get; set; } = null!;

        /// <summary>
        /// Postal code
        /// </summary>
        [Input("postalCode", required: true)]
        public Input<string> PostalCode { get; set; } = null!;

        /// <summary>
        /// State province
        /// </summary>
        [Input("stateProvince", required: true)]
        public Input<string> StateProvince { get; set; } = null!;

        public ContactArgs()
        {
        }
        public static new ContactArgs Empty => new ContactArgs();
    }

    public sealed class ContactState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The account ID for the contact.
        /// </summary>
        [Input("accountId")]
        public Input<int>? AccountId { get; set; }

        /// <summary>
        /// Address line 1
        /// </summary>
        [Input("address1")]
        public Input<string>? Address1 { get; set; }

        /// <summary>
        /// Address line 2
        /// </summary>
        [Input("address2")]
        public Input<string>? Address2 { get; set; }

        /// <summary>
        /// City
        /// </summary>
        [Input("city")]
        public Input<string>? City { get; set; }

        /// <summary>
        /// Country
        /// </summary>
        [Input("country")]
        public Input<string>? Country { get; set; }

        /// <summary>
        /// Timestamp representing when this contact was created.
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// Email
        /// 
        /// # Attributes Reference
        /// </summary>
        [Input("email")]
        public Input<string>? Email { get; set; }

        /// <summary>
        /// Fax
        /// </summary>
        [Input("fax")]
        public Input<string>? Fax { get; set; }

        /// <summary>
        /// The fax number, normalized.
        /// </summary>
        [Input("faxNormalized")]
        public Input<string>? FaxNormalized { get; set; }

        /// <summary>
        /// First name
        /// </summary>
        [Input("firstName")]
        public Input<string>? FirstName { get; set; }

        /// <summary>
        /// Job title
        /// </summary>
        [Input("jobTitle")]
        public Input<string>? JobTitle { get; set; }

        /// <summary>
        /// Label
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// Last name
        /// </summary>
        [Input("lastName")]
        public Input<string>? LastName { get; set; }

        /// <summary>
        /// Organization name
        /// </summary>
        [Input("organizationName")]
        public Input<string>? OrganizationName { get; set; }

        /// <summary>
        /// Phone
        /// </summary>
        [Input("phone")]
        public Input<string>? Phone { get; set; }

        /// <summary>
        /// The phone number, normalized.
        /// </summary>
        [Input("phoneNormalized")]
        public Input<string>? PhoneNormalized { get; set; }

        /// <summary>
        /// Postal code
        /// </summary>
        [Input("postalCode")]
        public Input<string>? PostalCode { get; set; }

        /// <summary>
        /// State province
        /// </summary>
        [Input("stateProvince")]
        public Input<string>? StateProvince { get; set; }

        /// <summary>
        /// Timestamp representing when this contact was updated.
        /// </summary>
        [Input("updatedAt")]
        public Input<string>? UpdatedAt { get; set; }

        public ContactState()
        {
        }
        public static new ContactState Empty => new ContactState();
    }
}