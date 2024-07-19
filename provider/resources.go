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
	"path"

	// embed is used to store bridge-metadata.json in the compiled binary
	_ "embed"

	dnsimple "github.com/terraform-providers/terraform-provider-dnsimple/shim"

	pfbridge "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	tfbridgetokens "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge/tokens"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"

	"github.com/pulumi/pulumi-dnsimple/provider/v3/pkg/version"
)

// all of the token components used below.
const (
	// packages:
	mainPkg = "dnsimple"
	// modules:
	mainMod = "index"
)

//go:embed cmd/pulumi-resource-dnsimple/bridge-metadata.json
var metadata []byte

// Provider returns additional overlaid schema and metadata associated with the provider.
func Provider() tfbridge.ProviderInfo {
	prov := tfbridge.ProviderInfo{
		P:                pfbridge.ShimProvider(dnsimple.Provider(version.Version)),
		Name:             "dnsimple",
		Description:      "A Pulumi package for creating and managing dnsimple cloud resources.",
		Keywords:         []string{"pulumi", "dnsimple"},
		License:          "Apache-2.0",
		Homepage:         "https://pulumi.io",
		Repository:       "https://github.com/pulumi/pulumi-dnsimple",
		GitHubOrg:        "terraform-providers",
		MetadataInfo:     tfbridge.NewProviderMetadata(metadata),
		Version:          version.Version,
		UpstreamRepoPath: "./upstream",
		JavaScript: &tfbridge.JavaScriptInfo{
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			Overlay: &tfbridge.OverlayInfo{
				DestFiles: []string{
					"recordType.ts",
				},
			},
			RespectSchemaVersion: true,
		},
		Python: &tfbridge.PythonInfo{
			RespectSchemaVersion: true,
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
			RespectSchemaVersion:           true,
		},
		CSharp: &tfbridge.CSharpInfo{
			RespectSchemaVersion: true,
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

	// Some resource's have non-string IDs. Pulumi requires string ID fields, so we
	// use a type override on these resources to tell Pulumi to present to users a
	// string, even though the underlying TF provider will see an integer.
	//
	// Related to https://github.com/pulumi/pulumi-terraform-bridge/issues/1198
	prov.P.ResourcesMap().Range(func(key string, value shim.Resource) bool {
		if value.Schema().Get("id").Type() != shim.TypeString {
			r := prov.Resources[key]
			if r.Fields == nil {
				r.Fields = make(map[string]*tfbridge.SchemaInfo, 1)
			}
			r.Fields["id"] = &tfbridge.SchemaInfo{Type: "string"}
		}
		return true
	})

	prov.MustApplyAutoAliases()

	return prov
}
