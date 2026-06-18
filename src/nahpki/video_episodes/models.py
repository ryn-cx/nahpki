# ruff: noqa: D100, D101
from __future__ import annotations

from pydantic import AwareDatetime, BaseModel, ConfigDict


class Pagination(BaseModel):
    model_config = ConfigDict(extra="forbid")
    limit: int
    offset: int
    count: int
    total: int
    next: str | None
    previous: str | None


class VideoProgram(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    title: str
    html_title: str
    url: str
    uri: str


class BroadcastSchedule(BaseModel):
    model_config = ConfigDict(extra="forbid")
    start_at: AwareDatetime
    end_at: AwareDatetime


class Image(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class Video(BaseModel):
    model_config = ConfigDict(extra="forbid")
    vod_id: None
    url: str
    duration: int
    analytics: str
    published_at: AwareDatetime
    expired_at: AwareDatetime


class Category(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    url: str
    name: str
    uri: str


class Tag(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    url: str
    name: str
    uri: str


class Item(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    id: str
    lang: str
    caption_langs: list[str]
    voice_langs: list[str]
    video_program: VideoProgram
    url: str
    title: str | None
    html_title: str | None
    description: str
    html_description: str
    broadcast_schedules: list[BroadcastSchedule]
    first_broadcasted_at: AwareDatetime
    images: list[Image]
    video: Video
    categories: list[Category]
    tags: list[Tag]


class Params(BaseModel):
    model_config = ConfigDict(extra="forbid")
    limit: int
    offset: int


class Nahpki(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    timestamp: AwareDatetime
    params: Params


class VideoEpisodesModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    pagination: Pagination
    items: list[Item]
    nahpki: Nahpki
