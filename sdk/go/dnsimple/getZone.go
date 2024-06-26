// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dnsimple

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-dnsimple/sdk/v3/go/dnsimple/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information about a DNSimple zone.
//
// Get zone:
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-dnsimple/sdk/v3/go/dnsimple"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := dnsimple.GetZone(ctx, &dnsimple.GetZoneArgs{
//				Name: "dnsimple.com",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// The following arguments are supported:
//
// * `name` - (Required) The name of the zone
//
// The following attributes are exported:
//
// * `id` - The zone ID
// * `accountId` - The account ID
// * `name` - The name of the zone
// * `reverse` - True for a reverse zone, false for a forward zone.
func GetZone(ctx *pulumi.Context, args *GetZoneArgs, opts ...pulumi.InvokeOption) (*GetZoneResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetZoneResult
	err := ctx.Invoke("dnsimple:index/getZone:getZone", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getZone.
type GetZoneArgs struct {
	Name string `pulumi:"name"`
}

// A collection of values returned by getZone.
type GetZoneResult struct {
	AccountId int    `pulumi:"accountId"`
	Id        int    `pulumi:"id"`
	Name      string `pulumi:"name"`
	Reverse   bool   `pulumi:"reverse"`
}

func GetZoneOutput(ctx *pulumi.Context, args GetZoneOutputArgs, opts ...pulumi.InvokeOption) GetZoneResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetZoneResult, error) {
			args := v.(GetZoneArgs)
			r, err := GetZone(ctx, &args, opts...)
			var s GetZoneResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetZoneResultOutput)
}

// A collection of arguments for invoking getZone.
type GetZoneOutputArgs struct {
	Name pulumi.StringInput `pulumi:"name"`
}

func (GetZoneOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetZoneArgs)(nil)).Elem()
}

// A collection of values returned by getZone.
type GetZoneResultOutput struct{ *pulumi.OutputState }

func (GetZoneResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetZoneResult)(nil)).Elem()
}

func (o GetZoneResultOutput) ToGetZoneResultOutput() GetZoneResultOutput {
	return o
}

func (o GetZoneResultOutput) ToGetZoneResultOutputWithContext(ctx context.Context) GetZoneResultOutput {
	return o
}

func (o GetZoneResultOutput) AccountId() pulumi.IntOutput {
	return o.ApplyT(func(v GetZoneResult) int { return v.AccountId }).(pulumi.IntOutput)
}

func (o GetZoneResultOutput) Id() pulumi.IntOutput {
	return o.ApplyT(func(v GetZoneResult) int { return v.Id }).(pulumi.IntOutput)
}

func (o GetZoneResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetZoneResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o GetZoneResultOutput) Reverse() pulumi.BoolOutput {
	return o.ApplyT(func(v GetZoneResult) bool { return v.Reverse }).(pulumi.BoolOutput)
}

func init() {
	pulumi.RegisterOutputType(GetZoneResultOutput{})
}
