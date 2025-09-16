# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CollectionCreateResponse",
    "Gating",
    "GatingMode",
    "GatingUnionMember2",
    "GatingUnionMember2Notifications",
    "Item",
    "ItemUnionMember0",
    "ItemUnionMember0DatasetsServerInfo",
    "ItemUnionMember0Note",
    "ItemUnionMember0ResourceGroup",
    "ItemUnionMember1",
    "ItemUnionMember1AvailableInferenceProvider",
    "ItemUnionMember1AvailableInferenceProviderFeatures",
    "ItemUnionMember1AuthorData",
    "ItemUnionMember1AuthorDataUnionMember0",
    "ItemUnionMember1AuthorDataUnionMember1",
    "ItemUnionMember1Note",
    "ItemUnionMember1ResourceGroup",
    "ItemUnionMember2",
    "ItemUnionMember2Runtime",
    "ItemUnionMember2RuntimeHardware",
    "ItemUnionMember2RuntimeReplicas",
    "ItemUnionMember2RuntimeDomain",
    "ItemUnionMember2AuthorData",
    "ItemUnionMember2AuthorDataUnionMember0",
    "ItemUnionMember2AuthorDataUnionMember1",
    "ItemUnionMember2Note",
    "ItemUnionMember2OriginSpace",
    "ItemUnionMember2OriginSpaceAuthor",
    "ItemUnionMember2OriginSpaceAuthorUnionMember0",
    "ItemUnionMember2OriginSpaceAuthorUnionMember1",
    "ItemUnionMember2ResourceGroup",
    "ItemUnionMember3",
    "ItemUnionMember3Note",
    "ItemUnionMember4",
    "ItemUnionMember4Owner",
    "ItemUnionMember4OwnerUnionMember0",
    "ItemUnionMember4OwnerUnionMember1",
    "ItemUnionMember4Note",
    "Owner",
    "OwnerUnionMember0",
    "OwnerUnionMember1",
]


class GatingMode(BaseModel):
    mode: Literal["auto"]


class GatingUnionMember2Notifications(BaseModel):
    mode: Literal["bulk", "real-time"]

    email: Optional[str] = None


class GatingUnionMember2(BaseModel):
    mode: Literal["manual"]

    notifications: GatingUnionMember2Notifications


Gating: TypeAlias = Union[Literal[True], GatingMode, GatingUnionMember2]


class ItemUnionMember0DatasetsServerInfo(BaseModel):
    formats: List[Literal["json", "csv", "parquet", "imagefolder", "audiofolder", "webdataset", "text", "arrow"]]

    libraries: List[
        Literal[
            "mlcroissant",
            "webdataset",
            "datasets",
            "pandas",
            "dask",
            "distilabel",
            "fiftyone",
            "argilla",
            "polars",
            "duckdb",
        ]
    ]

    modalities: List[
        Literal["3d", "audio", "document", "geospatial", "image", "tabular", "text", "timeseries", "video"]
    ]

    num_rows: Optional[float] = FieldInfo(alias="numRows", default=None)

    viewer: Literal["preview", "viewer-partial", "viewer"]


class ItemUnionMember0Note(BaseModel):
    html: str

    text: str


class ItemUnionMember0ResourceGroup(BaseModel):
    id: str

    name: str

    num_users: Optional[float] = FieldInfo(alias="numUsers", default=None)


class ItemUnionMember0(BaseModel):
    id: str

    author: str

    downloads: float

    gated: Union[Literal["auto", "manual"], object]

    is_liked_by_user: bool = FieldInfo(alias="isLikedByUser")

    last_modified: datetime = FieldInfo(alias="lastModified")

    likes: float

    private: bool

    repo_type: Literal["dataset"] = FieldInfo(alias="repoType")

    type: Literal["dataset"]

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    datasets_server_info: Optional[ItemUnionMember0DatasetsServerInfo] = FieldInfo(
        alias="datasetsServerInfo", default=None
    )

    gallery: Optional[List[str]] = None

    note: Optional[ItemUnionMember0Note] = None

    position: Optional[float] = None

    resource_group: Optional[ItemUnionMember0ResourceGroup] = FieldInfo(alias="resourceGroup", default=None)


