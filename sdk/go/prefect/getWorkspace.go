// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package prefect

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/ru5j4r0/pulumi-prefect/sdk/go/prefect/internal"
)

// Get information about an existing Workspace by handle.
// <br>
// Use this data source to obtain Workspace IDs
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
//			_, err := prefect.LookupWorkspace(ctx, &prefect.LookupWorkspaceArgs{
//				Id: pulumi.StringRef("00000000-0000-0000-0000-000000000000"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupWorkspace(ctx *pulumi.Context, args *LookupWorkspaceArgs, opts ...pulumi.InvokeOption) (*LookupWorkspaceResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupWorkspaceResult
	err := ctx.Invoke("prefect:index/getWorkspace:getWorkspace", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getWorkspace.
type LookupWorkspaceArgs struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId *string `pulumi:"accountId"`
	// Unique handle for the workspace
	Handle *string `pulumi:"handle"`
	// Workspace ID (UUID)
	Id *string `pulumi:"id"`
}

// A collection of values returned by getWorkspace.
type LookupWorkspaceResult struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId *string `pulumi:"accountId"`
	// Timestamp of when the resource was created (RFC3339)
	Created string `pulumi:"created"`
	// Description for the workspace
	Description string `pulumi:"description"`
	// Unique handle for the workspace
	Handle string `pulumi:"handle"`
	// Workspace ID (UUID)
	Id string `pulumi:"id"`
	// Name of the workspace
	Name string `pulumi:"name"`
	// Timestamp of when the resource was updated (RFC3339)
	Updated string `pulumi:"updated"`
}

func LookupWorkspaceOutput(ctx *pulumi.Context, args LookupWorkspaceOutputArgs, opts ...pulumi.InvokeOption) LookupWorkspaceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupWorkspaceResult, error) {
			args := v.(LookupWorkspaceArgs)
			r, err := LookupWorkspace(ctx, &args, opts...)
			var s LookupWorkspaceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupWorkspaceResultOutput)
}

// A collection of arguments for invoking getWorkspace.
type LookupWorkspaceOutputArgs struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId pulumi.StringPtrInput `pulumi:"accountId"`
	// Unique handle for the workspace
	Handle pulumi.StringPtrInput `pulumi:"handle"`
	// Workspace ID (UUID)
	Id pulumi.StringPtrInput `pulumi:"id"`
}

func (LookupWorkspaceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWorkspaceArgs)(nil)).Elem()
}

// A collection of values returned by getWorkspace.
type LookupWorkspaceResultOutput struct{ *pulumi.OutputState }

func (LookupWorkspaceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWorkspaceResult)(nil)).Elem()
}

func (o LookupWorkspaceResultOutput) ToLookupWorkspaceResultOutput() LookupWorkspaceResultOutput {
	return o
}

func (o LookupWorkspaceResultOutput) ToLookupWorkspaceResultOutputWithContext(ctx context.Context) LookupWorkspaceResultOutput {
	return o
}

// Account ID (UUID), defaults to the account set in the provider
func (o LookupWorkspaceResultOutput) AccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWorkspaceResult) *string { return v.AccountId }).(pulumi.StringPtrOutput)
}

// Timestamp of when the resource was created (RFC3339)
func (o LookupWorkspaceResultOutput) Created() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWorkspaceResult) string { return v.Created }).(pulumi.StringOutput)
}

// Description for the workspace
func (o LookupWorkspaceResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWorkspaceResult) string { return v.Description }).(pulumi.StringOutput)
}

// Unique handle for the workspace
func (o LookupWorkspaceResultOutput) Handle() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWorkspaceResult) string { return v.Handle }).(pulumi.StringOutput)
}

// Workspace ID (UUID)
func (o LookupWorkspaceResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWorkspaceResult) string { return v.Id }).(pulumi.StringOutput)
}

// Name of the workspace
func (o LookupWorkspaceResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWorkspaceResult) string { return v.Name }).(pulumi.StringOutput)
}

// Timestamp of when the resource was updated (RFC3339)
func (o LookupWorkspaceResultOutput) Updated() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWorkspaceResult) string { return v.Updated }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupWorkspaceResultOutput{})
}
