import requests
import base64
import fitz
import imghdr
import warnings
from .schema import MetaData, Page, ImageFilter
from typing import List


warnings.filterwarnings("ignore")


class Processor:

    def __init__(self, open_ai_key, open_ai_vision_model):
        self.open_ai_key = open_ai_key
        self.open_ai_vision_model = open_ai_vision_model
        self.pdf_content = None
        self.image_filter = None
        self.include_formatted_data = False

    def get_pdf_text(self, pdf_content: bytes, image_filter: ImageFilter,
                     page_index: int | None, include_formatted_data: bool) -> Page | List[Page]:
        """
        Get text from pdf.

        :param pdf_content:
        :param image_filter:
        :param page_index:
        :param include_formatted_data:
        :return:
        """
        self.pdf_content = pdf_content
        self.image_filter = image_filter
        self.include_formatted_data = include_formatted_data
        data = self.process_pdf(page_index)

        return data

    def process_pdf(self, page_index: int | None) -> Page | List[Page]:
        """
        Process full pdf or single page if page index is provided.

        :param page_index:
        :return:
        """
        if page_index:
            page = self.pdf_content[page_index-1]
            data = self.process_page(page)
        else:
            data = list()
            for page in self.pdf_content:
                data.append(self.process_page(page))

        return data

    def process_page(self, page: fitz.Page) -> Page | List[Page]:
        """
        Process single page in a pdf. This method generates text using fitz and image content using
        open AI.
        :param page:
        :return:
        """
        page_text_content = page.get_text()
        metadata = MetaData(
            page=page.number + 1
        )
        image_transcriptions = self.get_image_content(page.number)
        if self.include_formatted_data:
            page_content = self.format_page_content(page_text_content, image_transcriptions)
            data = Page(
                text_content=page_text_content,
                image_content=image_transcriptions,
                formatted_content=page_content,
                metadata=metadata
            )
        else:
            data = Page(
                text_content=page_text_content,
                image_content=image_transcriptions,
                metadata=metadata
            )


        return data

    @staticmethod
    def format_page_content(page_text_content: str, image_transcriptions: list) -> str:
        """
        Format text data and image transcriptions into page content.
        :param page_text_content:
        :param image_transcriptions:
        :return:
        """
        if not len(image_transcriptions):
            return page_text_content

        page_image_content = 'FIGURE TRANSCRIPTIONS: '

        for transcription in image_transcriptions:
            page_image_content = (page_image_content + f'\n ** START ** ' +
                                  transcription + ' ** END ** ')

        page_content = page_text_content + page_image_content
        return page_content

    def get_image_content(self, page_index: int) -> list:
        """ Get data associated with the image present on passed index in pdf content.

        :param page_index:
        """
        image_transcriptions = list()

        try:
            pix_maps = self.get_images_from_pdf_page(page_index)
            for pixmap in pix_maps:
                encoded_image = base64.b64encode(pixmap.tobytes('png')).decode('utf-8')
                image_transcriptions.append(self.get_image_transcription(b64_encoded_image_data=encoded_image))

        except Exception as e:
            raise e

        return image_transcriptions

    def get_images_from_pdf_page(self, page_index: int) -> List[fitz.Pixmap]:
        """
        Get images present on page with provided index.
        :param page_index:
        :return:
        """
        xrefs = set()
        for image in self.pdf_content.get_page_images(page_index):
            if self.filter_images(image):
                xrefs.add(image[0])
        pix_maps = [fitz.Pixmap(self.pdf_content, xref) for xref in xrefs]
        return pix_maps

    def filter_images(self, image: tuple) -> bool:
        """
        Filter images based on user supplier height and width bounds.
        :param image:
        :return:
        """
        if ((self.image_filter.lower_height < image[2] < self.image_filter.upper_height) and
                (self.image_filter.lower_width < image[3] < self.image_filter.upper_width)):
            return True
        return False

    def get_image_transcription(self, b64_encoded_image_data: str) -> str:
        """
        Call open AI chat completion api to fetch transcription of provided base 64 encoded image.
        Default Open AI vision model is gpt-4-vision-preview.

        :param b64_encoded_image_data:
        :return:
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.open_ai_key}"
        }

        payload = {
            "model": self.open_ai_vision_model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "what's this image? Please be precise and include numbers"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{b64_encoded_image_data}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 400
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload,
                                 verify=False)

        response.raise_for_status()
        choices = response.json().get('choices')
        if len(choices):
            content = choices[0].get('message', {}).get('content', '')
        else:
            raise Exception("Image transcript cannot be generated from open ai")

        return content

    @staticmethod
    def check_image_extension_from_base64(base64_str: str) -> bool:
        """
        Check if the passed base64 data is of a valid image type.
        :param base64_str:
        :return:
        """
        if base64_str.startswith("data:image/"):
            base64_str = base64_str.split(";base64,", 1)[1]

        image_data = base64.b64decode(base64_str, validate=True)

        extension = imghdr.what(None, h=image_data)
        if not extension:
            return False
        return True
