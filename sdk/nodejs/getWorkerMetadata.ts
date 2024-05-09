// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Get metadata information about the common Worker types, such as Kubernetes, ECS, etc.
 * <br>
 * Use this data source to get the default base job configurations for those common Worker types.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as prefect from "@pulumi/prefect";
 *
 * const workerMetadata = prefect.getWorkerMetadata({});
 * const kubernetes = new prefect.WorkPool("kubernetes", {
 *     type: "kubernetes",
 *     workspaceId: data.prefect_workspace.prd.id,
 *     paused: false,
 *     baseJobTemplate: workerMetadata.then(workerMetadata => workerMetadata.baseJobConfigs?.kubernetes),
 * });
 * const ecs = new prefect.WorkPool("ecs", {
 *     type: "ecs",
 *     workspaceId: data.prefect_workspace.prd.id,
 *     paused: false,
 *     baseJobTemplate: workerMetadata.then(workerMetadata => workerMetadata.baseJobConfigs?.ecs),
 * });
 * const process = new prefect.WorkPool("process", {
 *     type: "cloud-run:push",
 *     workspaceId: data.prefect_workspace.prd.id,
 *     paused: false,
 *     baseJobTemplate: workerMetadata.then(workerMetadata => workerMetadata.baseJobConfigs?.cloudRunPush),
 * });
 * ```
 */
export function getWorkerMetadata(opts?: pulumi.InvokeOptions): Promise<GetWorkerMetadataResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("prefect:index/getWorkerMetadata:getWorkerMetadata", {
    }, opts);
}

/**
 * A collection of values returned by getWorkerMetadata.
 */
export interface GetWorkerMetadataResult {
    /**
     * A map of default base job configurations (JSON) for each of the primary worker types
     */
    readonly baseJobConfigs: outputs.GetWorkerMetadataBaseJobConfigs;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
/**
 * Get metadata information about the common Worker types, such as Kubernetes, ECS, etc.
 * <br>
 * Use this data source to get the default base job configurations for those common Worker types.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as prefect from "@pulumi/prefect";
 *
 * const workerMetadata = prefect.getWorkerMetadata({});
 * const kubernetes = new prefect.WorkPool("kubernetes", {
 *     type: "kubernetes",
 *     workspaceId: data.prefect_workspace.prd.id,
 *     paused: false,
 *     baseJobTemplate: workerMetadata.then(workerMetadata => workerMetadata.baseJobConfigs?.kubernetes),
 * });
 * const ecs = new prefect.WorkPool("ecs", {
 *     type: "ecs",
 *     workspaceId: data.prefect_workspace.prd.id,
 *     paused: false,
 *     baseJobTemplate: workerMetadata.then(workerMetadata => workerMetadata.baseJobConfigs?.ecs),
 * });
 * const process = new prefect.WorkPool("process", {
 *     type: "cloud-run:push",
 *     workspaceId: data.prefect_workspace.prd.id,
 *     paused: false,
 *     baseJobTemplate: workerMetadata.then(workerMetadata => workerMetadata.baseJobConfigs?.cloudRunPush),
 * });
 * ```
 */
export function getWorkerMetadataOutput(opts?: pulumi.InvokeOptions): pulumi.Output<GetWorkerMetadataResult> {
    return pulumi.output(getWorkerMetadata(opts))
}
