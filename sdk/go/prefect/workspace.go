// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package prefect

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/ru5j4r0/pulumi-prefect/sdk/go/prefect/internal"
)

// The resource `workspace` represents a Prefect Cloud Workspace. Workspaces are discrete environments in Prefect Cloud for your flows, configurations, and deployments. Manage your workflows and RBAC policies using `workPool` and `workspaceAccess` resources.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/ru5j4r0/pulumi-prefect/sdk/go/prefect"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := prefect.NewWorkspace(ctx, "example", &prefect.WorkspaceArgs{
//				Handle: pulumi.String("my-workspace"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// Prefect Workspaces can be imported via handle in the form `handle/workspace-handle`
//
// ```sh
// $ pulumi import prefect:index/workspace:Workspace example handle/workspace-handle
// ```
//
// # Prefect Workspaces can also be imported via UUID
//
// ```sh
// $ pulumi import prefect:index/workspace:Workspace example 00000000-0000-0000-0000-000000000000
// ```
type Workspace struct {
	pulumi.CustomResourceState

	// Account ID (UUID), defaults to the account set in the provider
	AccountId pulumi.StringPtrOutput `pulumi:"accountId"`
	// Timestamp of when the resource was created (RFC3339)
	Created pulumi.StringOutput `pulumi:"created"`
	// Description for the workspace
	Description pulumi.StringOutput `pulumi:"description"`
	// Unique handle for the workspace
	Handle pulumi.StringOutput `pulumi:"handle"`
	// Name of the workspace
	Name pulumi.StringOutput `pulumi:"name"`
	// Timestamp of when the resource was updated (RFC3339)
	Updated pulumi.StringOutput `pulumi:"updated"`
}

// NewWorkspace registers a new resource with the given unique name, arguments, and options.
func NewWorkspace(ctx *pulumi.Context,
	name string, args *WorkspaceArgs, opts ...pulumi.ResourceOption) (*Workspace, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Handle == nil {
		return nil, errors.New("invalid value for required argument 'Handle'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Workspace
	err := ctx.RegisterResource("prefect:index/workspace:Workspace", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWorkspace gets an existing Workspace resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWorkspace(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WorkspaceState, opts ...pulumi.ResourceOption) (*Workspace, error) {
	var resource Workspace
	err := ctx.ReadResource("prefect:index/workspace:Workspace", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Workspace resources.
type workspaceState struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId *string `pulumi:"accountId"`
	// Timestamp of when the resource was created (RFC3339)
	Created *string `pulumi:"created"`
	// Description for the workspace
	Description *string `pulumi:"description"`
	// Unique handle for the workspace
	Handle *string `pulumi:"handle"`
	// Name of the workspace
	Name *string `pulumi:"name"`
	// Timestamp of when the resource was updated (RFC3339)
	Updated *string `pulumi:"updated"`
}

type WorkspaceState struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId pulumi.StringPtrInput
	// Timestamp of when the resource was created (RFC3339)
	Created pulumi.StringPtrInput
	// Description for the workspace
	Description pulumi.StringPtrInput
	// Unique handle for the workspace
	Handle pulumi.StringPtrInput
	// Name of the workspace
	Name pulumi.StringPtrInput
	// Timestamp of when the resource was updated (RFC3339)
	Updated pulumi.StringPtrInput
}

func (WorkspaceState) ElementType() reflect.Type {
	return reflect.TypeOf((*workspaceState)(nil)).Elem()
}

type workspaceArgs struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId *string `pulumi:"accountId"`
	// Description for the workspace
	Description *string `pulumi:"description"`
	// Unique handle for the workspace
	Handle string `pulumi:"handle"`
	// Name of the workspace
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a Workspace resource.
type WorkspaceArgs struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId pulumi.StringPtrInput
	// Description for the workspace
	Description pulumi.StringPtrInput
	// Unique handle for the workspace
	Handle pulumi.StringInput
	// Name of the workspace
	Name pulumi.StringPtrInput
}

func (WorkspaceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*workspaceArgs)(nil)).Elem()
}

type WorkspaceInput interface {
	pulumi.Input

	ToWorkspaceOutput() WorkspaceOutput
	ToWorkspaceOutputWithContext(ctx context.Context) WorkspaceOutput
}

func (*Workspace) ElementType() reflect.Type {
	return reflect.TypeOf((**Workspace)(nil)).Elem()
}

func (i *Workspace) ToWorkspaceOutput() WorkspaceOutput {
	return i.ToWorkspaceOutputWithContext(context.Background())
}

func (i *Workspace) ToWorkspaceOutputWithContext(ctx context.Context) WorkspaceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkspaceOutput)
}

