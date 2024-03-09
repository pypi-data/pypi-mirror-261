"""Module providing the MusicManager class"""
import os
import logging
from sqlite3 import Cursor
from pathlib import Path
from ._file import File as F
from ._database import DB


class MusicManager():
    """Class to manage finding media files within a directory"""
    app_name = 'MusicManagerMicro'

    # Directory and files
    root_config_dir: str = os.path.join(
        str(Path.home()), ".config/", app_name)
    root_cache_dir: str = os.path.join(
        str(Path.home()), ".cache/", app_name)
    library_cache_file = 'library.db'
    active_library_config_dir: str
    active_library_cache_dir: str

    db: DB
    db_cursor: Cursor

    extensions: tuple

    library: str
    media_path: str

    logging.basicConfig(
        format='%(asctime)s | %(levelname)s | %(message)s', level=logging.DEBUG)
    DEBUG: bool = False
    INFO: bool = False

    def _debug(self, message):
        if self.DEBUG:
            logging.debug(str(message))

    def _info(self, message):
        if self.INFO:
            logging.info(str(message))

    def __init__(self,
                 library: str = 'library',
                 media_dir: str = '.',
                 cache_dir: str = None,
                 extensions: tuple = None):
        """
        Set up a new MusicManager, will generate cache directories

        :param library: Useful name to give the library, will be used to
        generate a folder to store results
        :param media_dir: Root directory to start the file search from,
        can be relative or absolute, must have read access
        :param cache_dir: Optional to override where to store results,
        defaults to XDG cache directory
        :param extensions: Tuple containing file extensions to search for
        """
        self.db = DB()
        if cache_dir:
            self.root_cache_dir = cache_dir
        if extensions:
            self.extensions = extensions
        else:
            self.extensions = ('.mp3', '.flac')
        self.set_library(library)
        self.set_root_dir(media_dir)

    def set_library(self, library: str) -> None:
        """
        Used to set which library dataset we are using. Will create
        a sqlite db to store results in cache directory

        :param library: Useful name to give the library, will be used to
        generate a folder to store results
        :returns None:
        """
        self.library = library
        self._update_root_dir()

    def set_root_dir(self, media_dir: str) -> None:
        """
        Used to set the path to search for supported media files. 
        Can be relative or absolute, as long as the provided string 
        resolves to a directory

        :param media_dir: Root directory to start the file search from,
        can be relative or absolute, must have read access
        :returns None:
        """
        self.media_path = media_dir

    def _update_root_dir(self) -> None:
        self.active_library_config_dir = self._generate_library_dir()
        os.makedirs(self.active_library_config_dir, exist_ok=True)

    def _generate_library_dir(self) -> str:
        return os.path.join(
            self.root_cache_dir, self.library)

    ###
    # Utils
    ###

    def _get_files_from_folder(self, folder: str) -> list:
        """Returns the list of all files recursively in a directory"""
        ret_val = []
        for r, _, f in os.walk(folder):
            for file in f:
                if file.endswith(self.extensions):
                    ret_val.append(f'{r}/{file}')
        return ret_val

    ###
    # Program Functions
    ###

    library_list = []

    def _build_entry(self, file_path: str) -> tuple | None:
        try:
            file = F(file_path, '', '', os.path.getmtime(file_path))
            return (file.mtime, file.path)
        except FileNotFoundError as err:
            self._debug(f"Error in build_entry {err=}, {type(err)=}")
            return None

    def _build_list(self, root_path: str) -> list:
        """Given a path string constructs a list of File objects"""
        self.library_list = []
        files = self._get_files_from_folder(root_path)
        self._debug(f"Found {len(files)} files")
        for f in files:
            self._debug(f)
            self.library_list.append(self._build_entry(f))
        return self.library_list

    def execute(self) -> list[tuple[float, str]]:
        """
        Use to fully walk the directory and find all compatible
        media files. Will store the results in the standard
        cache directory.

        :returns: List of tuples representing the float mtime
        of the media file and path
        """
        self._build_list(self.media_path)
        self._save_list()
        return self.get_list()

    def reset_library(self) -> None:
        """
        Clears the cached results

        :returns None:
        """
        _file = self.__build_file_path()
        self.db.instantiate_sqlite_table(_file)
        self.db.db_delete()
        self.db.db_commit()
        self.db.db_close()

    def get_list(self) -> list[tuple[float, str]]:
        """
        Returns the list for the given library without running 
        the search

        :returns: List of tuples representing the float mtime
        of the media file and path
        """
        self._load_list()
        self._info(f"Found {len(self.library_list)} files")
        return self.library_list

    def __build_file_path(self) -> str:
        return os.path.join(self.active_library_config_dir, self.library_cache_file)

    def _load_list(self) -> None:
        _file = self.__build_file_path()
        self.db.instantiate_sqlite_table(_file)
        self.library_list = self.db.db_get_all()

    def _save_list(self) -> None:
        """Uses a filepath + filename string and content string overwrites the resulting file"""
        content = self.library_list
        write_file = self.__build_file_path()
        if os.path.dirname(write_file) != '':
            os.makedirs(os.path.dirname(write_file), exist_ok=True)
        self.db.instantiate_sqlite_table(write_file)
        for x in content:
            self._debug(f'Inserting {x}')
            self.db.db_insert(x)
        self.db.db_commit()
        self.db.db_close()
