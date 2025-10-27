import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [pattern, setPattern] = useState("Scholar\\s*No\\.?\\s*:\\s*([\\w/]+)");
  const [pagesPerStudent, setPagesPerStudent] = useState(2);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  // Preset patterns for common use cases
  const presetPatterns = [
    { name: "Scholar No. (with slash)", pattern: "Scholar\\s*No\\.?\\s*:\\s*([\\w/]+)", example: "Scholar No. : 3228/2019" },
    { name: "Scholar ID", pattern: "Scholar\\s*ID\\s*:\\s*([\\w]+)", example: "Scholar ID : 12345" },
    { name: "Student ID", pattern: "Student\\s*ID\\s*:\\s*([\\w]+)", example: "Student ID : ABC123" },
    { name: "Registration No.", pattern: "Registration\\s*No\\.?\\s*:\\s*([\\w]+)", example: "Registration No. : REG2024" },
    { name: "Roll Number", pattern: "Roll\\s*(?:No|Number)\\.?\\s*:\\s*([\\w]+)", example: "Roll No : 101" },
  ];

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile && selectedFile.type === 'application/pdf') {
      setFile(selectedFile);
      setError('');
    } else {
      setError('Please select a valid PDF file');
      setFile(null);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    
    if (!file) {
      setError('Please select a PDF file');
      return;
    }

    setLoading(true);

    try {
      const formData = new FormData();
      formData.append('pdf', file);
      formData.append('pattern', pattern);
      formData.append('pages_per_student', pagesPerStudent);

      const apiUrl = process.env.REACT_APP_API_URL || '';
      const response = await axios.post(`${apiUrl}/api/split_pdf`, formData, {
        responseType: 'blob',
      });

      // Create download link
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'split_pdfs.zip');
      document.body.appendChild(link);
      link.click();
      link.remove();

      setSuccess('PDF split successfully! Check your downloads folder.');
      setFile(null);
      document.getElementById('pdf-upload').value = '';
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to split PDF. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="container">
        <div className="card">
          <h1>📄 PDF Report Card Splitter</h1>
          <p className="subtitle">Split merged report cards into individual files</p>
          
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="pdf-upload">Select PDF File</label>
              <input
                id="pdf-upload"
                type="file"
                accept=".pdf"
                onChange={handleFileChange}
                className="file-input"
              />
              {file && (
                <div className="file-info">
                  ✅ {file.name} ({(file.size / 1024 / 1024).toFixed(2)} MB)
                </div>
              )}
            </div>

            <div className="form-group">
              <label htmlFor="pattern">ID Pattern - Choose a preset below or customize</label>
              <div className="preset-buttons">
                {presetPatterns.map((preset, idx) => (
                  <button
                    key={idx}
                    type="button"
                    className={`preset-btn ${pattern === preset.pattern ? 'active' : ''}`}
                    onClick={() => {
                      setPattern(preset.pattern);
                      setError('');
                    }}
                    title={`Example: ${preset.example}`}
                  >
                    {preset.name}
                  </button>
                ))}
              </div>
              <input
                id="pattern"
                type="text"
                value={pattern}
                onChange={(e) => setPattern(e.target.value)}
                className="input"
                placeholder='Enter custom pattern (leave as is if using preset above)'
              />
              <small>
                💡 Click a preset above to try it, or type a custom regex pattern
              </small>
            </div>

            <div className="form-group">
              <label htmlFor="pages">Pages per Report Card</label>
              <input
                id="pages"
                type="number"
                value={pagesPerStudent}
                onChange={(e) => setPagesPerStudent(Number(e.target.value))}
                className="input"
                min="1"
              />
              <small>Number of pages each report card has</small>
            </div>

            {error && <div className="alert alert-error">{error}</div>}
            {success && <div className="alert alert-success">{success}</div>}

            <button 
              type="submit" 
              className="btn-submit"
              disabled={loading || !file}
            >
              {loading ? '⏳ Processing...' : '🚀 Split PDF'}
            </button>
          </form>

          <div className="info-box">
            <h3>How it works:</h3>
            <ol>
              <li>Upload your merged PDF containing multiple report cards</li>
              <li>Click a preset pattern above to match your PDF format</li>
              <li>Set how many pages each report card has</li>
              <li>Click "Split PDF" and download the zip file with individual report cards</li>
            </ol>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
