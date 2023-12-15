// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class LetsEncryptCertificateArgs extends com.pulumi.resources.ResourceArgs {

    public static final LetsEncryptCertificateArgs Empty = new LetsEncryptCertificateArgs();

    /**
     * The certificate alternate names
     * 
     */
    @Import(name="alternateNames")
    private @Nullable Output<List<String>> alternateNames;

    /**
     * @return The certificate alternate names
     * 
     */
    public Optional<Output<List<String>>> alternateNames() {
        return Optional.ofNullable(this.alternateNames);
    }

    /**
     * True if the certificate should auto-renew
     * 
     */
    @Import(name="autoRenew", required=true)
    private Output<Boolean> autoRenew;

    /**
     * @return True if the certificate should auto-renew
     * 
     */
    public Output<Boolean> autoRenew() {
        return this.autoRenew;
    }

    /**
     * The domain to be issued the certificate for
     * 
     */
    @Import(name="domainId", required=true)
    private Output<String> domainId;

    /**
     * @return The domain to be issued the certificate for
     * 
     */
    public Output<String> domainId() {
        return this.domainId;
    }

    /**
     * The certificate name
     * 
     */
    @Import(name="name", required=true)
    private Output<String> name;

    /**
     * @return The certificate name
     * 
     */
    public Output<String> name() {
        return this.name;
    }

    /**
     * The signature algorithm to use for the certificate
     * 
     */
    @Import(name="signatureAlgorithm")
    private @Nullable Output<String> signatureAlgorithm;

    /**
     * @return The signature algorithm to use for the certificate
     * 
     */
    public Optional<Output<String>> signatureAlgorithm() {
        return Optional.ofNullable(this.signatureAlgorithm);
    }

    private LetsEncryptCertificateArgs() {}

    private LetsEncryptCertificateArgs(LetsEncryptCertificateArgs $) {
        this.alternateNames = $.alternateNames;
        this.autoRenew = $.autoRenew;
        this.domainId = $.domainId;
        this.name = $.name;
        this.signatureAlgorithm = $.signatureAlgorithm;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(LetsEncryptCertificateArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private LetsEncryptCertificateArgs $;

        public Builder() {
            $ = new LetsEncryptCertificateArgs();
        }

        public Builder(LetsEncryptCertificateArgs defaults) {
            $ = new LetsEncryptCertificateArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param alternateNames The certificate alternate names
         * 
         * @return builder
         * 
         */
        public Builder alternateNames(@Nullable Output<List<String>> alternateNames) {
            $.alternateNames = alternateNames;
            return this;
        }

        /**
         * @param alternateNames The certificate alternate names
         * 
         * @return builder
         * 
         */
        public Builder alternateNames(List<String> alternateNames) {
            return alternateNames(Output.of(alternateNames));
        }

        /**
         * @param alternateNames The certificate alternate names
         * 
         * @return builder
         * 
         */
        public Builder alternateNames(String... alternateNames) {
            return alternateNames(List.of(alternateNames));
        }

        /**
         * @param autoRenew True if the certificate should auto-renew
         * 
         * @return builder
         * 
         */
        public Builder autoRenew(Output<Boolean> autoRenew) {
            $.autoRenew = autoRenew;
            return this;
        }

        /**
         * @param autoRenew True if the certificate should auto-renew
         * 
         * @return builder
         * 
         */
        public Builder autoRenew(Boolean autoRenew) {
            return autoRenew(Output.of(autoRenew));
        }

        /**
         * @param domainId The domain to be issued the certificate for
         * 
         * @return builder
         * 
         */
        public Builder domainId(Output<String> domainId) {
            $.domainId = domainId;
            return this;
        }

        /**
         * @param domainId The domain to be issued the certificate for
         * 
         * @return builder
         * 
         */
        public Builder domainId(String domainId) {
            return domainId(Output.of(domainId));
        }

        /**
         * @param name The certificate name
         * 
         * @return builder
         * 
         */
        public Builder name(Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The certificate name
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param signatureAlgorithm The signature algorithm to use for the certificate
         * 
         * @return builder
         * 
         */
        public Builder signatureAlgorithm(@Nullable Output<String> signatureAlgorithm) {
            $.signatureAlgorithm = signatureAlgorithm;
            return this;
        }

        /**
         * @param signatureAlgorithm The signature algorithm to use for the certificate
         * 
         * @return builder
         * 
         */
        public Builder signatureAlgorithm(String signatureAlgorithm) {
            return signatureAlgorithm(Output.of(signatureAlgorithm));
        }

        public LetsEncryptCertificateArgs build() {
            $.autoRenew = Objects.requireNonNull($.autoRenew, "expected parameter 'autoRenew' to be non-null");
            $.domainId = Objects.requireNonNull($.domainId, "expected parameter 'domainId' to be non-null");
            $.name = Objects.requireNonNull($.name, "expected parameter 'name' to be non-null");
            return $;
        }
    }

}
