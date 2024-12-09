// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as enums from "./types/enums";
import * as utilities from "./utilities";

/**
 * Get information on the requirements of a registrant change.
 *
 * > **Note:** The registrant change API is currently in developer preview and is subject to change.
 *
 * Get registrant change requirements for the `dnsimple.com` domain and the contact with ID `1234`:
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as dnsimple from "@pulumi/dnsimple";
 *
 * const example = dnsimple.getRegistrantChangeCheck({
 *     domainId: "dnsimple.com",
 *     contactId: "1234",
 * });
 * ```
 *
 * The following arguments are supported:
 *
 * * `domainId` - (Required) The name or ID of the domain.
 * * `contactId` - (Required) The ID of the contact you are planning to change to.
 *
 * The following additional attributes are exported:
 *
 * * `contactId` - The ID of the contact you are planning to change to.
 * * `domainId` - The name or ID of the domain.
 * * `extendedAttributes` - (List) A list of extended attributes that are required for the registrant change. (see below for nested schema)
 * * `registryOwnerChange` - (Boolean) Whether the registrant change is going to result in an owner change at the registry.
 *
 * <a id="nestedblock--extended_attributes"></a>
 */
export function getRegistrantChangeCheck(args: GetRegistrantChangeCheckArgs, opts?: pulumi.InvokeOptions): Promise<GetRegistrantChangeCheckResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("dnsimple:index/getRegistrantChangeCheck:getRegistrantChangeCheck", {
        "contactId": args.contactId,
        "domainId": args.domainId,
    }, opts);
}

/**
 * A collection of arguments for invoking getRegistrantChangeCheck.
 */
export interface GetRegistrantChangeCheckArgs {
    contactId: string;
    domainId: string;
}

/**
 * A collection of values returned by getRegistrantChangeCheck.
 */
export interface GetRegistrantChangeCheckResult {
    readonly contactId: string;
    readonly domainId: string;
    readonly extendedAttributes: outputs.GetRegistrantChangeCheckExtendedAttribute[];
    readonly id: string;
    readonly registryOwnerChange: boolean;
}
/**
 * Get information on the requirements of a registrant change.
 *
 * > **Note:** The registrant change API is currently in developer preview and is subject to change.
 *
 * Get registrant change requirements for the `dnsimple.com` domain and the contact with ID `1234`:
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as dnsimple from "@pulumi/dnsimple";
 *
 * const example = dnsimple.getRegistrantChangeCheck({
 *     domainId: "dnsimple.com",
 *     contactId: "1234",
 * });
 * ```
 *
 * The following arguments are supported:
 *
 * * `domainId` - (Required) The name or ID of the domain.
 * * `contactId` - (Required) The ID of the contact you are planning to change to.
 *
 * The following additional attributes are exported:
 *
 * * `contactId` - The ID of the contact you are planning to change to.
 * * `domainId` - The name or ID of the domain.
 * * `extendedAttributes` - (List) A list of extended attributes that are required for the registrant change. (see below for nested schema)
 * * `registryOwnerChange` - (Boolean) Whether the registrant change is going to result in an owner change at the registry.
 *
 * <a id="nestedblock--extended_attributes"></a>
 */
export function getRegistrantChangeCheckOutput(args: GetRegistrantChangeCheckOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetRegistrantChangeCheckResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("dnsimple:index/getRegistrantChangeCheck:getRegistrantChangeCheck", {
        "contactId": args.contactId,
        "domainId": args.domainId,
    }, opts);
}

/**
 * A collection of arguments for invoking getRegistrantChangeCheck.
 */
export interface GetRegistrantChangeCheckOutputArgs {
    contactId: pulumi.Input<string>;
    domainId: pulumi.Input<string>;
}
