"""Shows search API endpoint."""

from __future__ import annotations

from typing import Any

from nahpki.base_api_endpoint import BaseEndpoint
from nahpki.shows_search.models import ShowsSearchModel


class ShowsSearch(BaseEndpoint[ShowsSearchModel]):
    """Provides methods to search for shows (video programs)."""

    _response_model = ShowsSearchModel

    def download(self, query: str) -> dict[str, Any]:
        """Searches for shows (video programs) matching a search term.

        Args:
            query: The search term, e.g. ``"japan"``.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        index = f"nhkworld@{self._client.language}@ondemand@vod@programs"
        endpoint = f"nwapi/showssearch/v1/{index}/list.json"
        body: dict[str, Any] = {
            "query": {
                "bool": {
                    "should": [
                        {
                            "multi_match": {
                                "query": query,
                                "type": "cross_fields",
                                "fields": ["title^16", "description^1"],
                                "operator": "and",
                            },
                        },
                        {
                            "multi_match": {
                                "query": query,
                                "type": "cross_fields",
                                "fields": ["body^1"],
                                "operator": "and",
                            },
                        },
                    ],
                },
            },
            "from": 0,
            "size": 40,
            "_source": ["title", "description", "slug", "url", "thumbnail"],
        }
        return self._client.download(endpoint, {}, json_body=body)

    def get(self, query: str) -> ShowsSearchModel:
        """Searches for shows and parses the result.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            query: The search term, e.g. ``"japan"``.

        Returns:
            A ShowsSearchModel containing the parsed search results.
        """
        response = self.download(query)
        return self.parse(response)
