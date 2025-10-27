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

def handler(req):
    """Vercel serverless function handler."""
    try:
        # Get request data
        body = req.get('body')
        headers = req.get('headers', {})
        
        # Handle multipart form data parsing
        # This is simplified - Vercel automatically parses multipart
        pattern = 'Scholar\\s*No\\.?\\s*:\\s*([\\w/]+)'
        pages_per_student = 2
        
        # For now, return helpful error for debugging
        if not body:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'No request body', 'method': req.get('method'), 'headers': str(headers)})
            }
        
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': 'PDF processing not fully configured',
                'message': 'Please check API implementation',
                'body_type': type(body).__name__
            })
        }
        
    except Exception as e:
        import traceback
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e), 'traceback': traceback.format_exc()})
        }
