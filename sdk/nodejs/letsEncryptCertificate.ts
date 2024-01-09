// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class LetsEncryptCertificate extends pulumi.CustomResource {
    /**
     * Get an existing LetsEncryptCertificate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LetsEncryptCertificateState, opts?: pulumi.CustomResourceOptions): LetsEncryptCertificate {
        return new LetsEncryptCertificate(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'dnsimple:index/letsEncryptCertificate:LetsEncryptCertificate';

    /**
     * Returns true if the given object is an instance of LetsEncryptCertificate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LetsEncryptCertificate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LetsEncryptCertificate.__pulumiType;
    }

    public readonly alternateNames!: pulumi.Output<string[] | undefined>;
    public /*out*/ readonly authorityIdentifier!: pulumi.Output<string>;
    public readonly autoRenew!: pulumi.Output<boolean>;
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    public /*out*/ readonly csr!: pulumi.Output<string>;
    public readonly domainId!: pulumi.Output<string>;
    public /*out*/ readonly expiresAt!: pulumi.Output<string>;
    public readonly name!: pulumi.Output<string>;
    public readonly signatureAlgorithm!: pulumi.Output<string | undefined>;
    public /*out*/ readonly state!: pulumi.Output<string>;
    public /*out*/ readonly updatedAt!: pulumi.Output<string>;
    public /*out*/ readonly years!: pulumi.Output<number>;

    /**
     * Create a LetsEncryptCertificate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LetsEncryptCertificateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: LetsEncryptCertificateArgs | LetsEncryptCertificateState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as LetsEncryptCertificateState | undefined;
            resourceInputs["alternateNames"] = state ? state.alternateNames : undefined;
            resourceInputs["authorityIdentifier"] = state ? state.authorityIdentifier : undefined;
            resourceInputs["autoRenew"] = state ? state.autoRenew : undefined;
            resourceInputs["createdAt"] = state ? state.createdAt : undefined;
            resourceInputs["csr"] = state ? state.csr : undefined;
            resourceInputs["domainId"] = state ? state.domainId : undefined;
            resourceInputs["expiresAt"] = state ? state.expiresAt : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["signatureAlgorithm"] = state ? state.signatureAlgorithm : undefined;
            resourceInputs["state"] = state ? state.state : undefined;
            resourceInputs["updatedAt"] = state ? state.updatedAt : undefined;
            resourceInputs["years"] = state ? state.years : undefined;
        } else {
            const args = argsOrState as LetsEncryptCertificateArgs | undefined;
            if ((!args || args.autoRenew === undefined) && !opts.urn) {
                throw new Error("Missing required property 'autoRenew'");
            }
            if ((!args || args.domainId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'domainId'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            resourceInputs["alternateNames"] = args ? args.alternateNames : undefined;
            resourceInputs["autoRenew"] = args ? args.autoRenew : undefined;
            resourceInputs["domainId"] = args ? args.domainId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["signatureAlgorithm"] = args ? args.signatureAlgorithm : undefined;
            resourceInputs["authorityIdentifier"] = undefined /*out*/;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["csr"] = undefined /*out*/;
            resourceInputs["expiresAt"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["updatedAt"] = undefined /*out*/;
            resourceInputs["years"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(LetsEncryptCertificate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering LetsEncryptCertificate resources.
 */
export interface LetsEncryptCertificateState {
    alternateNames?: pulumi.Input<pulumi.Input<string>[]>;
    authorityIdentifier?: pulumi.Input<string>;
    autoRenew?: pulumi.Input<boolean>;
    createdAt?: pulumi.Input<string>;
    csr?: pulumi.Input<string>;
    domainId?: pulumi.Input<string>;
    expiresAt?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    signatureAlgorithm?: pulumi.Input<string>;
    state?: pulumi.Input<string>;
    updatedAt?: pulumi.Input<string>;
    years?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a LetsEncryptCertificate resource.
 */
export interface LetsEncryptCertificateArgs {
    alternateNames?: pulumi.Input<pulumi.Input<string>[]>;
    autoRenew: pulumi.Input<boolean>;
    domainId: pulumi.Input<string>;
    name: pulumi.Input<string>;
    signatureAlgorithm?: pulumi.Input<string>;
}
