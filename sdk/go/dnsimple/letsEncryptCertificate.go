// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dnsimple

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-dnsimple/sdk/v4/go/dnsimple/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a DNSimple Let's Encrypt certificate resource.
//
// ## Example Usage
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
//			_, err := dnsimple.NewLetsEncryptCertificate(ctx, "foobar", &dnsimple.LetsEncryptCertificateArgs{
//				DomainId:  pulumi.Any(dnsimple.DomainId),
//				AutoRenew: pulumi.Bool(false),
//				Name:      pulumi.String("www"),
//				AlternateNames: pulumi.StringArray{
//					pulumi.String("docs.example.com"),
//					pulumi.String("status.example.com"),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
type LetsEncryptCertificate struct {
	pulumi.CustomResourceState

	// The certificate alternate names
	AlternateNames pulumi.StringArrayOutput `pulumi:"alternateNames"`
	// The identifying certification authority (CA)
	AuthorityIdentifier pulumi.StringOutput `pulumi:"authorityIdentifier"`
	// True if the certificate should auto-renew
	AutoRenew pulumi.BoolOutput `pulumi:"autoRenew"`
	// The datetime the certificate was created
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The certificate signing request
	Csr pulumi.StringOutput `pulumi:"csr"`
	// The domain to be issued the certificate for
	DomainId pulumi.StringOutput `pulumi:"domainId"`
	// The datetime the certificate will expire
	ExpiresAt pulumi.StringOutput `pulumi:"expiresAt"`
	// The certificate name; use `""` for the root domain. Wildcard names are supported.
	Name pulumi.StringOutput `pulumi:"name"`
	// The signature algorithm to use for the certificate
	SignatureAlgorithm pulumi.StringPtrOutput `pulumi:"signatureAlgorithm"`
	// The state of the certificate
	State pulumi.StringOutput `pulumi:"state"`
	// The datetime the certificate was last updated
	UpdatedAt pulumi.StringOutput `pulumi:"updatedAt"`
	// The years the certificate will last
	Years pulumi.IntOutput `pulumi:"years"`
}

