// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package prefect

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/ru5j4r0/pulumi-prefect/sdk/go/prefect/internal"
)

// Get information about an existing Work Pool by name.
// <br>
// Use this data source to obtain Work Pool-specific attributes.
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
//			_, err := prefect.LookupWorkPool(ctx, &prefect.LookupWorkPoolArgs{
//				Name: pulumi.StringRef("my-work-pool"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupWorkPool(ctx *pulumi.Context, args *LookupWorkPoolArgs, opts ...pulumi.InvokeOption) (*LookupWorkPoolResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupWorkPoolResult
	err := ctx.Invoke("prefect:index/getWorkPool:getWorkPool", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getWorkPool.
type LookupWorkPoolArgs struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId *string `pulumi:"accountId"`
	// The concurrency limit applied to this work pool
	ConcurrencyLimit *int `pulumi:"concurrencyLimit"`
	// The ID (UUID) of the default queue associated with this work pool
	DefaultQueueId *string `pulumi:"defaultQueueId"`
	// Description of the work pool
	Description *string `pulumi:"description"`
	// Work pool ID (UUID)
	Id *string `pulumi:"id"`
	// Name of the work pool
	Name *string `pulumi:"name"`
	// Workspace ID (UUID), defaults to the workspace set in the provider
	WorkspaceId *string `pulumi:"workspaceId"`
}

// A collection of values returned by getWorkPool.
type LookupWorkPoolResult struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId *string `pulumi:"accountId"`
	// The base job template for the work pool, as a JSON string
	BaseJobTemplate string `pulumi:"baseJobTemplate"`
	// The concurrency limit applied to this work pool
	ConcurrencyLimit int `pulumi:"concurrencyLimit"`
	// Date and time of the work pool creation in RFC 3339 format
	Created string `pulumi:"created"`
	// The ID (UUID) of the default queue associated with this work pool
	DefaultQueueId string `pulumi:"defaultQueueId"`
	// Description of the work pool
	Description string `pulumi:"description"`
	// Work pool ID (UUID)
	Id string `pulumi:"id"`
	// Name of the work pool
	Name string `pulumi:"name"`
	// Whether this work pool is paused
	Paused bool `pulumi:"paused"`
	// Type of the work pool
	Type string `pulumi:"type"`
	// Date and time that the work pool was last updated in RFC 3339 format
	Updated string `pulumi:"updated"`
	// Workspace ID (UUID), defaults to the workspace set in the provider
	WorkspaceId *string `pulumi:"workspaceId"`
}

func LookupWorkPoolOutput(ctx *pulumi.Context, args LookupWorkPoolOutputArgs, opts ...pulumi.InvokeOption) LookupWorkPoolResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupWorkPoolResult, error) {
			args := v.(LookupWorkPoolArgs)
			r, err := LookupWorkPool(ctx, &args, opts...)
			var s LookupWorkPoolResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupWorkPoolResultOutput)
}

// A collection of arguments for invoking getWorkPool.
type LookupWorkPoolOutputArgs struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId pulumi.StringPtrInput `pulumi:"accountId"`
	// The concurrency limit applied to this work pool
	ConcurrencyLimit pulumi.IntPtrInput `pulumi:"concurrencyLimit"`
	// The ID (UUID) of the default queue associated with this work pool
	DefaultQueueId pulumi.StringPtrInput `pulumi:"defaultQueueId"`
	// Description of the work pool
	Description pulumi.StringPtrInput `pulumi:"description"`
	// Work pool ID (UUID)
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Name of the work pool
	Name pulumi.StringPtrInput `pulumi:"name"`
	// Workspace ID (UUID), defaults to the workspace set in the provider
	WorkspaceId pulumi.StringPtrInput `pulumi:"workspaceId"`
}

func (LookupWorkPoolOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWorkPoolArgs)(nil)).Elem()
}

// A collection of values returned by getWorkPool.
type LookupWorkPoolResultOutput struct{ *pulumi.OutputState }

func (LookupWorkPoolResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWorkPoolResult)(nil)).Elem()
}

func (o LookupWorkPoolResultOutput) ToLookupWorkPoolResultOutput() LookupWorkPoolResultOutput {
	return o
}

func (o LookupWorkPoolResultOutput) ToLookupWorkPoolResultOutputWithContext(ctx context.Context) LookupWorkPoolResultOutput {
	return o
}

// Account ID (UUID), defaults to the account set in the provider
func (o LookupWorkPoolResultOutput) AccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWorkPoolResult) *string { return v.AccountId }).(pulumi.StringPtrOutput)
}

// The base job template for the work pool, as a JSON string
func (o LookupWorkPoolResultOutput) BaseJobTemplate() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWorkPoolResult) string { return v.BaseJobTemplate }).(pulumi.StringOutput)
}

// The concurrency limit applied to this work pool
func (o LookupWorkPoolResultOutput) ConcurrencyLimit() pulumi.IntOutput {
	return o.ApplyT(func(v LookupWorkPoolResult) int { return v.ConcurrencyLimit }).(pulumi.IntOutput)
}

// Date and time of the work pool creation in RFC 3339 format
func (o LookupWorkPoolResultOutput) Created() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWorkPoolResult) string { return v.Created }).(pulumi.StringOutput)
}

// The ID (UUID) of the default queue associated with this work pool
func (o LookupWorkPoolResultOutput) DefaultQueueId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWorkPoolResult) string { return v.DefaultQueueId }).(pulumi.StringOutput)
}

// Description of the work pool
func (o LookupWorkPoolResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWorkPoolResult) string { return v.Description }).(pulumi.StringOutput)
}

// Work pool ID (UUID)
func (o LookupWorkPoolResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWorkPoolResult) string { return v.Id }).(pulumi.StringOutput)
}

// Name of the work pool
func (o LookupWorkPoolResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWorkPoolResult) string { return v.Name }).(pulumi.StringOutput)
}

// Whether this work pool is paused
func (o LookupWorkPoolResultOutput) Paused() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupWorkPoolResult) bool { return v.Paused }).(pulumi.BoolOutput)
}

// Type of the work pool
func (o LookupWorkPoolResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWorkPoolResult) string { return v.Type }).(pulumi.StringOutput)
}

// Date and time that the work pool was last updated in RFC 3339 format
func (o LookupWorkPoolResultOutput) Updated() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWorkPoolResult) string { return v.Updated }).(pulumi.StringOutput)
}

// Workspace ID (UUID), defaults to the workspace set in the provider
func (o LookupWorkPoolResultOutput) WorkspaceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWorkPoolResult) *string { return v.WorkspaceId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupWorkPoolResultOutput{})
}
