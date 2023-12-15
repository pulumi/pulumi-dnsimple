// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class RegisteredDomainRegistrantChange {
    private @Nullable Integer accountId;
    /**
     * @return The ID of the contact to be used for the domain registration. The contact ID can be changed after the domain has been registered. The change will result in a new registrant change this may result in a [60-day lock](https://support.dnsimple.com/articles/icann-60-day-lock-registrant-change/).
     * 
     */
    private @Nullable Integer contactId;
    private @Nullable String domainId;
    /**
     * @return A map of extended attributes to be set for the domain registration. To see if there are any required extended attributes for any TLD use our [Lists the TLD Extended Attributes API](https://developer.dnsimple.com/v2/tlds/#getTldExtendedAttributes). The values provided in the `extended_attributes` will also be sent when a registrant change is initiated as part of changing the `contact_id`.
     * 
     */
    private @Nullable Map<String,String> extendedAttributes;
    /**
     * @return The ID of this resource.
     * 
     */
    private @Nullable Integer id;
    private @Nullable String irtLockLiftedBy;
    private @Nullable Boolean registryOwnerChange;
    /**
     * @return The state of the domain.
     * 
     */
    private @Nullable String state;

    private RegisteredDomainRegistrantChange() {}
    public Optional<Integer> accountId() {
        return Optional.ofNullable(this.accountId);
    }
    /**
     * @return The ID of the contact to be used for the domain registration. The contact ID can be changed after the domain has been registered. The change will result in a new registrant change this may result in a [60-day lock](https://support.dnsimple.com/articles/icann-60-day-lock-registrant-change/).
     * 
     */
    public Optional<Integer> contactId() {
        return Optional.ofNullable(this.contactId);
    }
    public Optional<String> domainId() {
        return Optional.ofNullable(this.domainId);
    }
    /**
     * @return A map of extended attributes to be set for the domain registration. To see if there are any required extended attributes for any TLD use our [Lists the TLD Extended Attributes API](https://developer.dnsimple.com/v2/tlds/#getTldExtendedAttributes). The values provided in the `extended_attributes` will also be sent when a registrant change is initiated as part of changing the `contact_id`.
     * 
     */
    public Map<String,String> extendedAttributes() {
        return this.extendedAttributes == null ? Map.of() : this.extendedAttributes;
    }
    /**
     * @return The ID of this resource.
     * 
     */
    public Optional<Integer> id() {
        return Optional.ofNullable(this.id);
    }
    public Optional<String> irtLockLiftedBy() {
        return Optional.ofNullable(this.irtLockLiftedBy);
    }
    public Optional<Boolean> registryOwnerChange() {
        return Optional.ofNullable(this.registryOwnerChange);
    }
    /**
     * @return The state of the domain.
     * 
     */
    public Optional<String> state() {
        return Optional.ofNullable(this.state);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(RegisteredDomainRegistrantChange defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable Integer accountId;
        private @Nullable Integer contactId;
        private @Nullable String domainId;
        private @Nullable Map<String,String> extendedAttributes;
        private @Nullable Integer id;
        private @Nullable String irtLockLiftedBy;
        private @Nullable Boolean registryOwnerChange;
        private @Nullable String state;
        public Builder() {}
        public Builder(RegisteredDomainRegistrantChange defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.accountId = defaults.accountId;
    	      this.contactId = defaults.contactId;
    	      this.domainId = defaults.domainId;
    	      this.extendedAttributes = defaults.extendedAttributes;
    	      this.id = defaults.id;
    	      this.irtLockLiftedBy = defaults.irtLockLiftedBy;
    	      this.registryOwnerChange = defaults.registryOwnerChange;
    	      this.state = defaults.state;
        }

        @CustomType.Setter
        public Builder accountId(@Nullable Integer accountId) {
            this.accountId = accountId;
            return this;
        }
        @CustomType.Setter
        public Builder contactId(@Nullable Integer contactId) {
            this.contactId = contactId;
            return this;
        }
        @CustomType.Setter
        public Builder domainId(@Nullable String domainId) {
            this.domainId = domainId;
            return this;
        }
        @CustomType.Setter
        public Builder extendedAttributes(@Nullable Map<String,String> extendedAttributes) {
            this.extendedAttributes = extendedAttributes;
            return this;
        }
        @CustomType.Setter
        public Builder id(@Nullable Integer id) {
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder irtLockLiftedBy(@Nullable String irtLockLiftedBy) {
            this.irtLockLiftedBy = irtLockLiftedBy;
            return this;
        }
        @CustomType.Setter
        public Builder registryOwnerChange(@Nullable Boolean registryOwnerChange) {
            this.registryOwnerChange = registryOwnerChange;
            return this;
        }
        @CustomType.Setter
        public Builder state(@Nullable String state) {
            this.state = state;
            return this;
        }
        public RegisteredDomainRegistrantChange build() {
            final var _resultValue = new RegisteredDomainRegistrantChange();
            _resultValue.accountId = accountId;
            _resultValue.contactId = contactId;
            _resultValue.domainId = domainId;
            _resultValue.extendedAttributes = extendedAttributes;
            _resultValue.id = id;
            _resultValue.irtLockLiftedBy = irtLockLiftedBy;
            _resultValue.registryOwnerChange = registryOwnerChange;
            _resultValue.state = state;
            return _resultValue;
        }
    }
}
