// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface RegisteredDomainDomainRegistration {
    /**
     * The ID of this resource.
     */
    id?: pulumi.Input<number>;
    /**
     * The registration period in years.
     */
    period?: pulumi.Input<number>;
    /**
     * The state of the domain.
     */
    state?: pulumi.Input<string>;
}

export interface RegisteredDomainRegistrantChange {
    accountId?: pulumi.Input<number>;
    /**
     * The ID of the contact to be used for the domain registration. The contact ID can be changed after the domain has been registered. The change will result in a new registrant change this may result in a [60-day lock](https://support.dnsimple.com/articles/icann-60-day-lock-registrant-change/).
     */
    contactId?: pulumi.Input<number>;
    domainId?: pulumi.Input<string>;
    /**
     * A map of extended attributes to be set for the domain registration. To see if there are any required extended attributes for any TLD use our [Lists the TLD Extended Attributes API](https://developer.dnsimple.com/v2/tlds/#getTldExtendedAttributes). The values provided in the `extendedAttributes` will also be sent when a registrant change is initiated as part of changing the `contactId`.
     */
    extendedAttributes?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The ID of this resource.
     */
    id?: pulumi.Input<number>;
    irtLockLiftedBy?: pulumi.Input<string>;
    registryOwnerChange?: pulumi.Input<boolean>;
    /**
     * The state of the domain.
     */
    state?: pulumi.Input<string>;
}

export interface RegisteredDomainTimeouts {
    /**
     * The timeout for the read operation e.g. `5m`
     */
    create?: pulumi.Input<string>;
    delete?: pulumi.Input<string>;
    /**
     * The timeout for the read operation e.g. `5m`
     *
     * <a id="nestedblock--domain_registration"></a>
     */
    update?: pulumi.Input<string>;
}