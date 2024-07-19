// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.dnsimple.ContactArgs;
import com.pulumi.dnsimple.Utilities;
import com.pulumi.dnsimple.inputs.ContactState;
import java.lang.Integer;
import java.lang.String;
import javax.annotation.Nullable;

/**
 * Provides a DNSimple contact resource.
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
 * import com.pulumi.dnsimple.Contact;
 * import com.pulumi.dnsimple.ContactArgs;
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
 *         // Create a contact
 *         var me = new Contact("me", ContactArgs.builder()
 *             .label("Apple Appleseed")
 *             .firstName("Apple")
 *             .lastName("Appleseed")
 *             .organizationName("Contoso")
 *             .jobTitle("Manager")
 *             .address1("Level 1, 2 Main St")
 *             .address2("Marsfield")
 *             .city("San Francisco")
 *             .stateProvince("California")
 *             .postalCode("90210")
 *             .country("US")
 *             .phone("+1401239523")
 *             .fax("+1849491024")
 *             .email("apple{@literal @}contoso.com")
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
 * DNSimple contacts can be imported using their numeric ID.
 * 
 * bash
 * 
 * ```sh
 * $ pulumi import dnsimple:index/contact:Contact resource_name 5678
 * ```
 * 
 * The ID can be found within [DNSimple Contacts API](https://developer.dnsimple.com/v2/contacts/#listContacts). Check out [Authentication](https://developer.dnsimple.com/v2/#authentication) in API Overview for available options.
 * 
 * bash
 * 
 * curl -u &#39;EMAIL:PASSWORD&#39; https://api.dnsimple.com/v2/1234/contacts?label_like=example.com | jq
 * 
 * {
 * 
 *   &#34;data&#34;: [
 * 
 *     {
 *     
 *       &#34;id&#34;: 1,
 *     
 *       &#34;account_id&#34;: 1010,
 *     
 *       &#34;label&#34;: &#34;Default&#34;,
 *     
 *       &#34;first_name&#34;: &#34;First&#34;,
 *     
 *       &#34;last_name&#34;: &#34;User&#34;,
 *     
 *       &#34;job_title&#34;: &#34;CEO&#34;,
 *     
 *       &#34;organization_name&#34;: &#34;Awesome Company&#34;,
 *     
 *       &#34;email&#34;: &#34;first{@literal @}example.com&#34;,
 *     
 *       &#34;phone&#34;: &#34;+18001234567&#34;,
 *     
 *       &#34;fax&#34;: &#34;+18011234567&#34;,
 *     
 *       &#34;address1&#34;: &#34;Italian Street, 10&#34;,
 *     
 *       &#34;address2&#34;: &#34;&#34;,
 *     
 *       &#34;city&#34;: &#34;Roma&#34;,
 *     
 *       &#34;state_province&#34;: &#34;RM&#34;,
 *     
 *       &#34;postal_code&#34;: &#34;00100&#34;,
 *     
 *       &#34;country&#34;: &#34;IT&#34;,
 *     
 *       &#34;created_at&#34;: &#34;2013-11-08T17:23:15Z&#34;,
 *     
 *       &#34;updated_at&#34;: &#34;2015-01-08T21:30:50Z&#34;
 *     
 *     },
 *     
 *     {
 *     
 *       &#34;id&#34;: 2,
 *     
 *       &#34;account_id&#34;: 1010,
 *     
 *       &#34;label&#34;: &#34;&#34;,
 *     
 *       &#34;first_name&#34;: &#34;Second&#34;,
 *     
 *       &#34;last_name&#34;: &#34;User&#34;,
 *     
 *       &#34;job_title&#34;: &#34;&#34;,
 *     
 *       &#34;organization_name&#34;: &#34;&#34;,
 *     
 *       &#34;email&#34;: &#34;second{@literal @}example.com&#34;,
 *     
 *       &#34;phone&#34;: &#34;+18881234567&#34;,
 *     
 *       &#34;fax&#34;: &#34;&#34;,
 *     
 *       &#34;address1&#34;: &#34;French Street&#34;,
 *     
 *       &#34;address2&#34;: &#34;c/o Someone&#34;,
 *     
 *       &#34;city&#34;: &#34;Paris&#34;,
 *     
 *       &#34;state_province&#34;: &#34;XY&#34;,
 *     
 *       &#34;postal_code&#34;: &#34;00200&#34;,
 *     
 *       &#34;country&#34;: &#34;FR&#34;,
 *     
 *       &#34;created_at&#34;: &#34;2014-12-06T15:46:18Z&#34;,
 *     
 *       &#34;updated_at&#34;: &#34;2014-12-06T15:46:18Z&#34;
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
 *     &#34;total_entries&#34;: 2,
 *     
 *     &#34;total_pages&#34;: 1
 * 
 *   }
 * 
 * }
 * 
 */
@ResourceType(type="dnsimple:index/contact:Contact")
public class Contact extends com.pulumi.resources.CustomResource {
    /**
     * The account ID for the contact.
     * 
     */
    @Export(name="accountId", refs={Integer.class}, tree="[0]")
    private Output<Integer> accountId;

    /**
     * @return The account ID for the contact.
     * 
     */
    public Output<Integer> accountId() {
        return this.accountId;
    }
    /**
     * Address line 1
     * 
     */
    @Export(name="address1", refs={String.class}, tree="[0]")
    private Output<String> address1;

