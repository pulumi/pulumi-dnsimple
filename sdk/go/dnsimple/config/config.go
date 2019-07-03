// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
	"github.com/pulumi/pulumi/sdk/go/pulumi/config"
)

// The account for API operations.
func GetAccount(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "dnsimple:account")
	if err == nil {
		return v
	}
	if dv, ok := getEnvOrDefault("", nil, "DNSIMPLE_ACCOUNT").(string); ok {
		return dv
	}
	return v
}

// The DNSimple account email address.
func GetEmail(ctx *pulumi.Context) string {
	return config.Get(ctx, "dnsimple:email")
}

// The API v2 token for API operations.
func GetToken(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "dnsimple:token")
	if err == nil {
		return v
	}
	if dv, ok := getEnvOrDefault("", nil, "DNSIMPLE_TOKEN").(string); ok {
		return dv
	}
	return v
}
