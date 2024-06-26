// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package prefect

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/ru5j4r0/pulumi-prefect/sdk/go/prefect/internal"
)

// Get information about all members of account.
// <br>
// Use this data source to obtain user or actor IDs to manage Workspace Access.
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
//			_, err := prefect.GetAccountMembers(ctx, nil, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetAccountMembers(ctx *pulumi.Context, args *GetAccountMembersArgs, opts ...pulumi.InvokeOption) (*GetAccountMembersResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetAccountMembersResult
	err := ctx.Invoke("prefect:index/getAccountMembers:getAccountMembers", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAccountMembers.
type GetAccountMembersArgs struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId *string `pulumi:"accountId"`
}

// A collection of values returned by getAccountMembers.
type GetAccountMembersResult struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId *string `pulumi:"accountId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// List of Account members of an account
	Members []GetAccountMembersMember `pulumi:"members"`
}

func GetAccountMembersOutput(ctx *pulumi.Context, args GetAccountMembersOutputArgs, opts ...pulumi.InvokeOption) GetAccountMembersResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetAccountMembersResult, error) {
			args := v.(GetAccountMembersArgs)
			r, err := GetAccountMembers(ctx, &args, opts...)
			var s GetAccountMembersResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetAccountMembersResultOutput)
}

// A collection of arguments for invoking getAccountMembers.
type GetAccountMembersOutputArgs struct {
	// Account ID (UUID), defaults to the account set in the provider
	AccountId pulumi.StringPtrInput `pulumi:"accountId"`
}

func (GetAccountMembersOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAccountMembersArgs)(nil)).Elem()
}

// A collection of values returned by getAccountMembers.
type GetAccountMembersResultOutput struct{ *pulumi.OutputState }

func (GetAccountMembersResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAccountMembersResult)(nil)).Elem()
}

func (o GetAccountMembersResultOutput) ToGetAccountMembersResultOutput() GetAccountMembersResultOutput {
	return o
}

func (o GetAccountMembersResultOutput) ToGetAccountMembersResultOutputWithContext(ctx context.Context) GetAccountMembersResultOutput {
	return o
}

// Account ID (UUID), defaults to the account set in the provider
func (o GetAccountMembersResultOutput) AccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetAccountMembersResult) *string { return v.AccountId }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetAccountMembersResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetAccountMembersResult) string { return v.Id }).(pulumi.StringOutput)
}

// List of Account members of an account
func (o GetAccountMembersResultOutput) Members() GetAccountMembersMemberArrayOutput {
	return o.ApplyT(func(v GetAccountMembersResult) []GetAccountMembersMember { return v.Members }).(GetAccountMembersMemberArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetAccountMembersResultOutput{})
}
