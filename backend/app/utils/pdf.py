from pypdf import PdfReader
from io import BytesIO

def extract_text_from_pdf(contents: bytes) -> str:
    pdf_file = BytesIO(contents)

    reader = PdfReader(pdf_file)

    text=""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text      

