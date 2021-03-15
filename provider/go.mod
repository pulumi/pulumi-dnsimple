module github.com/pulumi/pulumi-dnsimple/provider/v2

go 1.16

require (
	github.com/hashicorp/terraform-plugin-sdk v1.7.0
	github.com/pulumi/pulumi-terraform-bridge/v2 v2.21.0
	github.com/pulumi/pulumi/sdk/v2 v2.22.1-0.20210310211618-1f16423ede4c
	github.com/terraform-providers/terraform-provider-dnsimple v0.4.0
)

replace (
	github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
	github.com/hashicorp/terraform-plugin-test => github.com/hashicorp/terraform-plugin-test v1.3.0
	github.com/hashicorp/vault => github.com/hashicorp/vault v1.2.0
)
