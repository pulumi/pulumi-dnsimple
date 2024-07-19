// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class DomainArgs extends com.pulumi.resources.ResourceArgs {

    public static final DomainArgs Empty = new DomainArgs();

    /**
     * The domain name to be created
     * 
     * # Attributes Reference
     * 
     */
    @Import(name="name", required=true)
    private Output<String> name;

    /**
     * @return The domain name to be created
     * 
     * # Attributes Reference
     * 
     */
    public Output<String> name() {
        return this.name;
    }

    private DomainArgs() {}

    private DomainArgs(DomainArgs $) {
        this.name = $.name;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DomainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DomainArgs $;

        public Builder() {
            $ = new DomainArgs();
        }

        public Builder(DomainArgs defaults) {
            $ = new DomainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param name The domain name to be created
         * 
         * # Attributes Reference
         * 
         * @return builder
         * 
         */
        public Builder name(Output<String> name) {
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

        public DomainArgs build() {
            if ($.name == null) {
                throw new MissingRequiredPropertyException("DomainArgs", "name");
            }
            return $;
        }
    }

}
