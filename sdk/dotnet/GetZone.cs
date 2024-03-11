// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.DNSimple
{
    public static class GetZone
    {
        /// <summary>
        /// Get information about a DNSimple zone.
        /// 
        /// Get zone:
        /// 
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using DNSimple = Pulumi.DNSimple;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var foobar = DNSimple.GetZone.Invoke(new()
        ///     {
        ///         Name = "dnsimple.com",
        ///     });
        /// 
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// 
        /// The following arguments are supported:
        /// 
        /// * `name` - (Required) The name of the zone
        /// 
        /// The following attributes are exported:
        /// 
        /// * `id` - The zone ID
        /// * `account_id` - The account ID
        /// * `name` - The name of the zone
        /// * `reverse` - True for a reverse zone, false for a forward zone.
        /// </summary>
        public static Task<GetZoneResult> InvokeAsync(GetZoneArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetZoneResult>("dnsimple:index/getZone:getZone", args ?? new GetZoneArgs(), options.WithDefaults());

        /// <summary>
        /// Get information about a DNSimple zone.
        /// 
        /// Get zone:
        /// 
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using DNSimple = Pulumi.DNSimple;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var foobar = DNSimple.GetZone.Invoke(new()
        ///     {
        ///         Name = "dnsimple.com",
        ///     });
        /// 
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// 
        /// The following arguments are supported:
        /// 
        /// * `name` - (Required) The name of the zone
        /// 
        /// The following attributes are exported:
        /// 
        /// * `id` - The zone ID
        /// * `account_id` - The account ID
        /// * `name` - The name of the zone
        /// * `reverse` - True for a reverse zone, false for a forward zone.
        /// </summary>
        public static Output<GetZoneResult> Invoke(GetZoneInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetZoneResult>("dnsimple:index/getZone:getZone", args ?? new GetZoneInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetZoneArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetZoneArgs()
        {
        }
        public static new GetZoneArgs Empty => new GetZoneArgs();
    }

    public sealed class GetZoneInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetZoneInvokeArgs()
        {
        }
        public static new GetZoneInvokeArgs Empty => new GetZoneInvokeArgs();
    }


    [OutputType]
    public sealed class GetZoneResult
    {
        public readonly int AccountId;
        public readonly int Id;
        public readonly string Name;
        public readonly bool Reverse;

        [OutputConstructor]
        private GetZoneResult(
            int accountId,

            int id,

            string name,

            bool reverse)
        {
            AccountId = accountId;
            Id = id;
            Name = name;
            Reverse = reverse;
        }
    }
}
