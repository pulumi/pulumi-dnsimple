// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple.inputs;

import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;


public final class GetCertificatePlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetCertificatePlainArgs Empty = new GetCertificatePlainArgs();

    @Import(name="certificateId", required=true)
    private Integer certificateId;

    public Integer certificateId() {
        return this.certificateId;
    }

    @Import(name="domain", required=true)
    private String domain;

    public String domain() {
        return this.domain;
    }

    private GetCertificatePlainArgs() {}

    private GetCertificatePlainArgs(GetCertificatePlainArgs $) {
        this.certificateId = $.certificateId;
        this.domain = $.domain;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetCertificatePlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetCertificatePlainArgs $;

        public Builder() {
            $ = new GetCertificatePlainArgs();
        }

        public Builder(GetCertificatePlainArgs defaults) {
            $ = new GetCertificatePlainArgs(Objects.requireNonNull(defaults));
        }

        public Builder certificateId(Integer certificateId) {
            $.certificateId = certificateId;
            return this;
        }

        public Builder domain(String domain) {
            $.domain = domain;
            return this;
        }

        public GetCertificatePlainArgs build() {
            if ($.certificateId == null) {
                throw new MissingRequiredPropertyException("GetCertificatePlainArgs", "certificateId");
            }
            if ($.domain == null) {
                throw new MissingRequiredPropertyException("GetCertificatePlainArgs", "domain");
            }
            return $;
        }
    }

}
