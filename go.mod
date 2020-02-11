module github.com/pulumi/pulumi-dnsimple

go 1.13

require (
	github.com/hashicorp/terraform-plugin-sdk v1.6.0
	github.com/pkg/errors v0.9.1
	github.com/pulumi/pulumi v1.9.1
	github.com/pulumi/pulumi-terraform-bridge v1.6.6
	github.com/terraform-providers/terraform-provider-dnsimple v0.3.0
)

replace (
	github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
	github.com/hashicorp/vault => github.com/hashicorp/vault v1.2.0
)
