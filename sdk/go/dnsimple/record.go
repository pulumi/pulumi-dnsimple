// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package dnsimple

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a DNSimple record resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-dnsimple/sdk/v3/go/dnsimple"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := dnsimple.NewRecord(ctx, "foobar", &dnsimple.RecordArgs{
// 			Domain: pulumi.Any(_var.Dnsimple_domain),
// 			Name:   pulumi.String(""),
// 			Ttl:    pulumi.String("3600"),
// 			Type:   pulumi.String("A"),
// 			Value:  pulumi.String("192.168.0.11"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-dnsimple/sdk/v3/go/dnsimple"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := dnsimple.NewRecord(ctx, "foobar", &dnsimple.RecordArgs{
// 			Domain: pulumi.Any(_var.Dnsimple_domain),
// 			Name:   pulumi.String("terraform"),
// 			Ttl:    pulumi.String("3600"),
// 			Type:   pulumi.String("A"),
// 			Value:  pulumi.String("192.168.0.11"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// DNSimple resources can be imported using their parent zone name (domain name) and numeric record ID. **Importing record example.com with record ID 1234**
//
// ```sh
//  $ pulumi import dnsimple:index/record:Record resource_name example.com_1234
// ```
//
//  **Importing record www.example.com with record ID 1234**
//
// ```sh
//  $ pulumi import dnsimple:index/record:Record resource_name example.com_1234
// ```
//
//  The record ID can be found in the URL when editing a record on the DNSimple web dashboard.
type Record struct {
	pulumi.CustomResourceState

	// The domain to add the record to
	Domain pulumi.StringOutput `pulumi:"domain"`
	// The domain ID of the record
	DomainId pulumi.StringOutput `pulumi:"domainId"`
	// The FQDN of the record
	Hostname pulumi.StringOutput `pulumi:"hostname"`
	// The name of the record
	Name pulumi.StringOutput `pulumi:"name"`
	// The priority of the record - only useful for some record types
	Priority pulumi.StringOutput `pulumi:"priority"`
	// The TTL of the record
	Ttl pulumi.StringPtrOutput `pulumi:"ttl"`
	// The type of the record
	Type pulumi.StringOutput `pulumi:"type"`
	// The value of the record
	Value pulumi.StringOutput `pulumi:"value"`
}

// NewRecord registers a new resource with the given unique name, arguments, and options.
func NewRecord(ctx *pulumi.Context,
	name string, args *RecordArgs, opts ...pulumi.ResourceOption) (*Record, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Domain == nil {
		return nil, errors.New("invalid value for required argument 'Domain'")
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
	var resource Record
	err := ctx.RegisterResource("dnsimple:index/record:Record", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRecord gets an existing Record resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRecord(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RecordState, opts ...pulumi.ResourceOption) (*Record, error) {
	var resource Record
	err := ctx.ReadResource("dnsimple:index/record:Record", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Record resources.
type recordState struct {
	// The domain to add the record to
	Domain *string `pulumi:"domain"`
	// The domain ID of the record
	DomainId *string `pulumi:"domainId"`
	// The FQDN of the record
	Hostname *string `pulumi:"hostname"`
	// The name of the record
	Name *string `pulumi:"name"`
	// The priority of the record - only useful for some record types
	Priority *string `pulumi:"priority"`
	// The TTL of the record
	Ttl *string `pulumi:"ttl"`
	// The type of the record
	Type *string `pulumi:"type"`
	// The value of the record
	Value *string `pulumi:"value"`
}

type RecordState struct {
	// The domain to add the record to
	Domain pulumi.StringPtrInput
	// The domain ID of the record
	DomainId pulumi.StringPtrInput
	// The FQDN of the record
	Hostname pulumi.StringPtrInput
	// The name of the record
	Name pulumi.StringPtrInput
	// The priority of the record - only useful for some record types
	Priority pulumi.StringPtrInput
	// The TTL of the record
	Ttl pulumi.StringPtrInput
	// The type of the record
	Type pulumi.StringPtrInput
	// The value of the record
	Value pulumi.StringPtrInput
}

func (RecordState) ElementType() reflect.Type {
	return reflect.TypeOf((*recordState)(nil)).Elem()
}

type recordArgs struct {
	// The domain to add the record to
	Domain string `pulumi:"domain"`
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
}

// The set of arguments for constructing a Record resource.
type RecordArgs struct {
	// The domain to add the record to
	Domain pulumi.StringInput
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
}

func (RecordArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*recordArgs)(nil)).Elem()
}

type RecordInput interface {
	pulumi.Input

	ToRecordOutput() RecordOutput
	ToRecordOutputWithContext(ctx context.Context) RecordOutput
}

func (*Record) ElementType() reflect.Type {
	return reflect.TypeOf((*Record)(nil))
}

func (i *Record) ToRecordOutput() RecordOutput {
	return i.ToRecordOutputWithContext(context.Background())
}

func (i *Record) ToRecordOutputWithContext(ctx context.Context) RecordOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RecordOutput)
}

func (i *Record) ToRecordPtrOutput() RecordPtrOutput {
	return i.ToRecordPtrOutputWithContext(context.Background())
}

func (i *Record) ToRecordPtrOutputWithContext(ctx context.Context) RecordPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RecordPtrOutput)
}

