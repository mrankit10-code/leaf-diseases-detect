# Complete deployment guide for Render.com

## 🚀 DEPLOYMENT STEPS FOR RENDER

Your Leaf Disease Detection app is **READY** for Render deployment!

### ✅ What We've Prepared:

1. **runtime.txt** - Python 3.10.11 version specified
2. **Procfile** - Startup commands for both backend and frontend
3. **render.yaml** - Render-specific configuration
4. **.env.example** - Environment variables template
5. **Updated app.py** - Environment variable support
6. **Updated main.py** - Backend URL configuration

---

## 📋 PRE-DEPLOYMENT CHECKLIST

- ✅ Python version: 3.10.11
- ✅ FastAPI backend configured
- ✅ Streamlit frontend configured
- ✅ CORS enabled for production
- ✅ Environment variables support
- ✅ requirements.txt updated
- ✅ .gitignore configured
- ✅ Git initialized and pushed

---

## 📝 STEP 1: Create .env.example (Remove API Key)

Your `.env.example` should have:
```
GROQ_API_KEY=your_groq_api_key_here
BACKEND_URL=http://localhost:8000
PYTHONUNBUFFERED=1
```

**DO NOT PUSH** actual API keys to GitHub!

---

## 🔗 STEP 2: Create GitHub Repository

```powershell
# If not already done
cd "d:\My Desktop\Tech fest project\leaf-diseases-detect"
git init
git add .
git commit -m "Initial commit: Leaf Disease Detection App"
git remote add origin https://github.com/YOUR_USERNAME/leaf-diseases-detect.git
git branch -M main
git push -u origin main
```

**Make sure to add `.env` to `.gitignore`!**

---

## 🌐 STEP 3: Deploy on Render

### **Option A: Using render.yaml (Recommended)**

1. **Push your code to GitHub**
2. **Go to**: https://render.com
3. **Sign up** (link GitHub account)
4. **Create new service**
5. **Select**: "Build and deploy from GitHub repository"
6. **Select** your `leaf-diseases-detect` repository
7. **Render automatically detects** `render.yaml`
8. **Confirm settings** and click **"Deploy"**

### **Option B: Manual Setup (if render.yaml not detected)**

#### Backend Service:
1. New Web Service
2. Connect GitHub repo
3. **Name**: `leaf-disease-backend`
4. **Runtime**: Python 3
5. **Build Command**: `pip install -r requirements.txt`
6. **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
7. **Environment Variables**:
   - `GROQ_API_KEY` = (your API key)
   - `PYTHONUNBUFFERED` = `1`
8. **Deploy** ✅

#### Frontend Service:
1. New Web Service
2. Connect **same** GitHub repo
3. **Name**: `leaf-disease-frontend`
4. **Runtime**: Python 3
5. **Build Command**: `pip install -r requirements.txt`
6. **Start Command**: `streamlit run main.py --server.port $PORT --server.address 0.0.0.0`
7. **Environment Variables**:
   - `GROQ_API_KEY` = (your API key)
   - `BACKEND_URL` = `https://leaf-disease-backend.onrender.com`
   - `PYTHONUNBUFFERED` = `1`
8. **Deploy** ✅

---

## ✨ AFTER DEPLOYMENT

### Your URLs will be:
```
Backend:  https://leaf-disease-backend.onrender.com
Frontend: https://leaf-disease-frontend.onrender.com
```

### Access your app:
```
https://leaf-disease-frontend.onrender.com
```

---

## 🔧 TROUBLESHOOTING

**Issue: "Build failed"**
- Check: Python version compatibility
- Check: All dependencies in requirements.txt
- Check: No hardcoded localhost paths

**Issue: "App crashes on startup"**
- Check: GROQ_API_KEY environment variable is set
- Check: Logs in Render dashboard

**Issue: "Can't access camera"**
- Camera only works on HTTPS (Render provides HTTPS)
- Browser must allow camera access

**Issue: "Backend timeout"**
- First request takes 30-60 seconds (cold start)
- This is normal on free tier

---

## 💡 OPTIMIZATION TIPS

### For Better Performance:
1. Use Render's Pro plan for faster restarts
2. Add caching to Groq API responses
3. Optimize image file sizes
4. Use CDN for static files

### Production Settings:
```python
# In main.py
st.set_page_config(..., menu_items=None)  # Hide menu for cleaner UI
```

---

## 📊 COSTS

**Render Free Tier:**
- ✅ 750 free hours/month
- ✅ Auto-sleep after 15 min inactivity
- ⚠️ Cold starts (30-60 sec on wake)

**Render Pro Tier:**
- 💰 $7/month per service
- ⚡ Fast boot times
- 🚀 Better performance

---

## 🎯 NEXT STEPS

1. **Update .gitignore** - exclude .env file
2. **Create .env.example** - with placeholder values
3. **Push to GitHub** - all code and config
4. **Create Render account** - free tier available
5. **Deploy from render.yaml** - automatic setup
6. **Add environment variables** - in Render dashboard
7. **Test the app** - in browser
8. **Monitor logs** - check for errors

---

## 📞 SUPPORT

**If something goes wrong:**

1. Check Render Dashboard → Logs
2. Check GitHub Actions (if using)
3. Verify environment variables
4. Test locally first with: `python -m streamlit run main.py`

---

**Ready to deploy? 🚀**

All files are prepared! Just follow the steps above.
