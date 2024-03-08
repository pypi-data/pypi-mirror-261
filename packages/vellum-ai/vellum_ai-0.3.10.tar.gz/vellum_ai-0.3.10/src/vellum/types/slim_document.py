# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .document_document_to_document_index import DocumentDocumentToDocumentIndex
from .document_status import DocumentStatus
from .processing_failure_reason_enum import ProcessingFailureReasonEnum
from .processing_state_enum import ProcessingStateEnum

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SlimDocument(pydantic.BaseModel):
    id: str = pydantic.Field(description="Vellum-generated ID that uniquely identifies this document.")
    external_id: typing.Optional[str] = pydantic.Field(
        description="The external ID that was originally provided when uploading the document."
    )
    last_uploaded_at: dt.datetime = pydantic.Field(
        description="A timestamp representing when this document was most recently uploaded."
    )
    label: str = pydantic.Field(description="Human-friendly name for this document.")
    processing_state: typing.Optional[ProcessingStateEnum] = pydantic.Field(
        description=(
            "An enum value representing where this document is along its processing lifecycle. Note that this is different than its indexing lifecycle.\n"
            "\n"
            "- `QUEUED` - Queued\n"
            "- `PROCESSING` - Processing\n"
            "- `PROCESSED` - Processed\n"
            "- `FAILED` - Failed\n"
        )
    )
    processing_failure_reason: typing.Optional[ProcessingFailureReasonEnum] = pydantic.Field(
        description=(
            "An enum value representing why the document could not be processed. Is null unless processing_state is FAILED.\n"
            "\n"
            "- `EXCEEDED_CHARACTER_LIMIT` - Exceeded Character Limit\n"
            "- `INVALID_FILE` - Invalid File\n"
        )
    )
    status: typing.Optional[DocumentStatus] = pydantic.Field(
        description=("The document's current status.\n" "\n" "- `ACTIVE` - Active\n")
    )
    keywords: typing.Optional[typing.List[str]] = pydantic.Field(
        description="A list of keywords associated with this document. Originally provided when uploading the document."
    )
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        description="A previously supplied JSON object containing metadata that can be filtered on when searching."
    )
    document_to_document_indexes: typing.List[DocumentDocumentToDocumentIndex]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
