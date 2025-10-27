import os
import re
import pdfplumber
from PyPDF2 import PdfWriter, PdfReader

# ==== CONFIG ====
INPUT_PDF = "input.pdf"     # Path to your main PDF
OUTPUT_DIR = "output_pdfs"  # Folder to save split PDFs
PAGES_PER_STUDENT = 2       # Each student report = 2 pages
SCHOLAR_NO_PATTERN = r"Scholar\s*No\.?\s*:\s*([\w/]+)"  # Pattern like Scholar No. : 3228/2019
# =================

def extract_scholar_no(text):
    """Extract Scholar No. from text."""
    match = re.search(SCHOLAR_NO_PATTERN, text)
    if match:
        # Replace normal slash with Unicode fraction slash (⁄)
        return match.group(1).replace("/", "⁄")
    return None

def split_pdf_by_report(input_pdf, output_dir, pages_per_student):
    """Split PDF into individual report cards and name by Scholar No."""
    os.makedirs(output_dir, exist_ok=True)
    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)

    with pdfplumber.open(input_pdf) as pdf:
        for i in range(0, total_pages, pages_per_student):
            # Combine text from both pages to detect Scholar No.
            text = ""
            for j in range(i, min(i + pages_per_student, total_pages)):
                text += pdf.pages[j].extract_text() or ""

            scholar_no = extract_scholar_no(text) or f"student_{i//pages_per_student + 1}"
            output_filename = f"{scholar_no}.pdf"
            output_path = os.path.join(output_dir, output_filename)

            # Write the pages to a new PDF
            writer = PdfWriter()
            for j in range(i, min(i + pages_per_student, total_pages)):
                writer.add_page(reader.pages[j])

            with open(output_path, "wb") as f_out:
                writer.write(f_out)

            print(f"✅ Saved: {output_filename}")

if __name__ == "__main__":
    split_pdf_by_report(INPUT_PDF, OUTPUT_DIR, PAGES_PER_STUDENT)
    print("\n🎉 Done! All report cards have been split and saved.")