// NewLetsEncryptCertificate registers a new resource with the given unique name, arguments, and options.
func NewLetsEncryptCertificate(ctx *pulumi.Context,
	name string, args *LetsEncryptCertificateArgs, opts ...pulumi.ResourceOption) (*LetsEncryptCertificate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AutoRenew == nil {
		return nil, errors.New("invalid value for required argument 'AutoRenew'")
	}
	if args.DomainId == nil {
		return nil, errors.New("invalid value for required argument 'DomainId'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource LetsEncryptCertificate
	err := ctx.RegisterResource("dnsimple:index/letsEncryptCertificate:LetsEncryptCertificate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLetsEncryptCertificate gets an existing LetsEncryptCertificate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLetsEncryptCertificate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LetsEncryptCertificateState, opts ...pulumi.ResourceOption) (*LetsEncryptCertificate, error) {
	var resource LetsEncryptCertificate
	err := ctx.ReadResource("dnsimple:index/letsEncryptCertificate:LetsEncryptCertificate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LetsEncryptCertificate resources.
type letsEncryptCertificateState struct {
	// The certificate alternate names
	AlternateNames []string `pulumi:"alternateNames"`
	// The identifying certification authority (CA)
	AuthorityIdentifier *string `pulumi:"authorityIdentifier"`
	// True if the certificate should auto-renew
	AutoRenew *bool `pulumi:"autoRenew"`
	// The datetime the certificate was created
	CreatedAt *string `pulumi:"createdAt"`
	// The certificate signing request
	Csr *string `pulumi:"csr"`
	// The domain to be issued the certificate for
	DomainId *string `pulumi:"domainId"`
	// The datetime the certificate will expire
	ExpiresAt *string `pulumi:"expiresAt"`
	// The certificate name; use `""` for the root domain. Wildcard names are supported.
	Name *string `pulumi:"name"`
	// The signature algorithm to use for the certificate
	SignatureAlgorithm *string `pulumi:"signatureAlgorithm"`
	// The state of the certificate
	State *string `pulumi:"state"`
	// The datetime the certificate was last updated
	UpdatedAt *string `pulumi:"updatedAt"`
	// The years the certificate will last
	Years *int `pulumi:"years"`
}

type LetsEncryptCertificateState struct {
	// The certificate alternate names
	AlternateNames pulumi.StringArrayInput
	// The identifying certification authority (CA)
	AuthorityIdentifier pulumi.StringPtrInput
	// True if the certificate should auto-renew
	AutoRenew pulumi.BoolPtrInput
	// The datetime the certificate was created
	CreatedAt pulumi.StringPtrInput
	// The certificate signing request
	Csr pulumi.StringPtrInput
	// The domain to be issued the certificate for
	DomainId pulumi.StringPtrInput
	// The datetime the certificate will expire
	ExpiresAt pulumi.StringPtrInput
	// The certificate name; use `""` for the root domain. Wildcard names are supported.
	Name pulumi.StringPtrInput
	// The signature algorithm to use for the certificate
	SignatureAlgorithm pulumi.StringPtrInput
	// The state of the certificate
	State pulumi.StringPtrInput
	// The datetime the certificate was last updated
	UpdatedAt pulumi.StringPtrInput
	// The years the certificate will last
	Years pulumi.IntPtrInput
}

func (LetsEncryptCertificateState) ElementType() reflect.Type {
	return reflect.TypeOf((*letsEncryptCertificateState)(nil)).Elem()
}

type letsEncryptCertificateArgs struct {
	// The certificate alternate names
	AlternateNames []string `pulumi:"alternateNames"`
	// True if the certificate should auto-renew
	AutoRenew bool `pulumi:"autoRenew"`
	// The domain to be issued the certificate for
	DomainId string `pulumi:"domainId"`
	// The certificate name; use `""` for the root domain. Wildcard names are supported.
	Name string `pulumi:"name"`
	// The signature algorithm to use for the certificate
	SignatureAlgorithm *string `pulumi:"signatureAlgorithm"`
}

// The set of arguments for constructing a LetsEncryptCertificate resource.
type LetsEncryptCertificateArgs struct {
	// The certificate alternate names
	AlternateNames pulumi.StringArrayInput
	// True if the certificate should auto-renew
	AutoRenew pulumi.BoolInput
	// The domain to be issued the certificate for
	DomainId pulumi.StringInput
	// The certificate name; use `""` for the root domain. Wildcard names are supported.
	Name pulumi.StringInput
	// The signature algorithm to use for the certificate
	SignatureAlgorithm pulumi.StringPtrInput
}

func (LetsEncryptCertificateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*letsEncryptCertificateArgs)(nil)).Elem()
}

type LetsEncryptCertificateInput interface {
	pulumi.Input

	ToLetsEncryptCertificateOutput() LetsEncryptCertificateOutput
	ToLetsEncryptCertificateOutputWithContext(ctx context.Context) LetsEncryptCertificateOutput
}

func (*LetsEncryptCertificate) ElementType() reflect.Type {
	return reflect.TypeOf((**LetsEncryptCertificate)(nil)).Elem()
}

func (i *LetsEncryptCertificate) ToLetsEncryptCertificateOutput() LetsEncryptCertificateOutput {
	return i.ToLetsEncryptCertificateOutputWithContext(context.Background())
}

func (i *LetsEncryptCertificate) ToLetsEncryptCertificateOutputWithContext(ctx context.Context) LetsEncryptCertificateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LetsEncryptCertificateOutput)
}

// LetsEncryptCertificateArrayInput is an input type that accepts LetsEncryptCertificateArray and LetsEncryptCertificateArrayOutput values.
// You can construct a concrete instance of `LetsEncryptCertificateArrayInput` via:
//
//	LetsEncryptCertificateArray{ LetsEncryptCertificateArgs{...} }
type LetsEncryptCertificateArrayInput interface {
	pulumi.Input

	ToLetsEncryptCertificateArrayOutput() LetsEncryptCertificateArrayOutput
	ToLetsEncryptCertificateArrayOutputWithContext(context.Context) LetsEncryptCertificateArrayOutput
}

type LetsEncryptCertificateArray []LetsEncryptCertificateInput

func (LetsEncryptCertificateArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*LetsEncryptCertificate)(nil)).Elem()
}

