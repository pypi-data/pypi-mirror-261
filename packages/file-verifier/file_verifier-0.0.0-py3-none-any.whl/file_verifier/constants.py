"""In this module, the constants used at the library level are defined."""

MESSAGE_FOR_MIME_VALIDATION: str = "acceptable mimes: {acceptable_mimes}, \n" "file mime: {file_mime}\n"
MESSAGE_FOR_TYPE_VALIDATION: str = "acceptable types: {acceptable_types}, \n" "file type: {file_type}\n"
MESSAGE_FOR_EXTENSION_VALIDATION: str = (
    "acceptable extensions: {acceptable_extensions}, \n" "file extension: {file_extension}\n"
)

MESSAGE_FOR_FILE_SIZE_VALIDATION: str = (
    "{file_size} is not valid size for this file, \n" "you can upload files up to {max_file_size}."
)

SIZE_IS_EMPTY: str = "The size of file is empty"
IMAGE_IS_EMPTY: str = "The content of image is empty"

FONT: str = "font"
AUDIO: str = "audio"
VIDEO: str = "video"
IMAGE: str = "image"
ARCHIVE: str = "archive"
