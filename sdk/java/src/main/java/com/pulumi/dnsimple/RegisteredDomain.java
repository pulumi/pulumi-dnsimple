// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.dnsimple.RegisteredDomainArgs;
import com.pulumi.dnsimple.Utilities;
import com.pulumi.dnsimple.inputs.RegisteredDomainState;
import com.pulumi.dnsimple.outputs.RegisteredDomainDomainRegistration;
import com.pulumi.dnsimple.outputs.RegisteredDomainRegistrantChange;
import com.pulumi.dnsimple.outputs.RegisteredDomainTimeouts;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Map;
import java.util.Optional;
import javax.annotation.Nullable;

@ResourceType(type="dnsimple:index/registeredDomain:RegisteredDomain")
public class RegisteredDomain extends com.pulumi.resources.CustomResource {
    @Export(name="accountId", refs={Integer.class}, tree="[0]")
    private Output<Integer> accountId;

    public Output<Integer> accountId() {
        return this.accountId;
    }
    @Export(name="autoRenewEnabled", refs={Boolean.class}, tree="[0]")
    private Output<Boolean> autoRenewEnabled;

    public Output<Boolean> autoRenewEnabled() {
        return this.autoRenewEnabled;
    }
    @Export(name="contactId", refs={Integer.class}, tree="[0]")
    private Output<Integer> contactId;

    public Output<Integer> contactId() {
        return this.contactId;
    }
    @Export(name="dnssecEnabled", refs={Boolean.class}, tree="[0]")
    private Output<Boolean> dnssecEnabled;

    public Output<Boolean> dnssecEnabled() {
        return this.dnssecEnabled;
    }
    /**
     * The domain registration details.
     * 
     */
    @Export(name="domainRegistration", refs={RegisteredDomainDomainRegistration.class}, tree="[0]")
    private Output<RegisteredDomainDomainRegistration> domainRegistration;

    /**
     * @return The domain registration details.
     * 
     */
    public Output<RegisteredDomainDomainRegistration> domainRegistration() {
        return this.domainRegistration;
    }
    @Export(name="expiresAt", refs={String.class}, tree="[0]")
    private Output<String> expiresAt;

    public Output<String> expiresAt() {
        return this.expiresAt;
    }
    @Export(name="extendedAttributes", refs={Map.class,String.class}, tree="[0,1,1]")
    private Output</* @Nullable */ Map<String,String>> extendedAttributes;

    public Output<Optional<Map<String,String>>> extendedAttributes() {
        return Codegen.optional(this.extendedAttributes);
    }
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    public Output<String> name() {
        return this.name;
    }
    @Export(name="premiumPrice", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> premiumPrice;

    public Output<Optional<String>> premiumPrice() {
        return Codegen.optional(this.premiumPrice);
    }
    /**
     * The registrant change details.
     * 
     */
    @Export(name="registrantChange", refs={RegisteredDomainRegistrantChange.class}, tree="[0]")
    private Output<RegisteredDomainRegistrantChange> registrantChange;

    /**
     * @return The registrant change details.
     * 
     */
    public Output<RegisteredDomainRegistrantChange> registrantChange() {
        return this.registrantChange;
    }
    @Export(name="state", refs={String.class}, tree="[0]")
    private Output<String> state;

    public Output<String> state() {
        return this.state;
    }
    /**
     * Timeouts for operations, given as a parsable string as in `10m` or `30s`.
     * 
     */
    @Export(name="timeouts", refs={RegisteredDomainTimeouts.class}, tree="[0]")
    private Output</* @Nullable */ RegisteredDomainTimeouts> timeouts;

    /**
     * @return Timeouts for operations, given as a parsable string as in `10m` or `30s`.
     * 
     */
    public Output<Optional<RegisteredDomainTimeouts>> timeouts() {
        return Codegen.optional(this.timeouts);
    }
    @Export(name="transferLockEnabled", refs={Boolean.class}, tree="[0]")
    private Output<Boolean> transferLockEnabled;

    public Output<Boolean> transferLockEnabled() {
        return this.transferLockEnabled;
    }
    @Export(name="unicodeName", refs={String.class}, tree="[0]")
    private Output<String> unicodeName;

    public Output<String> unicodeName() {
        return this.unicodeName;
    }
    @Export(name="whoisPrivacyEnabled", refs={Boolean.class}, tree="[0]")
    private Output<Boolean> whoisPrivacyEnabled;

    public Output<Boolean> whoisPrivacyEnabled() {
        return this.whoisPrivacyEnabled;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public RegisteredDomain(String name) {
        this(name, RegisteredDomainArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public RegisteredDomain(String name, RegisteredDomainArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public RegisteredDomain(String name, RegisteredDomainArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("dnsimple:index/registeredDomain:RegisteredDomain", name, args == null ? RegisteredDomainArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private RegisteredDomain(String name, Output<String> id, @Nullable RegisteredDomainState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("dnsimple:index/registeredDomain:RegisteredDomain", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static RegisteredDomain get(String name, Output<String> id, @Nullable RegisteredDomainState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new RegisteredDomain(name, id, state, options);
    }
}
