# Pdf-Image-Text

Get text inside pdf pages with image transcriptions.
Powered by fitz and OpenAI.

## Instructions

### 1. Installation

pip install pdf-image-text

A library to get data from standalone images and images present inside pdf.

### 2. Initialize

`pdf_to_text = PdfToText(OPEN_AI_KEY='<>', OPEN_AI_VISION_MODEL='<>')`

Note: The parameters are not required if already present in environment variables.

### 3. Load data

#### From file - 
##### Pdf2Text: `pdf_to_text.load_data(file_name='<Path to file>')`
##### Image2Text: `image_to_text.load_data(file_name='<Path to file>')`

#### From file object - 

##### Pdf2Text: `pdf_to_text.load_data(file_bytes_object='<file content>')`
##### Image2Text: `image_to_text.load_data(file_bytes_object='<file content>')`



### 3. Get output

##### Pdf2Text: 
`image_filter = ImageFilter(lower_height=<int>, upper_height=<int>, lower_width=<int>, upper_width=<int>)`

`output = pdf_to_text.get_pdf_content(image_filter=image_filter, page_index=<optional field page index>)`

##### Image2Text: 
`output = image_to_text.get_image_transcription()`



