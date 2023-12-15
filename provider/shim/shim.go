package shim

import (
	"github.com/hashicorp/terraform-plugin-framework/provider"
	"github.com/pulumi/pulumi-dnsimple/provider/v3/pkg/version"
	dnsimpleProvider "github.com/terraform-providers/terraform-provider-dnsimple/internal/framework/provider"
)

func NewProvider() provider.Provider {
	p := dnsimpleProvider.New(version.Version)()
	return p
}
