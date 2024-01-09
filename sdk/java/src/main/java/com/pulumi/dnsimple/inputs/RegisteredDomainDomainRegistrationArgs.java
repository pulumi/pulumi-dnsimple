// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class RegisteredDomainDomainRegistrationArgs extends com.pulumi.resources.ResourceArgs {

    public static final RegisteredDomainDomainRegistrationArgs Empty = new RegisteredDomainDomainRegistrationArgs();

    @Import(name="id")
    private @Nullable Output<Integer> id;

    public Optional<Output<Integer>> id() {
        return Optional.ofNullable(this.id);
    }

    @Import(name="period")
    private @Nullable Output<Integer> period;

    public Optional<Output<Integer>> period() {
        return Optional.ofNullable(this.period);
    }

    @Import(name="state")
    private @Nullable Output<String> state;

    public Optional<Output<String>> state() {
        return Optional.ofNullable(this.state);
    }

    private RegisteredDomainDomainRegistrationArgs() {}

    private RegisteredDomainDomainRegistrationArgs(RegisteredDomainDomainRegistrationArgs $) {
        this.id = $.id;
        this.period = $.period;
        this.state = $.state;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(RegisteredDomainDomainRegistrationArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private RegisteredDomainDomainRegistrationArgs $;

        public Builder() {
            $ = new RegisteredDomainDomainRegistrationArgs();
        }

        public Builder(RegisteredDomainDomainRegistrationArgs defaults) {
            $ = new RegisteredDomainDomainRegistrationArgs(Objects.requireNonNull(defaults));
        }

        public Builder id(@Nullable Output<Integer> id) {
            $.id = id;
            return this;
        }

        public Builder id(Integer id) {
            return id(Output.of(id));
        }

        public Builder period(@Nullable Output<Integer> period) {
            $.period = period;
            return this;
        }

        public Builder period(Integer period) {
            return period(Output.of(period));
        }

        public Builder state(@Nullable Output<String> state) {
            $.state = state;
            return this;
        }

        public Builder state(String state) {
            return state(Output.of(state));
        }

        public RegisteredDomainDomainRegistrationArgs build() {
            return $;
        }
    }

}
