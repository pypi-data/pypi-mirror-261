from abc import ABCMeta, abstractmethod
from typing import Any, BinaryIO, Dict, List


class Convertor(metaclass=ABCMeta):
    """
    Convertor interface
    """

    @abstractmethod
    def io2image(self, resource: BinaryIO) -> Any:
        """
        Convert io to image.
        Arguments:
            resource: The stream
        Returns:
            Image Data
        """

    @abstractmethod
    def bytes2image(self, contents: bytes, path: str) -> Any:
        """
        Convert bytes to image.
        Arguments:
            contents: The contents of file
            path: name of file
        Returns:
            Image Data
        """

    @abstractmethod
    def bytes2images(self, contents: bytes, options: Dict[str, Any] = None) -> List[Any]:
        """
        Convert bytes to list of images.
        Arguments:
            contents: The contents of file
            options: Convert bytes to images options
        Returns:
            List of Image Data
        """

    @abstractmethod
    def image2io(self, image: Any, options: Dict[str, Any] = None) -> BinaryIO:
        """
        Convert image to IO.
        Arguments:
            image: Image Data
            options: Convert image to io options
        Returns:
            io.BinaryIO
        """

    @abstractmethod
    def image2bytes(self, image: Any, options: Dict[str, Any] = None) -> bytes:
        """
        Convert image to bytes.
        Arguments:
            image: Image Data
            options: Convert image to io options
        Returns:
            bytes
        """
