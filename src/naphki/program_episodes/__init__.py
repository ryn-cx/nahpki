"""Program episodes API endpoint."""

from __future__ import annotations

from typing import Any

from naphki.base_api_endpoint import BaseEndpoint
from naphki.program_episodes.models import ProgramEpisodesModel


class ProgramEpisodes(BaseEndpoint[ProgramEpisodesModel]):
    """Provides methods to download, parse, and retrieve a program's episodes."""

    _response_model = ProgramEpisodesModel

    def download(
        self,
        program_id: str,
        *,
        schedule: bool = True,
        sort: str = "-date",
        offset: int = 0,
        language: str = "",
    ) -> dict[str, Any]:
        """Downloads the episodes for a single video program.

        Args:
            program_id: The program (show) ID
            schedule: Whether to include broadcast schedule data.
            sort: The sort order, e.g. ``"-date"`` for newest first.
            offset: The number of episodes to skip.
            language: The language code to use for the request.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        language = language or self._client.language
        endpoint = f"showsapi/v1/{language}/video_programs/{program_id}/video_episodes"
        params: dict[str, str | int | bool] = {
            "schedule": schedule,
            "sort": sort,
            "offset": offset,
        }
        return self._client.download(endpoint, params)

    def get(
        self,
        program_id: str,
        *,
        schedule: bool = True,
        sort: str = "-date",
        offset: int = 0,
        language: str = "",
    ) -> ProgramEpisodesModel:
        """Downloads and parses the episodes for a single video program.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            program_id: The program (show) ID
            schedule: Whether to include broadcast schedule data.
            sort: The sort order, e.g. ``"-date"`` for newest first.
            offset: The number of episodes to skip.
            language: The language code to use for the request.

        Returns:
            A ProgramEpisodesModel containing the parsed data.
        """
        response = self.download(
            program_id,
            schedule=schedule,
            sort=sort,
            offset=offset,
            language=language,
        )
        return self.parse(response)

    def get_all(
        self,
        program_id: str,
        *,
        schedule: bool = True,
        sort: str = "-date",
        language: str = "",
    ) -> list[ProgramEpisodesModel]:
        """Downloads and parses every page of a program's episodes.

        Repeatedly calls ``get()``, advancing through the pagination until all
        episodes have been retrieved.

        Args:
            program_id: The program (show) ID
            schedule: Whether to include broadcast schedule data.
            sort: The sort order, e.g. ``"-date"`` for newest first.
            language: The language code to use for the request.

        Returns:
            A list of ProgramEpisodesModel, one per page.
        """
        pages: list[ProgramEpisodesModel] = []
        offset = 0
        while True:
            page = self.get(
                program_id,
                schedule=schedule,
                sort=sort,
                offset=offset,
                language=language,
            )
            pages.append(page)
            offset += page.pagination.count
            if page.pagination.next is None or page.pagination.count == 0:
                break
        return pages
