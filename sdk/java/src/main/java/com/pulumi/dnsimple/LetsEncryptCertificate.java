// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.dnsimple.LetsEncryptCertificateArgs;
import com.pulumi.dnsimple.Utilities;
import com.pulumi.dnsimple.inputs.LetsEncryptCertificateState;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Optional;
import javax.annotation.Nullable;

@ResourceType(type="dnsimple:index/letsEncryptCertificate:LetsEncryptCertificate")
public class LetsEncryptCertificate extends com.pulumi.resources.CustomResource {
    @Export(name="authorityIdentifier", type=String.class, parameters={})
    private Output<String> authorityIdentifier;

    public Output<String> authorityIdentifier() {
        return this.authorityIdentifier;
    }
    @Export(name="autoRenew", type=Boolean.class, parameters={})
    private Output<Boolean> autoRenew;

    public Output<Boolean> autoRenew() {
        return this.autoRenew;
    }
    /**
     * @deprecated
     * contact_id is deprecated and has no effect. The attribute will be removed in the next major version.
     * 
     */
    @Deprecated /* contact_id is deprecated and has no effect. The attribute will be removed in the next major version. */
    @Export(name="contactId", type=Integer.class, parameters={})
    private Output</* @Nullable */ Integer> contactId;

    public Output<Optional<Integer>> contactId() {
        return Codegen.optional(this.contactId);
    }
    @Export(name="createdAt", type=String.class, parameters={})
    private Output<String> createdAt;

    public Output<String> createdAt() {
        return this.createdAt;
    }
    @Export(name="csr", type=String.class, parameters={})
    private Output<String> csr;

    public Output<String> csr() {
        return this.csr;
    }
    @Export(name="domainId", type=String.class, parameters={})
    private Output</* @Nullable */ String> domainId;

    public Output<Optional<String>> domainId() {
        return Codegen.optional(this.domainId);
    }
    @Export(name="expiresOn", type=String.class, parameters={})
    private Output<String> expiresOn;

    public Output<String> expiresOn() {
        return this.expiresOn;
    }
    @Export(name="name", type=String.class, parameters={})
    private Output<String> name;

    public Output<String> name() {
        return this.name;
    }
    @Export(name="state", type=String.class, parameters={})
    private Output<String> state;

    public Output<String> state() {
        return this.state;
    }
    @Export(name="updatedAt", type=String.class, parameters={})
    private Output<String> updatedAt;

    public Output<String> updatedAt() {
        return this.updatedAt;
    }
    @Export(name="years", type=Integer.class, parameters={})
    private Output<Integer> years;

    public Output<Integer> years() {
        return this.years;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public LetsEncryptCertificate(String name) {
        this(name, LetsEncryptCertificateArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public LetsEncryptCertificate(String name, LetsEncryptCertificateArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public LetsEncryptCertificate(String name, LetsEncryptCertificateArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("dnsimple:index/letsEncryptCertificate:LetsEncryptCertificate", name, args == null ? LetsEncryptCertificateArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private LetsEncryptCertificate(String name, Output<String> id, @Nullable LetsEncryptCertificateState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("dnsimple:index/letsEncryptCertificate:LetsEncryptCertificate", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static LetsEncryptCertificate get(String name, Output<String> id, @Nullable LetsEncryptCertificateState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new LetsEncryptCertificate(name, id, state, options);
    }
}