// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.DNSimple.Inputs
{

    public sealed class RegisteredDomainTimeoutsGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("create")]
        public Input<string>? Create { get; set; }

        [Input("delete")]
        public Input<string>? Delete { get; set; }

        [Input("update")]
        public Input<string>? Update { get; set; }

        public RegisteredDomainTimeoutsGetArgs()
        {
        }
        public static new RegisteredDomainTimeoutsGetArgs Empty => new RegisteredDomainTimeoutsGetArgs();
    }
}
