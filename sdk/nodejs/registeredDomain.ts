// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as enums from "./types/enums";
import * as utilities from "./utilities";

export class RegisteredDomain extends pulumi.CustomResource {
    /**
     * Get an existing RegisteredDomain resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RegisteredDomainState, opts?: pulumi.CustomResourceOptions): RegisteredDomain {
        return new RegisteredDomain(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'dnsimple:index/registeredDomain:RegisteredDomain';

    /**
     * Returns true if the given object is an instance of RegisteredDomain.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RegisteredDomain {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RegisteredDomain.__pulumiType;
    }

    public /*out*/ readonly accountId!: pulumi.Output<number>;
    public readonly autoRenewEnabled!: pulumi.Output<boolean>;
    public readonly contactId!: pulumi.Output<number>;
    public readonly dnssecEnabled!: pulumi.Output<boolean>;
    /**
     * The domain registration details.
     */
    public /*out*/ readonly domainRegistration!: pulumi.Output<outputs.RegisteredDomainDomainRegistration>;
    public /*out*/ readonly expiresAt!: pulumi.Output<string>;
    public readonly extendedAttributes!: pulumi.Output<{[key: string]: string} | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly premiumPrice!: pulumi.Output<string | undefined>;
    /**
     * The registrant change details.
     */
    public /*out*/ readonly registrantChange!: pulumi.Output<outputs.RegisteredDomainRegistrantChange>;
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * Timeouts for operations, given as a parsable string as in `10m` or `30s`.
     */
    public readonly timeouts!: pulumi.Output<outputs.RegisteredDomainTimeouts | undefined>;
    public readonly transferLockEnabled!: pulumi.Output<boolean>;
    public /*out*/ readonly unicodeName!: pulumi.Output<string>;
    public readonly whoisPrivacyEnabled!: pulumi.Output<boolean>;

    /**
     * Create a RegisteredDomain resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RegisteredDomainArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RegisteredDomainArgs | RegisteredDomainState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as RegisteredDomainState | undefined;
            resourceInputs["accountId"] = state ? state.accountId : undefined;
            resourceInputs["autoRenewEnabled"] = state ? state.autoRenewEnabled : undefined;
            resourceInputs["contactId"] = state ? state.contactId : undefined;
            resourceInputs["dnssecEnabled"] = state ? state.dnssecEnabled : undefined;
            resourceInputs["domainRegistration"] = state ? state.domainRegistration : undefined;
            resourceInputs["expiresAt"] = state ? state.expiresAt : undefined;
            resourceInputs["extendedAttributes"] = state ? state.extendedAttributes : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["premiumPrice"] = state ? state.premiumPrice : undefined;
            resourceInputs["registrantChange"] = state ? state.registrantChange : undefined;
            resourceInputs["state"] = state ? state.state : undefined;
            resourceInputs["timeouts"] = state ? state.timeouts : undefined;
            resourceInputs["transferLockEnabled"] = state ? state.transferLockEnabled : undefined;
            resourceInputs["unicodeName"] = state ? state.unicodeName : undefined;
            resourceInputs["whoisPrivacyEnabled"] = state ? state.whoisPrivacyEnabled : undefined;
        } else {
            const args = argsOrState as RegisteredDomainArgs | undefined;
            if ((!args || args.contactId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'contactId'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            resourceInputs["autoRenewEnabled"] = args ? args.autoRenewEnabled : undefined;
            resourceInputs["contactId"] = args ? args.contactId : undefined;
            resourceInputs["dnssecEnabled"] = args ? args.dnssecEnabled : undefined;
            resourceInputs["extendedAttributes"] = args ? args.extendedAttributes : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["premiumPrice"] = args ? args.premiumPrice : undefined;
            resourceInputs["timeouts"] = args ? args.timeouts : undefined;
            resourceInputs["transferLockEnabled"] = args ? args.transferLockEnabled : undefined;
            resourceInputs["whoisPrivacyEnabled"] = args ? args.whoisPrivacyEnabled : undefined;
            resourceInputs["accountId"] = undefined /*out*/;
            resourceInputs["domainRegistration"] = undefined /*out*/;
            resourceInputs["expiresAt"] = undefined /*out*/;
            resourceInputs["registrantChange"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["unicodeName"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(RegisteredDomain.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RegisteredDomain resources.
 */
export interface RegisteredDomainState {
    accountId?: pulumi.Input<number>;
    autoRenewEnabled?: pulumi.Input<boolean>;
    contactId?: pulumi.Input<number>;
    dnssecEnabled?: pulumi.Input<boolean>;
    /**
     * The domain registration details.
     */
    domainRegistration?: pulumi.Input<inputs.RegisteredDomainDomainRegistration>;
    expiresAt?: pulumi.Input<string>;
    extendedAttributes?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    name?: pulumi.Input<string>;
    premiumPrice?: pulumi.Input<string>;
    /**
     * The registrant change details.
     */
    registrantChange?: pulumi.Input<inputs.RegisteredDomainRegistrantChange>;
    state?: pulumi.Input<string>;
    /**
     * Timeouts for operations, given as a parsable string as in `10m` or `30s`.
     */
    timeouts?: pulumi.Input<inputs.RegisteredDomainTimeouts>;
    transferLockEnabled?: pulumi.Input<boolean>;
    unicodeName?: pulumi.Input<string>;
    whoisPrivacyEnabled?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a RegisteredDomain resource.
 */
export interface RegisteredDomainArgs {
    autoRenewEnabled?: pulumi.Input<boolean>;
    contactId: pulumi.Input<number>;
    dnssecEnabled?: pulumi.Input<boolean>;
    extendedAttributes?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    name: pulumi.Input<string>;
    premiumPrice?: pulumi.Input<string>;
    /**
     * Timeouts for operations, given as a parsable string as in `10m` or `30s`.
     */
    timeouts?: pulumi.Input<inputs.RegisteredDomainTimeouts>;
    transferLockEnabled?: pulumi.Input<boolean>;
    whoisPrivacyEnabled?: pulumi.Input<boolean>;
}
