# ⚡ Quick Deploy - Copy & Paste

## 1️⃣ Go to Render
**https://render.com**

## 2️⃣ Click These Exact Buttons
- Click **"+ New"** (top right)
- Click **"Web Service"**

## 3️⃣ Connect GitHub
- You'll see: `sumaiyakhn1/pdfsplitter.1`
- Click **"Connect"**

## 4️⃣ Fill These Exact Values

```
Name: pdf-splitter-api

Environment: Python 3

Build Command: pip install -r requirements.txt && pip install gunicorn

Start Command: gunicorn app:app

Port: (leave as 10000)
```

## 5️⃣ Click
**"Create Web Service"**

## 6️⃣ Wait 2-3 Minutes
Watch the logs scroll by

## 7️⃣ Copy Your URL
You'll get: `https://pdf-splitter-api-xxx.onrender.com`
Save this URL!

---

## 8️⃣ Update Vercel Frontend

1. Go to **vercel.com**
2. Click your project
3. **Settings** → **Environment Variables**
4. Click **"Add New"**
5. Paste:
   - Name: `REACT_APP_API_URL`
   - Value: Your Render URL (from step 7)
6. **"Save"**
7. Go to **"Deployments"** → Click **"..."** → **"Redeploy"**

---

## ✅ Done!

Test at your Vercel URL 🎉
