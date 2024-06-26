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
    'GetAccountMemberResult',
    'AwaitableGetAccountMemberResult',
    'get_account_member',
    'get_account_member_output',
]

@pulumi.output_type
class GetAccountMemberResult:
    """
    A collection of values returned by getAccountMember.
    """
    def __init__(__self__, account_id=None, account_role_id=None, account_role_name=None, actor_id=None, email=None, first_name=None, handle=None, id=None, last_name=None, user_id=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if account_role_id and not isinstance(account_role_id, str):
            raise TypeError("Expected argument 'account_role_id' to be a str")
        pulumi.set(__self__, "account_role_id", account_role_id)
        if account_role_name and not isinstance(account_role_name, str):
            raise TypeError("Expected argument 'account_role_name' to be a str")
        pulumi.set(__self__, "account_role_name", account_role_name)
        if actor_id and not isinstance(actor_id, str):
            raise TypeError("Expected argument 'actor_id' to be a str")
        pulumi.set(__self__, "actor_id", actor_id)
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if first_name and not isinstance(first_name, str):
            raise TypeError("Expected argument 'first_name' to be a str")
        pulumi.set(__self__, "first_name", first_name)
        if handle and not isinstance(handle, str):
            raise TypeError("Expected argument 'handle' to be a str")
        pulumi.set(__self__, "handle", handle)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_name and not isinstance(last_name, str):
            raise TypeError("Expected argument 'last_name' to be a str")
        pulumi.set(__self__, "last_name", last_name)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[str]:
        """
        Account ID (UUID) where the member resides
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="accountRoleId")
    def account_role_id(self) -> str:
        """
        Acount Role ID (UUID)
        """
        return pulumi.get(self, "account_role_id")

    @property
    @pulumi.getter(name="accountRoleName")
    def account_role_name(self) -> str:
        """
        Name of Account Role assigned to member
        """
        return pulumi.get(self, "account_role_name")

    @property
    @pulumi.getter(name="actorId")
    def actor_id(self) -> str:
        """
        Actor ID (UUID)
        """
        return pulumi.get(self, "actor_id")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        Member email
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> str:
        """
        Member's first name
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter
    def handle(self) -> str:
        """
        Member handle, or a human-readable identifier
        """
        return pulumi.get(self, "handle")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Account Member ID (UUID)
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> str:
        """
        Member's last name
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        """
        User ID (UUID)
        """
        return pulumi.get(self, "user_id")


class AwaitableGetAccountMemberResult(GetAccountMemberResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountMemberResult(
            account_id=self.account_id,
            account_role_id=self.account_role_id,
            account_role_name=self.account_role_name,
            actor_id=self.actor_id,
            email=self.email,
            first_name=self.first_name,
            handle=self.handle,
            id=self.id,
            last_name=self.last_name,
            user_id=self.user_id)


def get_account_member(account_id: Optional[str] = None,
                       email: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountMemberResult:
    """
    Get information about an existing Account Member (user)	by their email.
    <br>
    Use this data source to obtain user or actor IDs to manage Workspace Access.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prefect as prefect

    marvin = prefect.get_account_member(email="marvin@prefect.io")
    ```


    :param str account_id: Account ID (UUID) where the member resides
    :param str email: Member email
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['email'] = email
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('prefect:index/getAccountMember:getAccountMember', __args__, opts=opts, typ=GetAccountMemberResult).value

    return AwaitableGetAccountMemberResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        account_role_id=pulumi.get(__ret__, 'account_role_id'),
        account_role_name=pulumi.get(__ret__, 'account_role_name'),
        actor_id=pulumi.get(__ret__, 'actor_id'),
        email=pulumi.get(__ret__, 'email'),
        first_name=pulumi.get(__ret__, 'first_name'),
        handle=pulumi.get(__ret__, 'handle'),
        id=pulumi.get(__ret__, 'id'),
        last_name=pulumi.get(__ret__, 'last_name'),
        user_id=pulumi.get(__ret__, 'user_id'))


@_utilities.lift_output_func(get_account_member)
def get_account_member_output(account_id: Optional[pulumi.Input[Optional[str]]] = None,
                              email: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccountMemberResult]:
    """
    Get information about an existing Account Member (user)	by their email.
    <br>
    Use this data source to obtain user or actor IDs to manage Workspace Access.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prefect as prefect

    marvin = prefect.get_account_member(email="marvin@prefect.io")
    ```


    :param str account_id: Account ID (UUID) where the member resides
    :param str email: Member email
    """
    ...
