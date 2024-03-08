import typing

import pydantic
from pydantic import ConfigDict

from ...updates import (
    MetadataChangeset,
    UpdateCondition,
)
from .record import Administrator, StorageLocation


class CreateDatasetRequest(pydantic.BaseModel):
    administrator: Administrator
    storage_location: StorageLocation
    description: typing.Optional[str] = None
    metadata: dict[str, typing.Any] = pydantic.Field(default_factory=dict)
    tags: list[str] = pydantic.Field(default_factory=list)


class QueryDatasetsRequest(pydantic.BaseModel):
    filters: dict[str, typing.Any] = pydantic.Field(default_factory=dict)
    model_config = ConfigDict(extra="forbid")


class UpdateDatasetRequest(pydantic.BaseModel):
    metadata_changeset: typing.Optional[MetadataChangeset] = None
    description: typing.Optional[str] = None
    conditions: typing.Optional[list[UpdateCondition]] = None


class QueryDatasetFilesRequest(pydantic.BaseModel):
    page_token: typing.Optional[str] = None
    include_patterns: typing.Optional[list[str]] = None
    exclude_patterns: typing.Optional[list[str]] = None


class BeginSingleFileUploadRequest(pydantic.BaseModel):
    origination: str
    resource_path: str
    resource_size: int


class BeginSingleFileUploadResponse(pydantic.BaseModel):
    upload_id: str
    upload_url: str
