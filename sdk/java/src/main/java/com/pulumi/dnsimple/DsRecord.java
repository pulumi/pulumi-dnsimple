// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.dnsimple.DsRecordArgs;
import com.pulumi.dnsimple.Utilities;
import com.pulumi.dnsimple.inputs.DsRecordState;
import java.lang.String;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Provides a DNSimple domain delegation signer record resource.
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
 * import com.pulumi.dnsimple.DsRecord;
 * import com.pulumi.dnsimple.DsRecordArgs;
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
 *         var foobar = new DsRecord("foobar", DsRecordArgs.builder()
 *             .domain(dnsimple.domain())
 *             .algorithm("8")
 *             .digest("6CEEA0117A02480216EBF745A7B690F938860074E4AD11AF2AC573007205682B")
 *             .digestType("2")
 *             .keyTag("12345")
 *             .build());
 * 
 *     }
 * }
 * }
 * </pre>
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 * ## Import
 * 
 * DNSimple DS record resources can be imported using their domain ID and numeric record ID.
 * 
 * bash
 * 
 * ```sh
 * $ pulumi import dnsimple:index/dsRecord:DsRecord resource_name example.com_5678
 * ```
 * 
 * The record ID can be found within [DNSimple DNSSEC API](https://developer.dnsimple.com/v2/domains/dnssec/#listDomainDelegationSignerRecords). Check out [Authentication](https://developer.dnsimple.com/v2/#authentication) in API Overview for available options.
 * 
 * bash
 * 
 * curl -u &#39;EMAIL:PASSWORD&#39; https://api.dnsimple.com/v2/1010/domains/example.com/ds_records | jq
 * 
 * {
 * 
 *   &#34;data&#34;: [
 * 
 *     {
 *     
 *       &#34;id&#34;: 24,
 *     
 *       &#34;domain_id&#34;: 1010,
 *     
 *       &#34;algorithm&#34;: &#34;8&#34;,
 *     
 *       &#34;digest&#34;: &#34;C1F6E04A5A61FBF65BF9DC8294C363CF11C89E802D926BDAB79C55D27BEFA94F&#34;,
 *     
 *       &#34;digest_type&#34;: &#34;2&#34;,
 *     
 *       &#34;keytag&#34;: &#34;44620&#34;,
 *     
 *       &#34;public_key&#34;: null,
 *     
 *       &#34;created_at&#34;: &#34;2017-03-03T13:49:58Z&#34;,
 *     
 *       &#34;updated_at&#34;: &#34;2017-03-03T13:49:58Z&#34;
 *     
 *     }
 * 
 *   ],
 * 
 *   &#34;pagination&#34;: {
 * 
 *     &#34;current_page&#34;: 1,
 *     
 *     &#34;per_page&#34;: 30,
 *     
 *     &#34;total_entries&#34;: 1,
 *     
 *     &#34;total_pages&#34;: 1
 * 
 *   }
 * 
 * }
 * 
 */
@ResourceType(type="dnsimple:index/dsRecord:DsRecord")
public class DsRecord extends com.pulumi.resources.CustomResource {
    /**
     * DNSSEC algorithm number as a string.
     * 
     */
    @Export(name="algorithm", refs={String.class}, tree="[0]")
    private Output<String> algorithm;

    /**
     * @return DNSSEC algorithm number as a string.
     * 
     */
    public Output<String> algorithm() {
        return this.algorithm;
    }
    /**
     * The time the DS record was created at.
     * 
     */
    @Export(name="createdAt", refs={String.class}, tree="[0]")
    private Output<String> createdAt;

    /**
     * @return The time the DS record was created at.
     * 
     */
    public Output<String> createdAt() {
        return this.createdAt;
    }
    /**
     * The hexidecimal representation of the digest of the corresponding DNSKEY record.
     * 
     */
    @Export(name="digest", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> digest;

    /**
     * @return The hexidecimal representation of the digest of the corresponding DNSKEY record.
     * 
     */
    public Output<Optional<String>> digest() {
        return Codegen.optional(this.digest);
    }
    /**
     * DNSSEC digest type number as a string.
     * 
     */
    @Export(name="digestType", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> digestType;

    /**
     * @return DNSSEC digest type number as a string.
     * 
     */
    public Output<Optional<String>> digestType() {
        return Codegen.optional(this.digestType);
    }
    /**
     * The domain name or numeric ID to create the delegation signer record for.
     * 
     */
    @Export(name="domain", refs={String.class}, tree="[0]")
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
    @Export(name="keytag", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> keytag;

    /**
     * @return A keytag that references the corresponding DNSKEY record.
     * 
     */
    public Output<Optional<String>> keytag() {
        return Codegen.optional(this.keytag);
    }
    /**
     * A public key that references the corresponding DNSKEY record.
     * 
     * # Attributes Reference
     * 
     */
    @Export(name="publicKey", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> publicKey;

    /**
     * @return A public key that references the corresponding DNSKEY record.
     * 
     * # Attributes Reference
     * 
     */
    public Output<Optional<String>> publicKey() {
        return Codegen.optional(this.publicKey);
    }
    /**
     * The time the DS record was last updated at.
     * 
     */
    @Export(name="updatedAt", refs={String.class}, tree="[0]")
    private Output<String> updatedAt;

    /**
     * @return The time the DS record was last updated at.
     * 
     */
    public Output<String> updatedAt() {
        return this.updatedAt;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public DsRecord(java.lang.String name) {
        this(name, DsRecordArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public DsRecord(java.lang.String name, DsRecordArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public DsRecord(java.lang.String name, DsRecordArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("dnsimple:index/dsRecord:DsRecord", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private DsRecord(java.lang.String name, Output<java.lang.String> id, @Nullable DsRecordState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("dnsimple:index/dsRecord:DsRecord", name, state, makeResourceOptions(options, id), false);
    }

    private static DsRecordArgs makeArgs(DsRecordArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? DsRecordArgs.Empty : args;
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<java.lang.String> id) {
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
    public static DsRecord get(java.lang.String name, Output<java.lang.String> id, @Nullable DsRecordState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new DsRecord(name, id, state, options);
    }
}
