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

// Provides a DNSimple domain delegation signer record resource.
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
//			_, err := dnsimple.NewDsRecord(ctx, "foobar", &dnsimple.DsRecordArgs{
//				Domain:     pulumi.Any(dnsimple.Domain),
//				Algorithm:  pulumi.String("8"),
//				Digest:     pulumi.String("6CEEA0117A02480216EBF745A7B690F938860074E4AD11AF2AC573007205682B"),
//				DigestType: pulumi.String("2"),
//				KeyTag:     pulumi.String("12345"),
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
// DNSimple DS record resources can be imported using their domain ID and numeric record ID.
//
// bash
//
// ```sh
// $ pulumi import dnsimple:index/dsRecord:DsRecord resource_name example.com_5678
// ```
//
// The record ID can be found within [DNSimple DNSSEC API](https://developer.dnsimple.com/v2/domains/dnssec/#listDomainDelegationSignerRecords). Check out [Authentication](https://developer.dnsimple.com/v2/#authentication) in API Overview for available options.
//
// bash
//
// curl -u 'EMAIL:PASSWORD' https://api.dnsimple.com/v2/1010/domains/example.com/ds_records | jq
//
// {
//
//	"data": [
//
//	  {
//
//	    "id": 24,
//
//	    "domain_id": 1010,
//
//	    "algorithm": "8",
//
//	    "digest": "C1F6E04A5A61FBF65BF9DC8294C363CF11C89E802D926BDAB79C55D27BEFA94F",
//
//	    "digest_type": "2",
//
//	    "keytag": "44620",
//
//	    "public_key": null,
//
//	    "created_at": "2017-03-03T13:49:58Z",
//
//	    "updated_at": "2017-03-03T13:49:58Z"
//
//	  }
//
//	],
//
//	"pagination": {
//
//	  "current_page": 1,
//
//	  "per_page": 30,
//
//	  "total_entries": 1,
//
//	  "total_pages": 1
//
//	}
//
// }
type DsRecord struct {
	pulumi.CustomResourceState

	// DNSSEC algorithm number as a string.
	Algorithm pulumi.StringOutput `pulumi:"algorithm"`
	// The time the DS record was created at.
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The hexidecimal representation of the digest of the corresponding DNSKEY record.
	Digest pulumi.StringPtrOutput `pulumi:"digest"`
	// DNSSEC digest type number as a string.
	DigestType pulumi.StringPtrOutput `pulumi:"digestType"`
	// The domain name or numeric ID to create the delegation signer record for.
	Domain pulumi.StringOutput `pulumi:"domain"`
	// A keytag that references the corresponding DNSKEY record.
	Keytag pulumi.StringPtrOutput `pulumi:"keytag"`
	// A public key that references the corresponding DNSKEY record.
	//
	// # Attributes Reference
	PublicKey pulumi.StringPtrOutput `pulumi:"publicKey"`
	// The time the DS record was last updated at.
	UpdatedAt pulumi.StringOutput `pulumi:"updatedAt"`
}

