# API

Types:

```python
from pyhfapi.types import (
    APIGetDailyPapersResponse,
    APIGetDatasetTagsResponse,
    APIGetModelTagsResponse,
    APIGetUserInfoResponse,
)
```

Methods:

- <code title="get /api/daily_papers">client.api.<a href="./src/pyhfapi/resources/api/api.py">get_daily_papers</a>(\*\*<a href="src/pyhfapi/types/api_get_daily_papers_params.py">params</a>) -> <a href="./src/pyhfapi/types/api_get_daily_papers_response.py">APIGetDailyPapersResponse</a></code>
- <code title="get /api/datasets-tags-by-type">client.api.<a href="./src/pyhfapi/resources/api/api.py">get_dataset_tags</a>(\*\*<a href="src/pyhfapi/types/api_get_dataset_tags_params.py">params</a>) -> <a href="./src/pyhfapi/types/api_get_dataset_tags_response.py">APIGetDatasetTagsResponse</a></code>
- <code title="get /api/models-tags-by-type">client.api.<a href="./src/pyhfapi/resources/api/api.py">get_model_tags</a>(\*\*<a href="src/pyhfapi/types/api_get_model_tags_params.py">params</a>) -> <a href="./src/pyhfapi/types/api_get_model_tags_response.py">APIGetModelTagsResponse</a></code>
- <code title="get /api/whoami-v2">client.api.<a href="./src/pyhfapi/resources/api/api.py">get_user_info</a>() -> <a href="./src/pyhfapi/types/api_get_user_info_response.py">APIGetUserInfoResponse</a></code>

## Notifications

Types:

```python
from pyhfapi.types.api import NotificationListResponse
```

Methods:

