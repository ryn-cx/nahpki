"""Tests for nahpki."""

import json
from datetime import UTC, datetime, timedelta

from nahpki import Nahpki
from nahpki.constants import MAX_PAGE_SIZE

client = Nahpki()


class TestParse:
    """Tests parsing files."""

    def test_parse_video_episodes(self) -> None:
        """Test parsing video episodes files."""
        for json_file in client.video_episodes.json_files():
            file_content = json.loads(json_file.read_text())
            client.video_episodes.parse(file_content)

    def test_parse_video_programs(self) -> None:
        """Test parsing video programs files."""
        for json_file in client.video_programs.json_files():
            file_content = json.loads(json_file.read_text())
            client.video_programs.parse(file_content)

    def test_parse_shows_search(self) -> None:
        """Test parsing shows search files."""
        for json_file in client.shows_search.json_files():
            file_content = json.loads(json_file.read_text())
            client.shows_search.parse(file_content)


class TestGet:
    """Tests getting data."""

    def test_get_video_episodes(self) -> None:
        """Test getting video episodes."""
        client.video_episodes.get(limit=20, offset=0)

    def test_get_video_episodes_for_program(self) -> None:
        """Test getting a single show's video episodes."""
        client.video_episodes.get("dwc")

    def test_get_video_programs(self) -> None:
        """Test getting a single video program."""
        client.video_programs.get("japanologyplus")

    def test_get_shows_search(self) -> None:
        """Test searching for shows."""
        client.shows_search.get("japan")


class TestGetAll:
    """Tests getting all pages of paginated endpoints."""

    def test_get_all_video_episodes_for_program(self) -> None:
        """Test getting every page of a single show's video episodes."""
        pages = client.video_episodes.get_all("dwc")
        assert pages
        items = sum(len(page.items) for page in pages)
        assert items == pages[0].pagination.total

    def test_get_all_shows_search(self) -> None:
        """Test getting every page of a shows search."""
        pages = client.shows_search.get_all("japan")
        assert len(pages) > 1
        hits = sum(len(page.hits.hits) for page in pages)
        assert hits == pages[0].hits.total.value

    def test_get_all_to_datetime(self) -> None:
        """Test get_all stops at an inclusive published_at cutoff."""
        cutoff = datetime.now(tz=UTC) - timedelta(days=5)
        pages = client.video_episodes.get_all(to_datetime=cutoff)
        assert pages
        items = [item for page in pages for item in page.items]
        # Scraped back to at least the cutoff.
        assert min(item.video.published_at for item in items) <= cutoff
        # Stopped early instead of fetching every page.
        total = pages[0].pagination.total
        full_pages = (total + MAX_PAGE_SIZE - 1) // MAX_PAGE_SIZE
        assert len(pages) < full_pages