// WorkspaceArrayInput is an input type that accepts WorkspaceArray and WorkspaceArrayOutput values.
// You can construct a concrete instance of `WorkspaceArrayInput` via:
//
//	WorkspaceArray{ WorkspaceArgs{...} }
type WorkspaceArrayInput interface {
	pulumi.Input

	ToWorkspaceArrayOutput() WorkspaceArrayOutput
	ToWorkspaceArrayOutputWithContext(context.Context) WorkspaceArrayOutput
}

type WorkspaceArray []WorkspaceInput

func (WorkspaceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Workspace)(nil)).Elem()
}

func (i WorkspaceArray) ToWorkspaceArrayOutput() WorkspaceArrayOutput {
	return i.ToWorkspaceArrayOutputWithContext(context.Background())
}

func (i WorkspaceArray) ToWorkspaceArrayOutputWithContext(ctx context.Context) WorkspaceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkspaceArrayOutput)
}

// WorkspaceMapInput is an input type that accepts WorkspaceMap and WorkspaceMapOutput values.
// You can construct a concrete instance of `WorkspaceMapInput` via:
//
//	WorkspaceMap{ "key": WorkspaceArgs{...} }
type WorkspaceMapInput interface {
	pulumi.Input

	ToWorkspaceMapOutput() WorkspaceMapOutput
	ToWorkspaceMapOutputWithContext(context.Context) WorkspaceMapOutput
}

type WorkspaceMap map[string]WorkspaceInput

func (WorkspaceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Workspace)(nil)).Elem()
}

func (i WorkspaceMap) ToWorkspaceMapOutput() WorkspaceMapOutput {
	return i.ToWorkspaceMapOutputWithContext(context.Background())
}

func (i WorkspaceMap) ToWorkspaceMapOutputWithContext(ctx context.Context) WorkspaceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkspaceMapOutput)
}

type WorkspaceOutput struct{ *pulumi.OutputState }

func (WorkspaceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Workspace)(nil)).Elem()
}

func (o WorkspaceOutput) ToWorkspaceOutput() WorkspaceOutput {
	return o
}

func (o WorkspaceOutput) ToWorkspaceOutputWithContext(ctx context.Context) WorkspaceOutput {
	return o
}

// Account ID (UUID), defaults to the account set in the provider
func (o WorkspaceOutput) AccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Workspace) pulumi.StringPtrOutput { return v.AccountId }).(pulumi.StringPtrOutput)
}

// Timestamp of when the resource was created (RFC3339)
func (o WorkspaceOutput) Created() pulumi.StringOutput {
	return o.ApplyT(func(v *Workspace) pulumi.StringOutput { return v.Created }).(pulumi.StringOutput)
}

// Description for the workspace
func (o WorkspaceOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *Workspace) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// Unique handle for the workspace
func (o WorkspaceOutput) Handle() pulumi.StringOutput {
	return o.ApplyT(func(v *Workspace) pulumi.StringOutput { return v.Handle }).(pulumi.StringOutput)
}

// Name of the workspace
func (o WorkspaceOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Workspace) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Timestamp of when the resource was updated (RFC3339)
func (o WorkspaceOutput) Updated() pulumi.StringOutput {
	return o.ApplyT(func(v *Workspace) pulumi.StringOutput { return v.Updated }).(pulumi.StringOutput)
}

type WorkspaceArrayOutput struct{ *pulumi.OutputState }

func (WorkspaceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Workspace)(nil)).Elem()
}

func (o WorkspaceArrayOutput) ToWorkspaceArrayOutput() WorkspaceArrayOutput {
	return o
}

func (o WorkspaceArrayOutput) ToWorkspaceArrayOutputWithContext(ctx context.Context) WorkspaceArrayOutput {
	return o
}

func (o WorkspaceArrayOutput) Index(i pulumi.IntInput) WorkspaceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Workspace {
		return vs[0].([]*Workspace)[vs[1].(int)]
	}).(WorkspaceOutput)
}

type WorkspaceMapOutput struct{ *pulumi.OutputState }

func (WorkspaceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Workspace)(nil)).Elem()
}

func (o WorkspaceMapOutput) ToWorkspaceMapOutput() WorkspaceMapOutput {
	return o
}

func (o WorkspaceMapOutput) ToWorkspaceMapOutputWithContext(ctx context.Context) WorkspaceMapOutput {
	return o
}

func (o WorkspaceMapOutput) MapIndex(k pulumi.StringInput) WorkspaceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Workspace {
		return vs[0].(map[string]*Workspace)[vs[1].(string)]
	}).(WorkspaceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*WorkspaceInput)(nil)).Elem(), &Workspace{})
	pulumi.RegisterInputType(reflect.TypeOf((*WorkspaceArrayInput)(nil)).Elem(), WorkspaceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*WorkspaceMapInput)(nil)).Elem(), WorkspaceMap{})
	pulumi.RegisterOutputType(WorkspaceOutput{})
	pulumi.RegisterOutputType(WorkspaceArrayOutput{})
	pulumi.RegisterOutputType(WorkspaceMapOutput{})
}
