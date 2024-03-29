// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class LetsEncryptCertificateArgs extends com.pulumi.resources.ResourceArgs {

    public static final LetsEncryptCertificateArgs Empty = new LetsEncryptCertificateArgs();

    /**
     * Set to true if the certificate will auto-renew
     * 
     */
    @Import(name="autoRenew", required=true)
    private Output<Boolean> autoRenew;

    /**
     * @return Set to true if the certificate will auto-renew
     * 
     */
    public Output<Boolean> autoRenew() {
        return this.autoRenew;
    }

    /**
     * The contact id for the certificate
     * 
     * @deprecated
     * contact_id is deprecated and has no effect. The attribute will be removed in the next major version.
     * 
     */
    @Deprecated /* contact_id is deprecated and has no effect. The attribute will be removed in the next major version. */
    @Import(name="contactId")
    private @Nullable Output<Integer> contactId;

    /**
     * @return The contact id for the certificate
     * 
     * @deprecated
     * contact_id is deprecated and has no effect. The attribute will be removed in the next major version.
     * 
     */
    @Deprecated /* contact_id is deprecated and has no effect. The attribute will be removed in the next major version. */
    public Optional<Output<Integer>> contactId() {
        return Optional.ofNullable(this.contactId);
    }

    /**
     * The domain to be issued the certificate for
     * 
     */
    @Import(name="domainId")
    private @Nullable Output<String> domainId;

    /**
     * @return The domain to be issued the certificate for
     * 
     */
    public Optional<Output<String>> domainId() {
        return Optional.ofNullable(this.domainId);
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

    private LetsEncryptCertificateArgs() {}

    private LetsEncryptCertificateArgs(LetsEncryptCertificateArgs $) {
        this.autoRenew = $.autoRenew;
        this.contactId = $.contactId;
        this.domainId = $.domainId;
        this.name = $.name;
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
         * @param autoRenew Set to true if the certificate will auto-renew
         * 
         * @return builder
         * 
         */
        public Builder autoRenew(Output<Boolean> autoRenew) {
            $.autoRenew = autoRenew;
            return this;
        }

        /**
         * @param autoRenew Set to true if the certificate will auto-renew
         * 
         * @return builder
         * 
         */
        public Builder autoRenew(Boolean autoRenew) {
            return autoRenew(Output.of(autoRenew));
        }

        /**
         * @param contactId The contact id for the certificate
         * 
         * @return builder
         * 
         * @deprecated
         * contact_id is deprecated and has no effect. The attribute will be removed in the next major version.
         * 
         */
        @Deprecated /* contact_id is deprecated and has no effect. The attribute will be removed in the next major version. */
        public Builder contactId(@Nullable Output<Integer> contactId) {
            $.contactId = contactId;
            return this;
        }

        /**
         * @param contactId The contact id for the certificate
         * 
         * @return builder
         * 
         * @deprecated
         * contact_id is deprecated and has no effect. The attribute will be removed in the next major version.
         * 
         */
        @Deprecated /* contact_id is deprecated and has no effect. The attribute will be removed in the next major version. */
        public Builder contactId(Integer contactId) {
            return contactId(Output.of(contactId));
        }

        /**
         * @param domainId The domain to be issued the certificate for
         * 
         * @return builder
         * 
         */
        public Builder domainId(@Nullable Output<String> domainId) {
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

        public LetsEncryptCertificateArgs build() {
            if ($.autoRenew == null) {
                throw new MissingRequiredPropertyException("LetsEncryptCertificateArgs", "autoRenew");
            }
            if ($.name == null) {
                throw new MissingRequiredPropertyException("LetsEncryptCertificateArgs", "name");
            }
            return $;
        }
    }

}
