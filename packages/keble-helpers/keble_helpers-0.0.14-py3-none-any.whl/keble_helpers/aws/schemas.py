from typing import List, Optional
from pydantic import BaseModel
from enum import Enum


class TextractBlockType(str, Enum):
    KEY_VALUE_SET = 'KEY_VALUE_SET'
    PAGE = 'PAGE'
    LINE = 'LINE'
    WORD = 'WORD'
    TABLE = 'TABLE'
    CELL = 'CELL'
    SELECTION_ELEMENT = 'SELECTION_ELEMENT'
    MERGED_CELL = 'MERGED_CELL'
    TITLE = 'TITLE'
    QUERY = 'QUERY'
    QUERY_RESULT = 'QUERY_RESULT'
    SIGNATURE = 'SIGNATURE'
    TABLE_TITLE = 'TABLE_TITLE'
    TABLE_FOOTER = 'TABLE_FOOTER'
    LAYOUT_TEXT = 'LAYOUT_TEXT'
    LAYOUT_TITLE = 'LAYOUT_TITLE'
    LAYOUT_HEADER = 'LAYOUT_HEADER'
    LAYOUT_FOOTER = 'LAYOUT_FOOTER'
    LAYOUT_SECTION_HEADER = 'LAYOUT_SECTION_HEADER'
    LAYOUT_PAGE_NUMBER = 'LAYOUT_PAGE_NUMBER'
    LAYOUT_LIST = 'LAYOUT_LIST'
    LAYOUT_FIGURE = 'LAYOUT_FIGURE'
    LAYOUT_TABLE = 'LAYOUT_TABLE'
    LAYOUT_KEY_VALUE = 'LAYOUT_KEY_VALUE'


class TextractTextTypeEnum(str, Enum):
    HANDWRITING = 'HANDWRITING'
    PRINTED = 'PRINTED'


class TextractRelationshipType(str, Enum):
    VALUE = 'VALUE'
    CHILD = 'CHILD'
    COMPLEX_FEATURES = 'COMPLEX_FEATURES'
    MERGED_CELL = 'MERGED_CELL'
    TITLE = 'TITLE'
    ANSWER = 'ANSWER'
    TABLE = 'TABLE'
    TABLE_TITLE = 'TABLE_TITLE'
    TABLE_FOOTER = 'TABLE_FOOTER'


class TextractEntityTypes(str, Enum):
    KEY = 'KEY'
    VALUE = 'VALUE'
    COLUMN_HEADER = 'COLUMN_HEADER'
    TABLE_TITLE = 'TABLE_TITLE'
    TABLE_FOOTER = 'TABLE_FOOTER'
    TABLE_SECTION_TITLE = 'TABLE_SECTION_TITLE'
    TABLE_SUMMARY = 'TABLE_SUMMARY'
    STRUCTURED_TABLE = 'STRUCTURED_TABLE'
    SEMI_STRUCTURED_TABLE = 'SEMI_STRUCTURED_TABLE'


class TextractSelectionStatus(str, Enum):
    SELECTED = 'SELECTED'
    NOT_SELECTED = 'NOT_SELECTED'


class TextractBoundingBox(BaseModel):
    Width: Optional[float]
    Height: Optional[float]
    Left: Optional[float]
    Top: Optional[float]


class TextractPolygon(BaseModel):
    X: Optional[float]
    Y: Optional[float]


class TextractGeometry(BaseModel):
    BoundingBox: Optional[TextractBoundingBox]
    Polygon: Optional[List[TextractPolygon]]


class TextractRelationship(BaseModel):
    Type: Optional[TextractRelationshipType]
    Ids: Optional[List[str]]


class TextractQuery(BaseModel):
    Text: Optional[str]
    Alias: Optional[str]
    Pages: Optional[List[str]]


class TextractBlock(BaseModel):
    BlockType: Optional[TextractBlockType]
    Confidence: Optional[float]
    Text: Optional[str]
    TextType: Optional[TextractTextTypeEnum]
    RowIndex: Optional[int]
    ColumnIndex: Optional[int]
    RowSpan: Optional[int]
    ColumnSpan: Optional[int]
    Geometry: Optional[TextractGeometry]
    Id: Optional[str]
    Relationships: Optional[List[TextractRelationship]]
    EntityTypes: Optional[List[TextractEntityTypes]]
    SelectionStatus: Optional[TextractSelectionStatus]
    Page: Optional[int]
    Query: Optional[TextractQuery]


class TextractDocumentMetadata(BaseModel):
    Pages: Optional[int]


class TextractResponse(BaseModel):
    DocumentMetadata: Optional[TextractDocumentMetadata]
    Blocks: Optional[List[TextractBlock]]
    DetectDocumentTextModelVersion: Optional[str]
