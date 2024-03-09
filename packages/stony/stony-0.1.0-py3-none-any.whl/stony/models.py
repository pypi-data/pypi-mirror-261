from re import sub
from typing import Any, Optional
from typing import Union, Literal
from pydantic import BaseModel, ConfigDict, Field


class UrlGeneratorMixin:
    def url(self):
        formatted_title = "-".join(
            sub(
                r"(\s|_|-)+",
                " ",
                sub(
                    r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
                    lambda mo: " " + mo.group(0).lower(),
                    self.title,
                ),
            ).split()
        )
        path = "/" + formatted_title + ".html"
        return path


class NotionPage(UrlGeneratorMixin, BaseModel):
    model_config = ConfigDict(extra="ignore")

    object: str
    id: str
    created_time: str
    last_edited_time: str
    properties: dict[str, Any]

    @property
    def title(self):
        if "title" in self.properties:
            return self.properties["title"]["title"][0]["plain_text"]


class NotionBlock(UrlGeneratorMixin, BaseModel):
    object: str
    id: str
    created_time: str
    last_edited_time: str
    has_children: bool
    archived: bool


class ChildPageBlockDetails(BaseModel):
    title: str


class NotionChildPageBlock(NotionBlock):
    type: Literal["child_page"]
    child_page: ChildPageBlockDetails

    @property
    def title(self):
        return self.child_page.title


class NotionRichTextDetails(BaseModel):
    content: str
    link: Optional[str]


class NotionRichTextAnnotations(BaseModel):
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    code: bool
    color: str


class NotionRichText(BaseModel):
    type: str
    text: NotionRichTextDetails
    annotations: NotionRichTextAnnotations
    plain_text: str
    href: Optional[str]


class NotionParagraphDetails(BaseModel):
    rich_text: list[NotionRichText]
    color: str


class NotionHeadingDetails(BaseModel):
    rich_text: list[NotionRichText]
    color: str
    is_toggleable: bool


class NotionQuoteDetails(BaseModel):
    rich_text: list[NotionRichText]
    color: str


class NotionParagraphBlock(NotionBlock):
    type: Literal["paragraph"]
    paragraph: NotionParagraphDetails


class NotionHeading1Block(NotionBlock):
    type: Literal["heading_1"]
    heading_1: NotionHeadingDetails


class NotionHeading2Block(NotionBlock):
    type: Literal["heading_2"]
    heading_2: NotionHeadingDetails


class NotionHeading3Block(NotionBlock):
    type: Literal["heading_3"]
    heading_3: NotionHeadingDetails


class NotionDividerBlock(NotionBlock):
    type: Literal["divider"]


class NotionQuoteBlock(NotionBlock):
    type: Literal["quote"]
    quote: NotionQuoteDetails


class NotionContentBlock(BaseModel):
    content: Union[
        NotionQuoteBlock,
        NotionParagraphBlock,
        NotionHeading3Block,
        NotionHeading2Block,
        NotionHeading1Block,
        NotionDividerBlock,
        NotionChildPageBlock,
    ] = Field(..., discriminator="type")

    @property
    def id(self):
        return self.content.id

    @property
    def type(self):
        return self.content.type


class RootPage(BaseModel):
    page: NotionPage
    children: list[NotionContentBlock]

    def pages(self):
        return [c.content for c in self.children if c.content.type == "child_page"]
