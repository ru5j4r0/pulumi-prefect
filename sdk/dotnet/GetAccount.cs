// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Prefect
{
    public static class GetAccount
    {
        /// <summary>
        /// Get information about an existing Account.
        /// &lt;br&gt;
        /// Use this data source to obtain account-level attributes
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Prefect = Pulumi.Prefect;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var myOrganization = Prefect.GetAccount.Invoke();
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetAccountResult> InvokeAsync(GetAccountArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetAccountResult>("prefect:index/getAccount:getAccount", args ?? new GetAccountArgs(), options.WithDefaults());

        /// <summary>
        /// Get information about an existing Account.
        /// &lt;br&gt;
        /// Use this data source to obtain account-level attributes
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Prefect = Pulumi.Prefect;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var myOrganization = Prefect.GetAccount.Invoke();
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetAccountResult> Invoke(GetAccountInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetAccountResult>("prefect:index/getAccount:getAccount", args ?? new GetAccountInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAccountArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Account ID (UUID)
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        public GetAccountArgs()
        {
        }
        public static new GetAccountArgs Empty => new GetAccountArgs();
    }

    public sealed class GetAccountInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Account ID (UUID)
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        public GetAccountInvokeArgs()
        {
        }
        public static new GetAccountInvokeArgs Empty => new GetAccountInvokeArgs();
    }


    [OutputType]
    public sealed class GetAccountResult
    {
        /// <summary>
        /// Whether or not this account allows public workspaces
        /// </summary>
        public readonly bool AllowPublicWorkspaces;
        /// <summary>
        /// Billing email to apply to the account's Stripe customer
        /// </summary>
        public readonly string BillingEmail;
        /// <summary>
        /// Timestamp of when the resource was created (RFC3339)
        /// </summary>
        public readonly string Created;
        /// <summary>
        /// Unique handle of the account
        /// </summary>
        public readonly string Handle;
        /// <summary>
        /// Account ID (UUID)
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// An optional for an external url associated with the account, e.g. https://prefect.io/
        /// </summary>
        public readonly string Link;
        /// <summary>
        /// An optional physical location for the account, e.g. Washington, D.C.
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// Name of the account
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Timestamp of when the resource was updated (RFC3339)
        /// </summary>
        public readonly string Updated;

        [OutputConstructor]
        private GetAccountResult(
            bool allowPublicWorkspaces,

            string billingEmail,

            string created,

            string handle,

            string? id,

            string link,

            string location,

            string name,

            string updated)
        {
            AllowPublicWorkspaces = allowPublicWorkspaces;
            BillingEmail = billingEmail;
            Created = created;
            Handle = handle;
            Id = id;
            Link = link;
            Location = location;
            Name = name;
            Updated = updated;
        }
    }
}
