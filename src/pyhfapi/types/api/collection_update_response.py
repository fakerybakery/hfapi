# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CollectionUpdateResponse",
    "Data",
    "DataGating",
    "DataGatingMode",
    "DataGatingUnionMember2",
    "DataGatingUnionMember2Notifications",
    "DataItem",
    "DataItemUnionMember0",
    "DataItemUnionMember0DatasetsServerInfo",
    "DataItemUnionMember0Note",
    "DataItemUnionMember0ResourceGroup",
    "DataItemUnionMember1",
    "DataItemUnionMember1AvailableInferenceProvider",
    "DataItemUnionMember1AvailableInferenceProviderFeatures",
    "DataItemUnionMember1AuthorData",
    "DataItemUnionMember1AuthorDataUnionMember0",
    "DataItemUnionMember1AuthorDataUnionMember1",
    "DataItemUnionMember1Note",
    "DataItemUnionMember1ResourceGroup",
    "DataItemUnionMember2",
    "DataItemUnionMember2Runtime",
    "DataItemUnionMember2RuntimeHardware",
    "DataItemUnionMember2RuntimeReplicas",
    "DataItemUnionMember2RuntimeDomain",
    "DataItemUnionMember2AuthorData",
    "DataItemUnionMember2AuthorDataUnionMember0",
    "DataItemUnionMember2AuthorDataUnionMember1",
    "DataItemUnionMember2Note",
    "DataItemUnionMember2OriginSpace",
    "DataItemUnionMember2OriginSpaceAuthor",
    "DataItemUnionMember2OriginSpaceAuthorUnionMember0",
    "DataItemUnionMember2OriginSpaceAuthorUnionMember1",
    "DataItemUnionMember2ResourceGroup",
    "DataItemUnionMember3",
    "DataItemUnionMember3Note",
    "DataItemUnionMember4",
    "DataItemUnionMember4Owner",
    "DataItemUnionMember4OwnerUnionMember0",
    "DataItemUnionMember4OwnerUnionMember1",
    "DataItemUnionMember4Note",
    "DataOwner",
    "DataOwnerUnionMember0",
    "DataOwnerUnionMember1",
]


class DataGatingMode(BaseModel):
    mode: Literal["auto"]


class DataGatingUnionMember2Notifications(BaseModel):
    mode: Literal["bulk", "real-time"]

    email: Optional[str] = None


class DataGatingUnionMember2(BaseModel):
    mode: Literal["manual"]

    notifications: DataGatingUnionMember2Notifications


DataGating: TypeAlias = Union[Literal[True], DataGatingMode, DataGatingUnionMember2]


class DataItemUnionMember0DatasetsServerInfo(BaseModel):
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


class DataItemUnionMember0Note(BaseModel):
    html: str

    text: str


class DataItemUnionMember0ResourceGroup(BaseModel):
    id: str

    name: str

    num_users: Optional[float] = FieldInfo(alias="numUsers", default=None)


class DataItemUnionMember0(BaseModel):
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

    datasets_server_info: Optional[DataItemUnionMember0DatasetsServerInfo] = FieldInfo(
        alias="datasetsServerInfo", default=None
    )

    gallery: Optional[List[str]] = None

    note: Optional[DataItemUnionMember0Note] = None

    position: Optional[float] = None

    resource_group: Optional[DataItemUnionMember0ResourceGroup] = FieldInfo(alias="resourceGroup", default=None)


class DataItemUnionMember1AvailableInferenceProviderFeatures(BaseModel):
    tool_calling: Optional[bool] = FieldInfo(alias="toolCalling", default=None)


class DataItemUnionMember1AvailableInferenceProvider(BaseModel):
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

    features: Optional[DataItemUnionMember1AvailableInferenceProviderFeatures] = None


class DataItemUnionMember1AuthorDataUnionMember0(BaseModel):
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


class DataItemUnionMember1AuthorDataUnionMember1(BaseModel):
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


DataItemUnionMember1AuthorData: TypeAlias = Union[
    DataItemUnionMember1AuthorDataUnionMember0, DataItemUnionMember1AuthorDataUnionMember1
]


class DataItemUnionMember1Note(BaseModel):
    html: str

    text: str


class DataItemUnionMember1ResourceGroup(BaseModel):
    id: str

    name: str

    num_users: Optional[float] = FieldInfo(alias="numUsers", default=None)


class DataItemUnionMember1(BaseModel):
    id: str

    author: str

    available_inference_providers: List[DataItemUnionMember1AvailableInferenceProvider] = FieldInfo(
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

    author_data: Optional[DataItemUnionMember1AuthorData] = FieldInfo(alias="authorData", default=None)

    gallery: Optional[List[str]] = None

    note: Optional[DataItemUnionMember1Note] = None

    num_parameters: Optional[float] = FieldInfo(alias="numParameters", default=None)

    pipeline_tag: Optional[str] = None

    position: Optional[float] = None

    resource_group: Optional[DataItemUnionMember1ResourceGroup] = FieldInfo(alias="resourceGroup", default=None)

    widget_output_urls: Optional[List[str]] = FieldInfo(alias="widgetOutputUrls", default=None)


class DataItemUnionMember2RuntimeHardware(BaseModel):
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


class DataItemUnionMember2RuntimeReplicas(BaseModel):
    requested: Union[float, Literal["auto"]]

    current: Optional[float] = None


class DataItemUnionMember2RuntimeDomain(BaseModel):
    domain: str

    stage: Literal["READY", "PENDING"]

    is_custom: Optional[bool] = FieldInfo(alias="isCustom", default=None)


class DataItemUnionMember2Runtime(BaseModel):
    hardware: DataItemUnionMember2RuntimeHardware

    replicas: DataItemUnionMember2RuntimeReplicas

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

    domains: Optional[List[DataItemUnionMember2RuntimeDomain]] = None

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)

    gc_timeout: Optional[float] = FieldInfo(alias="gcTimeout", default=None)

    sha: Optional[str] = None


