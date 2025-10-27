# Deploy to Vercel - Simple Guide

## Quick Deploy (3 minutes!)

### Option 1: GitHub Deploy (Easiest) ⭐

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Ready for Vercel"
   git push
   ```

2. **Deploy on Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Click "Add New Project"
   - Import your GitHub repo
   - Click "Deploy"
   - Done! 🎉

### Option 2: Vercel CLI

```bash
# Install CLI
npm i -g vercel

# Login
vercel login

# Deploy
vercel

# Follow prompts, type 'y' to confirm
```

---

## What's Included

✅ **Frontend** - React app auto-built  
✅ **Backend** - Python API as serverless function  
✅ **Routing** - Automatically configured  
✅ **Free** - Vercel's generous free tier

---

## Your Live URL

After deployment, you'll get:
- `https://your-project.vercel.app`

Bookmark it and share! 🚀

---

## Troubleshooting

**Build failing?**
- Check that `api/split_pdf.py` exists
- Ensure `requirements.txt` has all dependencies

**Need to update?**
- Just push to GitHub
- Vercel auto-deploys!

---

## Next Steps

1. Test your live app
2. Share the URL with others
3. Done! 🎉

Your PDF splitter is now live on the internet!
