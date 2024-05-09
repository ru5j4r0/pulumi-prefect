// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package prefect

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/ru5j4r0/pulumi-prefect/sdk/go/prefect/internal"
)

// Get information about an existing Account.
// <br>
// Use this data source to obtain account-level attributes
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
//			_, err := prefect.LookupAccount(ctx, nil, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupAccount(ctx *pulumi.Context, args *LookupAccountArgs, opts ...pulumi.InvokeOption) (*LookupAccountResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupAccountResult
	err := ctx.Invoke("prefect:index/getAccount:getAccount", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAccount.
type LookupAccountArgs struct {
	// Account ID (UUID)
	Id *string `pulumi:"id"`
}

// A collection of values returned by getAccount.
type LookupAccountResult struct {
	// Whether or not this account allows public workspaces
	AllowPublicWorkspaces bool `pulumi:"allowPublicWorkspaces"`
	// Billing email to apply to the account's Stripe customer
	BillingEmail string `pulumi:"billingEmail"`
	// Timestamp of when the resource was created (RFC3339)
	Created string `pulumi:"created"`
	// Unique handle of the account
	Handle string `pulumi:"handle"`
	// Account ID (UUID)
	Id *string `pulumi:"id"`
	// An optional for an external url associated with the account, e.g. https://prefect.io/
	Link string `pulumi:"link"`
	// An optional physical location for the account, e.g. Washington, D.C.
	Location string `pulumi:"location"`
	// Name of the account
	Name string `pulumi:"name"`
	// Timestamp of when the resource was updated (RFC3339)
	Updated string `pulumi:"updated"`
}

func LookupAccountOutput(ctx *pulumi.Context, args LookupAccountOutputArgs, opts ...pulumi.InvokeOption) LookupAccountResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAccountResult, error) {
			args := v.(LookupAccountArgs)
			r, err := LookupAccount(ctx, &args, opts...)
			var s LookupAccountResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAccountResultOutput)
}

// A collection of arguments for invoking getAccount.
type LookupAccountOutputArgs struct {
	// Account ID (UUID)
	Id pulumi.StringPtrInput `pulumi:"id"`
}

func (LookupAccountOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAccountArgs)(nil)).Elem()
}

// A collection of values returned by getAccount.
type LookupAccountResultOutput struct{ *pulumi.OutputState }

func (LookupAccountResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAccountResult)(nil)).Elem()
}

func (o LookupAccountResultOutput) ToLookupAccountResultOutput() LookupAccountResultOutput {
	return o
}

func (o LookupAccountResultOutput) ToLookupAccountResultOutputWithContext(ctx context.Context) LookupAccountResultOutput {
	return o
}

// Whether or not this account allows public workspaces
func (o LookupAccountResultOutput) AllowPublicWorkspaces() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupAccountResult) bool { return v.AllowPublicWorkspaces }).(pulumi.BoolOutput)
}

// Billing email to apply to the account's Stripe customer
func (o LookupAccountResultOutput) BillingEmail() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAccountResult) string { return v.BillingEmail }).(pulumi.StringOutput)
}

// Timestamp of when the resource was created (RFC3339)
func (o LookupAccountResultOutput) Created() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAccountResult) string { return v.Created }).(pulumi.StringOutput)
}

// Unique handle of the account
func (o LookupAccountResultOutput) Handle() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAccountResult) string { return v.Handle }).(pulumi.StringOutput)
}

// Account ID (UUID)
func (o LookupAccountResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAccountResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// An optional for an external url associated with the account, e.g. https://prefect.io/
func (o LookupAccountResultOutput) Link() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAccountResult) string { return v.Link }).(pulumi.StringOutput)
}

// An optional physical location for the account, e.g. Washington, D.C.
func (o LookupAccountResultOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAccountResult) string { return v.Location }).(pulumi.StringOutput)
}

// Name of the account
func (o LookupAccountResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAccountResult) string { return v.Name }).(pulumi.StringOutput)
}

// Timestamp of when the resource was updated (RFC3339)
func (o LookupAccountResultOutput) Updated() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAccountResult) string { return v.Updated }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAccountResultOutput{})
}