func (i LetsEncryptCertificateArray) ToLetsEncryptCertificateArrayOutput() LetsEncryptCertificateArrayOutput {
	return i.ToLetsEncryptCertificateArrayOutputWithContext(context.Background())
}

func (i LetsEncryptCertificateArray) ToLetsEncryptCertificateArrayOutputWithContext(ctx context.Context) LetsEncryptCertificateArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LetsEncryptCertificateArrayOutput)
}

// LetsEncryptCertificateMapInput is an input type that accepts LetsEncryptCertificateMap and LetsEncryptCertificateMapOutput values.
// You can construct a concrete instance of `LetsEncryptCertificateMapInput` via:
//
//	LetsEncryptCertificateMap{ "key": LetsEncryptCertificateArgs{...} }
type LetsEncryptCertificateMapInput interface {
	pulumi.Input

	ToLetsEncryptCertificateMapOutput() LetsEncryptCertificateMapOutput
	ToLetsEncryptCertificateMapOutputWithContext(context.Context) LetsEncryptCertificateMapOutput
}

type LetsEncryptCertificateMap map[string]LetsEncryptCertificateInput

func (LetsEncryptCertificateMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*LetsEncryptCertificate)(nil)).Elem()
}

func (i LetsEncryptCertificateMap) ToLetsEncryptCertificateMapOutput() LetsEncryptCertificateMapOutput {
	return i.ToLetsEncryptCertificateMapOutputWithContext(context.Background())
}

func (i LetsEncryptCertificateMap) ToLetsEncryptCertificateMapOutputWithContext(ctx context.Context) LetsEncryptCertificateMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LetsEncryptCertificateMapOutput)
}

type LetsEncryptCertificateOutput struct{ *pulumi.OutputState }

func (LetsEncryptCertificateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**LetsEncryptCertificate)(nil)).Elem()
}

func (o LetsEncryptCertificateOutput) ToLetsEncryptCertificateOutput() LetsEncryptCertificateOutput {
	return o
}

func (o LetsEncryptCertificateOutput) ToLetsEncryptCertificateOutputWithContext(ctx context.Context) LetsEncryptCertificateOutput {
	return o
}

// The certificate alternate names
func (o LetsEncryptCertificateOutput) AlternateNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *LetsEncryptCertificate) pulumi.StringArrayOutput { return v.AlternateNames }).(pulumi.StringArrayOutput)
}

// The identifying certification authority (CA)
func (o LetsEncryptCertificateOutput) AuthorityIdentifier() pulumi.StringOutput {
	return o.ApplyT(func(v *LetsEncryptCertificate) pulumi.StringOutput { return v.AuthorityIdentifier }).(pulumi.StringOutput)
}

// True if the certificate should auto-renew
func (o LetsEncryptCertificateOutput) AutoRenew() pulumi.BoolOutput {
	return o.ApplyT(func(v *LetsEncryptCertificate) pulumi.BoolOutput { return v.AutoRenew }).(pulumi.BoolOutput)
}

// The datetime the certificate was created
func (o LetsEncryptCertificateOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *LetsEncryptCertificate) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// The certificate signing request
func (o LetsEncryptCertificateOutput) Csr() pulumi.StringOutput {
	return o.ApplyT(func(v *LetsEncryptCertificate) pulumi.StringOutput { return v.Csr }).(pulumi.StringOutput)
}