class ItemUnionMember1AvailableInferenceProviderFeatures(BaseModel):
    tool_calling: Optional[bool] = FieldInfo(alias="toolCalling", default=None)


class ItemUnionMember1AvailableInferenceProvider(BaseModel):
    api_model_status: Literal["live", "staging", "error"] = FieldInfo(alias="modelStatus")

    provider: Literal[
        "black-forest-labs",
        "cerebras",
        "cohere",
        "fal-ai",
        "featherless-ai",
        "fireworks-ai",
        "groq",
        "hf-inference",
        "hyperbolic",
        "nebius",
        "novita",
        "nscale",
        "openai",
        "ovhcloud",
        "publicai",
        "replicate",
        "sambanova",
        "scaleway",
        "together",
    ]

    provider_id: str = FieldInfo(alias="providerId")

    provider_status: Literal["live", "staging", "error"] = FieldInfo(alias="providerStatus")

    task: Literal[
        "text-classification",
        "token-classification",
        "table-question-answering",
        "question-answering",
        "zero-shot-classification",
        "translation",
        "summarization",
        "feature-extraction",
        "text-generation",
        "fill-mask",
        "sentence-similarity",
        "text-to-speech",
        "text-to-audio",
        "automatic-speech-recognition",
        "audio-to-audio",
        "audio-classification",
        "audio-text-to-text",
        "voice-activity-detection",
        "depth-estimation",
        "image-classification",
        "object-detection",
        "image-segmentation",
        "text-to-image",
        "image-to-text",
        "image-to-image",
        "image-to-video",
        "unconditional-image-generation",
        "video-classification",
        "reinforcement-learning",
        "robotics",
        "tabular-classification",
        "tabular-regression",
        "tabular-to-text",
        "table-to-text",
        "multiple-choice",
        "text-ranking",
        "text-retrieval",
        "time-series-forecasting",
        "text-to-video",
        "image-text-to-text",
        "visual-question-answering",
        "document-question-answering",
        "zero-shot-image-classification",
        "graph-ml",
        "mask-generation",
        "zero-shot-object-detection",
        "text-to-3d",
        "image-to-3d",
        "image-feature-extraction",
        "video-text-to-text",
        "keypoint-detection",
        "visual-document-retrieval",
        "any-to-any",
        "video-to-video",
        "other",
        "conversational",
    ]

    adapter_type: Optional[Literal["lora"]] = FieldInfo(alias="adapterType", default=None)

    adapter_weights_path: Optional[str] = FieldInfo(alias="adapterWeightsPath", default=None)

    features: Optional[ItemUnionMember1AvailableInferenceProviderFeatures] = None


