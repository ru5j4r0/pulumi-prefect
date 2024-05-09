// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Get information about an existing Variable by name or ID.
 * <br>
 * Use this data source to obtain Variable-specific attributes, such as the value.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as prefect from "@pulumi/prefect";
 *
 * const existingById = prefect.getVariable({
 *     id: "00000000-0000-0000-0000-000000000000",
 * });
 * const existingByName = prefect.getVariable({
 *     name: "my_variable_name",
 * });
 * ```
 */
export function getVariable(args?: GetVariableArgs, opts?: pulumi.InvokeOptions): Promise<GetVariableResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("prefect:index/getVariable:getVariable", {
        "accountId": args.accountId,
        "id": args.id,
        "name": args.name,
        "workspaceId": args.workspaceId,
    }, opts);
}

/**
 * A collection of arguments for invoking getVariable.
 */
export interface GetVariableArgs {
    /**
     * Account ID (UUID), defaults to the account set in the provider
     */
    accountId?: string;
    /**
     * Variable ID (UUID)
     */
    id?: string;
    /**
     * Name of the variable
     */
    name?: string;
    /**
     * Workspace ID (UUID), defaults to the workspace set in the provider
     */
    workspaceId?: string;
}

/**
 * A collection of values returned by getVariable.
 */
export interface GetVariableResult {
    /**
     * Account ID (UUID), defaults to the account set in the provider
     */
    readonly accountId?: string;
    /**
     * Timestamp of when the resource was created (RFC3339)
     */
    readonly created: string;
    /**
     * Variable ID (UUID)
     */
    readonly id: string;
    /**
     * Name of the variable
     */
    readonly name: string;
    /**
     * Tags associated with the variable
     */
    readonly tags: string[];
    /**
     * Timestamp of when the resource was updated (RFC3339)
     */
    readonly updated: string;
    /**
     * Value of the variable
     */
    readonly value: string;
    /**
     * Workspace ID (UUID), defaults to the workspace set in the provider
     */
    readonly workspaceId?: string;
}
/**
 * Get information about an existing Variable by name or ID.
 * <br>
 * Use this data source to obtain Variable-specific attributes, such as the value.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as prefect from "@pulumi/prefect";
 *
 * const existingById = prefect.getVariable({
 *     id: "00000000-0000-0000-0000-000000000000",
 * });
 * const existingByName = prefect.getVariable({
 *     name: "my_variable_name",
 * });
 * ```
 */
export function getVariableOutput(args?: GetVariableOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetVariableResult> {
    return pulumi.output(args).apply((a: any) => getVariable(a, opts))
}

/**
 * A collection of arguments for invoking getVariable.
 */
export interface GetVariableOutputArgs {
    /**
     * Account ID (UUID), defaults to the account set in the provider
     */
    accountId?: pulumi.Input<string>;
    /**
     * Variable ID (UUID)
     */
    id?: pulumi.Input<string>;
    /**
     * Name of the variable
     */
    name?: pulumi.Input<string>;
    /**
     * Workspace ID (UUID), defaults to the workspace set in the provider
     */
    workspaceId?: pulumi.Input<string>;
}