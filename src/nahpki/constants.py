"""Constants."""

from pathlib import Path

NAHPKI_PATH = Path(__file__).parent
FILES_PATH = NAHPKI_PATH / "_files"

# The page size used when fetching all results. This is the maximum the showsapi
# pagination endpoints accept per page.
MAX_PAGE_SIZE = 100
