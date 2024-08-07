// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class DsRecordArgs extends com.pulumi.resources.ResourceArgs {

    public static final DsRecordArgs Empty = new DsRecordArgs();

    /**
     * DNSSEC algorithm number as a string.
     * 
     */
    @Import(name="algorithm", required=true)
    private Output<String> algorithm;

    /**
     * @return DNSSEC algorithm number as a string.
     * 
     */
    public Output<String> algorithm() {
        return this.algorithm;
    }

    /**
     * The hexidecimal representation of the digest of the corresponding DNSKEY record.
     * 
     */
    @Import(name="digest")
    private @Nullable Output<String> digest;

    /**
     * @return The hexidecimal representation of the digest of the corresponding DNSKEY record.
     * 
     */
    public Optional<Output<String>> digest() {
        return Optional.ofNullable(this.digest);
    }

    /**
     * DNSSEC digest type number as a string.
     * 
     */
    @Import(name="digestType")
    private @Nullable Output<String> digestType;

    /**
     * @return DNSSEC digest type number as a string.
     * 
     */
    public Optional<Output<String>> digestType() {
        return Optional.ofNullable(this.digestType);
    }

    /**
     * The domain name or numeric ID to create the delegation signer record for.
     * 
     */
    @Import(name="domain", required=true)
    private Output<String> domain;

    /**
     * @return The domain name or numeric ID to create the delegation signer record for.
     * 
     */
    public Output<String> domain() {
        return this.domain;
    }

    /**
     * A keytag that references the corresponding DNSKEY record.
     * 
     */
    @Import(name="keytag")
    private @Nullable Output<String> keytag;

    /**
     * @return A keytag that references the corresponding DNSKEY record.
     * 
     */
    public Optional<Output<String>> keytag() {
        return Optional.ofNullable(this.keytag);
    }

    /**
     * A public key that references the corresponding DNSKEY record.
     * 
     * # Attributes Reference
     * 
     */
    @Import(name="publicKey")
    private @Nullable Output<String> publicKey;

    /**
     * @return A public key that references the corresponding DNSKEY record.
     * 
     * # Attributes Reference
     * 
     */
    public Optional<Output<String>> publicKey() {
        return Optional.ofNullable(this.publicKey);
    }

    private DsRecordArgs() {}

    private DsRecordArgs(DsRecordArgs $) {
        this.algorithm = $.algorithm;
        this.digest = $.digest;
        this.digestType = $.digestType;
        this.domain = $.domain;
        this.keytag = $.keytag;
        this.publicKey = $.publicKey;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DsRecordArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DsRecordArgs $;

        public Builder() {
            $ = new DsRecordArgs();
        }

        public Builder(DsRecordArgs defaults) {
            $ = new DsRecordArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param algorithm DNSSEC algorithm number as a string.
         * 
         * @return builder
         * 
         */
        public Builder algorithm(Output<String> algorithm) {
            $.algorithm = algorithm;
            return this;
        }

        /**
         * @param algorithm DNSSEC algorithm number as a string.
         * 
         * @return builder
         * 
         */
        public Builder algorithm(String algorithm) {
            return algorithm(Output.of(algorithm));
        }

        /**
         * @param digest The hexidecimal representation of the digest of the corresponding DNSKEY record.
         * 
         * @return builder
         * 
         */
        public Builder digest(@Nullable Output<String> digest) {
            $.digest = digest;
            return this;
        }

        /**
         * @param digest The hexidecimal representation of the digest of the corresponding DNSKEY record.
         * 
         * @return builder
         * 
         */
        public Builder digest(String digest) {
            return digest(Output.of(digest));
        }

        /**
         * @param digestType DNSSEC digest type number as a string.
         * 
         * @return builder
         * 
         */
        public Builder digestType(@Nullable Output<String> digestType) {
            $.digestType = digestType;
            return this;
        }

        /**
         * @param digestType DNSSEC digest type number as a string.
         * 
         * @return builder
         * 
         */
        public Builder digestType(String digestType) {
            return digestType(Output.of(digestType));
        }

        /**
         * @param domain The domain name or numeric ID to create the delegation signer record for.
         * 
         * @return builder
         * 
         */
        public Builder domain(Output<String> domain) {
            $.domain = domain;
            return this;
        }

        /**
         * @param domain The domain name or numeric ID to create the delegation signer record for.
         * 
         * @return builder
         * 
         */
        public Builder domain(String domain) {
            return domain(Output.of(domain));
        }

        /**
         * @param keytag A keytag that references the corresponding DNSKEY record.
         * 
         * @return builder
         * 
         */
        public Builder keytag(@Nullable Output<String> keytag) {
            $.keytag = keytag;
            return this;
        }

        /**
         * @param keytag A keytag that references the corresponding DNSKEY record.
         * 
         * @return builder
         * 
         */
        public Builder keytag(String keytag) {
            return keytag(Output.of(keytag));
        }

        /**
         * @param publicKey A public key that references the corresponding DNSKEY record.
         * 
         * # Attributes Reference
         * 
         * @return builder
         * 
         */
        public Builder publicKey(@Nullable Output<String> publicKey) {
            $.publicKey = publicKey;
            return this;
        }

        /**
         * @param publicKey A public key that references the corresponding DNSKEY record.
         * 
         * # Attributes Reference
         * 
         * @return builder
         * 
         */
        public Builder publicKey(String publicKey) {
            return publicKey(Output.of(publicKey));
        }

        public DsRecordArgs build() {
            if ($.algorithm == null) {
                throw new MissingRequiredPropertyException("DsRecordArgs", "algorithm");
            }
            if ($.domain == null) {
                throw new MissingRequiredPropertyException("DsRecordArgs", "domain");
            }
            return $;
        }
    }

}
