// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.DNSimple.Outputs
{

    [OutputType]
    public sealed class RegisteredDomainRegistrantChange
    {
        public readonly int? AccountId;
        /// <summary>
        /// The ID of the contact to be used for the domain registration. The contact ID can be changed after the domain has been registered. The change will result in a new registrant change this may result in a [60-day lock](https://support.dnsimple.com/articles/icann-60-day-lock-registrant-change/).
        /// </summary>
        public readonly int? ContactId;
        public readonly string? DomainId;
        /// <summary>
        /// A map of extended attributes to be set for the domain registration. To see if there are any required extended attributes for any TLD use our [Lists the TLD Extended Attributes API](https://developer.dnsimple.com/v2/tlds/#getTldExtendedAttributes). The values provided in the `extended_attributes` will also be sent when a registrant change is initiated as part of changing the `contact_id`.
        /// </summary>
        public readonly ImmutableDictionary<string, string>? ExtendedAttributes;
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        public readonly int? Id;
        public readonly string? IrtLockLiftedBy;
        public readonly bool? RegistryOwnerChange;
        /// <summary>
        /// The state of the domain.
        /// </summary>
        public readonly string? State;

        [OutputConstructor]
        private RegisteredDomainRegistrantChange(
            int? accountId,

            int? contactId,

            string? domainId,

            ImmutableDictionary<string, string>? extendedAttributes,

            int? id,

            string? irtLockLiftedBy,

            bool? registryOwnerChange,

            string? state)
        {
            AccountId = accountId;
            ContactId = contactId;
            DomainId = domainId;
            ExtendedAttributes = extendedAttributes;
            Id = id;
            IrtLockLiftedBy = irtLockLiftedBy;
            RegistryOwnerChange = registryOwnerChange;
            State = state;
        }
    }
}
