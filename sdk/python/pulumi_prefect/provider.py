# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] account_id: Default Prefect Cloud Account ID. Can also be set via the `PREFECT_CLOUD_ACCOUNT_ID` environment variable.
        :param pulumi.Input[str] api_key: Prefect Cloud API Key. Can also be set via the `PREFECT_API_KEY` environment variable.
        :param pulumi.Input[str] endpoint: Prefect API URL. Can also be set via the `PREFECT_API_URL` environment variable. Defaults to `https://api.prefect.cloud`
        :param pulumi.Input[str] workspace_id: Default Prefect Cloud Workspace ID.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if workspace_id is not None:
            pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Default Prefect Cloud Account ID. Can also be set via the `PREFECT_CLOUD_ACCOUNT_ID` environment variable.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        Prefect Cloud API Key. Can also be set via the `PREFECT_API_KEY` environment variable.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        Prefect API URL. Can also be set via the `PREFECT_API_URL` environment variable. Defaults to `https://api.prefect.cloud`
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        Default Prefect Cloud Workspace ID.
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_id", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the prefect package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Default Prefect Cloud Account ID. Can also be set via the `PREFECT_CLOUD_ACCOUNT_ID` environment variable.
        :param pulumi.Input[str] api_key: Prefect Cloud API Key. Can also be set via the `PREFECT_API_KEY` environment variable.
        :param pulumi.Input[str] endpoint: Prefect API URL. Can also be set via the `PREFECT_API_URL` environment variable. Defaults to `https://api.prefect.cloud`
        :param pulumi.Input[str] workspace_id: Default Prefect Cloud Workspace ID.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the prefect package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["api_key"] = None if api_key is None else pulumi.Output.secret(api_key)
            __props__.__dict__["endpoint"] = endpoint
            __props__.__dict__["workspace_id"] = workspace_id
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Provider, __self__).__init__(
            'prefect',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[Optional[str]]:
        """
        Default Prefect Cloud Account ID. Can also be set via the `PREFECT_CLOUD_ACCOUNT_ID` environment variable.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[Optional[str]]:
        """
        Prefect Cloud API Key. Can also be set via the `PREFECT_API_KEY` environment variable.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[Optional[str]]:
        """
        Prefect API URL. Can also be set via the `PREFECT_API_URL` environment variable. Defaults to `https://api.prefect.cloud`
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[Optional[str]]:
        """
        Default Prefect Cloud Workspace ID.
        """
        return pulumi.get(self, "workspace_id")

