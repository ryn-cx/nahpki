"""Video episodes API endpoint."""

from __future__ import annotations

from typing import Any

from nahpki.base_api_endpoint import BaseEndpoint
from nahpki.constants import MAX_PAGE_SIZE
from nahpki.video_episodes.models import VideoEpisodesModel


class VideoEpisodes(BaseEndpoint[VideoEpisodesModel]):
    """Provides methods to download, parse, and retrieve video episode data.

    With no ``program_id`` this covers every video episode
    (``GET /video_episodes``). With a ``program_id`` it covers the episodes of a
    single show (``GET /video_programs/{program_id}/video_episodes``).
    """

    _response_model = VideoEpisodesModel

    def download(
        self,
        program_id: str | None = None,
        *,
        limit: int = 20,
        offset: int = 0,
        language: str = "",
    ) -> dict[str, Any]:
        """Downloads a page of video episodes.

        Args:
            program_id: A program (show) ID to limit results to a single show, e.g.
                ``"dwc"``. When omitted, every video episode is returned.
            limit: The maximum number of episodes to return.
            offset: The number of episodes to skip.
            language: The language code to use for the request.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        language = language or self._client.language
        if program_id is None:
            endpoint = f"showsapi/v1/{language}/video_episodes"
        else:
            endpoint = (
                f"showsapi/v1/{language}/video_programs/{program_id}/video_episodes"
            )
        params: dict[str, str | int] = {"limit": limit, "offset": offset}
        return self._client.download(endpoint, params)

    def get(
        self,
        program_id: str | None = None,
        *,
        limit: int = 20,
        offset: int = 0,
        language: str = "",
    ) -> VideoEpisodesModel:
        """Downloads and parses a page of video episodes.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            program_id: A program (show) ID to limit results to a single show, e.g.
                ``"dwc"``. When omitted, every video episode is returned.
            limit: The maximum number of episodes to return.
            offset: The number of episodes to skip.
            language: The language code to use for the request.

        Returns:
            A VideoEpisodesModel containing the parsed data.
        """
        response = self.download(
            program_id,
            limit=limit,
            offset=offset,
            language=language,
        )
        return self.parse(response)

    def get_all(
        self,
        program_id: str | None = None,
        *,
        language: str = "",
    ) -> list[VideoEpisodesModel]:
        """Downloads and parses every page of video episodes.

        Repeatedly calls ``get()`` with the maximum page size, advancing through
        the pagination until all episodes have been retrieved.

        Args:
            program_id: A program (show) ID to limit results to a single show, e.g.
                ``"dwc"``. When omitted, every video episode is returned.
            language: The language code to use for the request.

        Returns:
            A list of VideoEpisodesModel, one per page.
        """
        pages: list[VideoEpisodesModel] = []
        offset = 0
        while True:
            page = self.get(
                program_id,
                limit=MAX_PAGE_SIZE,
                offset=offset,
                language=language,
            )
            pages.append(page)
            offset += page.pagination.count
            if page.pagination.next is None or page.pagination.count == 0:
                break
        return pages
