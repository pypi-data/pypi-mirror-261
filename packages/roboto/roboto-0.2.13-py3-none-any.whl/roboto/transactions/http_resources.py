import typing

import pydantic

from .record import TransactionType


class BeginTransactionRequest(pydantic.BaseModel):
    transaction_type: TransactionType
    origination: str
    expected_resource_count: typing.Optional[int] = None


class BeginManifestTransactionRequest(pydantic.BaseModel):
    origination: str
    resource_manifest: dict[str, int]
    dataset_id: str


class ReportTransactionProgressRequest(pydantic.BaseModel):
    transaction_id: str
    manifest_items: list[str]


class TransactionCompletionResponse(pydantic.BaseModel):
    is_complete: bool
