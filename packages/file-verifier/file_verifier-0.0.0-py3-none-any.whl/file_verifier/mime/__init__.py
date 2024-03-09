"""
Module flysystem.adapters
"""

from abc import ABCMeta, abstractmethod
from typing import BinaryIO


class MimeValidator(metaclass=ABCMeta):
    """
    MimeValidator interface
    """

    @abstractmethod
    def validate_file(self, path: str) -> bool:
        """
        Validate mime of file.
        Arguments:
            path: The file path
        Returns:
            True if the file validated
        """

    @abstractmethod
    def validate_stream(self, resource: BinaryIO) -> bool:
        """
        Validate mime of BinaryIO stream.
        Arguments:
            resource: The stream
        Returns:
            True if the stream validated
        """
