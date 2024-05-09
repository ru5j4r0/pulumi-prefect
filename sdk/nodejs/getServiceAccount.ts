// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Get information about an existing Service Account, by name or ID.
 * <br>
 * Use this data source to obtain service account-level attributes, such as ID.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as prefect from "@pulumi/prefect";
 *
 * const bot = prefect.getServiceAccount({
 *     name: "my-bot-name",
 * });
 * ```
 */
export function getServiceAccount(args?: GetServiceAccountArgs, opts?: pulumi.InvokeOptions): Promise<GetServiceAccountResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("prefect:index/getServiceAccount:getServiceAccount", {
        "accountId": args.accountId,
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getServiceAccount.
 */
export interface GetServiceAccountArgs {
    /**
     * Account ID (UUID), defaults to the account set in the provider
     */
    accountId?: string;
    /**
     * Service Account ID (UUID)
     */
    id?: string;
    /**
     * Name of the service account
     */
    name?: string;
}

/**
 * A collection of values returned by getServiceAccount.
 */
export interface GetServiceAccountResult {
    /**
     * Account ID (UUID), defaults to the account set in the provider
     */
    readonly accountId?: string;
    /**
     * Account Role name of the service account
     */
    readonly accountRoleName: string;
    /**
     * API Key associated with the service account
     */
    readonly apiKey: string;
    /**
     * Date and time that the API Key was created in RFC 3339 format
     */
    readonly apiKeyCreated: string;
    /**
     * Date and time that the API Key expires in RFC 3339 format
     */
    readonly apiKeyExpiration: string;
    /**
     * API Key ID associated with the service account. NOTE: this is always null for reads. If you need the API Key ID, use the `prefect.ServiceAccount` resource instead.
     */
    readonly apiKeyId: string;
    /**
     * API Key Name associated with the service account
     */
    readonly apiKeyName: string;
    /**
     * Timestamp of when the resource was created (RFC3339)
     */
    readonly created: string;
    /**
     * Service Account ID (UUID)
     */
    readonly id: string;
    /**
     * Name of the service account
     */
    readonly name: string;
    /**
     * Timestamp of when the resource was updated (RFC3339)
     */
    readonly updated: string;
}
/**
 * Get information about an existing Service Account, by name or ID.
 * <br>
 * Use this data source to obtain service account-level attributes, such as ID.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as prefect from "@pulumi/prefect";
 *
 * const bot = prefect.getServiceAccount({
 *     name: "my-bot-name",
 * });
 * ```
 */
export function getServiceAccountOutput(args?: GetServiceAccountOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetServiceAccountResult> {
    return pulumi.output(args).apply((a: any) => getServiceAccount(a, opts))
}

/**
 * A collection of arguments for invoking getServiceAccount.
 */
export interface GetServiceAccountOutputArgs {
    /**
     * Account ID (UUID), defaults to the account set in the provider
     */
    accountId?: pulumi.Input<string>;
    /**
     * Service Account ID (UUID)
     */
    id?: pulumi.Input<string>;
    /**
     * Name of the service account
     */
    name?: pulumi.Input<string>;
}
