import pdfplumber


def extract_text(file):
    text = ""

    with pdfplumber.open(file) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text()

            if page_text:
                text += f"\n--- Page {page_number} ---\n"
                text += page_text

    return text


def get_page_count(file):
    with pdfplumber.open(file) as pdf:
        return len(pdf.pages)
