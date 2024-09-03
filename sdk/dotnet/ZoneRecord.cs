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
    /// Provides a DNSimple zone record resource.
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
    ///     // Add a record to the root domain
    ///     var foobar = new DNSimple.ZoneRecord("foobar", new()
    ///     {
    ///         ZoneName = dnsimpleDomain,
    ///         Name = "",
    ///         Value = "192.168.0.11",
    ///         Type = "A",
    ///         Ttl = 3600,
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using DNSimple = Pulumi.DNSimple;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     // Add a record to a sub-domain
    ///     var foobar = new DNSimple.ZoneRecord("foobar", new()
    ///     {
    ///         ZoneName = dnsimpleDomain,
    ///         Name = "terraform",
    ///         Value = "192.168.0.11",
    ///         Type = "A",
    ///         Ttl = 3600,
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// DNSimple resources can be imported using their parent zone name (domain name) and numeric record ID.
    /// 
    /// **Importing record example.com with record ID 1234**
    /// 
    /// bash
    /// 
    /// ```sh
    /// $ pulumi import dnsimple:index/zoneRecord:ZoneRecord resource_name example.com_1234
    /// ```
    /// 
    /// **Importing record &lt;http://www.example.com&gt; with record ID 1234**
    /// 
    /// bash
    /// 
    /// ```sh
    /// $ pulumi import dnsimple:index/zoneRecord:ZoneRecord resource_name example.com_1234
    /// ```
    /// 
    /// The record ID can be found in the URL when editing a record on the DNSimple web dashboard.
    /// </summary>
    [DNSimpleResourceType("dnsimple:index/zoneRecord:ZoneRecord")]
    public partial class ZoneRecord : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the record
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("nameNormalized")]
        public Output<string> NameNormalized { get; private set; } = null!;

        /// <summary>
        /// The priority of the record - only useful for some record types
        /// </summary>
        [Output("priority")]
        public Output<int> Priority { get; private set; } = null!;

        /// <summary>
        /// The FQDN of the record
        /// </summary>
        [Output("qualifiedName")]
        public Output<string> QualifiedName { get; private set; } = null!;

        /// <summary>
        /// A list of regions to serve the record from. You can find a list of supported values in our [developer documentation](https://developer.dnsimple.com/v2/zones/records/).
        /// </summary>
        [Output("regions")]
        public Output<ImmutableArray<string>> Regions { get; private set; } = null!;

        /// <summary>
        /// The TTL of the record - defaults to 3600
        /// </summary>
        [Output("ttl")]
        public Output<int> Ttl { get; private set; } = null!;

        /// <summary>
        /// The type of the record
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;

        /// <summary>
        /// The value of the record
        /// </summary>
        [Output("value")]
        public Output<string> Value { get; private set; } = null!;

        /// <summary>
        /// The normalized value of the record
        /// </summary>
        [Output("valueNormalized")]
        public Output<string> ValueNormalized { get; private set; } = null!;

        /// <summary>
        /// The zone ID of the record
        /// </summary>
        [Output("zoneId")]
        public Output<string> ZoneId { get; private set; } = null!;

        /// <summary>
        /// The zone name to add the record to
        /// </summary>
        [Output("zoneName")]
        public Output<string> ZoneName { get; private set; } = null!;


        /// <summary>
        /// Create a ZoneRecord resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ZoneRecord(string name, ZoneRecordArgs args, CustomResourceOptions? options = null)
            : base("dnsimple:index/zoneRecord:ZoneRecord", name, args ?? new ZoneRecordArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ZoneRecord(string name, Input<string> id, ZoneRecordState? state = null, CustomResourceOptions? options = null)
            : base("dnsimple:index/zoneRecord:ZoneRecord", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ZoneRecord resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ZoneRecord Get(string name, Input<string> id, ZoneRecordState? state = null, CustomResourceOptions? options = null)
        {
            return new ZoneRecord(name, id, state, options);
        }
    }

    public sealed class ZoneRecordArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the record
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The priority of the record - only useful for some record types
        /// </summary>
        [Input("priority")]
        public Input<int>? Priority { get; set; }

        [Input("regions")]
        private InputList<string>? _regions;

        /// <summary>
        /// A list of regions to serve the record from. You can find a list of supported values in our [developer documentation](https://developer.dnsimple.com/v2/zones/records/).
        /// </summary>
        public InputList<string> Regions
        {
            get => _regions ?? (_regions = new InputList<string>());
            set => _regions = value;
        }

        /// <summary>
        /// The TTL of the record - defaults to 3600
        /// </summary>
        [Input("ttl")]
        public Input<int>? Ttl { get; set; }

        /// <summary>
        /// The type of the record
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        /// <summary>
        /// The value of the record
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        /// <summary>
        /// The zone name to add the record to
        /// </summary>
        [Input("zoneName", required: true)]
        public Input<string> ZoneName { get; set; } = null!;

        public ZoneRecordArgs()
        {
        }
        public static new ZoneRecordArgs Empty => new ZoneRecordArgs();
    }

    public sealed class ZoneRecordState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the record
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("nameNormalized")]
        public Input<string>? NameNormalized { get; set; }

        /// <summary>
        /// The priority of the record - only useful for some record types
        /// </summary>
        [Input("priority")]
        public Input<int>? Priority { get; set; }

        /// <summary>
        /// The FQDN of the record
        /// </summary>
        [Input("qualifiedName")]
        public Input<string>? QualifiedName { get; set; }

        [Input("regions")]
        private InputList<string>? _regions;

        /// <summary>
        /// A list of regions to serve the record from. You can find a list of supported values in our [developer documentation](https://developer.dnsimple.com/v2/zones/records/).
        /// </summary>
        public InputList<string> Regions
        {
            get => _regions ?? (_regions = new InputList<string>());
            set => _regions = value;
        }

        /// <summary>
        /// The TTL of the record - defaults to 3600
        /// </summary>
        [Input("ttl")]
        public Input<int>? Ttl { get; set; }

        /// <summary>
        /// The type of the record
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        /// <summary>
        /// The value of the record
        /// </summary>
        [Input("value")]
        public Input<string>? Value { get; set; }

        /// <summary>
        /// The normalized value of the record
        /// </summary>
        [Input("valueNormalized")]
        public Input<string>? ValueNormalized { get; set; }

        /// <summary>
        /// The zone ID of the record
        /// </summary>
        [Input("zoneId")]
        public Input<string>? ZoneId { get; set; }

        /// <summary>
        /// The zone name to add the record to
        /// </summary>
        [Input("zoneName")]
        public Input<string>? ZoneName { get; set; }

        public ZoneRecordState()
        {
        }
        public static new ZoneRecordState Empty => new ZoneRecordState();
    }
}
