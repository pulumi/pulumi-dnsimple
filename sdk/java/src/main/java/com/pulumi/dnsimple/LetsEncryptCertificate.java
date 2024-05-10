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

/**
 * Provides a DNSimple Let&#39;s Encrypt certificate resource.
 * 
 * ## Example Usage
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * <pre>
 * {@code
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.dnsimple.LetsEncryptCertificate;
 * import com.pulumi.dnsimple.LetsEncryptCertificateArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         var foobar = new LetsEncryptCertificate("foobar", LetsEncryptCertificateArgs.builder()        
 *             .domainId(dnsimple.domainId())
 *             .autoRenew(false)
 *             .name("www")
 *             .build());
 * 
 *     }
 * }
 * }
 * </pre>
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 */
@ResourceType(type="dnsimple:index/letsEncryptCertificate:LetsEncryptCertificate")
public class LetsEncryptCertificate extends com.pulumi.resources.CustomResource {
    /**
     * The identifying certification authority (CA)
     * 
     */
    @Export(name="authorityIdentifier", refs={String.class}, tree="[0]")
    private Output<String> authorityIdentifier;

    /**
     * @return The identifying certification authority (CA)
     * 
     */
    public Output<String> authorityIdentifier() {
        return this.authorityIdentifier;
    }
    /**
     * Set to true if the certificate will auto-renew
     * 
     */
    @Export(name="autoRenew", refs={Boolean.class}, tree="[0]")
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
    @Export(name="contactId", refs={Integer.class}, tree="[0]")
    private Output</* @Nullable */ Integer> contactId;

    /**
     * @return The contact id for the certificate
     * 
     */
    public Output<Optional<Integer>> contactId() {
        return Codegen.optional(this.contactId);
    }
    @Export(name="createdAt", refs={String.class}, tree="[0]")
    private Output<String> createdAt;

    public Output<String> createdAt() {
        return this.createdAt;
    }
    /**
     * The certificate signing request
     * 
     */
    @Export(name="csr", refs={String.class}, tree="[0]")
    private Output<String> csr;

    /**
     * @return The certificate signing request
     * 
     */
    public Output<String> csr() {
        return this.csr;
    }
    /**
     * The domain to be issued the certificate for
     * 
     */
    @Export(name="domainId", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> domainId;

    /**
     * @return The domain to be issued the certificate for
     * 
     */
    public Output<Optional<String>> domainId() {
        return Codegen.optional(this.domainId);
    }
    @Export(name="expiresOn", refs={String.class}, tree="[0]")
    private Output<String> expiresOn;

    public Output<String> expiresOn() {
        return this.expiresOn;
    }
    /**
     * The certificate name
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return The certificate name
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * The state of the certificate
     * 
     */
    @Export(name="state", refs={String.class}, tree="[0]")
    private Output<String> state;

    /**
     * @return The state of the certificate
     * 
     */
    public Output<String> state() {
        return this.state;
    }
    @Export(name="updatedAt", refs={String.class}, tree="[0]")
    private Output<String> updatedAt;

    public Output<String> updatedAt() {
        return this.updatedAt;
    }
    /**
     * The years the certificate will last
     * 
     */
    @Export(name="years", refs={Integer.class}, tree="[0]")
    private Output<Integer> years;

    /**
     * @return The years the certificate will last
     * 
     */
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
