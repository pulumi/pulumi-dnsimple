// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dnsimple

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-dnsimple/sdk/v4/go/dnsimple/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information on the requirements of a registrant change.
//
// > **Note:** The registrant change API is currently in developer preview and is subject to change.
//
// Get registrant change requirements for the `dnsimple.com` domain and the contact with ID `1234`:
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-dnsimple/sdk/v4/go/dnsimple"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := dnsimple.GetRegistrantChangeCheck(ctx, &dnsimple.GetRegistrantChangeCheckArgs{
//				DomainId:  "dnsimple.com",
//				ContactId: "1234",
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
// * `domainId` - (Required) The name or ID of the domain.
// * `contactId` - (Required) The ID of the contact you are planning to change to.
//
// The following additional attributes are exported:
//
// * `contactId` - The ID of the contact you are planning to change to.
// * `domainId` - The name or ID of the domain.
// * `extendedAttributes` - (List) A list of extended attributes that are required for the registrant change. (see below for nested schema)
// * `registryOwnerChange` - (Boolean) Whether the registrant change is going to result in an owner change at the registry.
//
// <a id="nestedblock--extended_attributes"></a>
func GetRegistrantChangeCheck(ctx *pulumi.Context, args *GetRegistrantChangeCheckArgs, opts ...pulumi.InvokeOption) (*GetRegistrantChangeCheckResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetRegistrantChangeCheckResult
	err := ctx.Invoke("dnsimple:index/getRegistrantChangeCheck:getRegistrantChangeCheck", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getRegistrantChangeCheck.
type GetRegistrantChangeCheckArgs struct {
	ContactId string `pulumi:"contactId"`
	DomainId  string `pulumi:"domainId"`
}

// A collection of values returned by getRegistrantChangeCheck.
type GetRegistrantChangeCheckResult struct {
	ContactId           string                                      `pulumi:"contactId"`
	DomainId            string                                      `pulumi:"domainId"`
	ExtendedAttributes  []GetRegistrantChangeCheckExtendedAttribute `pulumi:"extendedAttributes"`
	Id                  string                                      `pulumi:"id"`
	RegistryOwnerChange bool                                        `pulumi:"registryOwnerChange"`
}

func GetRegistrantChangeCheckOutput(ctx *pulumi.Context, args GetRegistrantChangeCheckOutputArgs, opts ...pulumi.InvokeOption) GetRegistrantChangeCheckResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetRegistrantChangeCheckResultOutput, error) {
			args := v.(GetRegistrantChangeCheckArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("dnsimple:index/getRegistrantChangeCheck:getRegistrantChangeCheck", args, GetRegistrantChangeCheckResultOutput{}, options).(GetRegistrantChangeCheckResultOutput), nil
		}).(GetRegistrantChangeCheckResultOutput)
}

// A collection of arguments for invoking getRegistrantChangeCheck.
type GetRegistrantChangeCheckOutputArgs struct {
	ContactId pulumi.StringInput `pulumi:"contactId"`
	DomainId  pulumi.StringInput `pulumi:"domainId"`
}

func (GetRegistrantChangeCheckOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetRegistrantChangeCheckArgs)(nil)).Elem()
}

// A collection of values returned by getRegistrantChangeCheck.
type GetRegistrantChangeCheckResultOutput struct{ *pulumi.OutputState }

func (GetRegistrantChangeCheckResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetRegistrantChangeCheckResult)(nil)).Elem()
}

func (o GetRegistrantChangeCheckResultOutput) ToGetRegistrantChangeCheckResultOutput() GetRegistrantChangeCheckResultOutput {
	return o
}

func (o GetRegistrantChangeCheckResultOutput) ToGetRegistrantChangeCheckResultOutputWithContext(ctx context.Context) GetRegistrantChangeCheckResultOutput {
	return o
}

func (o GetRegistrantChangeCheckResultOutput) ContactId() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegistrantChangeCheckResult) string { return v.ContactId }).(pulumi.StringOutput)
}

func (o GetRegistrantChangeCheckResultOutput) DomainId() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegistrantChangeCheckResult) string { return v.DomainId }).(pulumi.StringOutput)
}

func (o GetRegistrantChangeCheckResultOutput) ExtendedAttributes() GetRegistrantChangeCheckExtendedAttributeArrayOutput {
	return o.ApplyT(func(v GetRegistrantChangeCheckResult) []GetRegistrantChangeCheckExtendedAttribute {
		return v.ExtendedAttributes
	}).(GetRegistrantChangeCheckExtendedAttributeArrayOutput)
}

func (o GetRegistrantChangeCheckResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegistrantChangeCheckResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetRegistrantChangeCheckResultOutput) RegistryOwnerChange() pulumi.BoolOutput {
	return o.ApplyT(func(v GetRegistrantChangeCheckResult) bool { return v.RegistryOwnerChange }).(pulumi.BoolOutput)
}

func init() {
	pulumi.RegisterOutputType(GetRegistrantChangeCheckResultOutput{})
}
