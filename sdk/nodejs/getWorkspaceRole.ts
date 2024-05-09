// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Get information about an existing Workspace Role.
 * <br>
 * Use this data source read down the pre-defined Roles, to manage User and Service Account access.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as prefect from "@pulumi/prefect";
 *
 * const owner = prefect.getWorkspaceRole({
 *     name: "Owner",
 * });
 * const worker = prefect.getWorkspaceRole({
 *     name: "Worker",
 * });
 * const developer = prefect.getWorkspaceRole({
 *     name: "Developer",
 * });
 * const viewer = prefect.getWorkspaceRole({
 *     name: "Viewer",
 * });
 * const runner = prefect.getWorkspaceRole({
 *     name: "Runner",
 * });
 * ```
 */
export function getWorkspaceRole(args: GetWorkspaceRoleArgs, opts?: pulumi.InvokeOptions): Promise<GetWorkspaceRoleResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("prefect:index/getWorkspaceRole:getWorkspaceRole", {
        "accountId": args.accountId,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getWorkspaceRole.
 */
export interface GetWorkspaceRoleArgs {
    /**
     * Account ID (UUID) where Workspace Role resides
     */
    accountId?: string;
    /**
     * Name of the Workspace Role
     */
    name: string;
}

/**
 * A collection of values returned by getWorkspaceRole.
 */
export interface GetWorkspaceRoleResult {
    /**
     * Account ID (UUID) where Workspace Role resides
     */
    readonly accountId?: string;
    /**
     * Timestamp of when the resource was created (RFC3339)
     */
    readonly created: string;
    /**
     * Description of the Workspace Role
     */
    readonly description: string;
    /**
     * Workspace Role ID (UUID)
     */
    readonly id: string;
    /**
     * Workspace Role ID (UUID), whose permissions are inherited by this Workspace Role
     */
    readonly inheritedRoleId: string;
    /**
     * Name of the Workspace Role
     */
    readonly name: string;
    /**
     * List of scopes linked to the Workspace Role
     */
    readonly scopes: string[];
    /**
     * Timestamp of when the resource was updated (RFC3339)
     */
    readonly updated: string;
}
/**
 * Get information about an existing Workspace Role.
 * <br>
 * Use this data source read down the pre-defined Roles, to manage User and Service Account access.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as prefect from "@pulumi/prefect";
 *
 * const owner = prefect.getWorkspaceRole({
 *     name: "Owner",
 * });
 * const worker = prefect.getWorkspaceRole({
 *     name: "Worker",
 * });
 * const developer = prefect.getWorkspaceRole({
 *     name: "Developer",
 * });
 * const viewer = prefect.getWorkspaceRole({
 *     name: "Viewer",
 * });
 * const runner = prefect.getWorkspaceRole({
 *     name: "Runner",
 * });
 * ```
 */
export function getWorkspaceRoleOutput(args: GetWorkspaceRoleOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetWorkspaceRoleResult> {
    return pulumi.output(args).apply((a: any) => getWorkspaceRole(a, opts))
}

/**
 * A collection of arguments for invoking getWorkspaceRole.
 */
export interface GetWorkspaceRoleOutputArgs {
    /**
     * Account ID (UUID) where Workspace Role resides
     */
    accountId?: pulumi.Input<string>;
    /**
     * Name of the Workspace Role
     */
    name: pulumi.Input<string>;
}
