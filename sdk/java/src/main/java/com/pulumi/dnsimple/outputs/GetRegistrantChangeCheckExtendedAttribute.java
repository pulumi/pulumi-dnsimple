// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.dnsimple.outputs.GetRegistrantChangeCheckExtendedAttributeOption;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetRegistrantChangeCheckExtendedAttribute {
    private String description;
    private String name;
    private List<GetRegistrantChangeCheckExtendedAttributeOption> options;
    private Boolean required;

    private GetRegistrantChangeCheckExtendedAttribute() {}
    public String description() {
        return this.description;
    }
    public String name() {
        return this.name;
    }
    public List<GetRegistrantChangeCheckExtendedAttributeOption> options() {
        return this.options;
    }
    public Boolean required() {
        return this.required;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetRegistrantChangeCheckExtendedAttribute defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String description;
        private String name;
        private List<GetRegistrantChangeCheckExtendedAttributeOption> options;
        private Boolean required;
        public Builder() {}
        public Builder(GetRegistrantChangeCheckExtendedAttribute defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.description = defaults.description;
    	      this.name = defaults.name;
    	      this.options = defaults.options;
    	      this.required = defaults.required;
        }

        @CustomType.Setter
        public Builder description(String description) {
            this.description = Objects.requireNonNull(description);
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            this.name = Objects.requireNonNull(name);
            return this;
        }
        @CustomType.Setter
        public Builder options(List<GetRegistrantChangeCheckExtendedAttributeOption> options) {
            this.options = Objects.requireNonNull(options);
            return this;
        }
        public Builder options(GetRegistrantChangeCheckExtendedAttributeOption... options) {
            return options(List.of(options));
        }
        @CustomType.Setter
        public Builder required(Boolean required) {
            this.required = Objects.requireNonNull(required);
            return this;
        }
        public GetRegistrantChangeCheckExtendedAttribute build() {
            final var _resultValue = new GetRegistrantChangeCheckExtendedAttribute();
            _resultValue.description = description;
            _resultValue.name = name;
            _resultValue.options = options;
            _resultValue.required = required;
            return _resultValue;
        }
    }
}