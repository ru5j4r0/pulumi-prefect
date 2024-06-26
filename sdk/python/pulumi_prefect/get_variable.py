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
    'GetVariableResult',
    'AwaitableGetVariableResult',
    'get_variable',
    'get_variable_output',
]

@pulumi.output_type
class GetVariableResult:
    """
    A collection of values returned by getVariable.
    """
    def __init__(__self__, account_id=None, created=None, id=None, name=None, tags=None, updated=None, value=None, workspace_id=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if updated and not isinstance(updated, str):
            raise TypeError("Expected argument 'updated' to be a str")
        pulumi.set(__self__, "updated", updated)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)
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
    @pulumi.getter
    def created(self) -> str:
        """
        Timestamp of when the resource was created (RFC3339)
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Variable ID (UUID)
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the variable
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        Tags associated with the variable
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def updated(self) -> str:
        """
        Timestamp of when the resource was updated (RFC3339)
        """
        return pulumi.get(self, "updated")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Value of the variable
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[str]:
        """
        Workspace ID (UUID), defaults to the workspace set in the provider
        """
        return pulumi.get(self, "workspace_id")


class AwaitableGetVariableResult(GetVariableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVariableResult(
            account_id=self.account_id,
            created=self.created,
            id=self.id,
            name=self.name,
            tags=self.tags,
            updated=self.updated,
            value=self.value,
            workspace_id=self.workspace_id)


def get_variable(account_id: Optional[str] = None,
                 id: Optional[str] = None,
                 name: Optional[str] = None,
                 workspace_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVariableResult:
    """
    Get information about an existing Variable by name or ID.
    <br>
    Use this data source to obtain Variable-specific attributes, such as the value.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prefect as prefect

    existing_by_id = prefect.get_variable(id="00000000-0000-0000-0000-000000000000")
    existing_by_name = prefect.get_variable(name="my_variable_name")
    ```


    :param str account_id: Account ID (UUID), defaults to the account set in the provider
    :param str id: Variable ID (UUID)
    :param str name: Name of the variable
    :param str workspace_id: Workspace ID (UUID), defaults to the workspace set in the provider
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['id'] = id
    __args__['name'] = name
    __args__['workspaceId'] = workspace_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('prefect:index/getVariable:getVariable', __args__, opts=opts, typ=GetVariableResult).value

    return AwaitableGetVariableResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        created=pulumi.get(__ret__, 'created'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        tags=pulumi.get(__ret__, 'tags'),
        updated=pulumi.get(__ret__, 'updated'),
        value=pulumi.get(__ret__, 'value'),
        workspace_id=pulumi.get(__ret__, 'workspace_id'))


@_utilities.lift_output_func(get_variable)
def get_variable_output(account_id: Optional[pulumi.Input[Optional[str]]] = None,
                        id: Optional[pulumi.Input[Optional[str]]] = None,
                        name: Optional[pulumi.Input[Optional[str]]] = None,
                        workspace_id: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVariableResult]:
    """
    Get information about an existing Variable by name or ID.
    <br>
    Use this data source to obtain Variable-specific attributes, such as the value.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prefect as prefect

    existing_by_id = prefect.get_variable(id="00000000-0000-0000-0000-000000000000")
    existing_by_name = prefect.get_variable(name="my_variable_name")
    ```


    :param str account_id: Account ID (UUID), defaults to the account set in the provider
    :param str id: Variable ID (UUID)
    :param str name: Name of the variable
    :param str workspace_id: Workspace ID (UUID), defaults to the workspace set in the provider
    """
    ...
