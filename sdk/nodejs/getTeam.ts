// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Get information about an existing Team by their name.
 * <br>
 * Use this data source to obtain team IDs to manage Workspace Access.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as prefect from "@pulumi/prefect";
 *
 * const myTeam = prefect.getTeam({
 *     name: "my-team",
 * });
 * ```
 */
export function getTeam(args?: GetTeamArgs, opts?: pulumi.InvokeOptions): Promise<GetTeamResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("prefect:index/getTeam:getTeam", {
        "accountId": args.accountId,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getTeam.
 */
export interface GetTeamArgs {
    /**
     * Account ID (UUID), defaults to the account set in the provider
     */
    accountId?: string;
    /**
     * Name of Team
     */
    name?: string;
}

/**
 * A collection of values returned by getTeam.
 */
export interface GetTeamResult {
    /**
     * Account ID (UUID), defaults to the account set in the provider
     */
    readonly accountId?: string;
    /**
     * Date and time of the team creation in RFC 3339 format
     */
    readonly created: string;
    /**
     * Description of team
     */
    readonly description: string;
    /**
     * Team ID (UUID)
     */
    readonly id: string;
    /**
     * Name of Team
     */
    readonly name: string;
    /**
     * Date and time that the team was last updated in RFC 3339 format
     */
    readonly updated: string;
}
/**
 * Get information about an existing Team by their name.
 * <br>
 * Use this data source to obtain team IDs to manage Workspace Access.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as prefect from "@pulumi/prefect";
 *
 * const myTeam = prefect.getTeam({
 *     name: "my-team",
 * });
 * ```
 */
export function getTeamOutput(args?: GetTeamOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTeamResult> {
    return pulumi.output(args).apply((a: any) => getTeam(a, opts))
}

/**
 * A collection of arguments for invoking getTeam.
 */
export interface GetTeamOutputArgs {
    /**
     * Account ID (UUID), defaults to the account set in the provider
     */
    accountId?: pulumi.Input<string>;
    /**
     * Name of Team
     */
    name?: pulumi.Input<string>;
}