// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dnsimple

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-dnsimple/sdk/v4/go/dnsimple/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Domain struct {
	pulumi.CustomResourceState

	AccountId    pulumi.IntOutput    `pulumi:"accountId"`
	AutoRenew    pulumi.BoolOutput   `pulumi:"autoRenew"`
	Name         pulumi.StringOutput `pulumi:"name"`
	PrivateWhois pulumi.BoolOutput   `pulumi:"privateWhois"`
	RegistrantId pulumi.IntOutput    `pulumi:"registrantId"`
	State        pulumi.StringOutput `pulumi:"state"`
	UnicodeName  pulumi.StringOutput `pulumi:"unicodeName"`
}

// NewDomain registers a new resource with the given unique name, arguments, and options.
func NewDomain(ctx *pulumi.Context,
	name string, args *DomainArgs, opts ...pulumi.ResourceOption) (*Domain, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Domain
	err := ctx.RegisterResource("dnsimple:index/domain:Domain", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDomain gets an existing Domain resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDomain(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DomainState, opts ...pulumi.ResourceOption) (*Domain, error) {
	var resource Domain
	err := ctx.ReadResource("dnsimple:index/domain:Domain", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Domain resources.
type domainState struct {
	AccountId    *int    `pulumi:"accountId"`
	AutoRenew    *bool   `pulumi:"autoRenew"`
	Name         *string `pulumi:"name"`
	PrivateWhois *bool   `pulumi:"privateWhois"`
	RegistrantId *int    `pulumi:"registrantId"`
	State        *string `pulumi:"state"`
	UnicodeName  *string `pulumi:"unicodeName"`
}

type DomainState struct {
	AccountId    pulumi.IntPtrInput
	AutoRenew    pulumi.BoolPtrInput
	Name         pulumi.StringPtrInput
	PrivateWhois pulumi.BoolPtrInput
	RegistrantId pulumi.IntPtrInput
	State        pulumi.StringPtrInput
	UnicodeName  pulumi.StringPtrInput
}

func (DomainState) ElementType() reflect.Type {
	return reflect.TypeOf((*domainState)(nil)).Elem()
}

type domainArgs struct {
	Name string `pulumi:"name"`
}

// The set of arguments for constructing a Domain resource.
type DomainArgs struct {
	Name pulumi.StringInput
}

func (DomainArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*domainArgs)(nil)).Elem()
}

type DomainInput interface {
	pulumi.Input

	ToDomainOutput() DomainOutput
	ToDomainOutputWithContext(ctx context.Context) DomainOutput
}

func (*Domain) ElementType() reflect.Type {
	return reflect.TypeOf((**Domain)(nil)).Elem()
}

func (i *Domain) ToDomainOutput() DomainOutput {
	return i.ToDomainOutputWithContext(context.Background())
}

func (i *Domain) ToDomainOutputWithContext(ctx context.Context) DomainOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainOutput)
}

// DomainArrayInput is an input type that accepts DomainArray and DomainArrayOutput values.
// You can construct a concrete instance of `DomainArrayInput` via:
//
//	DomainArray{ DomainArgs{...} }
type DomainArrayInput interface {
	pulumi.Input

	ToDomainArrayOutput() DomainArrayOutput
	ToDomainArrayOutputWithContext(context.Context) DomainArrayOutput
}

type DomainArray []DomainInput

func (DomainArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Domain)(nil)).Elem()
}

func (i DomainArray) ToDomainArrayOutput() DomainArrayOutput {
	return i.ToDomainArrayOutputWithContext(context.Background())
}

func (i DomainArray) ToDomainArrayOutputWithContext(ctx context.Context) DomainArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainArrayOutput)
}

// DomainMapInput is an input type that accepts DomainMap and DomainMapOutput values.
// You can construct a concrete instance of `DomainMapInput` via:
//
//	DomainMap{ "key": DomainArgs{...} }
type DomainMapInput interface {
	pulumi.Input

	ToDomainMapOutput() DomainMapOutput
	ToDomainMapOutputWithContext(context.Context) DomainMapOutput
}

type DomainMap map[string]DomainInput

func (DomainMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Domain)(nil)).Elem()
}

func (i DomainMap) ToDomainMapOutput() DomainMapOutput {
	return i.ToDomainMapOutputWithContext(context.Background())
}

func (i DomainMap) ToDomainMapOutputWithContext(ctx context.Context) DomainMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainMapOutput)
}

type DomainOutput struct{ *pulumi.OutputState }

func (DomainOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Domain)(nil)).Elem()
}

func (o DomainOutput) ToDomainOutput() DomainOutput {
	return o
}

func (o DomainOutput) ToDomainOutputWithContext(ctx context.Context) DomainOutput {
	return o
}

func (o DomainOutput) AccountId() pulumi.IntOutput {
	return o.ApplyT(func(v *Domain) pulumi.IntOutput { return v.AccountId }).(pulumi.IntOutput)
}

func (o DomainOutput) AutoRenew() pulumi.BoolOutput {
	return o.ApplyT(func(v *Domain) pulumi.BoolOutput { return v.AutoRenew }).(pulumi.BoolOutput)
}

func (o DomainOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o DomainOutput) PrivateWhois() pulumi.BoolOutput {
	return o.ApplyT(func(v *Domain) pulumi.BoolOutput { return v.PrivateWhois }).(pulumi.BoolOutput)
}

func (o DomainOutput) RegistrantId() pulumi.IntOutput {
	return o.ApplyT(func(v *Domain) pulumi.IntOutput { return v.RegistrantId }).(pulumi.IntOutput)
}

func (o DomainOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

func (o DomainOutput) UnicodeName() pulumi.StringOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringOutput { return v.UnicodeName }).(pulumi.StringOutput)
}

type DomainArrayOutput struct{ *pulumi.OutputState }

func (DomainArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Domain)(nil)).Elem()
}

func (o DomainArrayOutput) ToDomainArrayOutput() DomainArrayOutput {
	return o
}

func (o DomainArrayOutput) ToDomainArrayOutputWithContext(ctx context.Context) DomainArrayOutput {
	return o
}

func (o DomainArrayOutput) Index(i pulumi.IntInput) DomainOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Domain {
		return vs[0].([]*Domain)[vs[1].(int)]
	}).(DomainOutput)
}

type DomainMapOutput struct{ *pulumi.OutputState }

func (DomainMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Domain)(nil)).Elem()
}

func (o DomainMapOutput) ToDomainMapOutput() DomainMapOutput {
	return o
}

func (o DomainMapOutput) ToDomainMapOutputWithContext(ctx context.Context) DomainMapOutput {
	return o
}

func (o DomainMapOutput) MapIndex(k pulumi.StringInput) DomainOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Domain {
		return vs[0].(map[string]*Domain)[vs[1].(string)]
	}).(DomainOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DomainInput)(nil)).Elem(), &Domain{})
	pulumi.RegisterInputType(reflect.TypeOf((*DomainArrayInput)(nil)).Elem(), DomainArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DomainMapInput)(nil)).Elem(), DomainMap{})
	pulumi.RegisterOutputType(DomainOutput{})
	pulumi.RegisterOutputType(DomainArrayOutput{})
	pulumi.RegisterOutputType(DomainMapOutput{})
}
