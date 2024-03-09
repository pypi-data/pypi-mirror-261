"""
Module flysystem.adapters
"""

from abc import ABCMeta, abstractmethod
from typing import BinaryIO


class TypeValidator(metaclass=ABCMeta):
    """
    TypeValidator interface
    """

    @abstractmethod
    def validate_file(self, path: str) -> bool:
        """
        Validate type of file.
        Arguments:
            path: The file path
        Returns:
            True if the file validated
        """

    @abstractmethod
    def validate_stream(self, resource: BinaryIO) -> bool:
        """
        Validate type of BinaryIO stream.
        Arguments:
            resource: The stream
        Returns:
            True if the stream validated
        """
