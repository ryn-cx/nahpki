# ruff: noqa: D100, D101
from __future__ import annotations

from pydantic import AwareDatetime, BaseModel, ConfigDict


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


class Image1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int
    caption: str
    html_caption: str


class Content(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: None
    html_title: None
    image: Image1
    body: None
    html_body: None


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


class RelatedVideos(BaseModel):
    model_config = ConfigDict(extra="forbid")
    total: int
    uri: str


class Params(BaseModel):
    model_config = ConfigDict(extra="forbid")
    schedule: bool


class Nahpki(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    timestamp: AwareDatetime
    params: Params


class VideoEpisodeModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    id: str
    lang: str
    caption_langs: list[None]
    voice_langs: list[str]
    video_program: VideoProgram
    url: str
    title: str | None
    html_title: str | None
    description: str
    html_description: str
    broadcast_schedules: list[BroadcastSchedule]
    first_broadcasted_at: AwareDatetime
    sns_image: str
    images: list[Image]
    video: Video
    contents: list[Content]
    categories: list[Category]
    tags: list[Tag]
    related_videos: RelatedVideos
    nahpki: Nahpki
