from math import ceil

from pydantic import BaseModel, Field


class MessageResponse(BaseModel):
    """
    Generic response containing a message.
    """

    message: str


class PaginationMetadata(BaseModel):
    """
    Pagination metadata.
    """

    page: int = Field(
        ge=1,
        description="Current page number.",
    )

    page_size: int = Field(
        ge=1,
        description="Number of records per page.",
    )

    total_records: int = Field(
        ge=0,
        description="Total number of records.",
    )

    total_pages: int = Field(
        ge=0,
        description="Total number of pages.",
    )

    has_previous: bool = Field(
        description="Whether a previous page exists.",
    )

    has_next: bool = Field(
        description="Whether a next page exists.",
    )

    @classmethod
    def create(
        cls,
        page: int,
        page_size: int,
        total_records: int,
    ) -> "PaginationMetadata":
        """
        Build pagination metadata.
        """

        total_pages = (
            ceil(total_records / page_size)
            if total_records > 0
            else 0
        )

        return cls(
            page=page,
            page_size=page_size,
            total_records=total_records,
            total_pages=total_pages,
            has_previous=page > 1,
            has_next=page < total_pages,
        )