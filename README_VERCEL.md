# Deploy to Vercel - Easy Guide

## Quick Deploy (5 minutes!)

### Step 1: Prepare your code
1. Install dependencies for frontend:
```bash
cd frontend
npm install
cd ..
```

### Step 2: Deploy to Vercel

**Option A: Using Vercel CLI (Recommended)**
```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
vercel

# Follow the prompts, enter "y" when asked to override settings
```

**Option B: Using GitHub (Easiest)**
1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "Add New Project"
4. Import your GitHub repository
5. Vercel will auto-detect settings
6. Click "Deploy"

That's it! 🎉

---

## Configuration

Vercel will automatically:
- ✅ Build your React frontend
- ✅ Deploy Python backend as serverless functions
- ✅ Handle routing between frontend and `/api/*` routes

---

## Environment Variables

You might need to set these in Vercel Dashboard:

1. Go to your project settings
2. Click "Environment Variables"
3. Add if needed:
   - `NODE_ENV=production`

---

## File Structure for Vercel

```
project/
├── api/              # Backend API functions
│   └── split_pdf.py  # Python serverless function
├── frontend/         # React app
│   ├── src/
│   └── public/
├── vercel.json       # Vercel configuration
└── requirements.txt # Python dependencies
```

---

## Troubleshooting

### Build fails?
- Make sure all dependencies are in `package.json` and `requirements.txt`
- Check Vercel build logs for error details

### API not working?
- Check that `/api/split_pdf.py` exists in `api/` folder
- Verify CORS is enabled

### Need to update?
Just push to GitHub - Vercel auto-deploys on push!

---

## What gets deployed?

- **Frontend:** React app on `your-project.vercel.app`
- **Backend:** Python API on `your-project.vercel.app/api/split-pdf`
- **All FREE** on Vercel's generous plan!

---

## Alternative: Deploy frontend and backend separately

If you prefer:

1. **Frontend on Vercel:**
   - Connect `frontend/` folder
   - Deploy as React app

2. **Backend on Railway or Render:**
   - Deploy `app.py` 
   - Set `REACT_APP_API_URL` in Vercel to point to backend

This way backend has more resources for processing large PDFs.

---

## Next Steps

Your app will be live at: `https://your-project-name.vercel.app`

✨ Enjoy your live PDF splitter!
