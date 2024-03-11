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

// Provides a DNSimple zone record resource.
//
// ## Deprecation warning
//
// You can still use the _deprecated_ `Record` configuration, but be aware that it will be removed in the
// upcoming 1.0.0 release.
//
// ## Example Usage
//
// <!--Start PulumiCodeChooser -->
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
//			// Add a record to the root domain
//			_, err := dnsimple.NewZoneRecord(ctx, "foobar", &dnsimple.ZoneRecordArgs{
//				Name:     pulumi.String(""),
//				Ttl:      pulumi.String("3600"),
//				Type:     pulumi.String("A"),
//				Value:    pulumi.String("192.168.0.11"),
//				ZoneName: pulumi.Any(_var.Dnsimple_domain),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
//
// <!--Start PulumiCodeChooser -->
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
//			// Add a record to a sub-domain
//			_, err := dnsimple.NewZoneRecord(ctx, "foobar", &dnsimple.ZoneRecordArgs{
//				Name:     pulumi.String("terraform"),
//				Ttl:      pulumi.String("3600"),
//				Type:     pulumi.String("A"),
//				Value:    pulumi.String("192.168.0.11"),
//				ZoneName: pulumi.Any(_var.Dnsimple_domain),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
//
// ## Import
//
// DNSimple resources can be imported using their parent zone name (domain name) and numeric record ID.
//
// __Importing record example.com with record ID 1234__
//
// ```sh
// $ pulumi import dnsimple:index/zoneRecord:ZoneRecord resource_name example.com_1234
// ```
// __Importing record www.example.com with record ID 1234__
//
// ```sh
// $ pulumi import dnsimple:index/zoneRecord:ZoneRecord resource_name example.com_1234
// ```
// The record ID can be found in the URL when editing a record on the DNSimple web dashboard.
type ZoneRecord struct {
	pulumi.CustomResourceState

	// The name of the record
	Name pulumi.StringOutput `pulumi:"name"`
	// The priority of the record - only useful for some record types
	Priority pulumi.StringOutput `pulumi:"priority"`
	// The FQDN of the record
	QualifiedName pulumi.StringOutput `pulumi:"qualifiedName"`
	// The TTL of the record
	Ttl pulumi.StringPtrOutput `pulumi:"ttl"`
	// The type of the record
	Type pulumi.StringOutput `pulumi:"type"`
	// The value of the record
	Value pulumi.StringOutput `pulumi:"value"`
	// The domain ID of the record
	ZoneId pulumi.StringOutput `pulumi:"zoneId"`
	// The domain to add the record to
	ZoneName pulumi.StringOutput `pulumi:"zoneName"`
}

