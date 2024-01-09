// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";

export interface RegisteredDomainDomainRegistration {
    id?: pulumi.Input<number>;
    period?: pulumi.Input<number>;
    state?: pulumi.Input<string>;
}

export interface RegisteredDomainRegistrantChange {
    accountId?: pulumi.Input<number>;
    contactId?: pulumi.Input<number>;
    domainId?: pulumi.Input<string>;
    extendedAttributes?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    id?: pulumi.Input<number>;
    irtLockLiftedBy?: pulumi.Input<string>;
    registryOwnerChange?: pulumi.Input<boolean>;
    state?: pulumi.Input<string>;
}

export interface RegisteredDomainTimeouts {
    create?: pulumi.Input<string>;
    delete?: pulumi.Input<string>;
    update?: pulumi.Input<string>;
}