// The domain to be issued the certificate for
func (o LetsEncryptCertificateOutput) DomainId() pulumi.StringOutput {
	return o.ApplyT(func(v *LetsEncryptCertificate) pulumi.StringOutput { return v.DomainId }).(pulumi.StringOutput)
}

// The datetime the certificate will expire
func (o LetsEncryptCertificateOutput) ExpiresAt() pulumi.StringOutput {
	return o.ApplyT(func(v *LetsEncryptCertificate) pulumi.StringOutput { return v.ExpiresAt }).(pulumi.StringOutput)
}

// The certificate name; use `""` for the root domain. Wildcard names are supported.
func (o LetsEncryptCertificateOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *LetsEncryptCertificate) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The signature algorithm to use for the certificate
func (o LetsEncryptCertificateOutput) SignatureAlgorithm() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LetsEncryptCertificate) pulumi.StringPtrOutput { return v.SignatureAlgorithm }).(pulumi.StringPtrOutput)
}

// The state of the certificate
func (o LetsEncryptCertificateOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *LetsEncryptCertificate) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

// The datetime the certificate was last updated
func (o LetsEncryptCertificateOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *LetsEncryptCertificate) pulumi.StringOutput { return v.UpdatedAt }).(pulumi.StringOutput)
}

// The years the certificate will last
func (o LetsEncryptCertificateOutput) Years() pulumi.IntOutput {
	return o.ApplyT(func(v *LetsEncryptCertificate) pulumi.IntOutput { return v.Years }).(pulumi.IntOutput)
}

type LetsEncryptCertificateArrayOutput struct{ *pulumi.OutputState }

func (LetsEncryptCertificateArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*LetsEncryptCertificate)(nil)).Elem()
}

func (o LetsEncryptCertificateArrayOutput) ToLetsEncryptCertificateArrayOutput() LetsEncryptCertificateArrayOutput {
	return o
}

func (o LetsEncryptCertificateArrayOutput) ToLetsEncryptCertificateArrayOutputWithContext(ctx context.Context) LetsEncryptCertificateArrayOutput {
	return o
}

func (o LetsEncryptCertificateArrayOutput) Index(i pulumi.IntInput) LetsEncryptCertificateOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *LetsEncryptCertificate {
		return vs[0].([]*LetsEncryptCertificate)[vs[1].(int)]
	}).(LetsEncryptCertificateOutput)
}

type LetsEncryptCertificateMapOutput struct{ *pulumi.OutputState }

func (LetsEncryptCertificateMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*LetsEncryptCertificate)(nil)).Elem()
}

func (o LetsEncryptCertificateMapOutput) ToLetsEncryptCertificateMapOutput() LetsEncryptCertificateMapOutput {
	return o
}

func (o LetsEncryptCertificateMapOutput) ToLetsEncryptCertificateMapOutputWithContext(ctx context.Context) LetsEncryptCertificateMapOutput {
	return o
}

func (o LetsEncryptCertificateMapOutput) MapIndex(k pulumi.StringInput) LetsEncryptCertificateOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *LetsEncryptCertificate {
		return vs[0].(map[string]*LetsEncryptCertificate)[vs[1].(string)]
	}).(LetsEncryptCertificateOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LetsEncryptCertificateInput)(nil)).Elem(), &LetsEncryptCertificate{})
	pulumi.RegisterInputType(reflect.TypeOf((*LetsEncryptCertificateArrayInput)(nil)).Elem(), LetsEncryptCertificateArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*LetsEncryptCertificateMapInput)(nil)).Elem(), LetsEncryptCertificateMap{})
	pulumi.RegisterOutputType(LetsEncryptCertificateOutput{})
	pulumi.RegisterOutputType(LetsEncryptCertificateArrayOutput{})
	pulumi.RegisterOutputType(LetsEncryptCertificateMapOutput{})
}
