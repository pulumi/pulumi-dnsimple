[![Build Status](https://travis-ci.com/pulumi/pulumi-dnsimple.svg?token=eHg7Zp5zdDDJfTjY8ejq&branch=master)](https://travis-ci.com/pulumi/pulumi-dnsimple)

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

    $ go get github.com/pulumi/pulumi-dnsimple/sdk/go/...

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
