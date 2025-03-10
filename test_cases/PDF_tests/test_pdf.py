import os.path
import time
import difflib
from selenium import webdriver
from utilities.pdf_utiles import PDFUtiles


class TestPDF:
    pdf = os.path.abspath(os.path.curdir) + "\\test_data\\test_invoice.pdf"

    def test_invoice_text(self):
        text = PDFUtiles.extract_text_from_pdf(self.pdf)
        items = ["laptop","mouse","keyboard","monitor","key"]
        #Find missing items
        missing_items = [item for item in items if item not in text.lower()]
        # Assertion with detailed error message
        assert not missing_items, f"Missing items in PDF: {missing_items}"

    def test_invoice_table(self):
        table = PDFUtiles.extract_table_from_pdf(self.pdf,0)
        assert table[0][0] == "Item" , "Table not correct"


    def test_invoice_metadata(self):
        metadata = PDFUtiles.get_pdf_metadata(self.pdf)
        assert metadata.title == "Invoice", "Document title is not correct"
        assert metadata.creation_date.day == 10


    def test_pdf_rendering(self):
        driver = webdriver.Chrome()
        driver.get(self.pdf)
        assert "pdf" in driver.current_url, "PDF did not load correctly!"
        driver.quit()

    # def compare_two_pdfs(self):
    #     pdf1_text = PDFUtiles.extract_text_from_pdf("old_version.pdf")
    #     pdf2_text = PDFUtiles.extract_text_from_pdf("new_version.pdf")
    #     diff_results = PDFUtiles.compare_pdfs(pdf1_text, pdf2_text)
    #     print(diff_results)





