// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetRegistrantChangeCheckExtendedAttributeOption {
    private String description;
    private String title;
    private String value;

    private GetRegistrantChangeCheckExtendedAttributeOption() {}
    public String description() {
        return this.description;
    }
    public String title() {
        return this.title;
    }
    public String value() {
        return this.value;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetRegistrantChangeCheckExtendedAttributeOption defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String description;
        private String title;
        private String value;
        public Builder() {}
        public Builder(GetRegistrantChangeCheckExtendedAttributeOption defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.description = defaults.description;
    	      this.title = defaults.title;
    	      this.value = defaults.value;
        }

        @CustomType.Setter
        public Builder description(String description) {
            this.description = Objects.requireNonNull(description);
            return this;
        }
        @CustomType.Setter
        public Builder title(String title) {
            this.title = Objects.requireNonNull(title);
            return this;
        }
        @CustomType.Setter
        public Builder value(String value) {
            this.value = Objects.requireNonNull(value);
            return this;
        }
        public GetRegistrantChangeCheckExtendedAttributeOption build() {
            final var _resultValue = new GetRegistrantChangeCheckExtendedAttributeOption();
            _resultValue.description = description;
            _resultValue.title = title;
            _resultValue.value = value;
            return _resultValue;
        }
    }
}
