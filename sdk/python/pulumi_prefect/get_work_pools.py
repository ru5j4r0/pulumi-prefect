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
    'GetWorkPoolsResult',
    'AwaitableGetWorkPoolsResult',
    'get_work_pools',
    'get_work_pools_output',
]

@pulumi.output_type
class GetWorkPoolsResult:
    """
    A collection of values returned by getWorkPools.
    """
    def __init__(__self__, account_id=None, filter_anies=None, id=None, work_pools=None, workspace_id=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if filter_anies and not isinstance(filter_anies, list):
            raise TypeError("Expected argument 'filter_anies' to be a list")
        pulumi.set(__self__, "filter_anies", filter_anies)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if work_pools and not isinstance(work_pools, list):
            raise TypeError("Expected argument 'work_pools' to be a list")
        pulumi.set(__self__, "work_pools", work_pools)
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
    @pulumi.getter(name="filterAnies")
    def filter_anies(self) -> Optional[Sequence[str]]:
        """
        Work pool IDs (UUID) to search for (work pools with any matching UUID are returned)
        """
        return pulumi.get(self, "filter_anies")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="workPools")
    def work_pools(self) -> Sequence['outputs.GetWorkPoolsWorkPoolResult']:
        """
        Work pools returned by the server
        """
        return pulumi.get(self, "work_pools")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[str]:
        """
        Workspace ID (UUID), defaults to the workspace set in the provider
        """
        return pulumi.get(self, "workspace_id")


class AwaitableGetWorkPoolsResult(GetWorkPoolsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkPoolsResult(
            account_id=self.account_id,
            filter_anies=self.filter_anies,
            id=self.id,
            work_pools=self.work_pools,
            workspace_id=self.workspace_id)


def get_work_pools(account_id: Optional[str] = None,
                   filter_anies: Optional[Sequence[str]] = None,
                   workspace_id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkPoolsResult:
    """
    Get information about an multiple Work Pools.
    <br>
    Use this data source to search for multiple Work Pools. Defaults to fetching all Work Pools in the Workspace.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prefect as prefect

    all_pools = prefect.get_work_pools()
    ```


    :param str account_id: Account ID (UUID), defaults to the account set in the provider
    :param Sequence[str] filter_anies: Work pool IDs (UUID) to search for (work pools with any matching UUID are returned)
    :param str workspace_id: Workspace ID (UUID), defaults to the workspace set in the provider
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['filterAnies'] = filter_anies
    __args__['workspaceId'] = workspace_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('prefect:index/getWorkPools:getWorkPools', __args__, opts=opts, typ=GetWorkPoolsResult).value

    return AwaitableGetWorkPoolsResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        filter_anies=pulumi.get(__ret__, 'filter_anies'),
        id=pulumi.get(__ret__, 'id'),
        work_pools=pulumi.get(__ret__, 'work_pools'),
        workspace_id=pulumi.get(__ret__, 'workspace_id'))


@_utilities.lift_output_func(get_work_pools)
def get_work_pools_output(account_id: Optional[pulumi.Input[Optional[str]]] = None,
                          filter_anies: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                          workspace_id: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkPoolsResult]:
    """
    Get information about an multiple Work Pools.
    <br>
    Use this data source to search for multiple Work Pools. Defaults to fetching all Work Pools in the Workspace.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prefect as prefect

    all_pools = prefect.get_work_pools()
    ```


    :param str account_id: Account ID (UUID), defaults to the account set in the provider
    :param Sequence[str] filter_anies: Work pool IDs (UUID) to search for (work pools with any matching UUID are returned)
    :param str workspace_id: Workspace ID (UUID), defaults to the workspace set in the provider
    """
    ...
