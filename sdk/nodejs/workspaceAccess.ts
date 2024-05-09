// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The resource `workspaceAccess` represents a connection between an accessor (User, Service Account or Team) with a Workspace Role. This resource specifies an actor's access level to a specific Workspace in the Account.
 *
 * Use this resource in conjunction with the `workspaceRole` resource or data source to manage access to Workspaces.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as prefect from "@pulumi/prefect";
 *
 * const developer = prefect.getWorkspaceRole({
 *     name: "Developer",
 * });
 * const marvin = prefect.getAccountMember({
 *     email: "marvin@prefect.io",
 * });
 * // Assign the Workspace Role to the Account Member
 * const marvinDeveloper = new prefect.WorkspaceAccess("marvinDeveloper", {
 *     accessorType: "USER",
 *     accessorId: prefect_account_member.marvin.user_id,
 *     workspaceId: "00000000-0000-0000-0000-000000000000",
 *     workspaceRoleId: developer.then(developer => developer.id),
 * });
 * // ASSIGNING WORKSPACE ACCESS TO A SERVICE ACCOUNT
 * // Create a Service Account resource
 * const bot = new prefect.ServiceAccount("bot", {});
 * // Assign the Workspace Role to the Service Account
 * const botDeveloper = new prefect.WorkspaceAccess("botDeveloper", {
 *     accessorType: "SERVICE_ACCOUNT",
 *     accessorId: bot.id,
 *     workspaceId: "00000000-0000-0000-0000-000000000000",
 *     workspaceRoleId: developer.then(developer => developer.id),
 * });
 * // ASSIGNING WORKSPACE ACCESS TO A TEAM
 * // Assign the Workspace Role to the Team
 * const teamDeveloper = new prefect.WorkspaceAccess("teamDeveloper", {
 *     accessorType: "TEAM",
 *     accessorId: "11111111-1111-1111-1111-111111111111",
 *     workspaceId: "00000000-0000-0000-0000-000000000000",
 *     workspaceRoleId: developer.then(developer => developer.id),
 * });
 * ```
 */
export class WorkspaceAccess extends pulumi.CustomResource {
    /**
     * Get an existing WorkspaceAccess resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WorkspaceAccessState, opts?: pulumi.CustomResourceOptions): WorkspaceAccess {
        return new WorkspaceAccess(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'prefect:index/workspaceAccess:WorkspaceAccess';

    /**
     * Returns true if the given object is an instance of WorkspaceAccess.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is WorkspaceAccess {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === WorkspaceAccess.__pulumiType;
    }

    /**
     * ID (UUID) of accessor to the workspace. This can be an `account_member.user_id` or `service_account.id`
     */
    public readonly accessorId!: pulumi.Output<string>;
    /**
     * USER | SERVICE_ACCOUNT | TEAM
     */
    public readonly accessorType!: pulumi.Output<string>;
    /**
     * Account ID (UUID) where the workspace is located
     */
    public readonly accountId!: pulumi.Output<string | undefined>;
    /**
     * Workspace ID (UUID) to grant access to
     */
    public readonly workspaceId!: pulumi.Output<string | undefined>;
    /**
     * Workspace Role ID (UUID) to grant to accessor
     */
    public readonly workspaceRoleId!: pulumi.Output<string>;

    /**
     * Create a WorkspaceAccess resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WorkspaceAccessArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: WorkspaceAccessArgs | WorkspaceAccessState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as WorkspaceAccessState | undefined;
            resourceInputs["accessorId"] = state ? state.accessorId : undefined;
            resourceInputs["accessorType"] = state ? state.accessorType : undefined;
            resourceInputs["accountId"] = state ? state.accountId : undefined;
            resourceInputs["workspaceId"] = state ? state.workspaceId : undefined;
            resourceInputs["workspaceRoleId"] = state ? state.workspaceRoleId : undefined;
        } else {
            const args = argsOrState as WorkspaceAccessArgs | undefined;
            if ((!args || args.accessorId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'accessorId'");
            }
            if ((!args || args.accessorType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'accessorType'");
            }
            if ((!args || args.workspaceRoleId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'workspaceRoleId'");
            }
            resourceInputs["accessorId"] = args ? args.accessorId : undefined;
            resourceInputs["accessorType"] = args ? args.accessorType : undefined;
            resourceInputs["accountId"] = args ? args.accountId : undefined;
            resourceInputs["workspaceId"] = args ? args.workspaceId : undefined;
            resourceInputs["workspaceRoleId"] = args ? args.workspaceRoleId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(WorkspaceAccess.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering WorkspaceAccess resources.
 */
export interface WorkspaceAccessState {
    /**
     * ID (UUID) of accessor to the workspace. This can be an `account_member.user_id` or `service_account.id`
     */
    accessorId?: pulumi.Input<string>;
    /**
     * USER | SERVICE_ACCOUNT | TEAM
     */
    accessorType?: pulumi.Input<string>;
    /**
     * Account ID (UUID) where the workspace is located
     */
    accountId?: pulumi.Input<string>;
    /**
     * Workspace ID (UUID) to grant access to
     */
    workspaceId?: pulumi.Input<string>;
    /**
     * Workspace Role ID (UUID) to grant to accessor
     */
    workspaceRoleId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a WorkspaceAccess resource.
 */
export interface WorkspaceAccessArgs {
    /**
     * ID (UUID) of accessor to the workspace. This can be an `account_member.user_id` or `service_account.id`
     */
    accessorId: pulumi.Input<string>;
    /**
     * USER | SERVICE_ACCOUNT | TEAM
     */
    accessorType: pulumi.Input<string>;
    /**
     * Account ID (UUID) where the workspace is located
     */
    accountId?: pulumi.Input<string>;
    /**
     * Workspace ID (UUID) to grant access to
     */
    workspaceId?: pulumi.Input<string>;
    /**
     * Workspace Role ID (UUID) to grant to accessor
     */
    workspaceRoleId: pulumi.Input<string>;
}