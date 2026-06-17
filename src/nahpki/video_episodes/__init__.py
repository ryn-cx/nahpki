"""Video episodes API endpoint."""

from __future__ import annotations

from typing import Any

from nahpki.base_api_endpoint import BaseEndpoint
from nahpki.video_episodes.models import VideoEpisodesModel


class VideoEpisodes(BaseEndpoint[VideoEpisodesModel]):
    """Provides methods to download, parse, and retrieve video episode data."""

    _response_model = VideoEpisodesModel

    def download(
        self,
        limit: int = 20,
        offset: int = 0,
        language: str = "",
    ) -> dict[str, Any]:
        """Downloads a page of video episodes.

        Args:
            limit: The maximum number of episodes to return.
            offset: The number of episodes to skip.
            language: The language code to use for the request.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        language = language or self._client.language
        endpoint = f"showsapi/v1/{language}/video_episodes"
        params: dict[str, str | int] = {
            "limit": limit,
            "offset": offset,
        }
        return self._client.download(endpoint, params)

    def get(
        self,
        limit: int = 20,
        offset: int = 0,
        language: str = "",
    ) -> VideoEpisodesModel:
        """Downloads and parses a page of video episodes.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            limit: The maximum number of episodes to return.
            offset: The number of episodes to skip.
            language: The language code to use for the request.

        Returns:
            A VideoEpisodesModel containing the parsed data.
        """
        response = self.download(limit, offset, language)
        return self.parse(response)
