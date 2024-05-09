// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Prefect
{
    public static class GetServiceAccount
    {
        /// <summary>
        /// Get information about an existing Service Account, by name or ID.
        /// &lt;br&gt;
        /// Use this data source to obtain service account-level attributes, such as ID.
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
        ///     var bot = Prefect.GetServiceAccount.Invoke(new()
        ///     {
        ///         Name = "my-bot-name",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetServiceAccountResult> InvokeAsync(GetServiceAccountArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetServiceAccountResult>("prefect:index/getServiceAccount:getServiceAccount", args ?? new GetServiceAccountArgs(), options.WithDefaults());

        /// <summary>
        /// Get information about an existing Service Account, by name or ID.
        /// &lt;br&gt;
        /// Use this data source to obtain service account-level attributes, such as ID.
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
        ///     var bot = Prefect.GetServiceAccount.Invoke(new()
        ///     {
        ///         Name = "my-bot-name",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetServiceAccountResult> Invoke(GetServiceAccountInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetServiceAccountResult>("prefect:index/getServiceAccount:getServiceAccount", args ?? new GetServiceAccountInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetServiceAccountArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Account ID (UUID), defaults to the account set in the provider
        /// </summary>
        [Input("accountId")]
        public string? AccountId { get; set; }

        /// <summary>
        /// Service Account ID (UUID)
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name of the service account
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetServiceAccountArgs()
        {
        }
        public static new GetServiceAccountArgs Empty => new GetServiceAccountArgs();
    }

    public sealed class GetServiceAccountInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Account ID (UUID), defaults to the account set in the provider
        /// </summary>
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        /// <summary>
        /// Service Account ID (UUID)
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of the service account
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetServiceAccountInvokeArgs()
        {
        }
        public static new GetServiceAccountInvokeArgs Empty => new GetServiceAccountInvokeArgs();
    }


    [OutputType]
    public sealed class GetServiceAccountResult
    {
        /// <summary>
        /// Account ID (UUID), defaults to the account set in the provider
        /// </summary>
        public readonly string? AccountId;
        /// <summary>
        /// Account Role name of the service account
        /// </summary>
        public readonly string AccountRoleName;
        /// <summary>
        /// API Key associated with the service account
        /// </summary>
        public readonly string ApiKey;
        /// <summary>
        /// Date and time that the API Key was created in RFC 3339 format
        /// </summary>
        public readonly string ApiKeyCreated;
        /// <summary>
        /// Date and time that the API Key expires in RFC 3339 format
        /// </summary>
        public readonly string ApiKeyExpiration;
        /// <summary>
        /// API Key ID associated with the service account. NOTE: this is always null for reads. If you need the API Key ID, use the `prefect.ServiceAccount` resource instead.
        /// </summary>
        public readonly string ApiKeyId;
        /// <summary>
        /// API Key Name associated with the service account
        /// </summary>
        public readonly string ApiKeyName;
        /// <summary>
        /// Timestamp of when the resource was created (RFC3339)
        /// </summary>
        public readonly string Created;
        /// <summary>
        /// Service Account ID (UUID)
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Name of the service account
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Timestamp of when the resource was updated (RFC3339)
        /// </summary>
        public readonly string Updated;

        [OutputConstructor]
        private GetServiceAccountResult(
            string? accountId,

            string accountRoleName,

            string apiKey,

            string apiKeyCreated,

            string apiKeyExpiration,

            string apiKeyId,

            string apiKeyName,

            string created,

            string id,

            string name,

            string updated)
        {
            AccountId = accountId;
            AccountRoleName = accountRoleName;
            ApiKey = apiKey;
            ApiKeyCreated = apiKeyCreated;
            ApiKeyExpiration = apiKeyExpiration;
            ApiKeyId = apiKeyId;
            ApiKeyName = apiKeyName;
            Created = created;
            Id = id;
            Name = name;
            Updated = updated;
        }
    }
}