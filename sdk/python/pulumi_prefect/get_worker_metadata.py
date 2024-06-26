# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetWorkerMetadataResult',
    'AwaitableGetWorkerMetadataResult',
    'get_worker_metadata',
    'get_worker_metadata_output',
]

@pulumi.output_type
class GetWorkerMetadataResult:
    """
    A collection of values returned by getWorkerMetadata.
    """
    def __init__(__self__, base_job_configs=None, id=None):
        if base_job_configs and not isinstance(base_job_configs, dict):
            raise TypeError("Expected argument 'base_job_configs' to be a dict")
        pulumi.set(__self__, "base_job_configs", base_job_configs)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="baseJobConfigs")
    def base_job_configs(self) -> 'outputs.GetWorkerMetadataBaseJobConfigsResult':
        """
        A map of default base job configurations (JSON) for each of the primary worker types
        """
        return pulumi.get(self, "base_job_configs")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetWorkerMetadataResult(GetWorkerMetadataResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkerMetadataResult(
            base_job_configs=self.base_job_configs,
            id=self.id)


def get_worker_metadata(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkerMetadataResult:
    """
    Get metadata information about the common Worker types, such as Kubernetes, ECS, etc.
    <br>
    Use this data source to get the default base job configurations for those common Worker types.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prefect as prefect

    worker_metadata = prefect.get_worker_metadata()
    kubernetes = prefect.WorkPool("kubernetes",
        type="kubernetes",
        workspace_id=data["prefect_workspace"]["prd"]["id"],
        paused=False,
        base_job_template=worker_metadata.base_job_configs.kubernetes)
    ecs = prefect.WorkPool("ecs",
        type="ecs",
        workspace_id=data["prefect_workspace"]["prd"]["id"],
        paused=False,
        base_job_template=worker_metadata.base_job_configs.ecs)
    process = prefect.WorkPool("process",
        type="cloud-run:push",
        workspace_id=data["prefect_workspace"]["prd"]["id"],
        paused=False,
        base_job_template=worker_metadata.base_job_configs.cloud_run_push)
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('prefect:index/getWorkerMetadata:getWorkerMetadata', __args__, opts=opts, typ=GetWorkerMetadataResult).value

    return AwaitableGetWorkerMetadataResult(
        base_job_configs=pulumi.get(__ret__, 'base_job_configs'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_worker_metadata)
def get_worker_metadata_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkerMetadataResult]:
    """
    Get metadata information about the common Worker types, such as Kubernetes, ECS, etc.
    <br>
    Use this data source to get the default base job configurations for those common Worker types.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prefect as prefect

    worker_metadata = prefect.get_worker_metadata()
    kubernetes = prefect.WorkPool("kubernetes",
        type="kubernetes",
        workspace_id=data["prefect_workspace"]["prd"]["id"],
        paused=False,
        base_job_template=worker_metadata.base_job_configs.kubernetes)
    ecs = prefect.WorkPool("ecs",
        type="ecs",
        workspace_id=data["prefect_workspace"]["prd"]["id"],
        paused=False,
        base_job_template=worker_metadata.base_job_configs.ecs)
    process = prefect.WorkPool("process",
        type="cloud-run:push",
        workspace_id=data["prefect_workspace"]["prd"]["id"],
        paused=False,
        base_job_template=worker_metadata.base_job_configs.cloud_run_push)
    ```
    """
    ...
