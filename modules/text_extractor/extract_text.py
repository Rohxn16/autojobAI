from langchain_community.document_loaders import PyPDFLoader

def extract_text(path: str) -> str:
    """
    function to extract text from a pdf and return it in string format
    :param path: path to the pdf file
    :return: text extracted from the pdf file
    """

    loader = PyPDFLoader(path)
    pages = loader.load_and_split()

    text = ""
    for page in pages:
        text += page.page_content

    return text