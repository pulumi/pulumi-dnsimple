// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.DNSimple.Outputs
{

    [OutputType]
    public sealed class GetRegistrantChangeCheckExtendedAttributeOptionResult
    {
        public readonly string Description;
        public readonly string Title;
        public readonly string Value;

        [OutputConstructor]
        private GetRegistrantChangeCheckExtendedAttributeOptionResult(
            string description,

            string title,

            string value)
        {
            Description = description;
            Title = title;
            Value = value;
        }
    }
}