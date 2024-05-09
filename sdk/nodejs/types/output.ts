// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface GetAccountMembersMember {
    /**
     * Acount Role ID (UUID)
     */
    accountRoleId: string;
    /**
     * Name of Account Role assigned to member
     */
    accountRoleName: string;
    /**
     * Actor ID (UUID)
     */
    actorId: string;
    /**
     * Member email
     */
    email: string;
    /**
     * Member's first name
     */
    firstName: string;
    /**
     * Member handle, or a human-readable identifier
     */
    handle: string;
    /**
     * Account Member ID (UUID)
     */
    id: string;
    /**
     * Member's last name
     */
    lastName: string;
    /**
     * User ID (UUID)
     */
    userId: string;
}

export interface GetTeamsTeam {
    /**
     * Date and time of the team creation in RFC 3339 format
     */
    created: string;
    /**
     * Description of team
     */
    description: string;
    /**
     * Team ID (UUID)
     */
    id: string;
    /**
     * Name of Team
     */
    name: string;
    /**
     * Date and time that the team was last updated in RFC 3339 format
     */
    updated: string;
}

export interface GetWorkPoolsWorkPool {
    /**
     * The base job template for the work pool, as a JSON string
     */
    baseJobTemplate: string;
    /**
     * The concurrency limit applied to this work pool
     */
    concurrencyLimit: number;
    /**
     * Date and time of the work pool creation in RFC 3339 format
     */
    created: string;
    /**
     * The ID (UUID) of the default queue associated with this work pool
     */
    defaultQueueId: string;
    /**
     * Description of the work pool
     */
    description: string;
    /**
     * Work pool ID (UUID)
     */
    id: string;
    /**
     * Name of the work pool
     */
    name: string;
    /**
     * Whether this work pool is paused
     */
    paused: boolean;
    /**
     * Type of the work pool
     */
    type: string;
    /**
     * Date and time that the work pool was last updated in RFC 3339 format
     */
    updated: string;
}

export interface GetWorkerMetadataBaseJobConfigs {
    /**
     * Default base job configuration for Azure Container Instances workers
     */
    azureContainerInstances: string;
    /**
     * Default base job configuration for Azure Container Instances Push workers
     */
    azureContainerInstancesPush: string;
    /**
     * Default base job configuration for Cloud Run workers
     */
    cloudRun: string;
    /**
     * Default base job configuration for Cloud Run Push workers
     */
    cloudRunPush: string;
    /**
     * Default base job configuration for Docker workers
     */
    docker: string;
    /**
     * Default base job configuration for ECS workers
     */
    ecs: string;
    /**
     * Default base job configuration for ECS Push workers
     */
    ecsPush: string;
    /**
     * Default base job configuration for Kubernetes workers
     */
    kubernetes: string;
    /**
     * Default base job configuration for Prefect Agent workers
     */
    prefectAgent: string;
    /**
     * Default base job configuration for Process workers
     */
    process: string;
    /**
     * Default base job configuration for Vertex AI workers
     */
    vertexAi: string;
}

