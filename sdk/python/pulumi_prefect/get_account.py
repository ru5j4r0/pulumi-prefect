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
    'GetAccountResult',
    'AwaitableGetAccountResult',
    'get_account',
    'get_account_output',
]

@pulumi.output_type
class GetAccountResult:
    """
    A collection of values returned by getAccount.
    """
    def __init__(__self__, allow_public_workspaces=None, billing_email=None, created=None, handle=None, id=None, link=None, location=None, name=None, updated=None):
        if allow_public_workspaces and not isinstance(allow_public_workspaces, bool):
            raise TypeError("Expected argument 'allow_public_workspaces' to be a bool")
        pulumi.set(__self__, "allow_public_workspaces", allow_public_workspaces)
        if billing_email and not isinstance(billing_email, str):
            raise TypeError("Expected argument 'billing_email' to be a str")
        pulumi.set(__self__, "billing_email", billing_email)
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if handle and not isinstance(handle, str):
            raise TypeError("Expected argument 'handle' to be a str")
        pulumi.set(__self__, "handle", handle)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if link and not isinstance(link, str):
            raise TypeError("Expected argument 'link' to be a str")
        pulumi.set(__self__, "link", link)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if updated and not isinstance(updated, str):
            raise TypeError("Expected argument 'updated' to be a str")
        pulumi.set(__self__, "updated", updated)

    @property
    @pulumi.getter(name="allowPublicWorkspaces")
    def allow_public_workspaces(self) -> bool:
        """
        Whether or not this account allows public workspaces
        """
        return pulumi.get(self, "allow_public_workspaces")

    @property
    @pulumi.getter(name="billingEmail")
    def billing_email(self) -> str:
        """
        Billing email to apply to the account's Stripe customer
        """
        return pulumi.get(self, "billing_email")

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        Timestamp of when the resource was created (RFC3339)
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def handle(self) -> str:
        """
        Unique handle of the account
        """
        return pulumi.get(self, "handle")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Account ID (UUID)
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def link(self) -> str:
        """
        An optional for an external url associated with the account, e.g. https://prefect.io/
        """
        return pulumi.get(self, "link")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        An optional physical location for the account, e.g. Washington, D.C.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the account
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def updated(self) -> str:
        """
        Timestamp of when the resource was updated (RFC3339)
        """
        return pulumi.get(self, "updated")


class AwaitableGetAccountResult(GetAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountResult(
            allow_public_workspaces=self.allow_public_workspaces,
            billing_email=self.billing_email,
            created=self.created,
            handle=self.handle,
            id=self.id,
            link=self.link,
            location=self.location,
            name=self.name,
            updated=self.updated)


def get_account(id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountResult:
    """
    Get information about an existing Account.
    <br>
    Use this data source to obtain account-level attributes

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prefect as prefect

    my_organization = prefect.get_account()
    ```


    :param str id: Account ID (UUID)
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('prefect:index/getAccount:getAccount', __args__, opts=opts, typ=GetAccountResult).value

    return AwaitableGetAccountResult(
        allow_public_workspaces=pulumi.get(__ret__, 'allow_public_workspaces'),
        billing_email=pulumi.get(__ret__, 'billing_email'),
        created=pulumi.get(__ret__, 'created'),
        handle=pulumi.get(__ret__, 'handle'),
        id=pulumi.get(__ret__, 'id'),
        link=pulumi.get(__ret__, 'link'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        updated=pulumi.get(__ret__, 'updated'))


@_utilities.lift_output_func(get_account)
def get_account_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccountResult]:
    """
    Get information about an existing Account.
    <br>
    Use this data source to obtain account-level attributes

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prefect as prefect

    my_organization = prefect.get_account()
    ```


    :param str id: Account ID (UUID)
    """
    ...