    /**
     * @return Address line 1
     * 
     */
    public Output<String> address1() {
        return this.address1;
    }
    /**
     * Address line 2
     * 
     */
    @Export(name="address2", refs={String.class}, tree="[0]")
    private Output<String> address2;

    /**
     * @return Address line 2
     * 
     */
    public Output<String> address2() {
        return this.address2;
    }
    /**
     * City
     * 
     */
    @Export(name="city", refs={String.class}, tree="[0]")
    private Output<String> city;

    /**
     * @return City
     * 
     */
    public Output<String> city() {
        return this.city;
    }
    /**
     * Country
     * 
     */
    @Export(name="country", refs={String.class}, tree="[0]")
    private Output<String> country;

    /**
     * @return Country
     * 
     */
    public Output<String> country() {
        return this.country;
    }
    /**
     * Timestamp representing when this contact was created.
     * 
     */
    @Export(name="createdAt", refs={String.class}, tree="[0]")
    private Output<String> createdAt;

    /**
     * @return Timestamp representing when this contact was created.
     * 
     */
    public Output<String> createdAt() {
        return this.createdAt;
    }
    /**
     * Email
     * 
     * # Attributes Reference
     * 
     */
    @Export(name="email", refs={String.class}, tree="[0]")
    private Output<String> email;

    /**
     * @return Email
     * 
     * # Attributes Reference
     * 
     */
    public Output<String> email() {
        return this.email;
    }
    /**
     * Fax
     * 
     */
    @Export(name="fax", refs={String.class}, tree="[0]")
    private Output<String> fax;

    /**
     * @return Fax
     * 
     */
    public Output<String> fax() {
        return this.fax;
    }
    /**
     * The fax number, normalized.
     * 
     */
    @Export(name="faxNormalized", refs={String.class}, tree="[0]")
    private Output<String> faxNormalized;

    /**
     * @return The fax number, normalized.
     * 
     */
    public Output<String> faxNormalized() {
        return this.faxNormalized;
    }
    /**
     * First name
     * 
     */
    @Export(name="firstName", refs={String.class}, tree="[0]")
    private Output<String> firstName;

    /**
     * @return First name
     * 
     */
    public Output<String> firstName() {
        return this.firstName;
    }
    /**
     * Job title
     * 
     */
    @Export(name="jobTitle", refs={String.class}, tree="[0]")
    private Output<String> jobTitle;

    /**
     * @return Job title
     * 
     */
    public Output<String> jobTitle() {
        return this.jobTitle;
    }
    /**
     * Label
     * 
     */
    @Export(name="label", refs={String.class}, tree="[0]")
    private Output<String> label;

    /**
     * @return Label
     * 
     */
    public Output<String> label() {
        return this.label;
    }
    /**
     * Last name
     * 
     */
    @Export(name="lastName", refs={String.class}, tree="[0]")
    private Output<String> lastName;

    /**
     * @return Last name
     * 
     */
    public Output<String> lastName() {
        return this.lastName;
    }
    /**
     * Organization name
     * 
     */
    @Export(name="organizationName", refs={String.class}, tree="[0]")
    private Output<String> organizationName;

    /**
     * @return Organization name
     * 
     */
    public Output<String> organizationName() {
        return this.organizationName;
    }
    /**
     * Phone
     * 
     */
    @Export(name="phone", refs={String.class}, tree="[0]")
    private Output<String> phone;

    /**
     * @return Phone
     * 
     */
    public Output<String> phone() {
        return this.phone;
    }
    /**
     * The phone number, normalized.
     * 
     */
    @Export(name="phoneNormalized", refs={String.class}, tree="[0]")
    private Output<String> phoneNormalized;

    /**
     * @return The phone number, normalized.
     * 
     */
    public Output<String> phoneNormalized() {
        return this.phoneNormalized;
    }
    /**
     * Postal code
     * 
     */
    @Export(name="postalCode", refs={String.class}, tree="[0]")
    private Output<String> postalCode;

    /**
     * @return Postal code
     * 
     */
    public Output<String> postalCode() {
        return this.postalCode;
    }
    /**
     * State province
     * 
     */
    @Export(name="stateProvince", refs={String.class}, tree="[0]")
    private Output<String> stateProvince;

    /**
     * @return State province
     * 
     */
    public Output<String> stateProvince() {
        return this.stateProvince;
    }
    /**
     * Timestamp representing when this contact was updated.
     * 
     */
    @Export(name="updatedAt", refs={String.class}, tree="[0]")
    private Output<String> updatedAt;

    /**
     * @return Timestamp representing when this contact was updated.
     * 
     */
    public Output<String> updatedAt() {
        return this.updatedAt;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Contact(String name) {
        this(name, ContactArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Contact(String name, ContactArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Contact(String name, ContactArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("dnsimple:index/contact:Contact", name, args == null ? ContactArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private Contact(String name, Output<String> id, @Nullable ContactState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("dnsimple:index/contact:Contact", name, state, makeResourceOptions(options, id));
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
    public static Contact get(String name, Output<String> id, @Nullable ContactState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Contact(name, id, state, options);
    }
}