// NewDsRecord registers a new resource with the given unique name, arguments, and options.
func NewDsRecord(ctx *pulumi.Context,
	name string, args *DsRecordArgs, opts ...pulumi.ResourceOption) (*DsRecord, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Algorithm == nil {
		return nil, errors.New("invalid value for required argument 'Algorithm'")
	}
	if args.Domain == nil {
		return nil, errors.New("invalid value for required argument 'Domain'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DsRecord
	err := ctx.RegisterResource("dnsimple:index/dsRecord:DsRecord", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDsRecord gets an existing DsRecord resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDsRecord(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DsRecordState, opts ...pulumi.ResourceOption) (*DsRecord, error) {
	var resource DsRecord
	err := ctx.ReadResource("dnsimple:index/dsRecord:DsRecord", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DsRecord resources.
type dsRecordState struct {
	// DNSSEC algorithm number as a string.
	Algorithm *string `pulumi:"algorithm"`
	// The time the DS record was created at.
	CreatedAt *string `pulumi:"createdAt"`
	// The hexidecimal representation of the digest of the corresponding DNSKEY record.
	Digest *string `pulumi:"digest"`
	// DNSSEC digest type number as a string.
	DigestType *string `pulumi:"digestType"`
	// The domain name or numeric ID to create the delegation signer record for.
	Domain *string `pulumi:"domain"`
	// A keytag that references the corresponding DNSKEY record.
	Keytag *string `pulumi:"keytag"`
	// A public key that references the corresponding DNSKEY record.
	//
	// # Attributes Reference
	PublicKey *string `pulumi:"publicKey"`
	// The time the DS record was last updated at.
	UpdatedAt *string `pulumi:"updatedAt"`
}

type DsRecordState struct {
	// DNSSEC algorithm number as a string.
	Algorithm pulumi.StringPtrInput
	// The time the DS record was created at.
	CreatedAt pulumi.StringPtrInput
	// The hexidecimal representation of the digest of the corresponding DNSKEY record.
	Digest pulumi.StringPtrInput
	// DNSSEC digest type number as a string.
	DigestType pulumi.StringPtrInput
	// The domain name or numeric ID to create the delegation signer record for.
	Domain pulumi.StringPtrInput
	// A keytag that references the corresponding DNSKEY record.
	Keytag pulumi.StringPtrInput
	// A public key that references the corresponding DNSKEY record.
	//
	// # Attributes Reference
	PublicKey pulumi.StringPtrInput
	// The time the DS record was last updated at.
	UpdatedAt pulumi.StringPtrInput
}

func (DsRecordState) ElementType() reflect.Type {
	return reflect.TypeOf((*dsRecordState)(nil)).Elem()
}

type dsRecordArgs struct {
	// DNSSEC algorithm number as a string.
	Algorithm string `pulumi:"algorithm"`
	// The hexidecimal representation of the digest of the corresponding DNSKEY record.
	Digest *string `pulumi:"digest"`
	// DNSSEC digest type number as a string.
	DigestType *string `pulumi:"digestType"`
	// The domain name or numeric ID to create the delegation signer record for.
	Domain string `pulumi:"domain"`
	// A keytag that references the corresponding DNSKEY record.
	Keytag *string `pulumi:"keytag"`
	// A public key that references the corresponding DNSKEY record.
	//
	// # Attributes Reference
	PublicKey *string `pulumi:"publicKey"`
}

// The set of arguments for constructing a DsRecord resource.
type DsRecordArgs struct {
	// DNSSEC algorithm number as a string.
	Algorithm pulumi.StringInput
	// The hexidecimal representation of the digest of the corresponding DNSKEY record.
	Digest pulumi.StringPtrInput
	// DNSSEC digest type number as a string.
	DigestType pulumi.StringPtrInput
	// The domain name or numeric ID to create the delegation signer record for.
	Domain pulumi.StringInput
	// A keytag that references the corresponding DNSKEY record.
	Keytag pulumi.StringPtrInput
	// A public key that references the corresponding DNSKEY record.
	//
	// # Attributes Reference
	PublicKey pulumi.StringPtrInput
}

func (DsRecordArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dsRecordArgs)(nil)).Elem()
}

type DsRecordInput interface {
	pulumi.Input

	ToDsRecordOutput() DsRecordOutput
	ToDsRecordOutputWithContext(ctx context.Context) DsRecordOutput
}

func (*DsRecord) ElementType() reflect.Type {
	return reflect.TypeOf((**DsRecord)(nil)).Elem()
}

func (i *DsRecord) ToDsRecordOutput() DsRecordOutput {
	return i.ToDsRecordOutputWithContext(context.Background())
}

func (i *DsRecord) ToDsRecordOutputWithContext(ctx context.Context) DsRecordOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DsRecordOutput)
}

// DsRecordArrayInput is an input type that accepts DsRecordArray and DsRecordArrayOutput values.
// You can construct a concrete instance of `DsRecordArrayInput` via:
//
//	DsRecordArray{ DsRecordArgs{...} }
type DsRecordArrayInput interface {
	pulumi.Input

	ToDsRecordArrayOutput() DsRecordArrayOutput
	ToDsRecordArrayOutputWithContext(context.Context) DsRecordArrayOutput
}

type DsRecordArray []DsRecordInput

func (DsRecordArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DsRecord)(nil)).Elem()
}

func (i DsRecordArray) ToDsRecordArrayOutput() DsRecordArrayOutput {
	return i.ToDsRecordArrayOutputWithContext(context.Background())
}

func (i DsRecordArray) ToDsRecordArrayOutputWithContext(ctx context.Context) DsRecordArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DsRecordArrayOutput)
}

