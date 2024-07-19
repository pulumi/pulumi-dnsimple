[![Actions Status](https://github.com/pulumi/pulumi-dnsimple/workflows/master/badge.svg)](https://github.com/pulumi/pulumi-dnsimple/actions)
[![Slack](http://www.pulumi.com/images/docs/badges/slack.svg)](https://slack.pulumi.com)
[![NPM version](https://badge.fury.io/js/%40pulumi%2Fdnsimple.svg)](https://www.npmjs.com/package/@pulumi/dnsimple)
[![Python version](https://badge.fury.io/py/pulumi-dnsimple.svg)](https://pypi.org/project/pulumi-dnsimple)
[![NuGet version](https://badge.fury.io/nu/pulumi.dnsimple.svg)](https://badge.fury.io/nu/pulumi.dnsimple)
[![PkgGoDev](https://pkg.go.dev/badge/github.com/pulumi/pulumi-dnsimple/sdk/v4/go)](https://pkg.go.dev/github.com/pulumi/pulumi-dnsimple/sdk/v4/go)
[![License](https://img.shields.io/npm/l/%40pulumi%2Fpulumi.svg)](https://github.com/pulumi/pulumi-dnsimple/blob/master/LICENSE)

# dnsimple Resource Provider

The dnsimple resource provider for Pulumi lets you manage dnsimple resources in your cloud programs. To use
this package, please [install the Pulumi CLI first](https://pulumi.io/).

## Installing

This package is available in many languages in the standard packaging formats.

### Node.js (Java/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

    $ npm install @pulumi/dnsimple

or `yarn`:

    $ yarn add @pulumi/dnsimple

### Python

To use from Python, install using `pip`:

    $ pip install pulumi_dnsimple

### Go

To use from Go, use `go get` to grab the latest version of the library

    $ go get github.com/pulumi/pulumi-dnsimple/sdk/v4

### .NET

To use from .NET, install using `dotnet add package`:

    $ dotnet add package Pulumi.Dnsimple

## Configuration

The following configuration points are available:

- `dnsimple:token` - (required) The DNSimple API v2 token. Please note that this must be an API v2 token. You can use 
   either an User or Account token, but an Account token is recommended. Can be sourced from `DNSIMPLE_TOKEN` environment
   variable.
- `dnsimple:account` - (required) The ID of the account associated with the token. Can be sourced from `DNSIMPLE_ACCOUNT` 
   environment variable.

## Reference

For further information, please visit [the dnsimple provider docs](https://www.pulumi.com/docs/intro/cloud-providers/dnsimple) or for detailed reference documentation, please visit [the API docs](https://www.pulumi.com/docs/reference/pkg/dnsimple).