- <code title="get /api/notifications">client.api.notifications.<a href="./src/pyhfapi/resources/api/notifications.py">list</a>(\*\*<a href="src/pyhfapi/types/api/notification_list_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/notification_list_response.py">NotificationListResponse</a></code>
- <code title="delete /api/notifications">client.api.notifications.<a href="./src/pyhfapi/resources/api/notifications.py">delete</a>(\*\*<a href="src/pyhfapi/types/api/notification_delete_params.py">params</a>) -> None</code>

## Settings

Types:

```python
from pyhfapi.types.api import SettingGetMcpResponse
```

Methods:

- <code title="get /api/settings/mcp">client.api.settings.<a href="./src/pyhfapi/resources/api/settings/settings.py">get_mcp</a>() -> <a href="./src/pyhfapi/types/api/setting_get_mcp_response.py">SettingGetMcpResponse</a></code>
- <code title="patch /api/settings/notifications">client.api.settings.<a href="./src/pyhfapi/resources/api/settings/settings.py">update_notifications</a>(\*\*<a href="src/pyhfapi/types/api/setting_update_notifications_params.py">params</a>) -> None</code>
- <code title="patch /api/settings/watch">client.api.settings.<a href="./src/pyhfapi/resources/api/settings/settings.py">update_watch</a>(\*\*<a href="src/pyhfapi/types/api/setting_update_watch_params.py">params</a>) -> None</code>

### Webhooks

Types:

```python
from pyhfapi.types.api.settings import (
    WebhookCreateResponse,
    WebhookRetrieveResponse,
    WebhookUpdateResponse,
    WebhookListResponse,
    WebhookReplayLogResponse,
    WebhookToggleResponse,
)
```

Methods:

- <code title="post /api/settings/webhooks">client.api.settings.webhooks.<a href="./src/pyhfapi/resources/api/settings/webhooks.py">create</a>(\*\*<a href="src/pyhfapi/types/api/settings/webhook_create_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/settings/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /api/settings/webhooks/{webhookId}">client.api.settings.webhooks.<a href="./src/pyhfapi/resources/api/settings/webhooks.py">retrieve</a>(webhook_id) -> <a href="./src/pyhfapi/types/api/settings/webhook_retrieve_response.py">WebhookRetrieveResponse</a></code>
- <code title="post /api/settings/webhooks/{webhookId}">client.api.settings.webhooks.<a href="./src/pyhfapi/resources/api/settings/webhooks.py">update</a>(webhook_id, \*\*<a href="src/pyhfapi/types/api/settings/webhook_update_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/settings/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /api/settings/webhooks">client.api.settings.webhooks.<a href="./src/pyhfapi/resources/api/settings/webhooks.py">list</a>() -> <a href="./src/pyhfapi/types/api/settings/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /api/settings/webhooks/{webhookId}">client.api.settings.webhooks.<a href="./src/pyhfapi/resources/api/settings/webhooks.py">delete</a>(webhook_id) -> object</code>
- <code title="post /api/settings/webhooks/{webhookId}/replay/{logId}">client.api.settings.webhooks.<a href="./src/pyhfapi/resources/api/settings/webhooks.py">replay_log</a>(log_id, \*, webhook_id) -> <a href="./src/pyhfapi/types/api/settings/webhook_replay_log_response.py">WebhookReplayLogResponse</a></code>
- <code title="post /api/settings/webhooks/{webhookId}/{action}">client.api.settings.webhooks.<a href="./src/pyhfapi/resources/api/settings/webhooks.py">toggle</a>(action, \*, webhook_id) -> <a href="./src/pyhfapi/types/api/settings/webhook_toggle_response.py">WebhookToggleResponse</a></code>

### Billing

#### Usage

Types:

```python
from pyhfapi.types.api.settings.billing import UsageGetResponse, UsageGetJobsResponse
```

Methods:

- <code title="get /api/settings/billing/usage">client.api.settings.billing.usage.<a href="./src/pyhfapi/resources/api/settings/billing/usage.py">get</a>(\*\*<a href="src/pyhfapi/types/api/settings/billing/usage_get_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/settings/billing/usage_get_response.py">UsageGetResponse</a></code>
- <code title="get /api/settings/billing/usage/jobs">client.api.settings.billing.usage.<a href="./src/pyhfapi/resources/api/settings/billing/usage.py">get_jobs</a>() -> <a href="./src/pyhfapi/types/api/settings/billing/usage_get_jobs_response.py">UsageGetJobsResponse</a></code>
- <code title="get /api/settings/billing/usage/live">client.api.settings.billing.usage.<a href="./src/pyhfapi/resources/api/settings/billing/usage.py">get_live</a>() -> None</code>

## Organizations

Types:

```python
from pyhfapi.types.api import OrganizationListMembersResponse, OrganizationRetrieveAvatarResponse
```

Methods:

- <code title="get /api/organizations/{name}/members">client.api.organizations.<a href="./src/pyhfapi/resources/api/organizations/organizations.py">list_members</a>(name, \*\*<a href="src/pyhfapi/types/api/organization_list_members_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/organization_list_members_response.py">OrganizationListMembersResponse</a></code>
- <code title="get /api/organizations/{name}/avatar">client.api.organizations.<a href="./src/pyhfapi/resources/api/organizations/organizations.py">retrieve_avatar</a>(name, \*\*<a href="src/pyhfapi/types/api/organization_retrieve_avatar_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/organization_retrieve_avatar_response.py">OrganizationRetrieveAvatarResponse</a></code>

### AuditLog

Types:

```python
from pyhfapi.types.api.organizations import AuditLogExportResponse
```

Methods:

- <code title="get /api/organizations/{name}/audit-log/export">client.api.organizations.audit_log.<a href="./src/pyhfapi/resources/api/organizations/audit_log.py">export</a>(name, \*\*<a href="src/pyhfapi/types/api/organizations/audit_log_export_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/organizations/audit_log_export_response.py">AuditLogExportResponse</a></code>

### ResourceGroups

Types:

```python
from pyhfapi.types.api.organizations import (
    RepoID,
    ResourceGroupCreateResponse,
    ResourceGroupListResponse,
)
```

Methods:

- <code title="post /api/organizations/{name}/resource-groups">client.api.organizations.resource_groups.<a href="./src/pyhfapi/resources/api/organizations/resource_groups.py">create</a>(path_name, \*\*<a href="src/pyhfapi/types/api/organizations/resource_group_create_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/organizations/resource_group_create_response.py">ResourceGroupCreateResponse</a></code>
- <code title="get /api/organizations/{name}/resource-groups">client.api.organizations.resource_groups.<a href="./src/pyhfapi/resources/api/organizations/resource_groups.py">list</a>(name) -> <a href="./src/pyhfapi/types/api/organizations/resource_group_list_response.py">ResourceGroupListResponse</a></code>

### Scim

#### V2

##### Users

Types:

```python
from pyhfapi.types.api.organizations.scim.v2 import (
    UserCreateResponse,
    UserRetrieveResponse,
    UserUpdateResponse,
    UserListResponse,
    UserUpdateAttributesResponse,
)
```

Methods:

- <code title="post /api/organizations/{name}/scim/v2/Users">client.api.organizations.scim.v2.users.<a href="./src/pyhfapi/resources/api/organizations/scim/v2/users.py">create</a>(path_name, \*\*<a href="src/pyhfapi/types/api/organizations/scim/v2/user_create_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/organizations/scim/v2/user_create_response.py">UserCreateResponse</a></code>
- <code title="get /api/organizations/{name}/scim/v2/Users/{userId}">client.api.organizations.scim.v2.users.<a href="./src/pyhfapi/resources/api/organizations/scim/v2/users.py">retrieve</a>(user_id, \*, name) -> <a href="./src/pyhfapi/types/api/organizations/scim/v2/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="put /api/organizations/{name}/scim/v2/Users/{userId}">client.api.organizations.scim.v2.users.<a href="./src/pyhfapi/resources/api/organizations/scim/v2/users.py">update</a>(user_id, \*, path_name, \*\*<a href="src/pyhfapi/types/api/organizations/scim/v2/user_update_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/organizations/scim/v2/user_update_response.py">UserUpdateResponse</a></code>
- <code title="get /api/organizations/{name}/scim/v2/Users">client.api.organizations.scim.v2.users.<a href="./src/pyhfapi/resources/api/organizations/scim/v2/users.py">list</a>(name, \*\*<a href="src/pyhfapi/types/api/organizations/scim/v2/user_list_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/organizations/scim/v2/user_list_response.py">UserListResponse</a></code>
- <code title="delete /api/organizations/{name}/scim/v2/Users/{userId}">client.api.organizations.scim.v2.users.<a href="./src/pyhfapi/resources/api/organizations/scim/v2/users.py">delete</a>(user_id, \*, name) -> object</code>
- <code title="patch /api/organizations/{name}/scim/v2/Users/{userId}">client.api.organizations.scim.v2.users.<a href="./src/pyhfapi/resources/api/organizations/scim/v2/users.py">update_attributes</a>(user_id, \*, name, \*\*<a href="src/pyhfapi/types/api/organizations/scim/v2/user_update_attributes_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/organizations/scim/v2/user_update_attributes_response.py">UserUpdateAttributesResponse</a></code>

##### Groups

Types:

```python
from pyhfapi.types.api.organizations.scim.v2 import (
    GroupCreateResponse,
    GroupRetrieveResponse,
    GroupUpdateResponse,
    GroupListResponse,
    GroupUpdateAttributesResponse,
)
```

Methods:

- <code title="post /api/organizations/{name}/scim/v2/Groups">client.api.organizations.scim.v2.groups.<a href="./src/pyhfapi/resources/api/organizations/scim/v2/groups.py">create</a>(name, \*\*<a href="src/pyhfapi/types/api/organizations/scim/v2/group_create_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/organizations/scim/v2/group_create_response.py">GroupCreateResponse</a></code>
- <code title="get /api/organizations/{name}/scim/v2/Groups/{groupId}">client.api.organizations.scim.v2.groups.<a href="./src/pyhfapi/resources/api/organizations/scim/v2/groups.py">retrieve</a>(group_id, \*, name, \*\*<a href="src/pyhfapi/types/api/organizations/scim/v2/group_retrieve_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/organizations/scim/v2/group_retrieve_response.py">GroupRetrieveResponse</a></code>
- <code title="put /api/organizations/{name}/scim/v2/Groups/{groupId}">client.api.organizations.scim.v2.groups.<a href="./src/pyhfapi/resources/api/organizations/scim/v2/groups.py">update</a>(group_id, \*, name, \*\*<a href="src/pyhfapi/types/api/organizations/scim/v2/group_update_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/organizations/scim/v2/group_update_response.py">GroupUpdateResponse</a></code>
- <code title="get /api/organizations/{name}/scim/v2/Groups">client.api.organizations.scim.v2.groups.<a href="./src/pyhfapi/resources/api/organizations/scim/v2/groups.py">list</a>(name, \*\*<a href="src/pyhfapi/types/api/organizations/scim/v2/group_list_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/organizations/scim/v2/group_list_response.py">GroupListResponse</a></code>
- <code title="delete /api/organizations/{name}/scim/v2/Groups/{groupId}">client.api.organizations.scim.v2.groups.<a href="./src/pyhfapi/resources/api/organizations/scim/v2/groups.py">delete</a>(group_id, \*, name) -> object</code>
- <code title="patch /api/organizations/{name}/scim/v2/Groups/{groupId}">client.api.organizations.scim.v2.groups.<a href="./src/pyhfapi/resources/api/organizations/scim/v2/groups.py">update_attributes</a>(group_id, \*, name, \*\*<a href="src/pyhfapi/types/api/organizations/scim/v2/group_update_attributes_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/organizations/scim/v2/group_update_attributes_response.py">GroupUpdateAttributesResponse</a></code>

### Billing

#### Usage

Types:

```python
from pyhfapi.types.api.organizations.billing import UsageGetResponse
```

Methods:

- <code title="get /api/organizations/{name}/billing/usage">client.api.organizations.billing.usage.<a href="./src/pyhfapi/resources/api/organizations/billing/usage.py">get</a>(name, \*\*<a href="src/pyhfapi/types/api/organizations/billing/usage_get_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/organizations/billing/usage_get_response.py">UsageGetResponse</a></code>
- <code title="get /api/organizations/{name}/billing/usage/live">client.api.organizations.billing.usage.<a href="./src/pyhfapi/resources/api/organizations/billing/usage.py">get_live</a>(name) -> None</code>

## Blog

### Comment

Types:

```python
from pyhfapi.types.api.blog import CommentCreateResponse, CommentCreateWithNamespaceResponse
```

Methods:

- <code title="post /api/blog/{slug}/comment">client.api.blog.comment.<a href="./src/pyhfapi/resources/api/blog/comment/comment.py">create</a>(slug, \*\*<a href="src/pyhfapi/types/api/blog/comment_create_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/blog/comment_create_response.py">CommentCreateResponse</a></code>
- <code title="post /api/blog/{namespace}/{slug}/comment">client.api.blog.comment.<a href="./src/pyhfapi/resources/api/blog/comment/comment.py">create_with_namespace</a>(slug, \*, namespace, \*\*<a href="src/pyhfapi/types/api/blog/comment_create_with_namespace_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/blog/comment_create_with_namespace_response.py">CommentCreateWithNamespaceResponse</a></code>

#### Reply

Types:

```python
from pyhfapi.types.api.blog.comment import ReplyCreateResponse, ReplyCreateWithNamespaceResponse
```

Methods:

- <code title="post /api/blog/{slug}/comment/{commentId}/reply">client.api.blog.comment.reply.<a href="./src/pyhfapi/resources/api/blog/comment/reply.py">create</a>(comment_id, \*, slug, \*\*<a href="src/pyhfapi/types/api/blog/comment/reply_create_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/blog/comment/reply_create_response.py">ReplyCreateResponse</a></code>
- <code title="post /api/blog/{namespace}/{slug}/comment/{commentId}/reply">client.api.blog.comment.reply.<a href="./src/pyhfapi/resources/api/blog/comment/reply.py">create_with_namespace</a>(comment_id, \*, namespace, slug, \*\*<a href="src/pyhfapi/types/api/blog/comment/reply_create_with_namespace_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/blog/comment/reply_create_with_namespace_response.py">ReplyCreateWithNamespaceResponse</a></code>

## Docs

Types:

```python
from pyhfapi.types.api import DocSearchResponse
```

Methods:

- <code title="get /api/docs/search">client.api.docs.<a href="./src/pyhfapi/resources/api/docs.py">search</a>(\*\*<a href="src/pyhfapi/types/api/doc_search_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/doc_search_response.py">DocSearchResponse</a></code>

## Discussions

Types:

```python
from pyhfapi.types.api import (
    DiscussionCreateResponse,
    DiscussionRetrieveResponse,
    DiscussionListResponse,
    DiscussionAddCommentResponse,
    DiscussionChangeStatusResponse,
    DiscussionChangeTitleResponse,
)
```

Methods:

- <code title="post /api/{repoType}/{namespace}/{repo}/discussions">client.api.discussions.<a href="./src/pyhfapi/resources/api/discussions.py">create</a>(repo, \*, repo_type, namespace, \*\*<a href="src/pyhfapi/types/api/discussion_create_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/discussion_create_response.py">DiscussionCreateResponse</a></code>
- <code title="get /api/{repoType}/{namespace}/{repo}/discussions/{num}">client.api.discussions.<a href="./src/pyhfapi/resources/api/discussions.py">retrieve</a>(num, \*, repo_type, namespace, repo) -> <a href="./src/pyhfapi/types/api/discussion_retrieve_response.py">DiscussionRetrieveResponse</a></code>
- <code title="get /api/{repoType}/{namespace}/{repo}/discussions">client.api.discussions.<a href="./src/pyhfapi/resources/api/discussions.py">list</a>(repo, \*, repo_type, namespace, \*\*<a href="src/pyhfapi/types/api/discussion_list_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/discussion_list_response.py">DiscussionListResponse</a></code>
- <code title="delete /api/{repoType}/{namespace}/{repo}/discussions/{num}">client.api.discussions.<a href="./src/pyhfapi/resources/api/discussions.py">delete</a>(num, \*, repo_type, namespace, repo) -> None</code>
- <code title="post /api/{repoType}/{namespace}/{repo}/discussions/{num}/comment">client.api.discussions.<a href="./src/pyhfapi/resources/api/discussions.py">add_comment</a>(num, \*, repo_type, namespace, repo, \*\*<a href="src/pyhfapi/types/api/discussion_add_comment_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/discussion_add_comment_response.py">DiscussionAddCommentResponse</a></code>
- <code title="post /api/{repoType}/{namespace}/{repo}/discussions/{num}/status">client.api.discussions.<a href="./src/pyhfapi/resources/api/discussions.py">change_status</a>(num, \*, repo_type, namespace, repo, \*\*<a href="src/pyhfapi/types/api/discussion_change_status_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/discussion_change_status_response.py">DiscussionChangeStatusResponse</a></code>
- <code title="post /api/{repoType}/{namespace}/{repo}/discussions/{num}/title">client.api.discussions.<a href="./src/pyhfapi/resources/api/discussions.py">change_title</a>(num, \*, repo_type, namespace, repo, \*\*<a href="src/pyhfapi/types/api/discussion_change_title_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/discussion_change_title_response.py">DiscussionChangeTitleResponse</a></code>
- <code title="post /api/discussions/mark-as-read">client.api.discussions.<a href="./src/pyhfapi/resources/api/discussions.py">mark_as_read</a>(\*\*<a href="src/pyhfapi/types/api/discussion_mark_as_read_params.py">params</a>) -> None</code>
- <code title="post /api/{repoType}/{namespace}/{repo}/discussions/{num}/merge">client.api.discussions.<a href="./src/pyhfapi/resources/api/discussions.py">merge</a>(num, \*, repo_type, namespace, repo, \*\*<a href="src/pyhfapi/types/api/discussion_merge_params.py">params</a>) -> None</code>
- <code title="post /api/{repoType}/{namespace}/{repo}/discussions/{num}/pin">client.api.discussions.<a href="./src/pyhfapi/resources/api/discussions.py">pin</a>(num, \*, repo_type, namespace, repo, \*\*<a href="src/pyhfapi/types/api/discussion_pin_params.py">params</a>) -> None</code>

## Users

### Billing

#### Usage

Methods:

- <code title="get /api/users/{username}/billing/usage/live">client.api.users.billing.usage.<a href="./src/pyhfapi/resources/api/users/billing/usage.py">get_live_usage</a>(username) -> None</code>

## Models

Types:

```python
from pyhfapi.types.api import (
    ModelCheckPreuploadResponse,
    ModelCommitResponse,
    ModelCompareResponse,
    ModelGetNotebookURLResponse,
    ModelGetSecurityStatusResponse,
    ModelGetXetReadTokenResponse,
    ModelGetXetWriteTokenResponse,
    ModelListCommitsResponse,
    ModelListPathsInfoResponse,
    ModelListRefsResponse,
    ModelListTreeContentResponse,
    ModelSuperSquashResponse,
    ModelUpdateSettingsResponse,
)
```

Methods:

- <code title="post /api/models/{namespace}/{repo}/preupload/{rev}">client.api.models.<a href="./src/pyhfapi/resources/api/models/models.py">check_preupload</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/model_check_preupload_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/model_check_preupload_response.py">ModelCheckPreuploadResponse</a></code>
- <code title="post /api/models/{namespace}/{repo}/commit/{rev}">client.api.models.<a href="./src/pyhfapi/resources/api/models/models.py">commit</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/model_commit_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/model_commit_response.py">ModelCommitResponse</a></code>
- <code title="get /api/models/{namespace}/{repo}/compare/{compare}">client.api.models.<a href="./src/pyhfapi/resources/api/models/models.py">compare</a>(compare, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/model_compare_params.py">params</a>) -> str</code>
- <code title="get /api/models/{namespace}/{repo}/notebook/{rev}/{path}">client.api.models.<a href="./src/pyhfapi/resources/api/models/models.py">get_notebook_url</a>(path, \*, namespace, repo, rev) -> <a href="./src/pyhfapi/types/api/model_get_notebook_url_response.py">ModelGetNotebookURLResponse</a></code>
- <code title="get /api/models/{namespace}/{repo}/scan">client.api.models.<a href="./src/pyhfapi/resources/api/models/models.py">get_security_status</a>(repo, \*, namespace) -> <a href="./src/pyhfapi/types/api/model_get_security_status_response.py">ModelGetSecurityStatusResponse</a></code>
- <code title="get /api/models/{namespace}/{repo}/xet-read-token/{rev}">client.api.models.<a href="./src/pyhfapi/resources/api/models/models.py">get_xet_read_token</a>(rev, \*, namespace, repo) -> <a href="./src/pyhfapi/types/api/model_get_xet_read_token_response.py">ModelGetXetReadTokenResponse</a></code>
- <code title="get /api/models/{namespace}/{repo}/xet-write-token/{rev}">client.api.models.<a href="./src/pyhfapi/resources/api/models/models.py">get_xet_write_token</a>(rev, \*, namespace, repo) -> <a href="./src/pyhfapi/types/api/model_get_xet_write_token_response.py">ModelGetXetWriteTokenResponse</a></code>
- <code title="get /api/models/{namespace}/{repo}/commits/{rev}">client.api.models.<a href="./src/pyhfapi/resources/api/models/models.py">list_commits</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/model_list_commits_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/model_list_commits_response.py">ModelListCommitsResponse</a></code>
- <code title="post /api/models/{namespace}/{repo}/paths-info/{rev}">client.api.models.<a href="./src/pyhfapi/resources/api/models/models.py">list_paths_info</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/model_list_paths_info_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/model_list_paths_info_response.py">ModelListPathsInfoResponse</a></code>
- <code title="get /api/models/{namespace}/{repo}/refs">client.api.models.<a href="./src/pyhfapi/resources/api/models/models.py">list_refs</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/model_list_refs_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/model_list_refs_response.py">ModelListRefsResponse</a></code>
- <code title="get /api/models/{namespace}/{repo}/tree/{rev}/{path}">client.api.models.<a href="./src/pyhfapi/resources/api/models/models.py">list_tree_content</a>(path, \*, namespace, repo, rev, \*\*<a href="src/pyhfapi/types/api/model_list_tree_content_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/model_list_tree_content_response.py">ModelListTreeContentResponse</a></code>
- <code title="post /api/models/{namespace}/{repo}/super-squash/{rev}">client.api.models.<a href="./src/pyhfapi/resources/api/models/models.py">super_squash</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/model_super_squash_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/model_super_squash_response.py">ModelSuperSquashResponse</a></code>
- <code title="put /api/models/{namespace}/{repo}/settings">client.api.models.<a href="./src/pyhfapi/resources/api/models/models.py">update_settings</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/model_update_settings_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/model_update_settings_response.py">ModelUpdateSettingsResponse</a></code>

### LFSFiles

Types:

```python
from pyhfapi.types.api.models import LFSFileListResponse
```

Methods:

- <code title="get /api/models/{namespace}/{repo}/lfs-files">client.api.models.lfs_files.<a href="./src/pyhfapi/resources/api/models/lfs_files.py">list</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/models/lfs_file_list_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/models/lfs_file_list_response.py">LFSFileListResponse</a></code>
- <code title="delete /api/models/{namespace}/{repo}/lfs-files/{sha}">client.api.models.lfs_files.<a href="./src/pyhfapi/resources/api/models/lfs_files.py">delete</a>(sha, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/models/lfs_file_delete_params.py">params</a>) -> None</code>
- <code title="post /api/models/{namespace}/{repo}/lfs-files/batch">client.api.models.lfs_files.<a href="./src/pyhfapi/resources/api/models/lfs_files.py">delete_batch</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/models/lfs_file_delete_batch_params.py">params</a>) -> None</code>

### Tag

Methods:

- <code title="post /api/models/{namespace}/{repo}/tag/{rev}">client.api.models.tag.<a href="./src/pyhfapi/resources/api/models/tag.py">create</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/models/tag_create_params.py">params</a>) -> None</code>
- <code title="delete /api/models/{namespace}/{repo}/tag/{rev}">client.api.models.tag.<a href="./src/pyhfapi/resources/api/models/tag.py">delete</a>(rev, \*, namespace, repo) -> None</code>

### Branch

Methods:

- <code title="post /api/models/{namespace}/{repo}/branch/{rev}">client.api.models.branch.<a href="./src/pyhfapi/resources/api/models/branch.py">create</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/models/branch_create_params.py">params</a>) -> None</code>
- <code title="delete /api/models/{namespace}/{repo}/branch/{rev}">client.api.models.branch.<a href="./src/pyhfapi/resources/api/models/branch.py">delete</a>(rev, \*, namespace, repo) -> None</code>

### ResourceGroup

Types:

```python
from pyhfapi.types.api.models import ResourceGroupAddResponse, ResourceGroupGetResponse
```

Methods:

- <code title="post /api/models/{namespace}/{repo}/resource-group">client.api.models.resource_group.<a href="./src/pyhfapi/resources/api/models/resource_group.py">add</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/models/resource_group_add_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/models/resource_group_add_response.py">ResourceGroupAddResponse</a></code>
- <code title="get /api/models/{namespace}/{repo}/resource-group">client.api.models.resource_group.<a href="./src/pyhfapi/resources/api/models/resource_group.py">get</a>(repo, \*, namespace) -> <a href="./src/pyhfapi/types/api/models/resource_group_get_response.py">ResourceGroupGetResponse</a></code>

### UserAccessRequest

Types:

```python
from pyhfapi.types.api.models import UserAccessRequestListResponse
```

Methods:

- <code title="get /api/models/{namespace}/{repo}/user-access-request/{status}">client.api.models.user_access_request.<a href="./src/pyhfapi/resources/api/models/user_access_request.py">list</a>(status, \*, namespace, repo) -> <a href="./src/pyhfapi/types/api/models/user_access_request_list_response.py">UserAccessRequestListResponse</a></code>
- <code title="post /api/models/{namespace}/{repo}/user-access-request/cancel">client.api.models.user_access_request.<a href="./src/pyhfapi/resources/api/models/user_access_request.py">cancel</a>(repo, \*, namespace) -> None</code>
- <code title="post /api/models/{namespace}/{repo}/user-access-request/grant">client.api.models.user_access_request.<a href="./src/pyhfapi/resources/api/models/user_access_request.py">grant</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/models/user_access_request_grant_params.py">params</a>) -> None</code>
- <code title="post /api/models/{namespace}/{repo}/user-access-request/handle">client.api.models.user_access_request.<a href="./src/pyhfapi/resources/api/models/user_access_request.py">handle</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/models/user_access_request_handle_params.py">params</a>) -> None</code>

## Datasets

Types:

```python
from pyhfapi.types.api import (
    DatasetCheckPreuploadResponse,
    DatasetCommitResponse,
    DatasetCompareResponse,
    DatasetGetNotebookURLResponse,
    DatasetGetSecurityStatusResponse,
    DatasetGetXetReadTokenResponse,
    DatasetGetXetWriteTokenResponse,
    DatasetListCommitsResponse,
    DatasetListPathsInfoResponse,
    DatasetListRefsResponse,
    DatasetListTreeContentResponse,
    DatasetSuperSquashResponse,
    DatasetUpdateSettingsResponse,
)
```

Methods:

- <code title="post /api/datasets/{namespace}/{repo}/preupload/{rev}">client.api.datasets.<a href="./src/pyhfapi/resources/api/datasets/datasets.py">check_preupload</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/dataset_check_preupload_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/dataset_check_preupload_response.py">DatasetCheckPreuploadResponse</a></code>
- <code title="post /api/datasets/{namespace}/{repo}/commit/{rev}">client.api.datasets.<a href="./src/pyhfapi/resources/api/datasets/datasets.py">commit</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/dataset_commit_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/dataset_commit_response.py">DatasetCommitResponse</a></code>
- <code title="get /api/datasets/{namespace}/{repo}/compare/{compare}">client.api.datasets.<a href="./src/pyhfapi/resources/api/datasets/datasets.py">compare</a>(compare, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/dataset_compare_params.py">params</a>) -> str</code>
- <code title="get /api/datasets/{namespace}/{repo}/notebook/{rev}/{path}">client.api.datasets.<a href="./src/pyhfapi/resources/api/datasets/datasets.py">get_notebook_url</a>(path, \*, namespace, repo, rev) -> <a href="./src/pyhfapi/types/api/dataset_get_notebook_url_response.py">DatasetGetNotebookURLResponse</a></code>
- <code title="get /api/datasets/{namespace}/{repo}/scan">client.api.datasets.<a href="./src/pyhfapi/resources/api/datasets/datasets.py">get_security_status</a>(repo, \*, namespace) -> <a href="./src/pyhfapi/types/api/dataset_get_security_status_response.py">DatasetGetSecurityStatusResponse</a></code>
- <code title="get /api/datasets/{namespace}/{repo}/xet-read-token/{rev}">client.api.datasets.<a href="./src/pyhfapi/resources/api/datasets/datasets.py">get_xet_read_token</a>(rev, \*, namespace, repo) -> <a href="./src/pyhfapi/types/api/dataset_get_xet_read_token_response.py">DatasetGetXetReadTokenResponse</a></code>
- <code title="get /api/datasets/{namespace}/{repo}/xet-write-token/{rev}">client.api.datasets.<a href="./src/pyhfapi/resources/api/datasets/datasets.py">get_xet_write_token</a>(rev, \*, namespace, repo) -> <a href="./src/pyhfapi/types/api/dataset_get_xet_write_token_response.py">DatasetGetXetWriteTokenResponse</a></code>
- <code title="get /api/datasets/{namespace}/{repo}/commits/{rev}">client.api.datasets.<a href="./src/pyhfapi/resources/api/datasets/datasets.py">list_commits</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/dataset_list_commits_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/dataset_list_commits_response.py">DatasetListCommitsResponse</a></code>
- <code title="post /api/datasets/{namespace}/{repo}/paths-info/{rev}">client.api.datasets.<a href="./src/pyhfapi/resources/api/datasets/datasets.py">list_paths_info</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/dataset_list_paths_info_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/dataset_list_paths_info_response.py">DatasetListPathsInfoResponse</a></code>
- <code title="get /api/datasets/{namespace}/{repo}/refs">client.api.datasets.<a href="./src/pyhfapi/resources/api/datasets/datasets.py">list_refs</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/dataset_list_refs_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/dataset_list_refs_response.py">DatasetListRefsResponse</a></code>
- <code title="get /api/datasets/{namespace}/{repo}/tree/{rev}/{path}">client.api.datasets.<a href="./src/pyhfapi/resources/api/datasets/datasets.py">list_tree_content</a>(path, \*, namespace, repo, rev, \*\*<a href="src/pyhfapi/types/api/dataset_list_tree_content_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/dataset_list_tree_content_response.py">DatasetListTreeContentResponse</a></code>
- <code title="post /api/datasets/{namespace}/{repo}/super-squash/{rev}">client.api.datasets.<a href="./src/pyhfapi/resources/api/datasets/datasets.py">super_squash</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/dataset_super_squash_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/dataset_super_squash_response.py">DatasetSuperSquashResponse</a></code>
- <code title="put /api/datasets/{namespace}/{repo}/settings">client.api.datasets.<a href="./src/pyhfapi/resources/api/datasets/datasets.py">update_settings</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/dataset_update_settings_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/dataset_update_settings_response.py">DatasetUpdateSettingsResponse</a></code>

### LFSFiles

Types:

```python
from pyhfapi.types.api.datasets import LFSFileListResponse
```

Methods:

- <code title="get /api/datasets/{namespace}/{repo}/lfs-files">client.api.datasets.lfs_files.<a href="./src/pyhfapi/resources/api/datasets/lfs_files.py">list</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/datasets/lfs_file_list_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/datasets/lfs_file_list_response.py">LFSFileListResponse</a></code>
- <code title="delete /api/datasets/{namespace}/{repo}/lfs-files/{sha}">client.api.datasets.lfs_files.<a href="./src/pyhfapi/resources/api/datasets/lfs_files.py">delete</a>(sha, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/datasets/lfs_file_delete_params.py">params</a>) -> None</code>
- <code title="post /api/datasets/{namespace}/{repo}/lfs-files/batch">client.api.datasets.lfs_files.<a href="./src/pyhfapi/resources/api/datasets/lfs_files.py">delete_batch</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/datasets/lfs_file_delete_batch_params.py">params</a>) -> None</code>

### Tag

Methods:

- <code title="post /api/datasets/{namespace}/{repo}/tag/{rev}">client.api.datasets.tag.<a href="./src/pyhfapi/resources/api/datasets/tag.py">create</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/datasets/tag_create_params.py">params</a>) -> None</code>
- <code title="delete /api/datasets/{namespace}/{repo}/tag/{rev}">client.api.datasets.tag.<a href="./src/pyhfapi/resources/api/datasets/tag.py">delete</a>(rev, \*, namespace, repo) -> None</code>

### Branch

Methods:

- <code title="post /api/datasets/{namespace}/{repo}/branch/{rev}">client.api.datasets.branch.<a href="./src/pyhfapi/resources/api/datasets/branch.py">create</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/datasets/branch_create_params.py">params</a>) -> None</code>
- <code title="delete /api/datasets/{namespace}/{repo}/branch/{rev}">client.api.datasets.branch.<a href="./src/pyhfapi/resources/api/datasets/branch.py">delete</a>(rev, \*, namespace, repo) -> None</code>

### ResourceGroup

Types:

```python
from pyhfapi.types.api.datasets import ResourceGroupAddResponse, ResourceGroupGetResponse
```

Methods:

- <code title="post /api/datasets/{namespace}/{repo}/resource-group">client.api.datasets.resource_group.<a href="./src/pyhfapi/resources/api/datasets/resource_group.py">add</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/datasets/resource_group_add_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/datasets/resource_group_add_response.py">ResourceGroupAddResponse</a></code>
- <code title="get /api/datasets/{namespace}/{repo}/resource-group">client.api.datasets.resource_group.<a href="./src/pyhfapi/resources/api/datasets/resource_group.py">get</a>(repo, \*, namespace) -> <a href="./src/pyhfapi/types/api/datasets/resource_group_get_response.py">ResourceGroupGetResponse</a></code>

### UserAccessRequest

Types:

```python
from pyhfapi.types.api.datasets import UserAccessRequestListResponse
```

Methods:

- <code title="get /api/datasets/{namespace}/{repo}/user-access-request/{status}">client.api.datasets.user_access_request.<a href="./src/pyhfapi/resources/api/datasets/user_access_request.py">list</a>(status, \*, namespace, repo) -> <a href="./src/pyhfapi/types/api/datasets/user_access_request_list_response.py">UserAccessRequestListResponse</a></code>
- <code title="post /api/datasets/{namespace}/{repo}/user-access-request/cancel">client.api.datasets.user_access_request.<a href="./src/pyhfapi/resources/api/datasets/user_access_request.py">cancel</a>(repo, \*, namespace) -> None</code>
- <code title="post /api/datasets/{namespace}/{repo}/user-access-request/grant">client.api.datasets.user_access_request.<a href="./src/pyhfapi/resources/api/datasets/user_access_request.py">grant</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/datasets/user_access_request_grant_params.py">params</a>) -> None</code>
- <code title="post /api/datasets/{namespace}/{repo}/user-access-request/handle">client.api.datasets.user_access_request.<a href="./src/pyhfapi/resources/api/datasets/user_access_request.py">handle</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/datasets/user_access_request_handle_params.py">params</a>) -> None</code>

## Spaces

Types:

```python
from pyhfapi.types.api import (
    SpaceCheckPreuploadResponse,
    SpaceCommitResponse,
    SpaceCompareResponse,
    SpaceGetNotebookURLResponse,
    SpaceGetSecurityStatusResponse,
    SpaceGetXetReadTokenResponse,
    SpaceGetXetWriteTokenResponse,
    SpaceListCommitsResponse,
    SpaceListPathsInfoResponse,
    SpaceListRefsResponse,
    SpaceListTreeContentResponse,
    SpaceSuperSquashResponse,
    SpaceUpdateSettingsResponse,
)
```

Methods:

- <code title="post /api/spaces/{namespace}/{repo}/preupload/{rev}">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">check_preupload</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/space_check_preupload_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/space_check_preupload_response.py">SpaceCheckPreuploadResponse</a></code>
- <code title="post /api/spaces/{namespace}/{repo}/commit/{rev}">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">commit</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/space_commit_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/space_commit_response.py">SpaceCommitResponse</a></code>
- <code title="get /api/spaces/{namespace}/{repo}/compare/{compare}">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">compare</a>(compare, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/space_compare_params.py">params</a>) -> str</code>
- <code title="get /api/spaces/{namespace}/{repo}/notebook/{rev}/{path}">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">get_notebook_url</a>(path, \*, namespace, repo, rev) -> <a href="./src/pyhfapi/types/api/space_get_notebook_url_response.py">SpaceGetNotebookURLResponse</a></code>
- <code title="get /api/spaces/{namespace}/{repo}/scan">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">get_security_status</a>(repo, \*, namespace) -> <a href="./src/pyhfapi/types/api/space_get_security_status_response.py">SpaceGetSecurityStatusResponse</a></code>
- <code title="get /api/spaces/{namespace}/{repo}/xet-read-token/{rev}">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">get_xet_read_token</a>(rev, \*, namespace, repo) -> <a href="./src/pyhfapi/types/api/space_get_xet_read_token_response.py">SpaceGetXetReadTokenResponse</a></code>
- <code title="get /api/spaces/{namespace}/{repo}/xet-write-token/{rev}">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">get_xet_write_token</a>(rev, \*, namespace, repo) -> <a href="./src/pyhfapi/types/api/space_get_xet_write_token_response.py">SpaceGetXetWriteTokenResponse</a></code>
- <code title="get /api/spaces/{namespace}/{repo}/commits/{rev}">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">list_commits</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/space_list_commits_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/space_list_commits_response.py">SpaceListCommitsResponse</a></code>
- <code title="post /api/spaces/{namespace}/{repo}/paths-info/{rev}">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">list_paths_info</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/space_list_paths_info_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/space_list_paths_info_response.py">SpaceListPathsInfoResponse</a></code>
- <code title="get /api/spaces/{namespace}/{repo}/refs">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">list_refs</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/space_list_refs_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/space_list_refs_response.py">SpaceListRefsResponse</a></code>
- <code title="get /api/spaces/{namespace}/{repo}/tree/{rev}/{path}">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">list_tree_content</a>(path, \*, namespace, repo, rev, \*\*<a href="src/pyhfapi/types/api/space_list_tree_content_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/space_list_tree_content_response.py">SpaceListTreeContentResponse</a></code>
- <code title="get /api/spaces/{namespace}/{repo}/events">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">stream_events</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/space_stream_events_params.py">params</a>) -> None</code>
- <code title="get /api/spaces/{namespace}/{repo}/logs/{logType}">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">stream_logs</a>(log_type, \*, namespace, repo) -> None</code>
- <code title="get /api/spaces/{namespace}/{repo}/metrics">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">stream_metrics</a>(repo, \*, namespace) -> None</code>
- <code title="post /api/spaces/{namespace}/{repo}/super-squash/{rev}">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">super_squash</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/space_super_squash_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/space_super_squash_response.py">SpaceSuperSquashResponse</a></code>
- <code title="put /api/spaces/{namespace}/{repo}/settings">client.api.spaces.<a href="./src/pyhfapi/resources/api/spaces/spaces.py">update_settings</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/space_update_settings_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/space_update_settings_response.py">SpaceUpdateSettingsResponse</a></code>

### LFSFiles

Types:

```python
from pyhfapi.types.api.spaces import LFSFileListResponse
```

Methods:

- <code title="get /api/spaces/{namespace}/{repo}/lfs-files">client.api.spaces.lfs_files.<a href="./src/pyhfapi/resources/api/spaces/lfs_files.py">list</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/spaces/lfs_file_list_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/spaces/lfs_file_list_response.py">LFSFileListResponse</a></code>
- <code title="delete /api/spaces/{namespace}/{repo}/lfs-files/{sha}">client.api.spaces.lfs_files.<a href="./src/pyhfapi/resources/api/spaces/lfs_files.py">delete</a>(sha, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/spaces/lfs_file_delete_params.py">params</a>) -> None</code>
- <code title="post /api/spaces/{namespace}/{repo}/lfs-files/batch">client.api.spaces.lfs_files.<a href="./src/pyhfapi/resources/api/spaces/lfs_files.py">delete_batch</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/spaces/lfs_file_delete_batch_params.py">params</a>) -> None</code>

### Tag

Methods:

- <code title="post /api/spaces/{namespace}/{repo}/tag/{rev}">client.api.spaces.tag.<a href="./src/pyhfapi/resources/api/spaces/tag.py">create</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/spaces/tag_create_params.py">params</a>) -> None</code>
- <code title="delete /api/spaces/{namespace}/{repo}/tag/{rev}">client.api.spaces.tag.<a href="./src/pyhfapi/resources/api/spaces/tag.py">delete</a>(rev, \*, namespace, repo) -> None</code>

### Branch

Methods:

- <code title="post /api/spaces/{namespace}/{repo}/branch/{rev}">client.api.spaces.branch.<a href="./src/pyhfapi/resources/api/spaces/branch.py">create</a>(rev, \*, namespace, repo, \*\*<a href="src/pyhfapi/types/api/spaces/branch_create_params.py">params</a>) -> None</code>
- <code title="delete /api/spaces/{namespace}/{repo}/branch/{rev}">client.api.spaces.branch.<a href="./src/pyhfapi/resources/api/spaces/branch.py">delete</a>(rev, \*, namespace, repo) -> None</code>

### ResourceGroup

Types:

```python
from pyhfapi.types.api.spaces import ResourceGroupAddResponse, ResourceGroupGetResponse
```

Methods:

- <code title="post /api/spaces/{namespace}/{repo}/resource-group">client.api.spaces.resource_group.<a href="./src/pyhfapi/resources/api/spaces/resource_group.py">add</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/spaces/resource_group_add_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/spaces/resource_group_add_response.py">ResourceGroupAddResponse</a></code>
- <code title="get /api/spaces/{namespace}/{repo}/resource-group">client.api.spaces.resource_group.<a href="./src/pyhfapi/resources/api/spaces/resource_group.py">get</a>(repo, \*, namespace) -> <a href="./src/pyhfapi/types/api/spaces/resource_group_get_response.py">ResourceGroupGetResponse</a></code>

### Secrets

Methods:

- <code title="delete /api/spaces/{namespace}/{repo}/secrets">client.api.spaces.secrets.<a href="./src/pyhfapi/resources/api/spaces/secrets.py">delete</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/spaces/secret_delete_params.py">params</a>) -> None</code>
- <code title="post /api/spaces/{namespace}/{repo}/secrets">client.api.spaces.secrets.<a href="./src/pyhfapi/resources/api/spaces/secrets.py">upsert</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/spaces/secret_upsert_params.py">params</a>) -> None</code>

### Variables

Methods:

- <code title="delete /api/spaces/{namespace}/{repo}/variables">client.api.spaces.variables.<a href="./src/pyhfapi/resources/api/spaces/variables.py">delete</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/spaces/variable_delete_params.py">params</a>) -> None</code>
- <code title="post /api/spaces/{namespace}/{repo}/variables">client.api.spaces.variables.<a href="./src/pyhfapi/resources/api/spaces/variables.py">upsert</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/api/spaces/variable_upsert_params.py">params</a>) -> None</code>

## Repos

Types:

```python
from pyhfapi.types.api import RepoCreateResponse
```

Methods:

- <code title="post /api/repos/create">client.api.repos.<a href="./src/pyhfapi/resources/api/repos.py">create</a>(\*\*<a href="src/pyhfapi/types/api/repo_create_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/repo_create_response.py">RepoCreateResponse</a></code>
- <code title="post /api/repos/move">client.api.repos.<a href="./src/pyhfapi/resources/api/repos.py">move</a>(\*\*<a href="src/pyhfapi/types/api/repo_move_params.py">params</a>) -> None</code>

## SqlConsole

### Embed

Types:

```python
from pyhfapi.types.api.sql_console import EmbedCreateResponse, EmbedUpdateResponse
```

Methods:

- <code title="post /api/{repoType}/{namespace}/{repo}/sql-console/embed">client.api.sql_console.embed.<a href="./src/pyhfapi/resources/api/sql_console/embed.py">create</a>(repo, \*, repo_type, namespace, \*\*<a href="src/pyhfapi/types/api/sql_console/embed_create_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/sql_console/embed_create_response.py">EmbedCreateResponse</a></code>
- <code title="patch /api/{repoType}/{namespace}/{repo}/sql-console/embed/{id}">client.api.sql_console.embed.<a href="./src/pyhfapi/resources/api/sql_console/embed.py">update</a>(id, \*, repo_type, namespace, repo, \*\*<a href="src/pyhfapi/types/api/sql_console/embed_update_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/sql_console/embed_update_response.py">EmbedUpdateResponse</a></code>
- <code title="delete /api/{repoType}/{namespace}/{repo}/sql-console/embed/{id}">client.api.sql_console.embed.<a href="./src/pyhfapi/resources/api/sql_console/embed.py">delete</a>(id, \*, repo_type, namespace, repo) -> object</code>

## ResolveCache

Types:

```python
from pyhfapi.types.api import (
    ResolveCacheResolveDatasetResponse,
    ResolveCacheResolveModelResponse,
    ResolveCacheResolveSpaceResponse,
)
```

Methods:

- <code title="get /api/resolve-cache/datasets/{namespace}/{repo}/{rev}/{path}">client.api.resolve_cache.<a href="./src/pyhfapi/resources/api/resolve_cache.py">resolve_dataset</a>(path, \*, namespace, repo, rev) -> <a href="./src/pyhfapi/types/api/resolve_cache_resolve_dataset_response.py">ResolveCacheResolveDatasetResponse</a></code>
- <code title="get /api/resolve-cache/models/{namespace}/{repo}/{rev}/{path}">client.api.resolve_cache.<a href="./src/pyhfapi/resources/api/resolve_cache.py">resolve_model</a>(path, \*, namespace, repo, rev) -> <a href="./src/pyhfapi/types/api/resolve_cache_resolve_model_response.py">ResolveCacheResolveModelResponse</a></code>
- <code title="get /api/resolve-cache/spaces/{namespace}/{repo}/{rev}/{path}">client.api.resolve_cache.<a href="./src/pyhfapi/resources/api/resolve_cache.py">resolve_space</a>(path, \*, namespace, repo, rev) -> <a href="./src/pyhfapi/types/api/resolve_cache_resolve_space_response.py">ResolveCacheResolveSpaceResponse</a></code>

## Papers

Methods:

- <code title="get /api/papers/search">client.api.papers.<a href="./src/pyhfapi/resources/api/papers/papers.py">search</a>(\*\*<a href="src/pyhfapi/types/api/paper_search_params.py">params</a>) -> None</code>

### Comment

Types:

```python
from pyhfapi.types.api.papers import CommentCreateResponse, CommentReplyResponse
```

Methods:

- <code title="post /api/papers/{paperId}/comment">client.api.papers.comment.<a href="./src/pyhfapi/resources/api/papers/comment.py">create</a>(paper_id, \*\*<a href="src/pyhfapi/types/api/papers/comment_create_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/papers/comment_create_response.py">CommentCreateResponse</a></code>
- <code title="post /api/papers/{paperId}/comment/{commentId}/reply">client.api.papers.comment.<a href="./src/pyhfapi/resources/api/papers/comment.py">reply</a>(comment_id, \*, paper_id, \*\*<a href="src/pyhfapi/types/api/papers/comment_reply_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/papers/comment_reply_response.py">CommentReplyResponse</a></code>

## Posts

Methods:

- <code title="delete /api/posts/{username}/{postSlug}">client.api.posts.<a href="./src/pyhfapi/resources/api/posts/posts.py">delete</a>(post_slug, \*, username) -> None</code>

### Comment

Types:

```python
from pyhfapi.types.api.posts import CommentCreateResponse, CommentReplyResponse
```

Methods:

- <code title="post /api/posts/{username}/{postSlug}/comment">client.api.posts.comment.<a href="./src/pyhfapi/resources/api/posts/comment.py">create</a>(post_slug, \*, username, \*\*<a href="src/pyhfapi/types/api/posts/comment_create_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/posts/comment_create_response.py">CommentCreateResponse</a></code>
- <code title="post /api/posts/{username}/{postSlug}/comment/{commentId}/reply">client.api.posts.comment.<a href="./src/pyhfapi/resources/api/posts/comment.py">reply</a>(comment_id, \*, username, post_slug, \*\*<a href="src/pyhfapi/types/api/posts/comment_reply_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/posts/comment_reply_response.py">CommentReplyResponse</a></code>

## Collections

Types:

```python
from pyhfapi.types.api import (
    CollectionCreateResponse,
    CollectionUpdateResponse,
    CollectionListResponse,
    CollectionGetResponse,
)
```

Methods:

- <code title="post /api/collections">client.api.collections.<a href="./src/pyhfapi/resources/api/collections/collections.py">create</a>(\*\*<a href="src/pyhfapi/types/api/collection_create_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/collection_create_response.py">CollectionCreateResponse</a></code>
- <code title="patch /api/collections/{namespace}/{slug}-{id}">client.api.collections.<a href="./src/pyhfapi/resources/api/collections/collections.py">update</a>(id, \*, namespace, slug, \*\*<a href="src/pyhfapi/types/api/collection_update_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/collection_update_response.py">CollectionUpdateResponse</a></code>
- <code title="get /api/collections">client.api.collections.<a href="./src/pyhfapi/resources/api/collections/collections.py">list</a>(\*\*<a href="src/pyhfapi/types/api/collection_list_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/collection_list_response.py">CollectionListResponse</a></code>
- <code title="delete /api/collections/{namespace}/{slug}-{id}">client.api.collections.<a href="./src/pyhfapi/resources/api/collections/collections.py">delete</a>(id, \*, namespace, slug) -> None</code>
- <code title="get /api/collections/{namespace}/{slug}-{id}">client.api.collections.<a href="./src/pyhfapi/resources/api/collections/collections.py">get</a>(id, \*, namespace, slug) -> <a href="./src/pyhfapi/types/api/collection_get_response.py">CollectionGetResponse</a></code>

### Items

Types:

```python
from pyhfapi.types.api.collections import ItemAddResponse
```

Methods:

- <code title="delete /api/collections/{namespace}/{slug}-{id}/items/{itemId}">client.api.collections.items.<a href="./src/pyhfapi/resources/api/collections/items.py">delete</a>(item_id, \*, namespace, slug, id) -> None</code>
- <code title="post /api/collections/{namespace}/{slug}-{id}/items">client.api.collections.items.<a href="./src/pyhfapi/resources/api/collections/items.py">add</a>(id, \*, namespace, slug, \*\*<a href="src/pyhfapi/types/api/collections/item_add_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/collections/item_add_response.py">ItemAddResponse</a></code>
- <code title="post /api/collections/{namespace}/{slug}-{id}/items/batch">client.api.collections.items.<a href="./src/pyhfapi/resources/api/collections/items.py">batch_update</a>(id, \*, namespace, slug, \*\*<a href="src/pyhfapi/types/api/collections/item_batch_update_params.py">params</a>) -> None</code>

## Jobs

Types:

```python
from pyhfapi.types.api import (
    JobRetrieveResponse,
    JobListResponse,
    JobCancelResponse,
    JobStartResponse,
)
```

Methods:

- <code title="get /api/jobs/{namespace}/{jobId}">client.api.jobs.<a href="./src/pyhfapi/resources/api/jobs.py">retrieve</a>(job_id, \*, namespace) -> <a href="./src/pyhfapi/types/api/job_retrieve_response.py">JobRetrieveResponse</a></code>
- <code title="get /api/jobs/{namespace}">client.api.jobs.<a href="./src/pyhfapi/resources/api/jobs.py">list</a>(namespace) -> <a href="./src/pyhfapi/types/api/job_list_response.py">JobListResponse</a></code>
- <code title="post /api/jobs/{namespace}/{jobId}/cancel">client.api.jobs.<a href="./src/pyhfapi/resources/api/jobs.py">cancel</a>(job_id, \*, namespace) -> <a href="./src/pyhfapi/types/api/job_cancel_response.py">JobCancelResponse</a></code>
- <code title="post /api/jobs/{namespace}">client.api.jobs.<a href="./src/pyhfapi/resources/api/jobs.py">start</a>(namespace, \*\*<a href="src/pyhfapi/types/api/job_start_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/job_start_response.py">JobStartResponse</a></code>
- <code title="get /api/jobs/{namespace}/{jobId}/events">client.api.jobs.<a href="./src/pyhfapi/resources/api/jobs.py">stream_events</a>(job_id, \*, namespace) -> None</code>
- <code title="get /api/jobs/{namespace}/{jobId}/logs">client.api.jobs.<a href="./src/pyhfapi/resources/api/jobs.py">stream_logs</a>(job_id, \*, namespace) -> None</code>
- <code title="get /api/jobs/{namespace}/{jobId}/metrics">client.api.jobs.<a href="./src/pyhfapi/resources/api/jobs.py">stream_metrics</a>(job_id, \*, namespace) -> None</code>

## ScheduledJobs

Types:

```python
from pyhfapi.types.api import (
    ScheduledJobCreateResponse,
    ScheduledJobRetrieveResponse,
    ScheduledJobListResponse,
)
```

Methods:

- <code title="post /api/scheduled-jobs/{namespace}">client.api.scheduled_jobs.<a href="./src/pyhfapi/resources/api/scheduled_jobs.py">create</a>(namespace, \*\*<a href="src/pyhfapi/types/api/scheduled_job_create_params.py">params</a>) -> <a href="./src/pyhfapi/types/api/scheduled_job_create_response.py">ScheduledJobCreateResponse</a></code>
- <code title="get /api/scheduled-jobs/{namespace}/{scheduledJobId}">client.api.scheduled_jobs.<a href="./src/pyhfapi/resources/api/scheduled_jobs.py">retrieve</a>(scheduled_job_id, \*, namespace) -> <a href="./src/pyhfapi/types/api/scheduled_job_retrieve_response.py">ScheduledJobRetrieveResponse</a></code>
- <code title="get /api/scheduled-jobs/{namespace}">client.api.scheduled_jobs.<a href="./src/pyhfapi/resources/api/scheduled_jobs.py">list</a>(namespace) -> <a href="./src/pyhfapi/types/api/scheduled_job_list_response.py">ScheduledJobListResponse</a></code>
- <code title="delete /api/scheduled-jobs/{namespace}/{scheduledJobId}">client.api.scheduled_jobs.<a href="./src/pyhfapi/resources/api/scheduled_jobs.py">delete</a>(scheduled_job_id, \*, namespace) -> None</code>
- <code title="post /api/scheduled-jobs/{namespace}/{scheduledJobId}/resume">client.api.scheduled_jobs.<a href="./src/pyhfapi/resources/api/scheduled_jobs.py">resume</a>(scheduled_job_id, \*, namespace) -> None</code>
- <code title="post /api/scheduled-jobs/{namespace}/{scheduledJobId}/suspend">client.api.scheduled_jobs.<a href="./src/pyhfapi/resources/api/scheduled_jobs.py">suspend</a>(scheduled_job_id, \*, namespace) -> None</code>

# OAuth

## Userinfo

Types:

```python
from pyhfapi.types.oauth import UserinfoRetrieveResponse, UserinfoUpdateResponse
```

Methods:

- <code title="get /oauth/userinfo">client.oauth.userinfo.<a href="./src/pyhfapi/resources/oauth/userinfo.py">retrieve</a>() -> <a href="./src/pyhfapi/types/oauth/userinfo_retrieve_response.py">UserinfoRetrieveResponse</a></code>
- <code title="post /oauth/userinfo">client.oauth.userinfo.<a href="./src/pyhfapi/resources/oauth/userinfo.py">update</a>() -> <a href="./src/pyhfapi/types/oauth/userinfo_update_response.py">UserinfoUpdateResponse</a></code>

# Spaces

Types:

```python
from pyhfapi.types import SpaceResolveFileResponse
```

Methods:

- <code title="get /spaces/{namespace}/{repo}/resolve/{rev}/{path}">client.spaces.<a href="./src/pyhfapi/resources/spaces.py">resolve_file</a>(path, \*, namespace, repo, rev) -> <a href="./src/pyhfapi/types/space_resolve_file_response.py">SpaceResolveFileResponse</a></code>

# Datasets

Types:

```python
from pyhfapi.types import DatasetExportAccessReportResponse, DatasetResolveFileResponse
```

Methods:

- <code title="get /datasets/{namespace}/{repo}/user-access-report">client.datasets.<a href="./src/pyhfapi/resources/datasets.py">export_access_report</a>(repo, \*, namespace) -> str</code>
- <code title="post /datasets/{namespace}/{repo}/ask-access">client.datasets.<a href="./src/pyhfapi/resources/datasets.py">request_access</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/dataset_request_access_params.py">params</a>) -> None</code>
- <code title="get /datasets/{namespace}/{repo}/resolve/{rev}/{path}">client.datasets.<a href="./src/pyhfapi/resources/datasets.py">resolve_file</a>(path, \*, namespace, repo, rev) -> <a href="./src/pyhfapi/types/dataset_resolve_file_response.py">DatasetResolveFileResponse</a></code>

# Resolve

Types:

```python
from pyhfapi.types import ResolveFileResponse
```

Methods:

- <code title="get /{namespace}/{repo}/resolve/{rev}/{path}">client.resolve.<a href="./src/pyhfapi/resources/resolve.py">file</a>(path, \*, namespace, repo, rev) -> <a href="./src/pyhfapi/types/resolve_file_response.py">ResolveFileResponse</a></code>

# AskAccess

Methods:

- <code title="post /{namespace}/{repo}/ask-access">client.ask_access.<a href="./src/pyhfapi/resources/ask_access.py">request</a>(repo, \*, namespace, \*\*<a href="src/pyhfapi/types/ask_access_request_params.py">params</a>) -> None</code>

# UserAccessReport

Types:

```python
from pyhfapi.types import UserAccessReportExportResponse
```

Methods:

- <code title="get /{namespace}/{repo}/user-access-report">client.user_access_report.<a href="./src/pyhfapi/resources/user_access_report.py">export</a>(repo, \*, namespace) -> str</code>
