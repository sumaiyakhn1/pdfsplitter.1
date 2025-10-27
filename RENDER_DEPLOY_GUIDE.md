# 🚀 Deploy to Render - Step by Step

## Backend Deployment (Render)

### Step 1: Create Account
1. Go to **https://render.com**
2. Click **"Get Started for Free"** or **"Sign Up"**
3. Sign up using your **GitHub** account (easiest)
4. Authorize Render to access your GitHub

### Step 2: New Web Service
1. In Render dashboard, click **"+ New"** button (top right)
2. Select **"Web Service"**

### Step 3: Connect Repository
1. You'll see your GitHub repos
2. Find and select: **`sumaiyakhn1/pdfsplitter.1`**
3. Click **"Connect"**

### Step 4: Configure Settings

Fill in these settings:

**Name:**
```
pdf-splitter-api
```

**Region:**
```
Oregon (or closest to you)
```

**Branch:**
```
main
```

**Root Directory:**
```
(leave blank - root)
```

**Environment:**
```
Python 3
```

**Build Command:**
```
pip install -r requirements.txt && pip install gunicorn
```

**Start Command:**
```
gunicorn app:app
```

**Auto-Deploy:**
```
Yes (checked)
```

### Step 5: Deploy!
1. Scroll down to **"Create Web Service"**
2. Click the button
3. Wait for deployment (2-3 minutes)
4. You'll get a URL like: `https://pdf-splitter-api.onrender.com`

✅ **Backend is now live!**

---

## Frontend Update (Vercel)

### Step 1: Get Your Render URL
From Render dashboard:
- Copy your service URL: `https://pdf-splitter-api.onrender.com`

### Step 2: Update Vercel Environment Variables
1. Go to **https://vercel.com**
2. Select your project
3. Go to **Settings** → **Environment Variables**
4. Click **"Add New"**
5. Add:
   - **Name:** `REACT_APP_API_URL`
   - **Value:** `https://pdf-splitter-api.onrender.com`
6. Click **"Save"**

### Step 3: Redeploy
1. Go to **Deployments** tab
2. Click **"..."** (three dots) on latest deployment
3. Click **"Redeploy"**

✅ **Frontend now uses Render backend!**

---

## Test Your App

1. Go to your Vercel URL: `https://your-project.vercel.app`
2. Upload a test PDF
3. Click "Split PDF"
4. It should work! 🎉

---

## What's Happening?

- **Render:** Hosts Python backend (Flask) - Handles PDF processing
- **Vercel:** Hosts React frontend - Beautiful UI
- **Connection:** Environment variable links them

---

## Troubleshooting

**Backend not starting?**
- Check Render logs
- Make sure `requirements.txt` has all packages
- Verify `app.py` exists in root

**Frontend can't reach backend?**
- Check environment variable is set correctly
- Check API URL in browser console
- Verify CORS is enabled in app.py (it is!)

**Need help?**
Check Render logs or Vercel logs for error messages

---

You're all set! Just follow the steps above. 🚀