type RecordPtrInput interface {
	pulumi.Input

	ToRecordPtrOutput() RecordPtrOutput
	ToRecordPtrOutputWithContext(ctx context.Context) RecordPtrOutput
}

type recordPtrType RecordArgs

func (*recordPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Record)(nil))
}

func (i *recordPtrType) ToRecordPtrOutput() RecordPtrOutput {
	return i.ToRecordPtrOutputWithContext(context.Background())
}

func (i *recordPtrType) ToRecordPtrOutputWithContext(ctx context.Context) RecordPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RecordPtrOutput)
}

// RecordArrayInput is an input type that accepts RecordArray and RecordArrayOutput values.
// You can construct a concrete instance of `RecordArrayInput` via:
//
//          RecordArray{ RecordArgs{...} }
type RecordArrayInput interface {
	pulumi.Input

	ToRecordArrayOutput() RecordArrayOutput
	ToRecordArrayOutputWithContext(context.Context) RecordArrayOutput
}

type RecordArray []RecordInput

func (RecordArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*Record)(nil))
}

func (i RecordArray) ToRecordArrayOutput() RecordArrayOutput {
	return i.ToRecordArrayOutputWithContext(context.Background())
}

func (i RecordArray) ToRecordArrayOutputWithContext(ctx context.Context) RecordArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RecordArrayOutput)
}

// RecordMapInput is an input type that accepts RecordMap and RecordMapOutput values.
// You can construct a concrete instance of `RecordMapInput` via:
//
//          RecordMap{ "key": RecordArgs{...} }
type RecordMapInput interface {
	pulumi.Input

	ToRecordMapOutput() RecordMapOutput
	ToRecordMapOutputWithContext(context.Context) RecordMapOutput
}

type RecordMap map[string]RecordInput

func (RecordMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*Record)(nil))
}

func (i RecordMap) ToRecordMapOutput() RecordMapOutput {
	return i.ToRecordMapOutputWithContext(context.Background())
}

func (i RecordMap) ToRecordMapOutputWithContext(ctx context.Context) RecordMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RecordMapOutput)
}

type RecordOutput struct {
	*pulumi.OutputState
}

func (RecordOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Record)(nil))
}

func (o RecordOutput) ToRecordOutput() RecordOutput {
	return o
}

func (o RecordOutput) ToRecordOutputWithContext(ctx context.Context) RecordOutput {
	return o
}

func (o RecordOutput) ToRecordPtrOutput() RecordPtrOutput {
	return o.ToRecordPtrOutputWithContext(context.Background())
}

func (o RecordOutput) ToRecordPtrOutputWithContext(ctx context.Context) RecordPtrOutput {
	return o.ApplyT(func(v Record) *Record {
		return &v
	}).(RecordPtrOutput)
}

type RecordPtrOutput struct {
	*pulumi.OutputState
}

func (RecordPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Record)(nil))
}

func (o RecordPtrOutput) ToRecordPtrOutput() RecordPtrOutput {
	return o
}

func (o RecordPtrOutput) ToRecordPtrOutputWithContext(ctx context.Context) RecordPtrOutput {
	return o
}

type RecordArrayOutput struct{ *pulumi.OutputState }

func (RecordArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Record)(nil))
}

func (o RecordArrayOutput) ToRecordArrayOutput() RecordArrayOutput {
	return o
}

func (o RecordArrayOutput) ToRecordArrayOutputWithContext(ctx context.Context) RecordArrayOutput {
	return o
}

func (o RecordArrayOutput) Index(i pulumi.IntInput) RecordOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Record {
		return vs[0].([]Record)[vs[1].(int)]
	}).(RecordOutput)
}

type RecordMapOutput struct{ *pulumi.OutputState }

func (RecordMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Record)(nil))
}

func (o RecordMapOutput) ToRecordMapOutput() RecordMapOutput {
	return o
}

func (o RecordMapOutput) ToRecordMapOutputWithContext(ctx context.Context) RecordMapOutput {
	return o
}

func (o RecordMapOutput) MapIndex(k pulumi.StringInput) RecordOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Record {
		return vs[0].(map[string]Record)[vs[1].(string)]
	}).(RecordOutput)
}

func init() {
	pulumi.RegisterOutputType(RecordOutput{})
	pulumi.RegisterOutputType(RecordPtrOutput{})
	pulumi.RegisterOutputType(RecordArrayOutput{})
	pulumi.RegisterOutputType(RecordMapOutput{})
}
