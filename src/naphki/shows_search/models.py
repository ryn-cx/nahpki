# ruff: noqa: D100, D101
from __future__ import annotations

from typing import Any

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class FieldShards(BaseModel):
    model_config = ConfigDict(extra="forbid")
    total: int
    successful: int
    skipped: int
    failed: int


class Total(BaseModel):
    model_config = ConfigDict(extra="forbid")
    value: int
    relation: str


class FieldSource(BaseModel):
    model_config = ConfigDict(extra="forbid")
    thumbnail: str
    description: str
    title: str
    url: str
    slug: str


class Hit(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_index: str = Field(..., alias="_index")
    field_id: str = Field(..., alias="_id")
    field_score: float = Field(..., alias="_score")
    field_source: FieldSource = Field(..., alias="_source")


class Hits(BaseModel):
    model_config = ConfigDict(extra="forbid")
    total: Total
    max_score: float
    hits: list[Hit]


class MultiMatch(BaseModel):
    model_config = ConfigDict(extra="forbid")
    query: str
    type: str
    fields: list[str]
    operator: str


class ShouldItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    multi_match: MultiMatch


class Bool(BaseModel):
    model_config = ConfigDict(extra="forbid")
    should: list[ShouldItem]


class Query(BaseModel):
    model_config = ConfigDict(extra="forbid")
    bool: Bool


class Body(BaseModel):
    model_config = ConfigDict(extra="forbid")
    query: Query
    from_: int = Field(..., alias="from")
    size: int
    field_source: list[str] = Field(..., alias="_source")


class Naphki(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    timestamp: AwareDatetime
    params: dict[str, Any]
    body: Body


class ShowsSearchModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    took: int
    timed_out: bool
    field_shards: FieldShards = Field(..., alias="_shards")
    hits: Hits
    naphki: Naphki
