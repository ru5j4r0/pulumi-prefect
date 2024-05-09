// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package prefect

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/ru5j4r0/pulumi-prefect/sdk/go/prefect/internal"
)

// Get information about an existing Variable by name or ID.
// <br>
// Use this data source to obtain Variable-specific attributes, such as the value.
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
//			_, err := prefect.LookupVariable(ctx, &prefect.LookupVariableArgs{
//				Id: pulumi.StringRef("00000000-0000-0000-0000-000000000000"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			_, err = prefect.LookupVariable(ctx, &prefect.LookupVariableArgs{
//				Name: pulumi.StringRef("my_variable_name"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupVariable(ctx *pulumi.Context, args *LookupVariableArgs, opts ...pulumi.InvokeOption) (*LookupVariableResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupVariableResult
	err := ctx.Invoke("prefect:index/getVariable:getVariable", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVariable.
type LookupVariableArgs struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId *string `pulumi:"accountId"`
	// Variable ID (UUID)
	Id *string `pulumi:"id"`
	// Name of the variable
	Name *string `pulumi:"name"`
	// Workspace ID (UUID), defaults to the workspace set in the provider
	WorkspaceId *string `pulumi:"workspaceId"`
}

// A collection of values returned by getVariable.
type LookupVariableResult struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId *string `pulumi:"accountId"`
	// Timestamp of when the resource was created (RFC3339)
	Created string `pulumi:"created"`
	// Variable ID (UUID)
	Id string `pulumi:"id"`
	// Name of the variable
	Name string `pulumi:"name"`
	// Tags associated with the variable
	Tags []string `pulumi:"tags"`
	// Timestamp of when the resource was updated (RFC3339)
	Updated string `pulumi:"updated"`
	// Value of the variable
	Value string `pulumi:"value"`
	// Workspace ID (UUID), defaults to the workspace set in the provider
	WorkspaceId *string `pulumi:"workspaceId"`
}

func LookupVariableOutput(ctx *pulumi.Context, args LookupVariableOutputArgs, opts ...pulumi.InvokeOption) LookupVariableResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupVariableResult, error) {
			args := v.(LookupVariableArgs)
			r, err := LookupVariable(ctx, &args, opts...)
			var s LookupVariableResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupVariableResultOutput)
}

// A collection of arguments for invoking getVariable.
type LookupVariableOutputArgs struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId pulumi.StringPtrInput `pulumi:"accountId"`
	// Variable ID (UUID)
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Name of the variable
	Name pulumi.StringPtrInput `pulumi:"name"`
	// Workspace ID (UUID), defaults to the workspace set in the provider
	WorkspaceId pulumi.StringPtrInput `pulumi:"workspaceId"`
}

func (LookupVariableOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVariableArgs)(nil)).Elem()
}

// A collection of values returned by getVariable.
type LookupVariableResultOutput struct{ *pulumi.OutputState }

func (LookupVariableResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVariableResult)(nil)).Elem()
}

func (o LookupVariableResultOutput) ToLookupVariableResultOutput() LookupVariableResultOutput {
	return o
}

func (o LookupVariableResultOutput) ToLookupVariableResultOutputWithContext(ctx context.Context) LookupVariableResultOutput {
	return o
}

// Account ID (UUID), defaults to the account set in the provider
func (o LookupVariableResultOutput) AccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVariableResult) *string { return v.AccountId }).(pulumi.StringPtrOutput)
}

// Timestamp of when the resource was created (RFC3339)
func (o LookupVariableResultOutput) Created() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVariableResult) string { return v.Created }).(pulumi.StringOutput)
}

// Variable ID (UUID)
func (o LookupVariableResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVariableResult) string { return v.Id }).(pulumi.StringOutput)
}

// Name of the variable
func (o LookupVariableResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVariableResult) string { return v.Name }).(pulumi.StringOutput)
}

// Tags associated with the variable
func (o LookupVariableResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupVariableResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

// Timestamp of when the resource was updated (RFC3339)
func (o LookupVariableResultOutput) Updated() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVariableResult) string { return v.Updated }).(pulumi.StringOutput)
}

// Value of the variable
func (o LookupVariableResultOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVariableResult) string { return v.Value }).(pulumi.StringOutput)
}

// Workspace ID (UUID), defaults to the workspace set in the provider
func (o LookupVariableResultOutput) WorkspaceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVariableResult) *string { return v.WorkspaceId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupVariableResultOutput{})
}