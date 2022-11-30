// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dnsimple

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type EmailForward struct {
	pulumi.CustomResourceState

	AliasEmail       pulumi.StringOutput `pulumi:"aliasEmail"`
	AliasName        pulumi.StringOutput `pulumi:"aliasName"`
	DestinationEmail pulumi.StringOutput `pulumi:"destinationEmail"`
	Domain           pulumi.StringOutput `pulumi:"domain"`
}

// NewEmailForward registers a new resource with the given unique name, arguments, and options.
func NewEmailForward(ctx *pulumi.Context,
	name string, args *EmailForwardArgs, opts ...pulumi.ResourceOption) (*EmailForward, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AliasName == nil {
		return nil, errors.New("invalid value for required argument 'AliasName'")
	}
	if args.DestinationEmail == nil {
		return nil, errors.New("invalid value for required argument 'DestinationEmail'")
	}
	if args.Domain == nil {
		return nil, errors.New("invalid value for required argument 'Domain'")
	}
	var resource EmailForward
	err := ctx.RegisterResource("dnsimple:index/emailForward:EmailForward", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEmailForward gets an existing EmailForward resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEmailForward(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EmailForwardState, opts ...pulumi.ResourceOption) (*EmailForward, error) {
	var resource EmailForward
	err := ctx.ReadResource("dnsimple:index/emailForward:EmailForward", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EmailForward resources.
type emailForwardState struct {
	AliasEmail       *string `pulumi:"aliasEmail"`
	AliasName        *string `pulumi:"aliasName"`
	DestinationEmail *string `pulumi:"destinationEmail"`
	Domain           *string `pulumi:"domain"`
}

type EmailForwardState struct {
	AliasEmail       pulumi.StringPtrInput
	AliasName        pulumi.StringPtrInput
	DestinationEmail pulumi.StringPtrInput
	Domain           pulumi.StringPtrInput
}

func (EmailForwardState) ElementType() reflect.Type {
	return reflect.TypeOf((*emailForwardState)(nil)).Elem()
}

type emailForwardArgs struct {
	AliasName        string `pulumi:"aliasName"`
	DestinationEmail string `pulumi:"destinationEmail"`
	Domain           string `pulumi:"domain"`
}

// The set of arguments for constructing a EmailForward resource.
type EmailForwardArgs struct {
	AliasName        pulumi.StringInput
	DestinationEmail pulumi.StringInput
	Domain           pulumi.StringInput
}

func (EmailForwardArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*emailForwardArgs)(nil)).Elem()
}

type EmailForwardInput interface {
	pulumi.Input

	ToEmailForwardOutput() EmailForwardOutput
	ToEmailForwardOutputWithContext(ctx context.Context) EmailForwardOutput
}

func (*EmailForward) ElementType() reflect.Type {
	return reflect.TypeOf((**EmailForward)(nil)).Elem()
}

func (i *EmailForward) ToEmailForwardOutput() EmailForwardOutput {
	return i.ToEmailForwardOutputWithContext(context.Background())
}

func (i *EmailForward) ToEmailForwardOutputWithContext(ctx context.Context) EmailForwardOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EmailForwardOutput)
}

// EmailForwardArrayInput is an input type that accepts EmailForwardArray and EmailForwardArrayOutput values.
// You can construct a concrete instance of `EmailForwardArrayInput` via:
//
//	EmailForwardArray{ EmailForwardArgs{...} }
type EmailForwardArrayInput interface {
	pulumi.Input

	ToEmailForwardArrayOutput() EmailForwardArrayOutput
	ToEmailForwardArrayOutputWithContext(context.Context) EmailForwardArrayOutput
}

type EmailForwardArray []EmailForwardInput

func (EmailForwardArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*EmailForward)(nil)).Elem()
}

func (i EmailForwardArray) ToEmailForwardArrayOutput() EmailForwardArrayOutput {
	return i.ToEmailForwardArrayOutputWithContext(context.Background())
}

func (i EmailForwardArray) ToEmailForwardArrayOutputWithContext(ctx context.Context) EmailForwardArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EmailForwardArrayOutput)
}

