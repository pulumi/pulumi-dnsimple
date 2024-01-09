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

type Contact struct {
	pulumi.CustomResourceState

	AccountId        pulumi.IntOutput    `pulumi:"accountId"`
	Address1         pulumi.StringOutput `pulumi:"address1"`
	Address2         pulumi.StringOutput `pulumi:"address2"`
	City             pulumi.StringOutput `pulumi:"city"`
	Country          pulumi.StringOutput `pulumi:"country"`
	CreatedAt        pulumi.StringOutput `pulumi:"createdAt"`
	Email            pulumi.StringOutput `pulumi:"email"`
	Fax              pulumi.StringOutput `pulumi:"fax"`
	FaxNormalized    pulumi.StringOutput `pulumi:"faxNormalized"`
	FirstName        pulumi.StringOutput `pulumi:"firstName"`
	JobTitle         pulumi.StringOutput `pulumi:"jobTitle"`
	Label            pulumi.StringOutput `pulumi:"label"`
	LastName         pulumi.StringOutput `pulumi:"lastName"`
	OrganizationName pulumi.StringOutput `pulumi:"organizationName"`
	Phone            pulumi.StringOutput `pulumi:"phone"`
	PhoneNormalized  pulumi.StringOutput `pulumi:"phoneNormalized"`
	PostalCode       pulumi.StringOutput `pulumi:"postalCode"`
	StateProvince    pulumi.StringOutput `pulumi:"stateProvince"`
	UpdatedAt        pulumi.StringOutput `pulumi:"updatedAt"`
}

