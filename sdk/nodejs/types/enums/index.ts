// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const RecordTypes = {
    A: "A",
    AAAA: "AAAA",
    ALIAS: "ALIAS",
    CAA: "CAA",
    CNAME: "CNAME",
    HINFO: "HINFO",
    MX: "MX",
    NAPTR: "NAPTR",
    NS: "NS",
    POOL: "POOL",
    PTR: "PTR",
    SPF: "SPF",
    SRV: "SRV",
    SSHFP: "SSHFP",
    TXT: "TXT",
    URL: "URL",
} as const;

/**
 * DNS Record types.
 */
export type RecordTypes = (typeof RecordTypes)[keyof typeof RecordTypes];