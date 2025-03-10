from pypdf import PdfReader
import pdfplumber
import difflib

class PDFUtiles:

    @staticmethod
    def extract_text_from_pdf(file):
        with open(file,"rb") as pdf_file:
            reader = PdfReader(pdf_file)
            text = "\n".join([page.extract_text() for page in reader.pages])
            return text

    @staticmethod
    def extract_table_from_pdf(file,page_no):
        with pdfplumber.open(file) as pdf_file:
            table = pdf_file.pages[page_no].extract_table()
            return table

    @staticmethod
    def get_pdf_metadata(pdf_path):
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            metadata = reader.metadata
            return metadata

    @staticmethod
    def compare_pdfs(pdf1_text, pdf2_text):
        diff = list(difflib.unified_diff(pdf1_text.splitlines(), pdf2_text.splitlines()))
        return diff if diff else "PDFs are identical"