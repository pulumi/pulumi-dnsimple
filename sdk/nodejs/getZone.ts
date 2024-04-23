// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Get information about a DNSimple zone.
 *
 * Get zone:
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as dnsimple from "@pulumi/dnsimple";
 *
 * const foobar = dnsimple.getZone({
 *     name: "dnsimple.com",
 * });
 * ```
 *
 * The following arguments are supported:
 *
 * * `name` - (Required) The name of the zone
 *
 * The following attributes are exported:
 *
 * * `id` - The zone ID
 * * `accountId` - The account ID
 * * `name` - The name of the zone
 * * `reverse` - True for a reverse zone, false for a forward zone.
 */
export function getZone(args: GetZoneArgs, opts?: pulumi.InvokeOptions): Promise<GetZoneResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("dnsimple:index/getZone:getZone", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getZone.
 */
export interface GetZoneArgs {
    name: string;
}

/**
 * A collection of values returned by getZone.
 */
export interface GetZoneResult {
    readonly accountId: number;
    readonly id: number;
    readonly name: string;
    readonly reverse: boolean;
}
/**
 * Get information about a DNSimple zone.
 *
 * Get zone:
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as dnsimple from "@pulumi/dnsimple";
 *
 * const foobar = dnsimple.getZone({
 *     name: "dnsimple.com",
 * });
 * ```
 *
 * The following arguments are supported:
 *
 * * `name` - (Required) The name of the zone
 *
 * The following attributes are exported:
 *
 * * `id` - The zone ID
 * * `accountId` - The account ID
 * * `name` - The name of the zone
 * * `reverse` - True for a reverse zone, false for a forward zone.
 */
export function getZoneOutput(args: GetZoneOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetZoneResult> {
    return pulumi.output(args).apply((a: any) => getZone(a, opts))
}

/**
 * A collection of arguments for invoking getZone.
 */
export interface GetZoneOutputArgs {
    name: pulumi.Input<string>;
}
