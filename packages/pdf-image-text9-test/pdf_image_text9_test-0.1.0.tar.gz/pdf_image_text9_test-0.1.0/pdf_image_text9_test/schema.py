from pydantic import BaseModel
from enum import Enum, auto


class MetaData(BaseModel):
    page: int


class Page(BaseModel):
    text_content: str
    image_content: list
    formatted_content: str | None
    metadata: MetaData


class ImageFilter(BaseModel):
    lower_height: int
    upper_height: int
    lower_width: int
    upper_width: int
