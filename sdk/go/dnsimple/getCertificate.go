// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dnsimple

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-dnsimple/sdk/v3/go/dnsimple/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a DNSimple certificate data source.
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
//			_, err := dnsimple.GetCertificate(ctx, &dnsimple.GetCertificateArgs{
//				Domain:        dnsimpleDomain,
//				CertificateId: dnsimpleCertificateId,
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetCertificate(ctx *pulumi.Context, args *GetCertificateArgs, opts ...pulumi.InvokeOption) (*GetCertificateResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetCertificateResult
	err := ctx.Invoke("dnsimple:index/getCertificate:getCertificate", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getCertificate.
type GetCertificateArgs struct {
	// The ID of the SSL Certificate
	CertificateId int `pulumi:"certificateId"`
	// The domain of the SSL Certificate
	Domain string `pulumi:"domain"`
}

// A collection of values returned by getCertificate.
type GetCertificateResult struct {
	// A list of certificates that make up the chain
	CertificateChains []string `pulumi:"certificateChains"`
	CertificateId     int      `pulumi:"certificateId"`
	Domain            string   `pulumi:"domain"`
	Id                string   `pulumi:"id"`
	// The corresponding Private Key for the SSL Certificate
	PrivateKey string `pulumi:"privateKey"`
	// The Root Certificate of the issuing CA
	RootCertificate string `pulumi:"rootCertificate"`
	// The SSL Certificate
	ServerCertificate string `pulumi:"serverCertificate"`
}

func GetCertificateOutput(ctx *pulumi.Context, args GetCertificateOutputArgs, opts ...pulumi.InvokeOption) GetCertificateResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetCertificateResult, error) {
			args := v.(GetCertificateArgs)
			r, err := GetCertificate(ctx, &args, opts...)
			var s GetCertificateResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetCertificateResultOutput)
}

// A collection of arguments for invoking getCertificate.
type GetCertificateOutputArgs struct {
	// The ID of the SSL Certificate
	CertificateId pulumi.IntInput `pulumi:"certificateId"`
	// The domain of the SSL Certificate
	Domain pulumi.StringInput `pulumi:"domain"`
}

func (GetCertificateOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetCertificateArgs)(nil)).Elem()
}

// A collection of values returned by getCertificate.
type GetCertificateResultOutput struct{ *pulumi.OutputState }

func (GetCertificateResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetCertificateResult)(nil)).Elem()
}

func (o GetCertificateResultOutput) ToGetCertificateResultOutput() GetCertificateResultOutput {
	return o
}

func (o GetCertificateResultOutput) ToGetCertificateResultOutputWithContext(ctx context.Context) GetCertificateResultOutput {
	return o
}

// A list of certificates that make up the chain
func (o GetCertificateResultOutput) CertificateChains() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetCertificateResult) []string { return v.CertificateChains }).(pulumi.StringArrayOutput)
}

func (o GetCertificateResultOutput) CertificateId() pulumi.IntOutput {
	return o.ApplyT(func(v GetCertificateResult) int { return v.CertificateId }).(pulumi.IntOutput)
}

func (o GetCertificateResultOutput) Domain() pulumi.StringOutput {
	return o.ApplyT(func(v GetCertificateResult) string { return v.Domain }).(pulumi.StringOutput)
}

func (o GetCertificateResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetCertificateResult) string { return v.Id }).(pulumi.StringOutput)
}

// The corresponding Private Key for the SSL Certificate
func (o GetCertificateResultOutput) PrivateKey() pulumi.StringOutput {
	return o.ApplyT(func(v GetCertificateResult) string { return v.PrivateKey }).(pulumi.StringOutput)
}

// The Root Certificate of the issuing CA
func (o GetCertificateResultOutput) RootCertificate() pulumi.StringOutput {
	return o.ApplyT(func(v GetCertificateResult) string { return v.RootCertificate }).(pulumi.StringOutput)
}

// The SSL Certificate
func (o GetCertificateResultOutput) ServerCertificate() pulumi.StringOutput {
	return o.ApplyT(func(v GetCertificateResult) string { return v.ServerCertificate }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetCertificateResultOutput{})
}
