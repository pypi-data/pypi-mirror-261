"""
Module flysystem.adapters
"""

from abc import ABCMeta, abstractmethod
from typing import BinaryIO


class SizeValidator(metaclass=ABCMeta):
    """
    SizeValidator interface
    """

    @abstractmethod
    def validate_file(self, path: str) -> bool:
        """
        Validate size of file.
        Arguments:
            path: The file path
        Returns:
            True if the file validated
        """

    @abstractmethod
    def validate_stream(self, resource: BinaryIO) -> bool:
        """
        Validate size of BinaryIO stream.
        Arguments:
            resource: The stream
        Returns:
            True if the stream validated
        """
