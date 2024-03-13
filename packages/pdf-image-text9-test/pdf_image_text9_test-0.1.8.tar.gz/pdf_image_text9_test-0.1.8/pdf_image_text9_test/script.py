import os
import fitz
import base64
import filetype
from typing import List
from .processor import Processor
from .schema import ImageFilter, Page


class PdfToText:

    def __init__(self, open_ai_key=None,  model=None):
        self.open_ai_key = open_ai_key or os.environ.get("OPEN_AI_KEY")
        self.open_ai_vision_model = model or os.environ.get("OPEN_AI_MODEL") or "gpt-4-vision-preview"
        self.pdf_content = None
        self.processor = Processor(self.open_ai_key, self.open_ai_vision_model)

    def load_data(self, file_name: str | None = None, file_bytes_object: bytes | None = None) -> None:
        """
        Load pdf data
        :param file_name:
        :param file_bytes_object:
        """
        if file_name:
            file_type = os.path.splitext(file_name)
            if not filetype.is_document(file_name) and not file_type[1] == '.pdf':
                raise Exception('Only pdf format files are supported')
            self.pdf_content = fitz.open(file_name)
        elif file_bytes_object:
            if not filetype.guess_extension(file_bytes_object) == 'pdf':
                raise Exception('Only pdf format files are supported')
            self.pdf_content = fitz.open(stream=file_bytes_object, filetype="pdf")
        else:
            raise Exception("Please provide pdf file or object")

    def get_pdf_content(self, image_filter: ImageFilter, page_index: int | None = None,
                        include_formatted_data: bool = False) -> Page | List[Page]:
        """
        Get pdf content
        :param image_filter:
        :param page_index:
        :param include_formatted_data:
        :return:
        """
        if not self.pdf_content:
            raise Exception("Data not loaded. Please run load_data method")

        output = self.processor.get_pdf_text(pdf_content=self.pdf_content,
                                             page_index=page_index,
                                             image_filter=image_filter,
                                             include_formatted_data=include_formatted_data)
        return output


class ImageToText:

    def __init__(self, open_ai_key=None, model=None):
        self.open_ai_key = open_ai_key or os.environ.get("OPEN_AI_KEY")
        self.open_ai_vision_model = model or os.environ.get("OPEN_AI_MODEL") or "gpt-4-vision-preview"
        self.image_b64_content = None
        self.processor = Processor(self.open_ai_key, self.open_ai_vision_model)

    def load_data(self, file_name: str | None = None, b64_content: str | None = None) -> None:
        """
        Load image data
        :param file_name:
        :param b64_content: 
        """
        if file_name:
            if not filetype.is_image(file_name):
                raise Exception("Please provide a valid image")
            with open(file_name, "rb") as image_file:
                self.image_b64_content = base64.b64encode(image_file.read()).decode('utf-8')

        elif b64_content:
            if not self.processor.check_image_extension_from_base64(b64_content):
                raise Exception("Invalid Base64 content. Only image data is supported")
            self.image_b64_content = b64_content
        else:
            raise Exception("Please provide image_file or image_content")

    def get_image_transcription(self) -> str:
        """
        Get image transcription
        :return:
        """
        if not self.image_b64_content:
            raise Exception("Data not loaded. Please run load_data method")
        output = self.processor.get_image_transcription(self.image_b64_content)
        return output






