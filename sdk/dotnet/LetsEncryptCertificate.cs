// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.DNSimple
{
    /// <summary>
    /// Provides a DNSimple Let's Encrypt certificate resource.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using DNSimple = Pulumi.DNSimple;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var foobar = new DNSimple.LetsEncryptCertificate("foobar", new()
    ///     {
    ///         DomainId = dnsimple.DomainId,
    ///         AutoRenew = false,
    ///         Name = "www",
    ///     });
    /// 
    /// });
    /// ```
    /// </summary>
    [DNSimpleResourceType("dnsimple:index/letsEncryptCertificate:LetsEncryptCertificate")]
    public partial class LetsEncryptCertificate : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The identifying certification authority (CA)
        /// </summary>
        [Output("authorityIdentifier")]
        public Output<string> AuthorityIdentifier { get; private set; } = null!;

        /// <summary>
        /// Set to true if the certificate will auto-renew
        /// </summary>
        [Output("autoRenew")]
        public Output<bool> AutoRenew { get; private set; } = null!;

        /// <summary>
        /// The contact id for the certificate
        /// </summary>
        [Output("contactId")]
        public Output<int?> ContactId { get; private set; } = null!;

        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The certificate signing request
        /// </summary>
        [Output("csr")]
        public Output<string> Csr { get; private set; } = null!;

        /// <summary>
        /// The domain to be issued the certificate for
        /// </summary>
        [Output("domainId")]
        public Output<string?> DomainId { get; private set; } = null!;

        [Output("expiresOn")]
        public Output<string> ExpiresOn { get; private set; } = null!;

        /// <summary>
        /// The certificate name
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The state of the certificate
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        [Output("updatedAt")]
        public Output<string> UpdatedAt { get; private set; } = null!;

        /// <summary>
        /// The years the certificate will last
        /// </summary>
        [Output("years")]
        public Output<int> Years { get; private set; } = null!;


        /// <summary>
        /// Create a LetsEncryptCertificate resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LetsEncryptCertificate(string name, LetsEncryptCertificateArgs args, CustomResourceOptions? options = null)
            : base("dnsimple:index/letsEncryptCertificate:LetsEncryptCertificate", name, args ?? new LetsEncryptCertificateArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LetsEncryptCertificate(string name, Input<string> id, LetsEncryptCertificateState? state = null, CustomResourceOptions? options = null)
            : base("dnsimple:index/letsEncryptCertificate:LetsEncryptCertificate", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing LetsEncryptCertificate resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LetsEncryptCertificate Get(string name, Input<string> id, LetsEncryptCertificateState? state = null, CustomResourceOptions? options = null)
        {
            return new LetsEncryptCertificate(name, id, state, options);
        }
    }

    public sealed class LetsEncryptCertificateArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Set to true if the certificate will auto-renew
        /// </summary>
        [Input("autoRenew", required: true)]
        public Input<bool> AutoRenew { get; set; } = null!;

        /// <summary>
        /// The contact id for the certificate
        /// </summary>
        [Input("contactId")]
        public Input<int>? ContactId { get; set; }

        /// <summary>
        /// The domain to be issued the certificate for
        /// </summary>
        [Input("domainId")]
        public Input<string>? DomainId { get; set; }

        /// <summary>
        /// The certificate name
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public LetsEncryptCertificateArgs()
        {
        }
        public static new LetsEncryptCertificateArgs Empty => new LetsEncryptCertificateArgs();
    }

    public sealed class LetsEncryptCertificateState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The identifying certification authority (CA)
        /// </summary>
        [Input("authorityIdentifier")]
        public Input<string>? AuthorityIdentifier { get; set; }

        /// <summary>
        /// Set to true if the certificate will auto-renew
        /// </summary>
        [Input("autoRenew")]
        public Input<bool>? AutoRenew { get; set; }

        /// <summary>
        /// The contact id for the certificate
        /// </summary>
        [Input("contactId")]
        public Input<int>? ContactId { get; set; }

        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// The certificate signing request
        /// </summary>
        [Input("csr")]
        public Input<string>? Csr { get; set; }

        /// <summary>
        /// The domain to be issued the certificate for
        /// </summary>
        [Input("domainId")]
        public Input<string>? DomainId { get; set; }

        [Input("expiresOn")]
        public Input<string>? ExpiresOn { get; set; }

        /// <summary>
        /// The certificate name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The state of the certificate
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        [Input("updatedAt")]
        public Input<string>? UpdatedAt { get; set; }

        /// <summary>
        /// The years the certificate will last
        /// </summary>
        [Input("years")]
        public Input<int>? Years { get; set; }

        public LetsEncryptCertificateState()
        {
        }
        public static new LetsEncryptCertificateState Empty => new LetsEncryptCertificateState();
    }
}
