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


public final class ZoneState extends com.pulumi.resources.ResourceArgs {

    public static final ZoneState Empty = new ZoneState();

    /**
     * The account ID for the zone.
     * 
     */
    @Import(name="accountId")
    private @Nullable Output<Integer> accountId;

    /**
     * @return The account ID for the zone.
     * 
     */
    public Optional<Output<Integer>> accountId() {
        return Optional.ofNullable(this.accountId);
    }

    /**
     * Whether the zone is active.
     * 
     */
    @Import(name="active")
    private @Nullable Output<Boolean> active;

    /**
     * @return Whether the zone is active.
     * 
     */
    public Optional<Output<Boolean>> active() {
        return Optional.ofNullable(this.active);
    }

    /**
     * The last time the zone was transferred only applicable for **secondary** zones.
     * 
     */
    @Import(name="lastTransferredAt")
    private @Nullable Output<String> lastTransferredAt;

    /**
     * @return The last time the zone was transferred only applicable for **secondary** zones.
     * 
     */
    public Optional<Output<String>> lastTransferredAt() {
        return Optional.ofNullable(this.lastTransferredAt);
    }

    /**
     * The zone name
     * 
     * # Attributes Reference
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The zone name
     * 
     * # Attributes Reference
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * Whether the zone is a reverse zone.
     * 
     */
    @Import(name="reverse")
    private @Nullable Output<Boolean> reverse;

    /**
     * @return Whether the zone is a reverse zone.
     * 
     */
    public Optional<Output<Boolean>> reverse() {
        return Optional.ofNullable(this.reverse);
    }

    /**
     * Whether the zone is a secondary zone.
     * 
     */
    @Import(name="secondary")
    private @Nullable Output<Boolean> secondary;

    /**
     * @return Whether the zone is a secondary zone.
     * 
     */
    public Optional<Output<Boolean>> secondary() {
        return Optional.ofNullable(this.secondary);
    }

    private ZoneState() {}

    private ZoneState(ZoneState $) {
        this.accountId = $.accountId;
        this.active = $.active;
        this.lastTransferredAt = $.lastTransferredAt;
        this.name = $.name;
        this.reverse = $.reverse;
        this.secondary = $.secondary;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ZoneState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ZoneState $;

        public Builder() {
            $ = new ZoneState();
        }

        public Builder(ZoneState defaults) {
            $ = new ZoneState(Objects.requireNonNull(defaults));
        }

        /**
         * @param accountId The account ID for the zone.
         * 
         * @return builder
         * 
         */
        public Builder accountId(@Nullable Output<Integer> accountId) {
            $.accountId = accountId;
            return this;
        }

        /**
         * @param accountId The account ID for the zone.
         * 
         * @return builder
         * 
         */
        public Builder accountId(Integer accountId) {
            return accountId(Output.of(accountId));
        }

        /**
         * @param active Whether the zone is active.
         * 
         * @return builder
         * 
         */
        public Builder active(@Nullable Output<Boolean> active) {
            $.active = active;
            return this;
        }

        /**
         * @param active Whether the zone is active.
         * 
         * @return builder
         * 
         */
        public Builder active(Boolean active) {
            return active(Output.of(active));
        }

        /**
         * @param lastTransferredAt The last time the zone was transferred only applicable for **secondary** zones.
         * 
         * @return builder
         * 
         */
        public Builder lastTransferredAt(@Nullable Output<String> lastTransferredAt) {
            $.lastTransferredAt = lastTransferredAt;
            return this;
        }

        /**
         * @param lastTransferredAt The last time the zone was transferred only applicable for **secondary** zones.
         * 
         * @return builder
         * 
         */
        public Builder lastTransferredAt(String lastTransferredAt) {
            return lastTransferredAt(Output.of(lastTransferredAt));
        }

        /**
         * @param name The zone name
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
         * @param name The zone name
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
         * @param reverse Whether the zone is a reverse zone.
         * 
         * @return builder
         * 
         */
        public Builder reverse(@Nullable Output<Boolean> reverse) {
            $.reverse = reverse;
            return this;
        }

        /**
         * @param reverse Whether the zone is a reverse zone.
         * 
         * @return builder
         * 
         */
        public Builder reverse(Boolean reverse) {
            return reverse(Output.of(reverse));
        }

        /**
         * @param secondary Whether the zone is a secondary zone.
         * 
         * @return builder
         * 
         */
        public Builder secondary(@Nullable Output<Boolean> secondary) {
            $.secondary = secondary;
            return this;
        }

        /**
         * @param secondary Whether the zone is a secondary zone.
         * 
         * @return builder
         * 
         */
        public Builder secondary(Boolean secondary) {
            return secondary(Output.of(secondary));
        }

        public ZoneState build() {
            return $;
        }
    }

}
