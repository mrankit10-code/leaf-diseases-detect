# ✅ Deployment Checklist for Render

## Pre-Deployment (Local)

- [ ] **Verify files were updated**
  ```bash
  # Check that files have been modified
  git status
  ```
  Should show: `app.py`, `main.py`, `utils.py`, `render.yaml` as modified

- [ ] **Test locally**
  ```bash
  cd "d:\My Desktop\Tech fest project\leaf-diseases-detect"
  
  # Terminal 1: Start backend
  .\.venv\Scripts\python.exe -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
  
  # Terminal 2: Start frontend
  .\.venv\Scripts\python.exe -m streamlit run main.py --server.port 8502
  
  # Open: http://localhost:8502
  # Upload an image and verify it works
  ```
  - [ ] Backend starts without errors
  - [ ] Model loads on startup (check logs for "✅ Model loaded successfully!")
  - [ ] Frontend loads without errors
  - [ ] Image upload completes analysis successfully

---

## Deployment (GitHub & Render)

### Step 1: Commit Changes
- [ ] Open terminal in project directory
  ```bash
  cd "d:\My Desktop\Tech fest project\leaf-diseases-detect"
  ```

- [ ] Check what changed
  ```bash
  git status
  ```

- [ ] Stage all changes
  ```bash
  git add -A
  ```

- [ ] Commit with message
  ```bash
  git commit -m "Fix: Render timeout - singleton model + 120s timeout + retry logic"
  ```

- [ ] Verify commit
  ```bash
  git log -1
  ```
  Should show your commit message

### Step 2: Push to GitHub
- [ ] Push changes
  ```bash
  git push origin main
  ```
  
- [ ] Verify push succeeded
  ```bash
  git log --oneline -1
  # Should show: (HEAD -> main) [your commit message]
  ```

- [ ] Check GitHub
  - [ ] Go to https://github.com/YOUR_USERNAME/leaf-diseases-detect
  - [ ] Verify latest commit shows your changes

### Step 3: Deploy on Render
- [ ] Go to https://dashboard.render.com
- [ ] Click **leaf-disease-backend** service
- [ ] Click **Manual Deploy** → **Deploy latest commit**
  - [ ] Wait for build (5-10 minutes)
  - [ ] Status should show "Live" ✅
  - [ ] Check logs for `✅ Model loaded successfully!`

- [ ] Click **leaf-disease-frontend** service  
- [ ] Click **Manual Deploy** → **Deploy latest commit**
  - [ ] Wait for build (5-10 minutes)
  - [ ] Status should show "Live" ✅

---

## Post-Deployment Verification

### Check Backend Health
- [ ] Test endpoint: https://leaf-disease-backend.onrender.com/health
  Expected response:
  ```json
  {"status": "healthy"}
  ```

- [ ] Test warmup: https://leaf-disease-backend.onrender.com/warmup
  Expected response:
  ```json
  {"status": "ready", "message": "Model is loaded and ready for inference"}
  ```

### Check Frontend
- [ ] Open: https://leaf-disease-frontend.onrender.com
- [ ] Verify page loads (should see UI with Camera & Upload tabs)
- [ ] Upload a test image
  - [ ] Should start analyzing (~5-20s on first deploy)
  - [ ] Should complete WITHOUT timeout error ✅
  - [ ] Should show disease results

### Check Logs
- [ ] Backend logs (Render dashboard → leaf-disease-backend → Logs)
  - [ ] Look for: `✅ Model loaded successfully!`
  - [ ] Look for: `✅ Analysis completed successfully`
  - [ ] No error messages

- [ ] Frontend logs
  - [ ] Should show successful connection to backend
  - [ ] No timeout error messages

---

## Performance Testing

- [ ] **First Image Upload**
  - [ ] Time: 10-60 seconds (normal for first request after deploy)
  - [ ] Should complete ✅

- [ ] **Second Image Upload**  
  - [ ] Time: 5-10 seconds (faster due to cached model)
  - [ ] Should complete quickly ✅

- [ ] **Third Image Upload**
  - [ ] Time: 5-10 seconds (consistent)
  - [ ] Verify pattern is fast ✅

---

## Troubleshooting

### ❌ If Backend Status is "Building" for >15 minutes
- [ ] Click **Manual Deploy** → **Restart**
- [ ] Check logs for errors
- [ ] If persist, contact Render support

### ❌ If /health endpoint times out
- [ ] Check backend logs for errors
- [ ] Restart service manually on Render
- [ ] Try again after 5 minutes

### ❌ If Frontend shows "Cannot connect to backend"
- [ ] Verify `BACKEND_URL` environment variable is set correctly
- [ ] Check: https://YOUR_BACKEND.onrender.com/health
- [ ] If backend is dead, restart it

### ❌ If Image Analysis Still Times Out
- [ ] Verify it's using the new code (check commit hash in logs)
- [ ] Check backend logs for "Model loaded successfully!"
- [ ] Try uploading image again (retry logic should help)
- [ ] If persist: Upgrade Render plan to get more resources

### ❌ If Timeout Still Occurs on 3rd Attempt
- [ ] This indicates backend processing is very slow
- [ ] Check if GROQ_API_KEY is set in environment
- [ ] Check backend logs for API errors
- [ ] Consider upgrading Render plan

---

## Success Indicators

✅ **You're Done When:**
- [ ] Backend service shows "Live" status
- [ ] Frontend service shows "Live" status
- [ ] `/health` endpoint responds
- [ ] `/warmup` endpoint responds with "ready"
- [ ] Frontend page loads without errors
- [ ] First image upload completes in <60 seconds
- [ ] Subsequent uploads complete in <10 seconds
- [ ] No timeout errors appear
- [ ] Backend logs show `✅ Model loaded successfully!`

---

## Rollback (If Something Goes Wrong)

If deployment causes issues:

### Option 1: Revert to Previous Version
```bash
# Find previous commit
git log --oneline -5

# Reset to previous commit (replace COMMIT_ID)
git reset --hard COMMIT_ID

# Push to GitHub
git push -f origin main

# Redeploy on Render → Manual Deploy
```

### Option 2: Restore Specific Files
```bash
# If only one file is problematic, restore it
git checkout HEAD~1 -- app.py
git commit -m "Revert: Restore app.py"
git push origin main
```

---

## Final Sanity Check

Before considering this done, verify:

| Check | Status |
|-------|--------|
| Backend "Live" status | ✅ / ❌ |
| Frontend "Live" status | ✅ / ❌ |
| `/health` responds | ✅ / ❌ |
| `/warmup` shows "ready" | ✅ / ❌ |
| Image loads without timeout | ✅ / ❌ |
| Analysis completes successfully | ✅ / ❌ |
| Logs show model loaded | ✅ / ❌ |
| No error messages | ✅ / ❌ |

If all ✅: **Deployment Successful! 🎉**

---

## Need Help?

1. Check `DEPLOY_RENDER_GUIDE.md` for detailed steps
2. Check `RENDER_TIMEOUT_FIX.md` for technical details
3. Review Render logs (Render Dashboard → Logs tab)
4. Test locally first to isolate issues

---

**Estimated Total Time:**
- Local testing: 2-5 minutes
- Git commit & push: 1-2 minutes
- Backend build: 5-10 minutes
- Frontend build: 5-10 minutes
- **Total: 15-30 minutes**

Good luck! 🚀