// DsRecordMapInput is an input type that accepts DsRecordMap and DsRecordMapOutput values.
// You can construct a concrete instance of `DsRecordMapInput` via:
//
//	DsRecordMap{ "key": DsRecordArgs{...} }
type DsRecordMapInput interface {
	pulumi.Input

	ToDsRecordMapOutput() DsRecordMapOutput
	ToDsRecordMapOutputWithContext(context.Context) DsRecordMapOutput
}

type DsRecordMap map[string]DsRecordInput

func (DsRecordMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DsRecord)(nil)).Elem()
}

func (i DsRecordMap) ToDsRecordMapOutput() DsRecordMapOutput {
	return i.ToDsRecordMapOutputWithContext(context.Background())
}

func (i DsRecordMap) ToDsRecordMapOutputWithContext(ctx context.Context) DsRecordMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DsRecordMapOutput)
}

type DsRecordOutput struct{ *pulumi.OutputState }

func (DsRecordOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DsRecord)(nil)).Elem()
}

func (o DsRecordOutput) ToDsRecordOutput() DsRecordOutput {
	return o
}

func (o DsRecordOutput) ToDsRecordOutputWithContext(ctx context.Context) DsRecordOutput {
	return o
}

// DNSSEC algorithm number as a string.
func (o DsRecordOutput) Algorithm() pulumi.StringOutput {
	return o.ApplyT(func(v *DsRecord) pulumi.StringOutput { return v.Algorithm }).(pulumi.StringOutput)
}

// The time the DS record was created at.
func (o DsRecordOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *DsRecord) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// The hexidecimal representation of the digest of the corresponding DNSKEY record.
func (o DsRecordOutput) Digest() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DsRecord) pulumi.StringPtrOutput { return v.Digest }).(pulumi.StringPtrOutput)
}

// DNSSEC digest type number as a string.
func (o DsRecordOutput) DigestType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DsRecord) pulumi.StringPtrOutput { return v.DigestType }).(pulumi.StringPtrOutput)
}

// The domain name or numeric ID to create the delegation signer record for.
func (o DsRecordOutput) Domain() pulumi.StringOutput {
	return o.ApplyT(func(v *DsRecord) pulumi.StringOutput { return v.Domain }).(pulumi.StringOutput)
}

// A keytag that references the corresponding DNSKEY record.
func (o DsRecordOutput) Keytag() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DsRecord) pulumi.StringPtrOutput { return v.Keytag }).(pulumi.StringPtrOutput)
}

// A public key that references the corresponding DNSKEY record.
//
// # Attributes Reference
func (o DsRecordOutput) PublicKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DsRecord) pulumi.StringPtrOutput { return v.PublicKey }).(pulumi.StringPtrOutput)
}

// The time the DS record was last updated at.
func (o DsRecordOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *DsRecord) pulumi.StringOutput { return v.UpdatedAt }).(pulumi.StringOutput)
}

type DsRecordArrayOutput struct{ *pulumi.OutputState }

func (DsRecordArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DsRecord)(nil)).Elem()
}

func (o DsRecordArrayOutput) ToDsRecordArrayOutput() DsRecordArrayOutput {
	return o
}

func (o DsRecordArrayOutput) ToDsRecordArrayOutputWithContext(ctx context.Context) DsRecordArrayOutput {
	return o
}

func (o DsRecordArrayOutput) Index(i pulumi.IntInput) DsRecordOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *DsRecord {
		return vs[0].([]*DsRecord)[vs[1].(int)]
	}).(DsRecordOutput)
}

type DsRecordMapOutput struct{ *pulumi.OutputState }

func (DsRecordMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DsRecord)(nil)).Elem()
}

func (o DsRecordMapOutput) ToDsRecordMapOutput() DsRecordMapOutput {
	return o
}

func (o DsRecordMapOutput) ToDsRecordMapOutputWithContext(ctx context.Context) DsRecordMapOutput {
	return o
}

func (o DsRecordMapOutput) MapIndex(k pulumi.StringInput) DsRecordOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *DsRecord {
		return vs[0].(map[string]*DsRecord)[vs[1].(string)]
	}).(DsRecordOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DsRecordInput)(nil)).Elem(), &DsRecord{})
	pulumi.RegisterInputType(reflect.TypeOf((*DsRecordArrayInput)(nil)).Elem(), DsRecordArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DsRecordMapInput)(nil)).Elem(), DsRecordMap{})
	pulumi.RegisterOutputType(DsRecordOutput{})
	pulumi.RegisterOutputType(DsRecordArrayOutput{})
	pulumi.RegisterOutputType(DsRecordMapOutput{})
}
