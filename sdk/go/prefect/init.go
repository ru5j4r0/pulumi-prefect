// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package prefect

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/ru5j4r0/pulumi-prefect/sdk/go/prefect/internal"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "prefect:index/account:Account":
		r = &Account{}
	case "prefect:index/serviceAccount:ServiceAccount":
		r = &ServiceAccount{}
	case "prefect:index/variable:Variable":
		r = &Variable{}
	case "prefect:index/workPool:WorkPool":
		r = &WorkPool{}
	case "prefect:index/workspace:Workspace":
		r = &Workspace{}
	case "prefect:index/workspaceAccess:WorkspaceAccess":
		r = &WorkspaceAccess{}
	case "prefect:index/workspaceRole:WorkspaceRole":
		r = &WorkspaceRole{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:prefect" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"prefect",
		"index/account",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"prefect",
		"index/serviceAccount",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"prefect",
		"index/variable",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"prefect",
		"index/workPool",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"prefect",
		"index/workspace",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"prefect",
		"index/workspaceAccess",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"prefect",
		"index/workspaceRole",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"prefect",
		&pkg{version},
	)
}