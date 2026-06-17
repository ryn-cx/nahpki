"""Tests for nahpki."""

import json

from nahpki import Nahpki

client = Nahpki()


class TestParse:
    """Tests parsing files."""

    def test_parse_video_episodes(self) -> None:
        """Test parsing video episodes files."""
        for json_file in client.video_episodes.json_files():
            file_content = json.loads(json_file.read_text())
            client.video_episodes.parse(file_content)

    def test_parse_program_episodes(self) -> None:
        """Test parsing program episodes files."""
        for json_file in client.program_episodes.json_files():
            file_content = json.loads(json_file.read_text())
            client.program_episodes.parse(file_content)

    def test_parse_video_program(self) -> None:
        """Test parsing video program files."""
        for json_file in client.video_program.json_files():
            file_content = json.loads(json_file.read_text())
            client.video_program.parse(file_content)

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

    def test_get_program_episodes(self) -> None:
        """Test getting a program's episodes."""
        client.program_episodes.get("dwc")

    def test_get_video_program(self) -> None:
        """Test getting a single video program."""
        client.video_program.get("japanologyplus")

    def test_get_shows_search(self) -> None:
        """Test searching for shows."""
        client.shows_search.get("japan")
