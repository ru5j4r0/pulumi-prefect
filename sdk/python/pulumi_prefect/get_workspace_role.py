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
    'GetWorkspaceRoleResult',
    'AwaitableGetWorkspaceRoleResult',
    'get_workspace_role',
    'get_workspace_role_output',
]

@pulumi.output_type
class GetWorkspaceRoleResult:
    """
    A collection of values returned by getWorkspaceRole.
    """
    def __init__(__self__, account_id=None, created=None, description=None, id=None, inherited_role_id=None, name=None, scopes=None, updated=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if inherited_role_id and not isinstance(inherited_role_id, str):
            raise TypeError("Expected argument 'inherited_role_id' to be a str")
        pulumi.set(__self__, "inherited_role_id", inherited_role_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if scopes and not isinstance(scopes, list):
            raise TypeError("Expected argument 'scopes' to be a list")
        pulumi.set(__self__, "scopes", scopes)
        if updated and not isinstance(updated, str):
            raise TypeError("Expected argument 'updated' to be a str")
        pulumi.set(__self__, "updated", updated)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[str]:
        """
        Account ID (UUID) where Workspace Role resides
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
    def description(self) -> str:
        """
        Description of the Workspace Role
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Workspace Role ID (UUID)
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inheritedRoleId")
    def inherited_role_id(self) -> str:
        """
        Workspace Role ID (UUID), whose permissions are inherited by this Workspace Role
        """
        return pulumi.get(self, "inherited_role_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the Workspace Role
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scopes(self) -> Sequence[str]:
        """
        List of scopes linked to the Workspace Role
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter
    def updated(self) -> str:
        """
        Timestamp of when the resource was updated (RFC3339)
        """
        return pulumi.get(self, "updated")


class AwaitableGetWorkspaceRoleResult(GetWorkspaceRoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceRoleResult(
            account_id=self.account_id,
            created=self.created,
            description=self.description,
            id=self.id,
            inherited_role_id=self.inherited_role_id,
            name=self.name,
            scopes=self.scopes,
            updated=self.updated)


def get_workspace_role(account_id: Optional[str] = None,
                       name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceRoleResult:
    """
    Get information about an existing Workspace Role.
    <br>
    Use this data source read down the pre-defined Roles, to manage User and Service Account access.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prefect as prefect

    owner = prefect.get_workspace_role(name="Owner")
    worker = prefect.get_workspace_role(name="Worker")
    developer = prefect.get_workspace_role(name="Developer")
    viewer = prefect.get_workspace_role(name="Viewer")
    runner = prefect.get_workspace_role(name="Runner")
    ```


    :param str account_id: Account ID (UUID) where Workspace Role resides
    :param str name: Name of the Workspace Role
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('prefect:index/getWorkspaceRole:getWorkspaceRole', __args__, opts=opts, typ=GetWorkspaceRoleResult).value

    return AwaitableGetWorkspaceRoleResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        created=pulumi.get(__ret__, 'created'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        inherited_role_id=pulumi.get(__ret__, 'inherited_role_id'),
        name=pulumi.get(__ret__, 'name'),
        scopes=pulumi.get(__ret__, 'scopes'),
        updated=pulumi.get(__ret__, 'updated'))


@_utilities.lift_output_func(get_workspace_role)
def get_workspace_role_output(account_id: Optional[pulumi.Input[Optional[str]]] = None,
                              name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceRoleResult]:
    """
    Get information about an existing Workspace Role.
    <br>
    Use this data source read down the pre-defined Roles, to manage User and Service Account access.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prefect as prefect

    owner = prefect.get_workspace_role(name="Owner")
    worker = prefect.get_workspace_role(name="Worker")
    developer = prefect.get_workspace_role(name="Developer")
    viewer = prefect.get_workspace_role(name="Viewer")
    runner = prefect.get_workspace_role(name="Runner")
    ```


    :param str account_id: Account ID (UUID) where Workspace Role resides
    :param str name: Name of the Workspace Role
    """
    ...
