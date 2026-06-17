"""Video program API endpoint."""

from __future__ import annotations

from typing import Any

from nahpki.base_api_endpoint import BaseEndpoint
from nahpki.video_program.models import VideoProgramModel


class VideoProgram(BaseEndpoint[VideoProgramModel]):
    """Provides methods to download, parse, and retrieve a single video program."""

    _response_model = VideoProgramModel

    def download(self, program_id: str, language: str = "") -> dict[str, Any]:
        """Downloads a single video program (show).

        Args:
            program_id: The program (show) ID, e.g. ``"japanologyplus"`` for the show
                at https://www3.nhk.or.jp/nhkworld/en/shows/japanologyplus/.
            language: The language code to use for the request.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        language = language or self._client.language
        endpoint = f"showsapi/v1/{language}/video_programs/{program_id}"
        return self._client.download(endpoint, {})

    def get(self, program_id: str, language: str = "") -> VideoProgramModel:
        """Downloads and parses a single video program (show).

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            program_id: The program (show) ID, e.g. ``"japanologyplus"`` for the show
                at https://www3.nhk.or.jp/nhkworld/en/shows/japanologyplus/.
            language: The language code to use for the request.

        Returns:
            A VideoProgramModel containing the parsed data.
        """
        response = self.download(program_id, language)
        return self.parse(response)
