// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a DNSimple certificate data source.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as dnsimple from "@pulumi/dnsimple";
 *
 * const foobar = dnsimple.getCertificate({
 *     domain: dnsimpleDomain,
 *     certificateId: dnsimpleCertificateId,
 * });
 * ```
 */
export function getCertificate(args: GetCertificateArgs, opts?: pulumi.InvokeOptions): Promise<GetCertificateResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("dnsimple:index/getCertificate:getCertificate", {
        "certificateId": args.certificateId,
        "domain": args.domain,
    }, opts);
}

/**
 * A collection of arguments for invoking getCertificate.
 */
export interface GetCertificateArgs {
    /**
     * The ID of the SSL Certificate
     */
    certificateId: string;
    /**
     * The domain of the SSL Certificate
     */
    domain: string;
}

/**
 * A collection of values returned by getCertificate.
 */
export interface GetCertificateResult {
    /**
     * A list of certificates that make up the chain
     */
    readonly certificateChains: string[];
    readonly certificateId: string;
    readonly domain: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The corresponding Private Key for the SSL Certificate
     */
    readonly privateKey: string;
    /**
     * The Root Certificate of the issuing CA
     */
    readonly rootCertificate: string;
    /**
     * The SSL Certificate
     */
    readonly serverCertificate: string;
}
/**
 * Provides a DNSimple certificate data source.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as dnsimple from "@pulumi/dnsimple";
 *
 * const foobar = dnsimple.getCertificate({
 *     domain: dnsimpleDomain,
 *     certificateId: dnsimpleCertificateId,
 * });
 * ```
 */
export function getCertificateOutput(args: GetCertificateOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetCertificateResult> {
    return pulumi.output(args).apply((a: any) => getCertificate(a, opts))
}

/**
 * A collection of arguments for invoking getCertificate.
 */
export interface GetCertificateOutputArgs {
    /**
     * The ID of the SSL Certificate
     */
    certificateId: pulumi.Input<string>;
    /**
     * The domain of the SSL Certificate
     */
    domain: pulumi.Input<string>;
}
