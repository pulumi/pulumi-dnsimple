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
	"unicode"

	"github.com/hashicorp/terraform-plugin-sdk/helper/schema"
	"github.com/hashicorp/terraform-plugin-sdk/terraform"
	"github.com/pulumi/pulumi-terraform-bridge/v2/pkg/tfbridge"
	"github.com/pulumi/pulumi/sdk/v2/go/common/resource"
	"github.com/pulumi/pulumi/sdk/v2/go/common/tokens"
	"github.com/terraform-providers/terraform-provider-dnsimple/dnsimple"
)

// all of the token components used below.
const (
	// packages:
	mainPkg = "dnsimple"
	// modules:
	mainMod = "index"
)

// makeMember manufactures a type token for the package and the given module and type.
func makeMember(mod string, mem string) tokens.ModuleMember {
	return tokens.ModuleMember(mainPkg + ":" + mod + ":" + mem)
}

// makeType manufactures a type token for the package and the given module and type.
func makeType(mod string, typ string) tokens.Type {
	return tokens.Type(makeMember(mod, typ))
}

// makeResource manufactures a standard resource token given a module and resource name.  It
// automatically uses the main package and names the file by simply lower casing the resource's
// first character.
func makeResource(mod string, res string) tokens.Type {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return makeType(mod+"/"+fn, res)
}

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c *terraform.ResourceConfig) error {
	return nil
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	p := dnsimple.Provider().(*schema.Provider)

	prov := tfbridge.ProviderInfo{
		P:                    p,
		Name:                 "dnsimple",
		Description:          "A Pulumi package for creating and managing dnsimple cloud resources.",
		Keywords:             []string{"pulumi", "dnsimple"},
		License:              "Apache-2.0",
		Homepage:             "https://pulumi.io",
		Repository:           "https://github.com/pulumi/pulumi-dnsimple",
		PreConfigureCallback: preConfigureCallback,
		Config: map[string]*tfbridge.SchemaInfo{
			"token": {
				Default: &tfbridge.DefaultInfo{
					Value:   "",
					EnvVars: []string{"DNSIMPLE_TOKEN"},
				},
			},
			"account": {
				Default: &tfbridge.DefaultInfo{
					Value:   "",
					EnvVars: []string{"DNSIMPLE_ACCOUNT"},
				},
			},
		},
		Resources: map[string]*tfbridge.ResourceInfo{
			"dnsimple_record": {Tok: makeResource(mainMod, "Record"),
				Fields: map[string]*tfbridge.SchemaInfo{
					"name": {
						Type: "string",
					},
					"ttl": {
						Type: "number",
					},
					"priority": {
						Type: "number",
					},
					"type": {
						Type: makeType(mainMod, "RecordType"),
					},
				},
			},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{},
		JavaScript: &tfbridge.JavaScriptInfo{
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^2.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^8.0.25", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			Overlay: &tfbridge.OverlayInfo{
				DestFiles: []string{
					"recordType.ts",
				},
			},
		},
		Python: &tfbridge.PythonInfo{
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=2.0.0,<3.0.0",
			},
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi":                       "2.*",
				"System.Collections.Immutable": "1.6.0",
			},
			Namespaces: map[string]string{
				mainPkg: "DNSimple",
			},
		},
	}

	return prov
}
