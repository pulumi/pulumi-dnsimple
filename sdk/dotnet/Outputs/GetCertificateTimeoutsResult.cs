// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.DNSimple.Outputs
{

    [OutputType]
    public sealed class GetCertificateTimeoutsResult
    {
        /// <summary>
        /// (String) - The timeout for the read operation e.g. `5m`
        /// </summary>
        public readonly string? Read;

        [OutputConstructor]
        private GetCertificateTimeoutsResult(string? read)
        {
            Read = read;
        }
    }
}
