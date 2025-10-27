from http.server import BaseHTTPRequestHandler
import json
import os
import re
import tempfile
import zipfile
import pdfplumber
from PyPDF2 import PdfWriter, PdfReader
import io

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
            text = ""
            for j in range(i, min(i + pages_per_student, total_pages)):
                text += pdf.pages[j].extract_text() or ""

            scholar_no = extract_scholar_no(text, pattern) or f"student_{i//pages_per_student + 1}"
            
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

    return files_info

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_type = self.headers.get('Content-Type', '')
            content_length = int(self.headers.get('Content-Length', 0))
            
            if 'multipart/form-data' not in content_type:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Expected multipart/form-data'}).encode())
                return
            
            # Read request data
            data = self.rfile.read(content_length)
            
            # Parse multipart
            files = {}
            form = {}
            
            boundary = content_type.split('boundary=')[1].encode()
            parts = data.split(b'--' + boundary)
            
            for part in parts:
                if b'Content-Disposition: form-data' in part:
                    headers, body = part.split(b'\r\n\r\n', 1)
                    if b'name="pdf"' in headers:
                        files['pdf'] = body.rstrip(b'\r\n--')
                    elif b'name=' in headers:
                        name = headers.split(b'name="')[1].split(b'"')[0].decode()
                        value = body.rstrip(b'\r\n--').decode()
                        form[name] = value
            
            if 'pdf' not in files:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'No PDF file provided'}).encode())
                return
            
            pattern = form.get('pattern', r"Scholar\s*No\.?\s*:\s*([\w/]+)")
            pages_per_student = int(form.get('pages_per_student', 2))
            
            # Save file temporarily
            temp_dir = tempfile.mkdtemp()
            input_path = os.path.join(temp_dir, 'input.pdf')
            with open(input_path, 'wb') as f:
                f.write(files['pdf'])
            
            # Split PDF
            files_info = split_pdf_by_report(input_path, pattern, pages_per_student)
            
            # Create zip
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for file_info in files_info:
                    zip_file.writestr(file_info['filename'], file_info['data'])
            
            zip_buffer.seek(0)
            
            # Cleanup
            os.remove(input_path)
            os.rmdir(temp_dir)
            
            # Send response
            self.send_response(200)
            self.send_header('Content-Type', 'application/zip')
            self.send_header('Content-Disposition', 'attachment; filename=split_pdfs.zip')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(zip_buffer.getvalue())
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())
    
    def do_GET(self):
        if '/health' in self.path:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'ok'}).encode())
        else:
            self.send_response(404)
            self.end_headers()
