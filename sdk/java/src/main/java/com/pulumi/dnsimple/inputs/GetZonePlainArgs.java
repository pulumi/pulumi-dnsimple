// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;


public final class GetZonePlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetZonePlainArgs Empty = new GetZonePlainArgs();

    @Import(name="name", required=true)
    private String name;

    public String name() {
        return this.name;
    }

    private GetZonePlainArgs() {}

    private GetZonePlainArgs(GetZonePlainArgs $) {
        this.name = $.name;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetZonePlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetZonePlainArgs $;

        public Builder() {
            $ = new GetZonePlainArgs();
        }

        public Builder(GetZonePlainArgs defaults) {
            $ = new GetZonePlainArgs(Objects.requireNonNull(defaults));
        }

        public Builder name(String name) {
            $.name = name;
            return this;
        }

        public GetZonePlainArgs build() {
            $.name = Objects.requireNonNull($.name, "expected parameter 'name' to be non-null");
            return $;
        }
    }

}