// EmailForwardMapInput is an input type that accepts EmailForwardMap and EmailForwardMapOutput values.
// You can construct a concrete instance of `EmailForwardMapInput` via:
//
//	EmailForwardMap{ "key": EmailForwardArgs{...} }
type EmailForwardMapInput interface {
	pulumi.Input

	ToEmailForwardMapOutput() EmailForwardMapOutput
	ToEmailForwardMapOutputWithContext(context.Context) EmailForwardMapOutput
}

type EmailForwardMap map[string]EmailForwardInput

func (EmailForwardMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*EmailForward)(nil)).Elem()
}

func (i EmailForwardMap) ToEmailForwardMapOutput() EmailForwardMapOutput {
	return i.ToEmailForwardMapOutputWithContext(context.Background())
}

func (i EmailForwardMap) ToEmailForwardMapOutputWithContext(ctx context.Context) EmailForwardMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EmailForwardMapOutput)
}

type EmailForwardOutput struct{ *pulumi.OutputState }

func (EmailForwardOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EmailForward)(nil)).Elem()
}

func (o EmailForwardOutput) ToEmailForwardOutput() EmailForwardOutput {
	return o
}

func (o EmailForwardOutput) ToEmailForwardOutputWithContext(ctx context.Context) EmailForwardOutput {
	return o
}

func (o EmailForwardOutput) AliasEmail() pulumi.StringOutput {
	return o.ApplyT(func(v *EmailForward) pulumi.StringOutput { return v.AliasEmail }).(pulumi.StringOutput)
}

func (o EmailForwardOutput) AliasName() pulumi.StringOutput {
	return o.ApplyT(func(v *EmailForward) pulumi.StringOutput { return v.AliasName }).(pulumi.StringOutput)
}

func (o EmailForwardOutput) DestinationEmail() pulumi.StringOutput {
	return o.ApplyT(func(v *EmailForward) pulumi.StringOutput { return v.DestinationEmail }).(pulumi.StringOutput)
}

func (o EmailForwardOutput) Domain() pulumi.StringOutput {
	return o.ApplyT(func(v *EmailForward) pulumi.StringOutput { return v.Domain }).(pulumi.StringOutput)
}

type EmailForwardArrayOutput struct{ *pulumi.OutputState }

func (EmailForwardArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*EmailForward)(nil)).Elem()
}

func (o EmailForwardArrayOutput) ToEmailForwardArrayOutput() EmailForwardArrayOutput {
	return o
}

func (o EmailForwardArrayOutput) ToEmailForwardArrayOutputWithContext(ctx context.Context) EmailForwardArrayOutput {
	return o
}

func (o EmailForwardArrayOutput) Index(i pulumi.IntInput) EmailForwardOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *EmailForward {
		return vs[0].([]*EmailForward)[vs[1].(int)]
	}).(EmailForwardOutput)
}

type EmailForwardMapOutput struct{ *pulumi.OutputState }

func (EmailForwardMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*EmailForward)(nil)).Elem()
}

func (o EmailForwardMapOutput) ToEmailForwardMapOutput() EmailForwardMapOutput {
	return o
}

func (o EmailForwardMapOutput) ToEmailForwardMapOutputWithContext(ctx context.Context) EmailForwardMapOutput {
	return o
}

func (o EmailForwardMapOutput) MapIndex(k pulumi.StringInput) EmailForwardOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *EmailForward {
		return vs[0].(map[string]*EmailForward)[vs[1].(string)]
	}).(EmailForwardOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EmailForwardInput)(nil)).Elem(), &EmailForward{})
	pulumi.RegisterInputType(reflect.TypeOf((*EmailForwardArrayInput)(nil)).Elem(), EmailForwardArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*EmailForwardMapInput)(nil)).Elem(), EmailForwardMap{})
	pulumi.RegisterOutputType(EmailForwardOutput{})
	pulumi.RegisterOutputType(EmailForwardArrayOutput{})
	pulumi.RegisterOutputType(EmailForwardMapOutput{})
}
