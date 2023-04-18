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

    @Import(name="accountId")
    private @Nullable Output<Integer> accountId;

    public Optional<Output<Integer>> accountId() {
        return Optional.ofNullable(this.accountId);
    }

    @Import(name="autoRenew")
    private @Nullable Output<Boolean> autoRenew;

    public Optional<Output<Boolean>> autoRenew() {
        return Optional.ofNullable(this.autoRenew);
    }

    @Import(name="name")
    private @Nullable Output<String> name;

    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    @Import(name="privateWhois")
    private @Nullable Output<Boolean> privateWhois;

    public Optional<Output<Boolean>> privateWhois() {
        return Optional.ofNullable(this.privateWhois);
    }

    @Import(name="registrantId")
    private @Nullable Output<Integer> registrantId;

    public Optional<Output<Integer>> registrantId() {
        return Optional.ofNullable(this.registrantId);
    }

    @Import(name="state")
    private @Nullable Output<String> state;

    public Optional<Output<String>> state() {
        return Optional.ofNullable(this.state);
    }

    @Import(name="unicodeName")
    private @Nullable Output<String> unicodeName;

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

        public Builder accountId(@Nullable Output<Integer> accountId) {
            $.accountId = accountId;
            return this;
        }

        public Builder accountId(Integer accountId) {
            return accountId(Output.of(accountId));
        }

        public Builder autoRenew(@Nullable Output<Boolean> autoRenew) {
            $.autoRenew = autoRenew;
            return this;
        }

        public Builder autoRenew(Boolean autoRenew) {
            return autoRenew(Output.of(autoRenew));
        }

        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        public Builder name(String name) {
            return name(Output.of(name));
        }

        public Builder privateWhois(@Nullable Output<Boolean> privateWhois) {
            $.privateWhois = privateWhois;
            return this;
        }

        public Builder privateWhois(Boolean privateWhois) {
            return privateWhois(Output.of(privateWhois));
        }

        public Builder registrantId(@Nullable Output<Integer> registrantId) {
            $.registrantId = registrantId;
            return this;
        }

        public Builder registrantId(Integer registrantId) {
            return registrantId(Output.of(registrantId));
        }

        public Builder state(@Nullable Output<String> state) {
            $.state = state;
            return this;
        }

        public Builder state(String state) {
            return state(Output.of(state));
        }

        public Builder unicodeName(@Nullable Output<String> unicodeName) {
            $.unicodeName = unicodeName;
            return this;
        }

        public Builder unicodeName(String unicodeName) {
            return unicodeName(Output.of(unicodeName));
        }

        public DomainState build() {
            return $;
        }
    }

}