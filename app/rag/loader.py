import fitz


def load_pdf(file_path):
    """
    Load PDF and extract text page by page.
    """

    documents = []

    pdf = fitz.open(file_path)

    for page_num, page in enumerate(pdf):

        text = page.get_text()

        if text.strip():

            documents.append({
                "page": page_num + 1,
                "text": text
            })

    return documents