// NewContact registers a new resource with the given unique name, arguments, and options.
func NewContact(ctx *pulumi.Context,
	name string, args *ContactArgs, opts ...pulumi.ResourceOption) (*Contact, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Address1 == nil {
		return nil, errors.New("invalid value for required argument 'Address1'")
	}
	if args.City == nil {
		return nil, errors.New("invalid value for required argument 'City'")
	}
	if args.Country == nil {
		return nil, errors.New("invalid value for required argument 'Country'")
	}
	if args.Email == nil {
		return nil, errors.New("invalid value for required argument 'Email'")
	}
	if args.FirstName == nil {
		return nil, errors.New("invalid value for required argument 'FirstName'")
	}
	if args.LastName == nil {
		return nil, errors.New("invalid value for required argument 'LastName'")
	}
	if args.Phone == nil {
		return nil, errors.New("invalid value for required argument 'Phone'")
	}
	if args.PostalCode == nil {
		return nil, errors.New("invalid value for required argument 'PostalCode'")
	}
	if args.StateProvince == nil {
		return nil, errors.New("invalid value for required argument 'StateProvince'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Contact
	err := ctx.RegisterResource("dnsimple:index/contact:Contact", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetContact gets an existing Contact resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetContact(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ContactState, opts ...pulumi.ResourceOption) (*Contact, error) {
	var resource Contact
	err := ctx.ReadResource("dnsimple:index/contact:Contact", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Contact resources.
type contactState struct {
	AccountId        *int    `pulumi:"accountId"`
	Address1         *string `pulumi:"address1"`
	Address2         *string `pulumi:"address2"`
	City             *string `pulumi:"city"`
	Country          *string `pulumi:"country"`
	CreatedAt        *string `pulumi:"createdAt"`
	Email            *string `pulumi:"email"`
	Fax              *string `pulumi:"fax"`
	FaxNormalized    *string `pulumi:"faxNormalized"`
	FirstName        *string `pulumi:"firstName"`
	JobTitle         *string `pulumi:"jobTitle"`
	Label            *string `pulumi:"label"`
	LastName         *string `pulumi:"lastName"`
	OrganizationName *string `pulumi:"organizationName"`
	Phone            *string `pulumi:"phone"`
	PhoneNormalized  *string `pulumi:"phoneNormalized"`
	PostalCode       *string `pulumi:"postalCode"`
	StateProvince    *string `pulumi:"stateProvince"`
	UpdatedAt        *string `pulumi:"updatedAt"`
}

type ContactState struct {
	AccountId        pulumi.IntPtrInput
	Address1         pulumi.StringPtrInput
	Address2         pulumi.StringPtrInput
	City             pulumi.StringPtrInput
	Country          pulumi.StringPtrInput
	CreatedAt        pulumi.StringPtrInput
	Email            pulumi.StringPtrInput
	Fax              pulumi.StringPtrInput
	FaxNormalized    pulumi.StringPtrInput
	FirstName        pulumi.StringPtrInput
	JobTitle         pulumi.StringPtrInput
	Label            pulumi.StringPtrInput
	LastName         pulumi.StringPtrInput
	OrganizationName pulumi.StringPtrInput
	Phone            pulumi.StringPtrInput
	PhoneNormalized  pulumi.StringPtrInput
	PostalCode       pulumi.StringPtrInput
	StateProvince    pulumi.StringPtrInput
	UpdatedAt        pulumi.StringPtrInput
}

func (ContactState) ElementType() reflect.Type {
	return reflect.TypeOf((*contactState)(nil)).Elem()
}

type contactArgs struct {
	Address1         string  `pulumi:"address1"`
	Address2         *string `pulumi:"address2"`
	City             string  `pulumi:"city"`
	Country          string  `pulumi:"country"`
	Email            string  `pulumi:"email"`
	Fax              *string `pulumi:"fax"`
	FirstName        string  `pulumi:"firstName"`
	JobTitle         *string `pulumi:"jobTitle"`
	Label            *string `pulumi:"label"`
	LastName         string  `pulumi:"lastName"`
	OrganizationName *string `pulumi:"organizationName"`
	Phone            string  `pulumi:"phone"`
	PostalCode       string  `pulumi:"postalCode"`
	StateProvince    string  `pulumi:"stateProvince"`
}

// The set of arguments for constructing a Contact resource.
type ContactArgs struct {
	Address1         pulumi.StringInput
	Address2         pulumi.StringPtrInput
	City             pulumi.StringInput
	Country          pulumi.StringInput
	Email            pulumi.StringInput
	Fax              pulumi.StringPtrInput
	FirstName        pulumi.StringInput
	JobTitle         pulumi.StringPtrInput
	Label            pulumi.StringPtrInput
	LastName         pulumi.StringInput
	OrganizationName pulumi.StringPtrInput
	Phone            pulumi.StringInput
	PostalCode       pulumi.StringInput
	StateProvince    pulumi.StringInput
}

func (ContactArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*contactArgs)(nil)).Elem()
}

type ContactInput interface {
	pulumi.Input

	ToContactOutput() ContactOutput
	ToContactOutputWithContext(ctx context.Context) ContactOutput
}

func (*Contact) ElementType() reflect.Type {
	return reflect.TypeOf((**Contact)(nil)).Elem()
}

func (i *Contact) ToContactOutput() ContactOutput {
	return i.ToContactOutputWithContext(context.Background())
}

func (i *Contact) ToContactOutputWithContext(ctx context.Context) ContactOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ContactOutput)
}

// ContactArrayInput is an input type that accepts ContactArray and ContactArrayOutput values.
// You can construct a concrete instance of `ContactArrayInput` via:
//
//	ContactArray{ ContactArgs{...} }
type ContactArrayInput interface {
	pulumi.Input

	ToContactArrayOutput() ContactArrayOutput
	ToContactArrayOutputWithContext(context.Context) ContactArrayOutput
}

type ContactArray []ContactInput

func (ContactArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Contact)(nil)).Elem()
}

func (i ContactArray) ToContactArrayOutput() ContactArrayOutput {
	return i.ToContactArrayOutputWithContext(context.Background())
}

func (i ContactArray) ToContactArrayOutputWithContext(ctx context.Context) ContactArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ContactArrayOutput)
}

// ContactMapInput is an input type that accepts ContactMap and ContactMapOutput values.
// You can construct a concrete instance of `ContactMapInput` via:
//
//	ContactMap{ "key": ContactArgs{...} }
type ContactMapInput interface {
	pulumi.Input

	ToContactMapOutput() ContactMapOutput
	ToContactMapOutputWithContext(context.Context) ContactMapOutput
}

