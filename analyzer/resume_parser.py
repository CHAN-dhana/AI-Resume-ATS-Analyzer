import PyPDF2
import docx

def extract_text_from_pdf(file):

    reader = PyPDF2.PdfReader(file)

    text = ""

    for page in reader.pages:

        text += page.extract_text()

    return text


def extract_text_from_docx(file):

    doc = docx.Document(file)

    text = ""

    for para in doc.paragraphs:

        text += para.text

    return text


def extract_resume_text(file):

    filename = file.name.lower()

    if filename.endswith(".pdf"):

        return extract_text_from_pdf(file)

    elif filename.endswith(".docx"):

        return extract_text_from_docx(file)

    else:

        return ""