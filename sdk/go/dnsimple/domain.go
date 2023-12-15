// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dnsimple

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-dnsimple/sdk/v3/go/dnsimple/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a DNSimple domain resource.
//
// ## Example Usage
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
//			_, err := dnsimple.NewDomain(ctx, "foobar", &dnsimple.DomainArgs{
//				Name: pulumi.Any(_var.Dnsimple.Domain),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// DNSimple domains can be imported using their numeric record ID. bash
//
// ```sh
//
//	$ pulumi import dnsimple:index/domain:Domain resource_name 5678
//
// ```
//
//	The record ID can be found within [DNSimple Domains API](https://developer.dnsimple.com/v2/domains/#listDomains). Check out [Authentication](https://developer.dnsimple.com/v2/#authentication) in API Overview for available options. bash curl -u 'EMAIL:PASSWORD' https://api.dnsimple.com/v2/1234/domains?name_like=example.com | jq {
//
//	"data"[
//
//	{
//
//	"id"5678,
//
//	"account_id"1234,
//
//	"registrant_id"null,
//
//	"name""example.com",
//
//	"unicode_name""example.com",
//
//	"state""hosted",
//
//	"auto_renew"false,
//
//	"private_whois"false,
//
//	"expires_on"null,
//
//	"expires_at"null,
//
//	"created_at""2021-10-01T00:00:00Z",
//
//	"updated_at""2021-10-01T00:00:00Z"
//
//	}
//
//	],
//
//	"pagination"{
//
//	"current_page"1,
//
//	"per_page"30,
//
//	"total_entries"1,
//
//	"total_pages"1
//
//	} }
type Domain struct {
	pulumi.CustomResourceState

	// The account ID for the domain.
	AccountId pulumi.IntOutput `pulumi:"accountId"`
	// Whether the domain is set to auto-renew.
	AutoRenew pulumi.BoolOutput `pulumi:"autoRenew"`
	// The domain name to be created
	//
	// # Attributes Reference
	Name pulumi.StringOutput `pulumi:"name"`
	// Whether the domain has WhoIs privacy enabled.
	PrivateWhois pulumi.BoolOutput `pulumi:"privateWhois"`
	// The ID of the registrant (contact) for the domain.
	RegistrantId pulumi.IntOutput `pulumi:"registrantId"`
	// The state of the domain.
	State pulumi.StringOutput `pulumi:"state"`
	// The domain name in Unicode format.
	UnicodeName pulumi.StringOutput `pulumi:"unicodeName"`
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
	// The account ID for the domain.
	AccountId *int `pulumi:"accountId"`
	// Whether the domain is set to auto-renew.
	AutoRenew *bool `pulumi:"autoRenew"`
	// The domain name to be created
	//
	// # Attributes Reference
	Name *string `pulumi:"name"`
	// Whether the domain has WhoIs privacy enabled.
	PrivateWhois *bool `pulumi:"privateWhois"`
	// The ID of the registrant (contact) for the domain.
	RegistrantId *int `pulumi:"registrantId"`
	// The state of the domain.
	State *string `pulumi:"state"`
	// The domain name in Unicode format.
	UnicodeName *string `pulumi:"unicodeName"`
}

type DomainState struct {
	// The account ID for the domain.
	AccountId pulumi.IntPtrInput
	// Whether the domain is set to auto-renew.
	AutoRenew pulumi.BoolPtrInput
	// The domain name to be created
	//
	// # Attributes Reference
	Name pulumi.StringPtrInput
	// Whether the domain has WhoIs privacy enabled.
	PrivateWhois pulumi.BoolPtrInput
	// The ID of the registrant (contact) for the domain.
	RegistrantId pulumi.IntPtrInput
	// The state of the domain.
	State pulumi.StringPtrInput
	// The domain name in Unicode format.
	UnicodeName pulumi.StringPtrInput
}

func (DomainState) ElementType() reflect.Type {
	return reflect.TypeOf((*domainState)(nil)).Elem()
}

type domainArgs struct {
	// The domain name to be created
	//
	// # Attributes Reference
	Name string `pulumi:"name"`
}

// The set of arguments for constructing a Domain resource.
type DomainArgs struct {
	// The domain name to be created
	//
	// # Attributes Reference
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

// The account ID for the domain.
func (o DomainOutput) AccountId() pulumi.IntOutput {
	return o.ApplyT(func(v *Domain) pulumi.IntOutput { return v.AccountId }).(pulumi.IntOutput)
}

// Whether the domain is set to auto-renew.
func (o DomainOutput) AutoRenew() pulumi.BoolOutput {
	return o.ApplyT(func(v *Domain) pulumi.BoolOutput { return v.AutoRenew }).(pulumi.BoolOutput)
}

// The domain name to be created
//
// # Attributes Reference
func (o DomainOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Whether the domain has WhoIs privacy enabled.
func (o DomainOutput) PrivateWhois() pulumi.BoolOutput {
	return o.ApplyT(func(v *Domain) pulumi.BoolOutput { return v.PrivateWhois }).(pulumi.BoolOutput)
}

// The ID of the registrant (contact) for the domain.
func (o DomainOutput) RegistrantId() pulumi.IntOutput {
	return o.ApplyT(func(v *Domain) pulumi.IntOutput { return v.RegistrantId }).(pulumi.IntOutput)
}

// The state of the domain.
func (o DomainOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

// The domain name in Unicode format.
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
