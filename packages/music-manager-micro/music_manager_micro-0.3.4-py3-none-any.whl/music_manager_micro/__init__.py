"""
Build a list of media files from a root directory, store the results in a cache
db for fast retrieval
"""

from .music_manager import MusicManager

VERSION = (0, 3, 4)

VERSION_STRING = ".".join(map(str, VERSION))

MusicManager
