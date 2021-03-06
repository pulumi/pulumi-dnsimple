// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;

namespace Pulumi.DNSimple
{
    public static class Config
    {
        private static readonly Pulumi.Config __config = new Pulumi.Config("dnsimple");
        /// <summary>
        /// The account for API operations.
        /// </summary>
        public static string? Account { get; set; } = __config.Get("account");

        /// <summary>
        /// Flag to enable the sandbox API.
        /// </summary>
        public static bool? Sandbox { get; set; } = __config.GetBoolean("sandbox");

        /// <summary>
        /// The API v2 token for API operations.
        /// </summary>
        public static string? Token { get; set; } = __config.Get("token");

    }
}