class ItemUnionMember1AuthorDataUnionMember0(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_enterprise: bool = FieldInfo(alias="isEnterprise")

    is_hf: bool = FieldInfo(alias="isHf")

    is_hf_admin: bool = FieldInfo(alias="isHfAdmin")

    is_mod: bool = FieldInfo(alias="isMod")

    name: str

    type: Literal["org"]

    follower_count: Optional[float] = FieldInfo(alias="followerCount", default=None)

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


class ItemUnionMember1AuthorDataUnionMember1(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_hf: bool = FieldInfo(alias="isHf")

    is_hf_admin: bool = FieldInfo(alias="isHfAdmin")

    is_mod: bool = FieldInfo(alias="isMod")

    is_pro: bool = FieldInfo(alias="isPro")

    name: str

    type: Literal["user"]

    follower_count: Optional[float] = FieldInfo(alias="followerCount", default=None)

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


ItemUnionMember1AuthorData: TypeAlias = Union[
    ItemUnionMember1AuthorDataUnionMember0, ItemUnionMember1AuthorDataUnionMember1
]


class ItemUnionMember1Note(BaseModel):
    html: str

    text: str


class ItemUnionMember1ResourceGroup(BaseModel):
    id: str

    name: str

    num_users: Optional[float] = FieldInfo(alias="numUsers", default=None)


class ItemUnionMember1(BaseModel):
    id: str

    author: str

    available_inference_providers: List[ItemUnionMember1AvailableInferenceProvider] = FieldInfo(
        alias="availableInferenceProviders"
    )

    downloads: float

    gated: Union[Literal["auto", "manual"], object]

    is_liked_by_user: bool = FieldInfo(alias="isLikedByUser")

    last_modified: datetime = FieldInfo(alias="lastModified")

    likes: float

    private: bool

    repo_type: Literal["model"] = FieldInfo(alias="repoType")

    type: Literal["model"]

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    author_data: Optional[ItemUnionMember1AuthorData] = FieldInfo(alias="authorData", default=None)

    gallery: Optional[List[str]] = None

    note: Optional[ItemUnionMember1Note] = None

    num_parameters: Optional[float] = FieldInfo(alias="numParameters", default=None)

    pipeline_tag: Optional[str] = None

    position: Optional[float] = None

    resource_group: Optional[ItemUnionMember1ResourceGroup] = FieldInfo(alias="resourceGroup", default=None)

    widget_output_urls: Optional[List[str]] = FieldInfo(alias="widgetOutputUrls", default=None)


class ItemUnionMember2RuntimeHardware(BaseModel):
    current: Optional[
        Literal[
            "cpu-basic",
            "cpu-upgrade",
            "cpu-performance",
            "cpu-xl",
            "zero-a10g",
            "t4-small",
            "t4-medium",
            "l4x1",
            "l4x4",
            "l40sx1",
            "l40sx4",
            "l40sx8",
            "a10g-small",
            "a10g-large",
            "a10g-largex2",
            "a10g-largex4",
            "a100-large",
            "h100",
            "h100x8",
            "inf2x6",
        ]
    ] = None

    requested: Optional[
        Literal[
            "cpu-basic",
            "cpu-upgrade",
            "cpu-performance",
            "cpu-xl",
            "zero-a10g",
            "t4-small",
            "t4-medium",
            "l4x1",
            "l4x4",
            "l40sx1",
            "l40sx4",
            "l40sx8",
            "a10g-small",
            "a10g-large",
            "a10g-largex2",
            "a10g-largex4",
            "a100-large",
            "h100",
            "h100x8",
            "inf2x6",
        ]
    ] = None


class ItemUnionMember2RuntimeReplicas(BaseModel):
    requested: Union[float, Literal["auto"]]

    current: Optional[float] = None


class ItemUnionMember2RuntimeDomain(BaseModel):
    domain: str

    stage: Literal["READY", "PENDING"]

    is_custom: Optional[bool] = FieldInfo(alias="isCustom", default=None)


class ItemUnionMember2Runtime(BaseModel):
    hardware: ItemUnionMember2RuntimeHardware

    replicas: ItemUnionMember2RuntimeReplicas

    stage: Literal[
        "NO_APP_FILE",
        "CONFIG_ERROR",
        "BUILDING",
        "BUILD_ERROR",
        "APP_STARTING",
        "RUNNING",
        "RUNNING_BUILDING",
        "RUNNING_APP_STARTING",
        "RUNTIME_ERROR",
        "DELETING",
        "STOPPED",
        "PAUSED",
        "SLEEPING",
    ]

    storage: Optional[Literal["small", "medium", "large"]] = None

    dev_mode: Optional[bool] = FieldInfo(alias="devMode", default=None)

    domains: Optional[List[ItemUnionMember2RuntimeDomain]] = None

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)

    gc_timeout: Optional[float] = FieldInfo(alias="gcTimeout", default=None)

    sha: Optional[str] = None


class ItemUnionMember2AuthorDataUnionMember0(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_enterprise: bool = FieldInfo(alias="isEnterprise")

    is_hf: bool = FieldInfo(alias="isHf")

    is_hf_admin: bool = FieldInfo(alias="isHfAdmin")

    is_mod: bool = FieldInfo(alias="isMod")

    name: str

    type: Literal["org"]

    follower_count: Optional[float] = FieldInfo(alias="followerCount", default=None)

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


class ItemUnionMember2AuthorDataUnionMember1(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_hf: bool = FieldInfo(alias="isHf")

    is_hf_admin: bool = FieldInfo(alias="isHfAdmin")

    is_mod: bool = FieldInfo(alias="isMod")

    is_pro: bool = FieldInfo(alias="isPro")

    name: str

    type: Literal["user"]

    follower_count: Optional[float] = FieldInfo(alias="followerCount", default=None)

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


ItemUnionMember2AuthorData: TypeAlias = Union[
    ItemUnionMember2AuthorDataUnionMember0, ItemUnionMember2AuthorDataUnionMember1
]


class ItemUnionMember2Note(BaseModel):
    html: str

    text: str


class ItemUnionMember2OriginSpaceAuthorUnionMember0(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_enterprise: bool = FieldInfo(alias="isEnterprise")

    is_hf: bool = FieldInfo(alias="isHf")

    is_hf_admin: bool = FieldInfo(alias="isHfAdmin")

    is_mod: bool = FieldInfo(alias="isMod")

    name: str

    type: Literal["org"]

    follower_count: Optional[float] = FieldInfo(alias="followerCount", default=None)

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


class ItemUnionMember2OriginSpaceAuthorUnionMember1(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_hf: bool = FieldInfo(alias="isHf")

    is_hf_admin: bool = FieldInfo(alias="isHfAdmin")

    is_mod: bool = FieldInfo(alias="isMod")

    is_pro: bool = FieldInfo(alias="isPro")

    name: str

    type: Literal["user"]

    follower_count: Optional[float] = FieldInfo(alias="followerCount", default=None)

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


ItemUnionMember2OriginSpaceAuthor: TypeAlias = Union[
    ItemUnionMember2OriginSpaceAuthorUnionMember0, ItemUnionMember2OriginSpaceAuthorUnionMember1
]


class ItemUnionMember2OriginSpace(BaseModel):
    author: ItemUnionMember2OriginSpaceAuthor

    name: str


class ItemUnionMember2ResourceGroup(BaseModel):
    id: str

    name: str

    num_users: Optional[float] = FieldInfo(alias="numUsers", default=None)


class ItemUnionMember2(BaseModel):
    id: str

    author: str

    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    created_at: datetime = FieldInfo(alias="createdAt")

    emoji: str

    is_liked_by_user: bool = FieldInfo(alias="isLikedByUser")

    last_modified: datetime = FieldInfo(alias="lastModified")

    likes: float

    pinned: bool

    private: bool

    repo_type: Literal["space"] = FieldInfo(alias="repoType")

    runtime: ItemUnionMember2Runtime

    tags: List[str]

    title: str

    type: Literal["space"]

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    ai_category: Optional[str] = None

    ai_short_description: Optional[str] = None

    author_data: Optional[ItemUnionMember2AuthorData] = FieldInfo(alias="authorData", default=None)

    gallery: Optional[List[str]] = None

    note: Optional[ItemUnionMember2Note] = None

    origin_space: Optional[ItemUnionMember2OriginSpace] = FieldInfo(alias="originSpace", default=None)

    position: Optional[float] = None

    resource_group: Optional[ItemUnionMember2ResourceGroup] = FieldInfo(alias="resourceGroup", default=None)

    sdk: Optional[Literal["gradio", "docker", "static", "streamlit"]] = None

    semantic_relevancy_score: Optional[float] = FieldInfo(alias="semanticRelevancyScore", default=None)

    short_description: Optional[str] = FieldInfo(alias="shortDescription", default=None)

    trending_score: Optional[float] = FieldInfo(alias="trendingScore", default=None)


class ItemUnionMember3Note(BaseModel):
    html: str

    text: str


class ItemUnionMember3(BaseModel):
    id: str

    published_at: datetime = FieldInfo(alias="publishedAt")

    title: str

    type: Literal["paper"]

    upvotes: float

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    gallery: Optional[List[str]] = None

    is_upvoted_by_user: Optional[bool] = FieldInfo(alias="isUpvotedByUser", default=None)

    note: Optional[ItemUnionMember3Note] = None

    position: Optional[float] = None

    thumbnail_url: Optional[str] = FieldInfo(alias="thumbnailUrl", default=None)


class ItemUnionMember4OwnerUnionMember0(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_enterprise: bool = FieldInfo(alias="isEnterprise")

    is_hf: bool = FieldInfo(alias="isHf")

    is_hf_admin: bool = FieldInfo(alias="isHfAdmin")

    is_mod: bool = FieldInfo(alias="isMod")

    name: str

    type: Literal["org"]

    follower_count: Optional[float] = FieldInfo(alias="followerCount", default=None)

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


class ItemUnionMember4OwnerUnionMember1(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_hf: bool = FieldInfo(alias="isHf")

    is_hf_admin: bool = FieldInfo(alias="isHfAdmin")

    is_mod: bool = FieldInfo(alias="isMod")

    is_pro: bool = FieldInfo(alias="isPro")

    name: str

    type: Literal["user"]

    follower_count: Optional[float] = FieldInfo(alias="followerCount", default=None)

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


ItemUnionMember4Owner: TypeAlias = Union[ItemUnionMember4OwnerUnionMember0, ItemUnionMember4OwnerUnionMember1]


class ItemUnionMember4Note(BaseModel):
    html: str

    text: str


class ItemUnionMember4(BaseModel):
    id: str

    is_upvoted_by_user: bool = FieldInfo(alias="isUpvotedByUser")

    last_updated: datetime = FieldInfo(alias="lastUpdated")

    number_items: float = FieldInfo(alias="numberItems")

    owner: ItemUnionMember4Owner

    share_url: str = FieldInfo(alias="shareUrl")

    slug: str

    theme: Literal["orange", "blue", "green", "purple", "pink", "indigo"]

    title: str

    type: Literal["collection"]

    upvotes: float

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    description: Optional[str] = None

    gallery: Optional[List[str]] = None

    note: Optional[ItemUnionMember4Note] = None

    position: Optional[float] = None


Item: TypeAlias = Union[ItemUnionMember0, ItemUnionMember1, ItemUnionMember2, ItemUnionMember3, ItemUnionMember4]


class OwnerUnionMember0(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_enterprise: bool = FieldInfo(alias="isEnterprise")

    is_hf: bool = FieldInfo(alias="isHf")

    is_hf_admin: bool = FieldInfo(alias="isHfAdmin")

    is_mod: bool = FieldInfo(alias="isMod")

    name: str

    type: Literal["org"]

    follower_count: Optional[float] = FieldInfo(alias="followerCount", default=None)

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


class OwnerUnionMember1(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_hf: bool = FieldInfo(alias="isHf")

    is_hf_admin: bool = FieldInfo(alias="isHfAdmin")

    is_mod: bool = FieldInfo(alias="isMod")

    is_pro: bool = FieldInfo(alias="isPro")

    name: str

    type: Literal["user"]

    follower_count: Optional[float] = FieldInfo(alias="followerCount", default=None)

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


Owner: TypeAlias = Union[OwnerUnionMember0, OwnerUnionMember1]


class CollectionCreateResponse(BaseModel):
    gating: Gating

    is_upvoted_by_user: bool = FieldInfo(alias="isUpvotedByUser")

    items: List[Item]

    last_updated: datetime = FieldInfo(alias="lastUpdated")

    owner: Owner

    position: float

    private: bool

    share_url: str = FieldInfo(alias="shareUrl")

    slug: str

    theme: Literal["orange", "blue", "green", "purple", "pink", "indigo"]

    title: str

    upvotes: float

    description: Optional[str] = None
