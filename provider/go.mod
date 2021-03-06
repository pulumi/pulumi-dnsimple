module github.com/pulumi/pulumi-dnsimple/provider/v3

go 1.16

require (
	github.com/dnsimple/terraform-provider-dnsimple v0.0.0
	github.com/hashicorp/terraform-plugin-sdk v1.7.0
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.2.1
	github.com/pulumi/pulumi/pkg/v3 v3.3.2-0.20210526172205-85142462c7ed
	github.com/pulumi/pulumi/sdk/v3 v3.3.2-0.20210526172205-85142462c7ed
)

replace (
	github.com/dnsimple/terraform-provider-dnsimple => github.com/pulumi/terraform-provider-dnsimple v0.5.2-0.20210427112559-df2b72e2df2d
	github.com/hashicorp/terraform-plugin-test => github.com/hashicorp/terraform-plugin-test v1.3.0
	github.com/hashicorp/vault => github.com/hashicorp/vault v1.2.0
)