// NewZoneRecord registers a new resource with the given unique name, arguments, and options.
func NewZoneRecord(ctx *pulumi.Context,
	name string, args *ZoneRecordArgs, opts ...pulumi.ResourceOption) (*ZoneRecord, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	if args.Value == nil {
		return nil, errors.New("invalid value for required argument 'Value'")
	}
	if args.ZoneName == nil {
		return nil, errors.New("invalid value for required argument 'ZoneName'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ZoneRecord
	err := ctx.RegisterResource("dnsimple:index/zoneRecord:ZoneRecord", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetZoneRecord gets an existing ZoneRecord resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetZoneRecord(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ZoneRecordState, opts ...pulumi.ResourceOption) (*ZoneRecord, error) {
	var resource ZoneRecord
	err := ctx.ReadResource("dnsimple:index/zoneRecord:ZoneRecord", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ZoneRecord resources.
type zoneRecordState struct {
	// The name of the record
	Name *string `pulumi:"name"`
	// The priority of the record - only useful for some record types
	Priority *string `pulumi:"priority"`
	// The FQDN of the record
	QualifiedName *string `pulumi:"qualifiedName"`
	// The TTL of the record
	Ttl *string `pulumi:"ttl"`
	// The type of the record
	Type *string `pulumi:"type"`
	// The value of the record
	Value *string `pulumi:"value"`
	// The domain ID of the record
	ZoneId *string `pulumi:"zoneId"`
	// The domain to add the record to
	ZoneName *string `pulumi:"zoneName"`
}

type ZoneRecordState struct {
	// The name of the record
	Name pulumi.StringPtrInput
	// The priority of the record - only useful for some record types
	Priority pulumi.StringPtrInput
	// The FQDN of the record
	QualifiedName pulumi.StringPtrInput
	// The TTL of the record
	Ttl pulumi.StringPtrInput
	// The type of the record
	Type pulumi.StringPtrInput
	// The value of the record
	Value pulumi.StringPtrInput
	// The domain ID of the record
	ZoneId pulumi.StringPtrInput
	// The domain to add the record to
	ZoneName pulumi.StringPtrInput
}

func (ZoneRecordState) ElementType() reflect.Type {
	return reflect.TypeOf((*zoneRecordState)(nil)).Elem()
}

type zoneRecordArgs struct {
	// The name of the record
	Name string `pulumi:"name"`
	// The priority of the record - only useful for some record types
	Priority *string `pulumi:"priority"`
	// The TTL of the record
	Ttl *string `pulumi:"ttl"`
	// The type of the record
	Type string `pulumi:"type"`
	// The value of the record
	Value string `pulumi:"value"`
	// The domain to add the record to
	ZoneName string `pulumi:"zoneName"`
}

// The set of arguments for constructing a ZoneRecord resource.
type ZoneRecordArgs struct {
	// The name of the record
	Name pulumi.StringInput
	// The priority of the record - only useful for some record types
	Priority pulumi.StringPtrInput
	// The TTL of the record
	Ttl pulumi.StringPtrInput
	// The type of the record
	Type pulumi.StringInput
	// The value of the record
	Value pulumi.StringInput
	// The domain to add the record to
	ZoneName pulumi.StringInput
}

func (ZoneRecordArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*zoneRecordArgs)(nil)).Elem()
}

type ZoneRecordInput interface {
	pulumi.Input

	ToZoneRecordOutput() ZoneRecordOutput
	ToZoneRecordOutputWithContext(ctx context.Context) ZoneRecordOutput
}

func (*ZoneRecord) ElementType() reflect.Type {
	return reflect.TypeOf((**ZoneRecord)(nil)).Elem()
}

func (i *ZoneRecord) ToZoneRecordOutput() ZoneRecordOutput {
	return i.ToZoneRecordOutputWithContext(context.Background())
}

func (i *ZoneRecord) ToZoneRecordOutputWithContext(ctx context.Context) ZoneRecordOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZoneRecordOutput)
}

// ZoneRecordArrayInput is an input type that accepts ZoneRecordArray and ZoneRecordArrayOutput values.
// You can construct a concrete instance of `ZoneRecordArrayInput` via:
//
//	ZoneRecordArray{ ZoneRecordArgs{...} }
type ZoneRecordArrayInput interface {
	pulumi.Input

	ToZoneRecordArrayOutput() ZoneRecordArrayOutput
	ToZoneRecordArrayOutputWithContext(context.Context) ZoneRecordArrayOutput
}

type ZoneRecordArray []ZoneRecordInput

func (ZoneRecordArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ZoneRecord)(nil)).Elem()
}

func (i ZoneRecordArray) ToZoneRecordArrayOutput() ZoneRecordArrayOutput {
	return i.ToZoneRecordArrayOutputWithContext(context.Background())
}

func (i ZoneRecordArray) ToZoneRecordArrayOutputWithContext(ctx context.Context) ZoneRecordArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZoneRecordArrayOutput)
}

// ZoneRecordMapInput is an input type that accepts ZoneRecordMap and ZoneRecordMapOutput values.
// You can construct a concrete instance of `ZoneRecordMapInput` via:
//
//	ZoneRecordMap{ "key": ZoneRecordArgs{...} }
type ZoneRecordMapInput interface {
	pulumi.Input

	ToZoneRecordMapOutput() ZoneRecordMapOutput
	ToZoneRecordMapOutputWithContext(context.Context) ZoneRecordMapOutput
}

type ZoneRecordMap map[string]ZoneRecordInput

func (ZoneRecordMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ZoneRecord)(nil)).Elem()
}

