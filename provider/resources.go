// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package dnsimple

import (
	"fmt"
	// embed is used to store bridge-metadata.json in the compiled binary
	_ "embed"
	"path"

	"github.com/pulumi/pulumi-dnsimple/provider/v4/pkg/version"
	pfbridge "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	tfbridgetokens "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge/tokens"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/pkg/v3/codegen/schema"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"

	dnsimple "github.com/terraform-providers/terraform-provider-dnsimple/shim"
)

// all of the token components used below.
const (
	// packages:
	mainPkg = "dnsimple"
	// modules:
	mainMod = "index"
)

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	recordTypeName := string(tfbridge.MakeResource(mainPkg, mainMod, "RecordType"))

	prov := tfbridge.ProviderInfo{
		P:            pfbridge.ShimProvider(dnsimple.New(version.Version)),
		Name:         "dnsimple",
		Description:  "A Pulumi package for creating and managing dnsimple cloud resources.",
		Keywords:     []string{"pulumi", "dnsimple"},
		License:      "Apache-2.0",
		Homepage:     "https://pulumi.io",
		Repository:   "https://github.com/pulumi/pulumi-dnsimple",
		MetadataInfo: tfbridge.NewProviderMetadata(metadata),
		GitHubOrg:    "dnsimple",
		Resources: map[string]*tfbridge.ResourceInfo{
			"dnsimple_record": {
				Fields: map[string]*tfbridge.SchemaInfo{
					"name": {Type: "string"},
					"type": {Type: tokens.Type(recordTypeName)},
				},
				Docs:               &tfbridge.DocInfo{AllowMissing: true},
				DeprecationMessage: "This resource is deprecated.\nIt will be removed in the next major version.",
			},
		},
		ExtraTypes: map[string]schema.ComplexTypeSpec{
			recordTypeName: recordType(),
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
		},
		Python: &tfbridge.PythonInfo{
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
			PyProject: struct{ Enabled bool }{true},
		},

		Golang: &tfbridge.GolangInfo{
			ImportBasePath: path.Join(
				fmt.Sprintf("github.com/pulumi/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
			Namespaces: map[string]string{
				mainPkg: "DNSimple",
			},
		},
	}

	prov.MustComputeTokens(tfbridgetokens.SingleModule("dnsimple_", mainMod,
		tfbridgetokens.MakeStandard(mainPkg)))
	prov.MustApplyAutoAliases()

	return prov
}

//go:embed cmd/pulumi-resource-dnsimple/bridge-metadata.json
var metadata []byte

func recordType() schema.ComplexTypeSpec {
	return schema.ComplexTypeSpec{
		ObjectTypeSpec: schema.ObjectTypeSpec{
			Type:        "string",
			Description: "A DNS Record Type",
		},
		Enum: []schema.EnumValueSpec{
			{Value: "A", Name: "A"},
			{Value: "AAAA", Name: "AAAA"},
			{Value: "ALIAS", Name: "ALIAS"},
			{Value: "CAA", Name: "CAA"},
			{Value: "CNAME", Name: "CNAME"},
			{Value: "HINFO", Name: "HINFO"},
			{Value: "MX", Name: "MX"},
			{Value: "NAPTR", Name: "NAPTR"},
			{Value: "NS", Name: "NS"},
			{Value: "POOL", Name: "POOL"},
			{Value: "PTR", Name: "PTR"},
			{Value: "SPF", Name: "SPF"},
			{Value: "SRV", Name: "SRV"},
			{Value: "SSHFP", Name: "SSHFP"},
			{Value: "TXT", Name: "TXT"},
			{Value: "URL", Name: "URL"},
		},
	}
}
