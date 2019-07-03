// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package dnsimple

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a DNSimple record resource.
type Record struct {
	s *pulumi.ResourceState
}

// NewRecord registers a new resource with the given unique name, arguments, and options.
func NewRecord(ctx *pulumi.Context,
	name string, args *RecordArgs, opts ...pulumi.ResourceOpt) (*Record, error) {
	if args == nil || args.Domain == nil {
		return nil, errors.New("missing required argument 'Domain'")
	}
	if args == nil || args.Name == nil {
		return nil, errors.New("missing required argument 'Name'")
	}
	if args == nil || args.Type == nil {
		return nil, errors.New("missing required argument 'Type'")
	}
	if args == nil || args.Value == nil {
		return nil, errors.New("missing required argument 'Value'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["domain"] = nil
		inputs["name"] = nil
		inputs["priority"] = nil
		inputs["ttl"] = nil
		inputs["type"] = nil
		inputs["value"] = nil
	} else {
		inputs["domain"] = args.Domain
		inputs["name"] = args.Name
		inputs["priority"] = args.Priority
		inputs["ttl"] = args.Ttl
		inputs["type"] = args.Type
		inputs["value"] = args.Value
	}
	inputs["domainId"] = nil
	inputs["hostname"] = nil
	s, err := ctx.RegisterResource("dnsimple:index/record:Record", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Record{s: s}, nil
}

// GetRecord gets an existing Record resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRecord(ctx *pulumi.Context,
	name string, id pulumi.ID, state *RecordState, opts ...pulumi.ResourceOpt) (*Record, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["domain"] = state.Domain
		inputs["domainId"] = state.DomainId
		inputs["hostname"] = state.Hostname
		inputs["name"] = state.Name
		inputs["priority"] = state.Priority
		inputs["ttl"] = state.Ttl
		inputs["type"] = state.Type
		inputs["value"] = state.Value
	}
	s, err := ctx.ReadResource("dnsimple:index/record:Record", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Record{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Record) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Record) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The domain to add the record to
func (r *Record) Domain() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["domain"])
}

// The domain ID of the record
func (r *Record) DomainId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["domainId"])
}

// The FQDN of the record
func (r *Record) Hostname() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["hostname"])
}

// The name of the record
func (r *Record) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The priority of the record - only useful for some record types
func (r *Record) Priority() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["priority"])
}

// The TTL of the record
func (r *Record) Ttl() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["ttl"])
}

// The type of the record
func (r *Record) Type() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["type"])
}

// The value of the record
func (r *Record) Value() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["value"])
}

// Input properties used for looking up and filtering Record resources.
type RecordState struct {
	// The domain to add the record to
	Domain interface{}
	// The domain ID of the record
	DomainId interface{}
	// The FQDN of the record
	Hostname interface{}
	// The name of the record
	Name interface{}
	// The priority of the record - only useful for some record types
	Priority interface{}
	// The TTL of the record
	Ttl interface{}
	// The type of the record
	Type interface{}
	// The value of the record
	Value interface{}
}

// The set of arguments for constructing a Record resource.
type RecordArgs struct {
	// The domain to add the record to
	Domain interface{}
	// The name of the record
	Name interface{}
	// The priority of the record - only useful for some record types
	Priority interface{}
	// The TTL of the record
	Ttl interface{}
	// The type of the record
	Type interface{}
	// The value of the record
	Value interface{}
}