func (i ZoneRecordMap) ToZoneRecordMapOutput() ZoneRecordMapOutput {
	return i.ToZoneRecordMapOutputWithContext(context.Background())
}

func (i ZoneRecordMap) ToZoneRecordMapOutputWithContext(ctx context.Context) ZoneRecordMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZoneRecordMapOutput)
}

type ZoneRecordOutput struct{ *pulumi.OutputState }

func (ZoneRecordOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ZoneRecord)(nil)).Elem()
}

func (o ZoneRecordOutput) ToZoneRecordOutput() ZoneRecordOutput {
	return o
}

func (o ZoneRecordOutput) ToZoneRecordOutputWithContext(ctx context.Context) ZoneRecordOutput {
	return o
}

// The name of the record
func (o ZoneRecordOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ZoneRecord) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The priority of the record - only useful for some record types
func (o ZoneRecordOutput) Priority() pulumi.StringOutput {
	return o.ApplyT(func(v *ZoneRecord) pulumi.StringOutput { return v.Priority }).(pulumi.StringOutput)
}

// The FQDN of the record
func (o ZoneRecordOutput) QualifiedName() pulumi.StringOutput {
	return o.ApplyT(func(v *ZoneRecord) pulumi.StringOutput { return v.QualifiedName }).(pulumi.StringOutput)
}

// The TTL of the record
func (o ZoneRecordOutput) Ttl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZoneRecord) pulumi.StringPtrOutput { return v.Ttl }).(pulumi.StringPtrOutput)
}

// The type of the record
func (o ZoneRecordOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *ZoneRecord) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

// The value of the record
func (o ZoneRecordOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v *ZoneRecord) pulumi.StringOutput { return v.Value }).(pulumi.StringOutput)
}

// The domain ID of the record
func (o ZoneRecordOutput) ZoneId() pulumi.StringOutput {
	return o.ApplyT(func(v *ZoneRecord) pulumi.StringOutput { return v.ZoneId }).(pulumi.StringOutput)
}

// The domain to add the record to
func (o ZoneRecordOutput) ZoneName() pulumi.StringOutput {
	return o.ApplyT(func(v *ZoneRecord) pulumi.StringOutput { return v.ZoneName }).(pulumi.StringOutput)
}

type ZoneRecordArrayOutput struct{ *pulumi.OutputState }

func (ZoneRecordArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ZoneRecord)(nil)).Elem()
}

func (o ZoneRecordArrayOutput) ToZoneRecordArrayOutput() ZoneRecordArrayOutput {
	return o
}

func (o ZoneRecordArrayOutput) ToZoneRecordArrayOutputWithContext(ctx context.Context) ZoneRecordArrayOutput {
	return o
}

func (o ZoneRecordArrayOutput) Index(i pulumi.IntInput) ZoneRecordOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ZoneRecord {
		return vs[0].([]*ZoneRecord)[vs[1].(int)]
	}).(ZoneRecordOutput)
}

type ZoneRecordMapOutput struct{ *pulumi.OutputState }

func (ZoneRecordMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ZoneRecord)(nil)).Elem()
}

func (o ZoneRecordMapOutput) ToZoneRecordMapOutput() ZoneRecordMapOutput {
	return o
}

func (o ZoneRecordMapOutput) ToZoneRecordMapOutputWithContext(ctx context.Context) ZoneRecordMapOutput {
	return o
}

func (o ZoneRecordMapOutput) MapIndex(k pulumi.StringInput) ZoneRecordOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ZoneRecord {
		return vs[0].(map[string]*ZoneRecord)[vs[1].(string)]
	}).(ZoneRecordOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ZoneRecordInput)(nil)).Elem(), &ZoneRecord{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZoneRecordArrayInput)(nil)).Elem(), ZoneRecordArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZoneRecordMapInput)(nil)).Elem(), ZoneRecordMap{})
	pulumi.RegisterOutputType(ZoneRecordOutput{})
	pulumi.RegisterOutputType(ZoneRecordArrayOutput{})
	pulumi.RegisterOutputType(ZoneRecordMapOutput{})
}
