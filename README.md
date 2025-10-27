# 📄 PDF Report Card Splitter

A modern web application to split merged PDF report cards into individual files, automatically named by Scholar Number.

## ✨ Features

- 📄 Upload PDF file via beautiful web interface
- 🔍 Extract Scholar Numbers using custom regex patterns
- 🎯 Click preset patterns for instant setup
- ⚙️ Configure pages per report card
- 📦 Download as zip file
- 🎨 Modern React frontend
- 🚀 Serverless backend powered by Vercel

## 🚀 Quick Deploy to Vercel

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/pdf-splitter.git
git push -u origin main
```

### Step 2: Deploy on Vercel

1. Go to [vercel.com](https://vercel.com)
2. Sign up/login with GitHub
3. Click **"New Project"**
4. Import your GitHub repository
5. Click **"Deploy"**
6. Done! 🎉

Your app will be live at: `https://your-project.vercel.app`

## 📋 What Gets Uploaded

**All of these files/folders:**
- ✅ `frontend/` - React app
- ✅ `api/` - Python backend
- ✅ `vercel.json` - Vercel config
- ✅ `requirements.txt` - Python dependencies
- ✅ `pdf_splitter.py` - Original script
- ✅ `README.md` - This file

**These are auto-ignored (.gitignore):**
- ❌ `node_modules/`
- ❌ `build/`
- ❌ `*.pdf` and `*.zip` files
- ❌ Environment files

## 🏃 Running Locally

### Backend
```bash
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## 📝 How It Works

1. Upload your merged PDF containing all report cards
2. Choose a preset pattern (or customize) to identify Scholar Numbers
3. Set the number of pages per report card
4. Click "Split PDF"
5. Download the zip with individual files named by Scholar Number

## 🛠️ Built With

- **React** - Frontend framework
- **Flask** - Backend API
- **PyPDF2** - PDF manipulation
- **pdfplumber** - Text extraction
- **Vercel** - Hosting platform

## 📞 Support

Need help? Check the deployment guide or open an issue on GitHub.

---

Made with ❤️ for easy PDF splitting
