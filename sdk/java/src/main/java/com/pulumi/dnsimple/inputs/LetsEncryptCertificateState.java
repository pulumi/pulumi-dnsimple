// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class LetsEncryptCertificateState extends com.pulumi.resources.ResourceArgs {

    public static final LetsEncryptCertificateState Empty = new LetsEncryptCertificateState();

    /**
     * The identifying certification authority (CA)
     * 
     */
    @Import(name="authorityIdentifier")
    private @Nullable Output<String> authorityIdentifier;

    /**
     * @return The identifying certification authority (CA)
     * 
     */
    public Optional<Output<String>> authorityIdentifier() {
        return Optional.ofNullable(this.authorityIdentifier);
    }

    /**
     * Set to true if the certificate will auto-renew
     * 
     */
    @Import(name="autoRenew")
    private @Nullable Output<Boolean> autoRenew;

    /**
     * @return Set to true if the certificate will auto-renew
     * 
     */
    public Optional<Output<Boolean>> autoRenew() {
        return Optional.ofNullable(this.autoRenew);
    }

    /**
     * (Deprecated) The contact id for the certificate
     * 
     * @deprecated
     * contact_id is deprecated and has no effect. The attribute will be removed in the next major version.
     * 
     */
    @Deprecated /* contact_id is deprecated and has no effect. The attribute will be removed in the next major version. */
    @Import(name="contactId")
    private @Nullable Output<Integer> contactId;

    /**
     * @return (Deprecated) The contact id for the certificate
     * 
     * @deprecated
     * contact_id is deprecated and has no effect. The attribute will be removed in the next major version.
     * 
     */
    @Deprecated /* contact_id is deprecated and has no effect. The attribute will be removed in the next major version. */
    public Optional<Output<Integer>> contactId() {
        return Optional.ofNullable(this.contactId);
    }

    @Import(name="createdAt")
    private @Nullable Output<String> createdAt;

    public Optional<Output<String>> createdAt() {
        return Optional.ofNullable(this.createdAt);
    }

    /**
     * The certificate signing request
     * 
     */
    @Import(name="csr")
    private @Nullable Output<String> csr;

    /**
     * @return The certificate signing request
     * 
     */
    public Optional<Output<String>> csr() {
        return Optional.ofNullable(this.csr);
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

    @Import(name="expiresOn")
    private @Nullable Output<String> expiresOn;

    public Optional<Output<String>> expiresOn() {
        return Optional.ofNullable(this.expiresOn);
    }

    /**
     * The certificate name
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The certificate name
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The state of the certificate
     * 
     */
    @Import(name="state")
    private @Nullable Output<String> state;

    /**
     * @return The state of the certificate
     * 
     */
    public Optional<Output<String>> state() {
        return Optional.ofNullable(this.state);
    }

    @Import(name="updatedAt")
    private @Nullable Output<String> updatedAt;

    public Optional<Output<String>> updatedAt() {
        return Optional.ofNullable(this.updatedAt);
    }

    /**
     * The years the certificate will last
     * 
     */
    @Import(name="years")
    private @Nullable Output<Integer> years;

    /**
     * @return The years the certificate will last
     * 
     */
    public Optional<Output<Integer>> years() {
        return Optional.ofNullable(this.years);
    }

    private LetsEncryptCertificateState() {}

    private LetsEncryptCertificateState(LetsEncryptCertificateState $) {
        this.authorityIdentifier = $.authorityIdentifier;
        this.autoRenew = $.autoRenew;
        this.contactId = $.contactId;
        this.createdAt = $.createdAt;
        this.csr = $.csr;
        this.domainId = $.domainId;
        this.expiresOn = $.expiresOn;
        this.name = $.name;
        this.state = $.state;
        this.updatedAt = $.updatedAt;
        this.years = $.years;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(LetsEncryptCertificateState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private LetsEncryptCertificateState $;

        public Builder() {
            $ = new LetsEncryptCertificateState();
        }

        public Builder(LetsEncryptCertificateState defaults) {
            $ = new LetsEncryptCertificateState(Objects.requireNonNull(defaults));
        }

        /**
         * @param authorityIdentifier The identifying certification authority (CA)
         * 
         * @return builder
         * 
         */
        public Builder authorityIdentifier(@Nullable Output<String> authorityIdentifier) {
            $.authorityIdentifier = authorityIdentifier;
            return this;
        }

        /**
         * @param authorityIdentifier The identifying certification authority (CA)
         * 
         * @return builder
         * 
         */
        public Builder authorityIdentifier(String authorityIdentifier) {
            return authorityIdentifier(Output.of(authorityIdentifier));
        }

        /**
         * @param autoRenew Set to true if the certificate will auto-renew
         * 
         * @return builder
         * 
         */
        public Builder autoRenew(@Nullable Output<Boolean> autoRenew) {
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
         * @param contactId (Deprecated) The contact id for the certificate
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
         * @param contactId (Deprecated) The contact id for the certificate
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

        public Builder createdAt(@Nullable Output<String> createdAt) {
            $.createdAt = createdAt;
            return this;
        }

        public Builder createdAt(String createdAt) {
            return createdAt(Output.of(createdAt));
        }

        /**
         * @param csr The certificate signing request
         * 
         * @return builder
         * 
         */
        public Builder csr(@Nullable Output<String> csr) {
            $.csr = csr;
            return this;
        }

        /**
         * @param csr The certificate signing request
         * 
         * @return builder
         * 
         */
        public Builder csr(String csr) {
            return csr(Output.of(csr));
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

        public Builder expiresOn(@Nullable Output<String> expiresOn) {
            $.expiresOn = expiresOn;
            return this;
        }

        public Builder expiresOn(String expiresOn) {
            return expiresOn(Output.of(expiresOn));
        }

        /**
         * @param name The certificate name
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
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
         * @param state The state of the certificate
         * 
         * @return builder
         * 
         */
        public Builder state(@Nullable Output<String> state) {
            $.state = state;
            return this;
        }

        /**
         * @param state The state of the certificate
         * 
         * @return builder
         * 
         */
        public Builder state(String state) {
            return state(Output.of(state));
        }

        public Builder updatedAt(@Nullable Output<String> updatedAt) {
            $.updatedAt = updatedAt;
            return this;
        }

        public Builder updatedAt(String updatedAt) {
            return updatedAt(Output.of(updatedAt));
        }

        /**
         * @param years The years the certificate will last
         * 
         * @return builder
         * 
         */
        public Builder years(@Nullable Output<Integer> years) {
            $.years = years;
            return this;
        }

        /**
         * @param years The years the certificate will last
         * 
         * @return builder
         * 
         */
        public Builder years(Integer years) {
            return years(Output.of(years));
        }

        public LetsEncryptCertificateState build() {
            return $;
        }
    }

}