class DataItemUnionMember2AuthorDataUnionMember0(BaseModel):
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


class DataItemUnionMember2AuthorDataUnionMember1(BaseModel):
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


DataItemUnionMember2AuthorData: TypeAlias = Union[
    DataItemUnionMember2AuthorDataUnionMember0, DataItemUnionMember2AuthorDataUnionMember1
]


class DataItemUnionMember2Note(BaseModel):
    html: str

    text: str


class DataItemUnionMember2OriginSpaceAuthorUnionMember0(BaseModel):
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


class DataItemUnionMember2OriginSpaceAuthorUnionMember1(BaseModel):
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


DataItemUnionMember2OriginSpaceAuthor: TypeAlias = Union[
    DataItemUnionMember2OriginSpaceAuthorUnionMember0, DataItemUnionMember2OriginSpaceAuthorUnionMember1
]


class DataItemUnionMember2OriginSpace(BaseModel):
    author: DataItemUnionMember2OriginSpaceAuthor

    name: str


class DataItemUnionMember2ResourceGroup(BaseModel):
    id: str

    name: str

    num_users: Optional[float] = FieldInfo(alias="numUsers", default=None)


class DataItemUnionMember2(BaseModel):
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

    runtime: DataItemUnionMember2Runtime

    tags: List[str]

    title: str

    type: Literal["space"]

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    ai_category: Optional[str] = None

    ai_short_description: Optional[str] = None

    author_data: Optional[DataItemUnionMember2AuthorData] = FieldInfo(alias="authorData", default=None)

    gallery: Optional[List[str]] = None

    note: Optional[DataItemUnionMember2Note] = None

    origin_space: Optional[DataItemUnionMember2OriginSpace] = FieldInfo(alias="originSpace", default=None)

    position: Optional[float] = None

    resource_group: Optional[DataItemUnionMember2ResourceGroup] = FieldInfo(alias="resourceGroup", default=None)

    sdk: Optional[Literal["gradio", "docker", "static", "streamlit"]] = None

    semantic_relevancy_score: Optional[float] = FieldInfo(alias="semanticRelevancyScore", default=None)

    short_description: Optional[str] = FieldInfo(alias="shortDescription", default=None)

    trending_score: Optional[float] = FieldInfo(alias="trendingScore", default=None)


class DataItemUnionMember3Note(BaseModel):
    html: str

    text: str


class DataItemUnionMember3(BaseModel):
    id: str

    published_at: datetime = FieldInfo(alias="publishedAt")

    title: str

    type: Literal["paper"]

    upvotes: float

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    gallery: Optional[List[str]] = None

    is_upvoted_by_user: Optional[bool] = FieldInfo(alias="isUpvotedByUser", default=None)

    note: Optional[DataItemUnionMember3Note] = None

    position: Optional[float] = None

    thumbnail_url: Optional[str] = FieldInfo(alias="thumbnailUrl", default=None)


class DataItemUnionMember4OwnerUnionMember0(BaseModel):
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


class DataItemUnionMember4OwnerUnionMember1(BaseModel):
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


DataItemUnionMember4Owner: TypeAlias = Union[
    DataItemUnionMember4OwnerUnionMember0, DataItemUnionMember4OwnerUnionMember1
]


class DataItemUnionMember4Note(BaseModel):
    html: str

    text: str


class DataItemUnionMember4(BaseModel):
    id: str

    is_upvoted_by_user: bool = FieldInfo(alias="isUpvotedByUser")

    last_updated: datetime = FieldInfo(alias="lastUpdated")

    number_items: float = FieldInfo(alias="numberItems")

    owner: DataItemUnionMember4Owner

    share_url: str = FieldInfo(alias="shareUrl")

    slug: str

    theme: Literal["orange", "blue", "green", "purple", "pink", "indigo"]

    title: str

    type: Literal["collection"]

    upvotes: float

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    description: Optional[str] = None

    gallery: Optional[List[str]] = None

    note: Optional[DataItemUnionMember4Note] = None

    position: Optional[float] = None


DataItem: TypeAlias = Union[
    DataItemUnionMember0, DataItemUnionMember1, DataItemUnionMember2, DataItemUnionMember3, DataItemUnionMember4
]


class DataOwnerUnionMember0(BaseModel):
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


class DataOwnerUnionMember1(BaseModel):
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


DataOwner: TypeAlias = Union[DataOwnerUnionMember0, DataOwnerUnionMember1]


class Data(BaseModel):
    gating: DataGating

    is_upvoted_by_user: bool = FieldInfo(alias="isUpvotedByUser")

    items: List[DataItem]

    last_updated: datetime = FieldInfo(alias="lastUpdated")

    owner: DataOwner

    position: float

    private: bool

    share_url: str = FieldInfo(alias="shareUrl")

    slug: str

    theme: Literal["orange", "blue", "green", "purple", "pink", "indigo"]

    title: str

    upvotes: float

    description: Optional[str] = None


class CollectionUpdateResponse(BaseModel):
    data: Data
