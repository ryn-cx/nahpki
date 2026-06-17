"""Nahpki is a client for downloading and parsing data from NHK World."""

from datetime import datetime
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from nahpki.exceptions import HTTPError
from nahpki.program_episodes import ProgramEpisodes
from nahpki.shows_search import ShowsSearch
from nahpki.video_episodes import VideoEpisodes
from nahpki.video_program import VideoProgram

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Nahpki:
    """Interface for downloading and parsing data from NHK World."""

    API_DOMAIN = "api.nhkworld.jp"
    BASE_API_URL = f"https://{API_DOMAIN}"

    def __init__(
        self,
        language: str = "en",
        timeout: int = 30,
        get_around_server: str | None = None,
        get_around_password: str | None = None,
    ) -> None:
        """Initialize the Nahpki client."""
        self.language = language
        self.timeout = timeout

        self.get_around_client = GetAround(
            server=get_around_server,
            password=get_around_password,
        )

        self.video_episodes = VideoEpisodes(self)
        self.program_episodes = ProgramEpisodes(self)
        self.video_program = VideoProgram(self)
        self.shows_search = ShowsSearch(self)

        super().__init__()

    def download(
        self,
        endpoint: str,
        params: dict[str, Any],
        base_url: str | None = None,
        *,
        json_body: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Downloads data from the API for a given endpoint.

        Sends a GET request, or a POST request when ``json_body`` is provided.
        """
        url = f"{base_url or self.BASE_API_URL}/{endpoint}"

        if json_body is not None:
            logger.info("Downloading API data (POST): %s body=%s", url, json_body)
            response = self.get_around_client.post(
                url=url,
                json=json_body,
                timeout=self.timeout,
            )
        else:
            logger.info("Downloading API data: %s params=%s", url, params)
            response = self.get_around_client.get(
                url=url,
                params=params,
                timeout=self.timeout,
            )

        # PLR2004 - 200 represents the status code "200 OK".
        if response.status_code != 200:  # noqa: PLR2004
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)

        output = response.json()
        output["nahpki"] = {}
        output["nahpki"]["url"] = url
        output["nahpki"]["timestamp"] = datetime.now().astimezone().isoformat()
        output["nahpki"]["params"] = params
        if json_body is not None:
            output["nahpki"]["body"] = json_body

        return output
