from flask import Flask, request, send_file
from flask_cors import CORS
import os
import re
import tempfile
import zipfile
from werkzeug.utils import secure_filename
import pdfplumber
from PyPDF2 import PdfWriter, PdfReader
import io

app = Flask(__name__)
CORS(app)

def extract_scholar_no(text, pattern):
    """Extract Scholar No. from text using custom pattern."""
    try:
        match = re.search(pattern, text)
        if match:
            return match.group(1).replace("/", "⁄")
        return None
    except:
        return None

def split_pdf_by_report(input_pdf_path, pattern, pages_per_student):
    """Split PDF into individual report cards and return as zip."""
    reader = PdfReader(input_pdf_path)
    total_pages = len(reader.pages)
    files_info = []

    with pdfplumber.open(input_pdf_path) as pdf:
        for i in range(0, total_pages, pages_per_student):
            # Combine text from pages to detect pattern
            text = ""
            for j in range(i, min(i + pages_per_student, total_pages)):
                text += pdf.pages[j].extract_text() or ""

            scholar_no = extract_scholar_no(text, pattern) or f"student_{i//pages_per_student + 1}"
            
            # Create PDF in memory
            output_buffer = io.BytesIO()
            writer = PdfWriter()
            for j in range(i, min(i + pages_per_student, total_pages)):
                writer.add_page(reader.pages[j])
            
            writer.write(output_buffer)
            output_buffer.seek(0)
            
            files_info.append({
                'filename': f"{scholar_no}.pdf",
                'data': output_buffer.getvalue()
            })

            print(f"✅ Created: {scholar_no}.pdf")

    return files_info

@app.route('/api/split-pdf', methods=['POST'])
def split_pdf():
    try:
        if 'pdf' not in request.files:
            return {'error': 'No PDF file provided'}, 400
        
        pdf_file = request.files['pdf']
        pattern = request.form.get('pattern', r"Scholar\s*No\.?\s*:\s*([\w/]+)")
        pages_per_student = int(request.form.get('pages_per_student', 2))
        
        if pdf_file.filename == '':
            return {'error': 'No file selected'}, 400

        # Save uploaded file temporarily
        temp_dir = tempfile.mkdtemp()
        input_path = os.path.join(temp_dir, secure_filename(pdf_file.filename))
        pdf_file.save(input_path)

        # Split the PDF
        files_info = split_pdf_by_report(input_path, pattern, pages_per_student)

        # Create zip file
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for file_info in files_info:
                zip_file.writestr(file_info['filename'], file_info['data'])
        
        zip_buffer.seek(0)

        # Cleanup
        os.remove(input_path)
        os.rmdir(temp_dir)

        return send_file(
            zip_buffer,
            mimetype='application/zip',
            as_attachment=True,
            download_name='split_pdfs.zip'
        )

    except Exception as e:
        return {'error': str(e)}, 500

@app.route('/api/health', methods=['GET'])
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
