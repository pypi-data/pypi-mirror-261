"""
Module flysystem
"""

from typing import Any, BinaryIO, Dict, List

from file_verifier.convertor import Convertor
from file_verifier.mime import MimeValidator
from file_verifier.size import SizeValidator
from file_verifier.type import TypeValidator


class FileValidator(object):
    """
    Filesystem
    """

    def __init__(
        self,
        mime_validator: MimeValidator,
        size_validator: SizeValidator,
        type_validator: TypeValidator,
        file_convertor: Convertor,
    ):
        self.mime_validator = mime_validator
        self.size_validator = size_validator
        self.type_validator = type_validator
        self.file_convertor = file_convertor

    def validate_file(self, path: str) -> bool:
        self.mime_validator.validate_file(path)
        self.size_validator.validate_file(path)
        self.type_validator.validate_file(path)

        return True

    def validate_stream(self, resource: BinaryIO) -> bool:
        self.mime_validator.validate_stream(resource)
        self.size_validator.validate_stream(resource)
        self.type_validator.validate_stream(resource)

        return True

    async def validate_file_async(self, path: str) -> bool:
        await self.mime_validator.validate_file(path)
        await self.size_validator.validate_file(path)
        await self.type_validator.validate_file(path)

        return True

    async def validate_stream_async(self, resource: BinaryIO) -> bool:
        await self.mime_validator.validate_stream(resource)
        await self.size_validator.validate_stream(resource)
        await self.type_validator.validate_stream(resource)

        return True

    def io2image(self, resource: BinaryIO) -> Any:
        return self.file_convertor.io2image(resource)

    def bytes2image(self, contents: bytes, path: str) -> Any:
        return self.file_convertor.bytes2image(contents, path)

    def bytes2images(self, contents: bytes, options: Dict[str, Any] = None) -> List[Any]:
        return self.file_convertor.bytes2images(contents, options)

    def image2io(self, image: Any, options: Dict[str, Any] = None) -> BinaryIO:
        return self.file_convertor.image2io(image, options)

    def image2bytes(self, image: Any, options: Dict[str, Any] = None) -> bytes:
        return self.file_convertor.image2bytes(image, options)
