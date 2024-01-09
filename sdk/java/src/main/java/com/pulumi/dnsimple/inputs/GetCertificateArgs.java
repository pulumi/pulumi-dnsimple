// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;


public final class GetCertificateArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetCertificateArgs Empty = new GetCertificateArgs();

    @Import(name="certificateId", required=true)
    private Output<Integer> certificateId;

    public Output<Integer> certificateId() {
        return this.certificateId;
    }

    @Import(name="domain", required=true)
    private Output<String> domain;

    public Output<String> domain() {
        return this.domain;
    }

    private GetCertificateArgs() {}

    private GetCertificateArgs(GetCertificateArgs $) {
        this.certificateId = $.certificateId;
        this.domain = $.domain;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetCertificateArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetCertificateArgs $;

        public Builder() {
            $ = new GetCertificateArgs();
        }

        public Builder(GetCertificateArgs defaults) {
            $ = new GetCertificateArgs(Objects.requireNonNull(defaults));
        }

        public Builder certificateId(Output<Integer> certificateId) {
            $.certificateId = certificateId;
            return this;
        }

        public Builder certificateId(Integer certificateId) {
            return certificateId(Output.of(certificateId));
        }

        public Builder domain(Output<String> domain) {
            $.domain = domain;
            return this;
        }

        public Builder domain(String domain) {
            return domain(Output.of(domain));
        }

        public GetCertificateArgs build() {
            if ($.certificateId == null) {
                throw new MissingRequiredPropertyException("GetCertificateArgs", "certificateId");
            }
            if ($.domain == null) {
                throw new MissingRequiredPropertyException("GetCertificateArgs", "domain");
            }
            return $;
        }
    }

}
