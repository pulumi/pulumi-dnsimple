// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class DomainState extends com.pulumi.resources.ResourceArgs {

    public static final DomainState Empty = new DomainState();

    /**
     * The account ID for the domain.
     * 
     */
    @Import(name="accountId")
    private @Nullable Output<Integer> accountId;

    /**
     * @return The account ID for the domain.
     * 
     */
    public Optional<Output<Integer>> accountId() {
        return Optional.ofNullable(this.accountId);
    }

    /**
     * Whether the domain is set to auto-renew.
     * 
     */
    @Import(name="autoRenew")
    private @Nullable Output<Boolean> autoRenew;

    /**
     * @return Whether the domain is set to auto-renew.
     * 
     */
    public Optional<Output<Boolean>> autoRenew() {
        return Optional.ofNullable(this.autoRenew);
    }

    /**
     * The domain name to be created
     * 
     * # Attributes Reference
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The domain name to be created
     * 
     * # Attributes Reference
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * Whether the domain has WhoIs privacy enabled.
     * 
     */
    @Import(name="privateWhois")
    private @Nullable Output<Boolean> privateWhois;

    /**
     * @return Whether the domain has WhoIs privacy enabled.
     * 
     */
    public Optional<Output<Boolean>> privateWhois() {
        return Optional.ofNullable(this.privateWhois);
    }

    /**
     * The ID of the registrant (contact) for the domain.
     * 
     */
    @Import(name="registrantId")
    private @Nullable Output<Integer> registrantId;

    /**
     * @return The ID of the registrant (contact) for the domain.
     * 
     */
    public Optional<Output<Integer>> registrantId() {
        return Optional.ofNullable(this.registrantId);
    }

    /**
     * The state of the domain.
     * 
     */
    @Import(name="state")
    private @Nullable Output<String> state;

    /**
     * @return The state of the domain.
     * 
     */
    public Optional<Output<String>> state() {
        return Optional.ofNullable(this.state);
    }

    /**
     * The domain name in Unicode format.
     * 
     */
    @Import(name="unicodeName")
    private @Nullable Output<String> unicodeName;

    /**
     * @return The domain name in Unicode format.
     * 
     */
    public Optional<Output<String>> unicodeName() {
        return Optional.ofNullable(this.unicodeName);
    }

    private DomainState() {}

    private DomainState(DomainState $) {
        this.accountId = $.accountId;
        this.autoRenew = $.autoRenew;
        this.name = $.name;
        this.privateWhois = $.privateWhois;
        this.registrantId = $.registrantId;
        this.state = $.state;
        this.unicodeName = $.unicodeName;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DomainState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DomainState $;

        public Builder() {
            $ = new DomainState();
        }

        public Builder(DomainState defaults) {
            $ = new DomainState(Objects.requireNonNull(defaults));
        }

        /**
         * @param accountId The account ID for the domain.
         * 
         * @return builder
         * 
         */
        public Builder accountId(@Nullable Output<Integer> accountId) {
            $.accountId = accountId;
            return this;
        }

        /**
         * @param accountId The account ID for the domain.
         * 
         * @return builder
         * 
         */
        public Builder accountId(Integer accountId) {
            return accountId(Output.of(accountId));
        }

        /**
         * @param autoRenew Whether the domain is set to auto-renew.
         * 
         * @return builder
         * 
         */
        public Builder autoRenew(@Nullable Output<Boolean> autoRenew) {
            $.autoRenew = autoRenew;
            return this;
        }

        /**
         * @param autoRenew Whether the domain is set to auto-renew.
         * 
         * @return builder
         * 
         */
        public Builder autoRenew(Boolean autoRenew) {
            return autoRenew(Output.of(autoRenew));
        }

        /**
         * @param name The domain name to be created
         * 
         * # Attributes Reference
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The domain name to be created
         * 
         * # Attributes Reference
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param privateWhois Whether the domain has WhoIs privacy enabled.
         * 
         * @return builder
         * 
         */
        public Builder privateWhois(@Nullable Output<Boolean> privateWhois) {
            $.privateWhois = privateWhois;
            return this;
        }

        /**
         * @param privateWhois Whether the domain has WhoIs privacy enabled.
         * 
         * @return builder
         * 
         */
        public Builder privateWhois(Boolean privateWhois) {
            return privateWhois(Output.of(privateWhois));
        }

        /**
         * @param registrantId The ID of the registrant (contact) for the domain.
         * 
         * @return builder
         * 
         */
        public Builder registrantId(@Nullable Output<Integer> registrantId) {
            $.registrantId = registrantId;
            return this;
        }

        /**
         * @param registrantId The ID of the registrant (contact) for the domain.
         * 
         * @return builder
         * 
         */
        public Builder registrantId(Integer registrantId) {
            return registrantId(Output.of(registrantId));
        }

        /**
         * @param state The state of the domain.
         * 
         * @return builder
         * 
         */
        public Builder state(@Nullable Output<String> state) {
            $.state = state;
            return this;
        }

        /**
         * @param state The state of the domain.
         * 
         * @return builder
         * 
         */
        public Builder state(String state) {
            return state(Output.of(state));
        }

        /**
         * @param unicodeName The domain name in Unicode format.
         * 
         * @return builder
         * 
         */
        public Builder unicodeName(@Nullable Output<String> unicodeName) {
            $.unicodeName = unicodeName;
            return this;
        }

        /**
         * @param unicodeName The domain name in Unicode format.
         * 
         * @return builder
         * 
         */
        public Builder unicodeName(String unicodeName) {
            return unicodeName(Output.of(unicodeName));
        }

        public DomainState build() {
            return $;
        }
    }

}
