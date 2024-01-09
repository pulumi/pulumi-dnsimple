// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.List;
import java.util.Objects;


public final class DomainDelegationArgs extends com.pulumi.resources.ResourceArgs {

    public static final DomainDelegationArgs Empty = new DomainDelegationArgs();

    @Import(name="domain", required=true)
    private Output<String> domain;

    public Output<String> domain() {
        return this.domain;
    }

    @Import(name="nameServers", required=true)
    private Output<List<String>> nameServers;

    public Output<List<String>> nameServers() {
        return this.nameServers;
    }

    private DomainDelegationArgs() {}

    private DomainDelegationArgs(DomainDelegationArgs $) {
        this.domain = $.domain;
        this.nameServers = $.nameServers;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DomainDelegationArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DomainDelegationArgs $;

        public Builder() {
            $ = new DomainDelegationArgs();
        }

        public Builder(DomainDelegationArgs defaults) {
            $ = new DomainDelegationArgs(Objects.requireNonNull(defaults));
        }

        public Builder domain(Output<String> domain) {
            $.domain = domain;
            return this;
        }

        public Builder domain(String domain) {
            return domain(Output.of(domain));
        }

        public Builder nameServers(Output<List<String>> nameServers) {
            $.nameServers = nameServers;
            return this;
        }

        public Builder nameServers(List<String> nameServers) {
            return nameServers(Output.of(nameServers));
        }

        public Builder nameServers(String... nameServers) {
            return nameServers(List.of(nameServers));
        }

        public DomainDelegationArgs build() {
            if ($.domain == null) {
                throw new MissingRequiredPropertyException("DomainDelegationArgs", "domain");
            }
            if ($.nameServers == null) {
                throw new MissingRequiredPropertyException("DomainDelegationArgs", "nameServers");
            }
            return $;
        }
    }

}
