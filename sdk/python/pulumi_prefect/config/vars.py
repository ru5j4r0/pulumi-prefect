# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('prefect')


class _ExportableConfig(types.ModuleType):
    @property
    def account_id(self) -> Optional[str]:
        """
        Default Prefect Cloud Account ID. Can also be set via the `PREFECT_CLOUD_ACCOUNT_ID` environment variable.
        """
        return __config__.get('accountId')

    @property
    def api_key(self) -> Optional[str]:
        """
        Prefect Cloud API Key. Can also be set via the `PREFECT_API_KEY` environment variable.
        """
        return __config__.get('apiKey')

    @property
    def endpoint(self) -> Optional[str]:
        """
        Prefect API URL. Can also be set via the `PREFECT_API_URL` environment variable. Defaults to `https://api.prefect.cloud`
        """
        return __config__.get('endpoint')

    @property
    def workspace_id(self) -> Optional[str]:
        """
        Default Prefect Cloud Workspace ID.
        """
        return __config__.get('workspaceId')

