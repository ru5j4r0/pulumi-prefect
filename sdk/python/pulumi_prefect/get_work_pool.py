# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetWorkPoolResult',
    'AwaitableGetWorkPoolResult',
    'get_work_pool',
    'get_work_pool_output',
]

@pulumi.output_type
class GetWorkPoolResult:
    """
    A collection of values returned by getWorkPool.
    """
    def __init__(__self__, account_id=None, base_job_template=None, concurrency_limit=None, created=None, default_queue_id=None, description=None, id=None, name=None, paused=None, type=None, updated=None, workspace_id=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if base_job_template and not isinstance(base_job_template, str):
            raise TypeError("Expected argument 'base_job_template' to be a str")
        pulumi.set(__self__, "base_job_template", base_job_template)
        if concurrency_limit and not isinstance(concurrency_limit, int):
            raise TypeError("Expected argument 'concurrency_limit' to be a int")
        pulumi.set(__self__, "concurrency_limit", concurrency_limit)
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if default_queue_id and not isinstance(default_queue_id, str):
            raise TypeError("Expected argument 'default_queue_id' to be a str")
        pulumi.set(__self__, "default_queue_id", default_queue_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if paused and not isinstance(paused, bool):
            raise TypeError("Expected argument 'paused' to be a bool")
        pulumi.set(__self__, "paused", paused)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated and not isinstance(updated, str):
            raise TypeError("Expected argument 'updated' to be a str")
        pulumi.set(__self__, "updated", updated)
        if workspace_id and not isinstance(workspace_id, str):
            raise TypeError("Expected argument 'workspace_id' to be a str")
        pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[str]:
        """
        Account ID (UUID), defaults to the account set in the provider
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="baseJobTemplate")
    def base_job_template(self) -> str:
        """
        The base job template for the work pool, as a JSON string
        """
        return pulumi.get(self, "base_job_template")

    @property
    @pulumi.getter(name="concurrencyLimit")
    def concurrency_limit(self) -> int:
        """
        The concurrency limit applied to this work pool
        """
        return pulumi.get(self, "concurrency_limit")

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        Date and time of the work pool creation in RFC 3339 format
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="defaultQueueId")
    def default_queue_id(self) -> str:
        """
        The ID (UUID) of the default queue associated with this work pool
        """
        return pulumi.get(self, "default_queue_id")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the work pool
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Work pool ID (UUID)
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the work pool
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def paused(self) -> bool:
        """
        Whether this work pool is paused
        """
        return pulumi.get(self, "paused")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the work pool
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def updated(self) -> str:
        """
        Date and time that the work pool was last updated in RFC 3339 format
        """
        return pulumi.get(self, "updated")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[str]:
        """
        Workspace ID (UUID), defaults to the workspace set in the provider
        """
        return pulumi.get(self, "workspace_id")


class AwaitableGetWorkPoolResult(GetWorkPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkPoolResult(
            account_id=self.account_id,
            base_job_template=self.base_job_template,
            concurrency_limit=self.concurrency_limit,
            created=self.created,
            default_queue_id=self.default_queue_id,
            description=self.description,
            id=self.id,
            name=self.name,
            paused=self.paused,
            type=self.type,
            updated=self.updated,
            workspace_id=self.workspace_id)


def get_work_pool(account_id: Optional[str] = None,
                  concurrency_limit: Optional[int] = None,
                  default_queue_id: Optional[str] = None,
                  description: Optional[str] = None,
                  id: Optional[str] = None,
                  name: Optional[str] = None,
                  workspace_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkPoolResult:
    """
    Get information about an existing Work Pool by name.
    <br>
    Use this data source to obtain Work Pool-specific attributes.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prefect as prefect

    my_pool = prefect.get_work_pool(name="my-work-pool")
    ```


    :param str account_id: Account ID (UUID), defaults to the account set in the provider
    :param int concurrency_limit: The concurrency limit applied to this work pool
    :param str default_queue_id: The ID (UUID) of the default queue associated with this work pool
    :param str description: Description of the work pool
    :param str id: Work pool ID (UUID)
    :param str name: Name of the work pool
    :param str workspace_id: Workspace ID (UUID), defaults to the workspace set in the provider
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['concurrencyLimit'] = concurrency_limit
    __args__['defaultQueueId'] = default_queue_id
    __args__['description'] = description
    __args__['id'] = id
    __args__['name'] = name
    __args__['workspaceId'] = workspace_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('prefect:index/getWorkPool:getWorkPool', __args__, opts=opts, typ=GetWorkPoolResult).value

    return AwaitableGetWorkPoolResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        base_job_template=pulumi.get(__ret__, 'base_job_template'),
        concurrency_limit=pulumi.get(__ret__, 'concurrency_limit'),
        created=pulumi.get(__ret__, 'created'),
        default_queue_id=pulumi.get(__ret__, 'default_queue_id'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        paused=pulumi.get(__ret__, 'paused'),
        type=pulumi.get(__ret__, 'type'),
        updated=pulumi.get(__ret__, 'updated'),
        workspace_id=pulumi.get(__ret__, 'workspace_id'))


@_utilities.lift_output_func(get_work_pool)
def get_work_pool_output(account_id: Optional[pulumi.Input[Optional[str]]] = None,
                         concurrency_limit: Optional[pulumi.Input[Optional[int]]] = None,
                         default_queue_id: Optional[pulumi.Input[Optional[str]]] = None,
                         description: Optional[pulumi.Input[Optional[str]]] = None,
                         id: Optional[pulumi.Input[Optional[str]]] = None,
                         name: Optional[pulumi.Input[Optional[str]]] = None,
                         workspace_id: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkPoolResult]:
    """
    Get information about an existing Work Pool by name.
    <br>
    Use this data source to obtain Work Pool-specific attributes.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prefect as prefect

    my_pool = prefect.get_work_pool(name="my-work-pool")
    ```


    :param str account_id: Account ID (UUID), defaults to the account set in the provider
    :param int concurrency_limit: The concurrency limit applied to this work pool
    :param str default_queue_id: The ID (UUID) of the default queue associated with this work pool
    :param str description: Description of the work pool
    :param str id: Work pool ID (UUID)
    :param str name: Name of the work pool
    :param str workspace_id: Workspace ID (UUID), defaults to the workspace set in the provider
    """
    ...
