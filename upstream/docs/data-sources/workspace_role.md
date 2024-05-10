---
# generated by https://github.com/hashicorp/terraform-plugin-docs
page_title: "prefect_workspace_role Data Source - prefect"
subcategory: ""
description: |-
  Get information about an existing Workspace Role.
  
  Use this data source read down the pre-defined Roles, to manage User and Service Account access.
---

# prefect_workspace_role (Data Source)

Get information about an existing Workspace Role.
<br>
Use this data source read down the pre-defined Roles, to manage User and Service Account access.

## Example Usage

```terraform
# Read down the default Owner Workspace Role
data "prefect_workspace_role" "owner" {
  name = "Owner"
}

# Read down the default Worker Workspace Role
data "prefect_workspace_role" "worker" {
  name = "Worker"
}

# Read down the default Developer Workspace Role
data "prefect_workspace_role" "developer" {
  name = "Developer"
}

# Read down the default Viewer Workspace Role
data "prefect_workspace_role" "viewer" {
  name = "Viewer"
}

# Read down the default Runner Workspace Role
data "prefect_workspace_role" "runner" {
  name = "Runner"
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `name` (String) Name of the Workspace Role

### Optional

- `account_id` (String) Account ID (UUID) where Workspace Role resides

### Read-Only

- `created` (String) Timestamp of when the resource was created (RFC3339)
- `description` (String) Description of the Workspace Role
- `id` (String) Workspace Role ID (UUID)
- `inherited_role_id` (String) Workspace Role ID (UUID), whose permissions are inherited by this Workspace Role
- `scopes` (List of String) List of scopes linked to the Workspace Role
- `updated` (String) Timestamp of when the resource was updated (RFC3339)