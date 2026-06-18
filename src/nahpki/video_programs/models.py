# ruff: noqa: D100, D101
from __future__ import annotations

from typing import Any

from pydantic import AwareDatetime, BaseModel, ConfigDict


class LandscapeItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class PortraitItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class Images(BaseModel):
    model_config = ConfigDict(extra="forbid")
    landscape: list[LandscapeItem]
    portrait: list[PortraitItem]


class Image(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int
    height: int


class Logo(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    width: int


class Sp(BaseModel):
    model_config = ConfigDict(extra="forbid")
    images: list[Image]
    logo: Logo


class Pc(BaseModel):
    model_config = ConfigDict(extra="forbid")
    images: list[Image]
    logo: Logo


class Hero(BaseModel):
    model_config = ConfigDict(extra="forbid")
    sp: Sp
    pc: Pc


class Category(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    url: str
    name: str
    uri: str


class VideoEpisodes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    total: int
    uri: str


class VideoClips(BaseModel):
    model_config = ConfigDict(extra="forbid")
    total: int
    uri: str


class Casts(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: None
    total: int
    uri: str


class Nahpki(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    timestamp: AwareDatetime
    params: dict[str, Any]


class VideoProgramsModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    id: str
    lang: str
    langs: list[str]
    url: str
    external_url: None
    title: str
    html_title: str
    description: str
    html_description: str
    series_id: str
    sort_key: str
    is_new: bool
    is_closed: bool
    episode_sort: str
    sns_image: str
    images: Images
    hero: Hero
    banners: list[None]
    categories: list[Category]
    tags: list[None]
    video_episodes: VideoEpisodes
    video_clips: VideoClips
    casts: Casts
    nahpki: Nahpki
