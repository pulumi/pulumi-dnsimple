// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetCertificateResult {
    /**
     * @return A list of certificates that make up the chain
     * 
     */
    private List<String> certificateChains;
    private String certificateId;
    private String domain;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    /**
     * @return The corresponding Private Key for the SSL Certificate
     * 
     */
    private String privateKey;
    /**
     * @return The Root Certificate of the issuing CA
     * 
     */
    private String rootCertificate;
    /**
     * @return The SSL Certificate
     * 
     */
    private String serverCertificate;

    private GetCertificateResult() {}
    /**
     * @return A list of certificates that make up the chain
     * 
     */
    public List<String> certificateChains() {
        return this.certificateChains;
    }
    public String certificateId() {
        return this.certificateId;
    }
    public String domain() {
        return this.domain;
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return The corresponding Private Key for the SSL Certificate
     * 
     */
    public String privateKey() {
        return this.privateKey;
    }
    /**
     * @return The Root Certificate of the issuing CA
     * 
     */
    public String rootCertificate() {
        return this.rootCertificate;
    }
    /**
     * @return The SSL Certificate
     * 
     */
    public String serverCertificate() {
        return this.serverCertificate;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetCertificateResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<String> certificateChains;
        private String certificateId;
        private String domain;
        private String id;
        private String privateKey;
        private String rootCertificate;
        private String serverCertificate;
        public Builder() {}
        public Builder(GetCertificateResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.certificateChains = defaults.certificateChains;
    	      this.certificateId = defaults.certificateId;
    	      this.domain = defaults.domain;
    	      this.id = defaults.id;
    	      this.privateKey = defaults.privateKey;
    	      this.rootCertificate = defaults.rootCertificate;
    	      this.serverCertificate = defaults.serverCertificate;
        }

        @CustomType.Setter
        public Builder certificateChains(List<String> certificateChains) {
            if (certificateChains == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "certificateChains");
            }
            this.certificateChains = certificateChains;
            return this;
        }
        public Builder certificateChains(String... certificateChains) {
            return certificateChains(List.of(certificateChains));
        }
        @CustomType.Setter
        public Builder certificateId(String certificateId) {
            if (certificateId == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "certificateId");
            }
            this.certificateId = certificateId;
            return this;
        }
        @CustomType.Setter
        public Builder domain(String domain) {
            if (domain == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "domain");
            }
            this.domain = domain;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder privateKey(String privateKey) {
            if (privateKey == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "privateKey");
            }
            this.privateKey = privateKey;
            return this;
        }
        @CustomType.Setter
        public Builder rootCertificate(String rootCertificate) {
            if (rootCertificate == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "rootCertificate");
            }
            this.rootCertificate = rootCertificate;
            return this;
        }
        @CustomType.Setter
        public Builder serverCertificate(String serverCertificate) {
            if (serverCertificate == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "serverCertificate");
            }
            this.serverCertificate = serverCertificate;
            return this;
        }
        public GetCertificateResult build() {
            final var _resultValue = new GetCertificateResult();
            _resultValue.certificateChains = certificateChains;
            _resultValue.certificateId = certificateId;
            _resultValue.domain = domain;
            _resultValue.id = id;
            _resultValue.privateKey = privateKey;
            _resultValue.rootCertificate = rootCertificate;
            _resultValue.serverCertificate = serverCertificate;
            return _resultValue;
        }
    }
}