type ContactMap map[string]ContactInput

func (ContactMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Contact)(nil)).Elem()
}

func (i ContactMap) ToContactMapOutput() ContactMapOutput {
	return i.ToContactMapOutputWithContext(context.Background())
}

func (i ContactMap) ToContactMapOutputWithContext(ctx context.Context) ContactMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ContactMapOutput)
}

type ContactOutput struct{ *pulumi.OutputState }

func (ContactOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Contact)(nil)).Elem()
}

func (o ContactOutput) ToContactOutput() ContactOutput {
	return o
}

func (o ContactOutput) ToContactOutputWithContext(ctx context.Context) ContactOutput {
	return o
}

func (o ContactOutput) AccountId() pulumi.IntOutput {
	return o.ApplyT(func(v *Contact) pulumi.IntOutput { return v.AccountId }).(pulumi.IntOutput)
}

func (o ContactOutput) Address1() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.Address1 }).(pulumi.StringOutput)
}

func (o ContactOutput) Address2() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.Address2 }).(pulumi.StringOutput)
}

func (o ContactOutput) City() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.City }).(pulumi.StringOutput)
}

func (o ContactOutput) Country() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.Country }).(pulumi.StringOutput)
}

func (o ContactOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

func (o ContactOutput) Email() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.Email }).(pulumi.StringOutput)
}

func (o ContactOutput) Fax() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.Fax }).(pulumi.StringOutput)
}

func (o ContactOutput) FaxNormalized() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.FaxNormalized }).(pulumi.StringOutput)
}

func (o ContactOutput) FirstName() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.FirstName }).(pulumi.StringOutput)
}

func (o ContactOutput) JobTitle() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.JobTitle }).(pulumi.StringOutput)
}

func (o ContactOutput) Label() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.Label }).(pulumi.StringOutput)
}

func (o ContactOutput) LastName() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.LastName }).(pulumi.StringOutput)
}

func (o ContactOutput) OrganizationName() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.OrganizationName }).(pulumi.StringOutput)
}

func (o ContactOutput) Phone() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.Phone }).(pulumi.StringOutput)
}

func (o ContactOutput) PhoneNormalized() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.PhoneNormalized }).(pulumi.StringOutput)
}

func (o ContactOutput) PostalCode() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.PostalCode }).(pulumi.StringOutput)
}

func (o ContactOutput) StateProvince() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.StateProvince }).(pulumi.StringOutput)
}

func (o ContactOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *Contact) pulumi.StringOutput { return v.UpdatedAt }).(pulumi.StringOutput)
}

type ContactArrayOutput struct{ *pulumi.OutputState }

func (ContactArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Contact)(nil)).Elem()
}

func (o ContactArrayOutput) ToContactArrayOutput() ContactArrayOutput {
	return o
}

func (o ContactArrayOutput) ToContactArrayOutputWithContext(ctx context.Context) ContactArrayOutput {
	return o
}

func (o ContactArrayOutput) Index(i pulumi.IntInput) ContactOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Contact {
		return vs[0].([]*Contact)[vs[1].(int)]
	}).(ContactOutput)
}

type ContactMapOutput struct{ *pulumi.OutputState }

func (ContactMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Contact)(nil)).Elem()
}

func (o ContactMapOutput) ToContactMapOutput() ContactMapOutput {
	return o
}

func (o ContactMapOutput) ToContactMapOutputWithContext(ctx context.Context) ContactMapOutput {
	return o
}

func (o ContactMapOutput) MapIndex(k pulumi.StringInput) ContactOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Contact {
		return vs[0].(map[string]*Contact)[vs[1].(string)]
	}).(ContactOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ContactInput)(nil)).Elem(), &Contact{})
	pulumi.RegisterInputType(reflect.TypeOf((*ContactArrayInput)(nil)).Elem(), ContactArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ContactMapInput)(nil)).Elem(), ContactMap{})
	pulumi.RegisterOutputType(ContactOutput{})
	pulumi.RegisterOutputType(ContactArrayOutput{})
	pulumi.RegisterOutputType(ContactMapOutput{})
}
