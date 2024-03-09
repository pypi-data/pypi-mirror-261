"""
Module flysystem
"""

from typing import final

from typing_extensions import Self


class FileValidatorException(Exception):
    """
    Base exception class for FileValidatorException package
    """


class UnableToCheckToFile(FileValidatorException):
    """
    Unable to check to file exception
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self._location = ""
        self._reason = ""

    @final
    def location(self) -> str:
        return self._location

    @final
    def reason(self) -> str:
        return self._reason


@final
class TypeNotSupported(UnableToCheckToFile):
    @classmethod
    def with_location(cls, location: str, reason: str = "") -> Self:
        msg = f"Not supported type of file from location: {location}. {reason}".rstrip()
        this = cls(msg)
        this._location = location
        this._reason = reason
        return this


@final
class MimeNotSupported(UnableToCheckToFile):
    @classmethod
    def with_location(cls, location: str, reason: str = "") -> Self:
        msg = f"Not supported mime of file from location: {location}. {reason}".rstrip()
        this = cls(msg)
        this._location = location
        this._reason = reason
        return this


@final
class SizeNotSupported(UnableToCheckToFile):
    @classmethod
    def with_location(cls, location: str, reason: str = "") -> Self:
        msg = f"Not supported size of file from location: {location}. {reason}".rstrip()
        this = cls(msg)
        this._location = location
        this._reason = reason
        return this


@final
class UnableToDecodeFile(UnableToCheckToFile):
    @classmethod
    def with_location(cls, location: str, reason: str = "") -> Self:
        msg = f"Unable to decode file from location: {location}. {reason}".rstrip()
        this = cls(msg)
        this._location = location
        this._reason = reason
        return this
