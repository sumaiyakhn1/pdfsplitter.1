# Push to GitHub - Step by Step

## Already Done ✅
- Git repository initialized
- Files committed

## Next Steps

### 1. Create GitHub Repository
1. Go to https://github.com
2. Click the **+** icon → "New repository"
3. Name it: `pdf-splitter` (or any name you like)
4. **Don't** initialize with README (you already have one)
5. Click **"Create repository"**

### 2. Connect and Push
Run these commands:

```bash
git remote add origin https://github.com/YOUR_USERNAME/pdf-splitter.git
git branch -M main
git push -u origin main
```

(Replace `YOUR_USERNAME` with your actual GitHub username)

### 3. Deploy on Vercel
1. Go to https://vercel.com
2. Sign up with your GitHub account
3. Click **"Add New Project"**
4. Select your repository
5. Click **"Deploy"**
6. Done! 🎉

---

## Summary

**What to upload:** The entire `work-script` folder (everything in the root)

**Files included:**
- frontend/ folder (React app)
- api/ folder (Python backend)
- Configuration files
- Original pdf_splitter.py
- README.md

**Excluded by .gitignore:**
- node_modules/
- build files
- PDF/zip files
- Temporary files

Your app will be live at: `https://your-project.vercel.app` ✨
