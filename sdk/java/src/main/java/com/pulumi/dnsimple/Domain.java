// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.dnsimple.DomainArgs;
import com.pulumi.dnsimple.Utilities;
import com.pulumi.dnsimple.inputs.DomainState;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import javax.annotation.Nullable;

/**
 * Provides a DNSimple domain resource.
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
 * import com.pulumi.dnsimple.Domain;
 * import com.pulumi.dnsimple.DomainArgs;
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
 *         // Create a domain
 *         var foobar = new Domain("foobar", DomainArgs.builder()
 *             .name(dnsimple.domain())
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
 * DNSimple domains can be imported using their numeric record ID.
 * 
 * bash
 * 
 * ```sh
 * $ pulumi import dnsimple:index/domain:Domain resource_name 5678
 * ```
 * 
 * The record ID can be found within [DNSimple Domains API](https://developer.dnsimple.com/v2/domains/#listDomains). Check out [Authentication](https://developer.dnsimple.com/v2/#authentication) in API Overview for available options.
 * 
 * bash
 * 
 * curl -u &#39;EMAIL:PASSWORD&#39; https://api.dnsimple.com/v2/1234/domains?name_like=example.com | jq
 * 
 * {
 * 
 *   &#34;data&#34;: [
 * 
 *     {
 *     
 *       &#34;id&#34;: 5678,
 *     
 *       &#34;account_id&#34;: 1234,
 *     
 *       &#34;registrant_id&#34;: null,
 *     
 *       &#34;name&#34;: &#34;example.com&#34;,
 *     
 *       &#34;unicode_name&#34;: &#34;example.com&#34;,
 *     
 *       &#34;state&#34;: &#34;hosted&#34;,
 *     
 *       &#34;auto_renew&#34;: false,
 *     
 *       &#34;private_whois&#34;: false,
 *     
 *       &#34;expires_on&#34;: null,
 *     
 *       &#34;expires_at&#34;: null,
 *     
 *       &#34;created_at&#34;: &#34;2021-10-01T00:00:00Z&#34;,
 *     
 *       &#34;updated_at&#34;: &#34;2021-10-01T00:00:00Z&#34;
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
@ResourceType(type="dnsimple:index/domain:Domain")
public class Domain extends com.pulumi.resources.CustomResource {
    /**
     * The account ID for the domain.
     * 
     */
    @Export(name="accountId", refs={Integer.class}, tree="[0]")
    private Output<Integer> accountId;

    /**
     * @return The account ID for the domain.
     * 
     */
    public Output<Integer> accountId() {
        return this.accountId;
    }
    /**
     * Whether the domain is set to auto-renew.
     * 
     */
    @Export(name="autoRenew", refs={Boolean.class}, tree="[0]")
    private Output<Boolean> autoRenew;

    /**
     * @return Whether the domain is set to auto-renew.
     * 
     */
    public Output<Boolean> autoRenew() {
        return this.autoRenew;
    }
    /**
     * The domain name to be created
     * 
     * # Attributes Reference
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return The domain name to be created
     * 
     * # Attributes Reference
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * Whether the domain has WhoIs privacy enabled.
     * 
     */
    @Export(name="privateWhois", refs={Boolean.class}, tree="[0]")
    private Output<Boolean> privateWhois;

    /**
     * @return Whether the domain has WhoIs privacy enabled.
     * 
     */
    public Output<Boolean> privateWhois() {
        return this.privateWhois;
    }
    /**
     * The ID of the registrant (contact) for the domain.
     * 
     */
    @Export(name="registrantId", refs={Integer.class}, tree="[0]")
    private Output<Integer> registrantId;

    /**
     * @return The ID of the registrant (contact) for the domain.
     * 
     */
    public Output<Integer> registrantId() {
        return this.registrantId;
    }
    /**
     * The state of the domain.
     * 
     */
    @Export(name="state", refs={String.class}, tree="[0]")
    private Output<String> state;

    /**
     * @return The state of the domain.
     * 
     */
    public Output<String> state() {
        return this.state;
    }
    /**
     * The domain name in Unicode format.
     * 
     */
    @Export(name="unicodeName", refs={String.class}, tree="[0]")
    private Output<String> unicodeName;

    /**
     * @return The domain name in Unicode format.
     * 
     */
    public Output<String> unicodeName() {
        return this.unicodeName;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Domain(java.lang.String name) {
        this(name, DomainArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Domain(java.lang.String name, DomainArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Domain(java.lang.String name, DomainArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("dnsimple:index/domain:Domain", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private Domain(java.lang.String name, Output<java.lang.String> id, @Nullable DomainState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("dnsimple:index/domain:Domain", name, state, makeResourceOptions(options, id), false);
    }

    private static DomainArgs makeArgs(DomainArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? DomainArgs.Empty : args;
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
    public static Domain get(java.lang.String name, Output<java.lang.String> id, @Nullable DomainState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Domain(name, id, state, options);
    }
}
