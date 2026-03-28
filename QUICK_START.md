# 📱 QUICK REFERENCE - Mobile Installation

## 🎯 STEP-BY-STEP: Install App on Phone (2 minutes)

### **STEP 1: Get Your Computer IP Address**

**Windows:**
```powershell
ipconfig
```
Look for this line:
```
IPv4 Address . . . . . . : 192.168.**x.x**
```
Copy this IP address (e.g., `192.168.1.100`)

### **STEP 2: Make Sure Backend is Running**

Open PowerShell and run (keep it open):
```powershell
cd "d:\My Desktop\Tech fest project\leaf-diseases-detect"
.\.venv\Scripts\python.exe -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Wait until you see:
```
Uvicorn running on http://0.0.0.0:8000
```

### **STEP 3: Make Sure Frontend is Running**

Open another PowerShell and run (keep it open):
```powershell
cd "d:\My Desktop\Tech fest project\leaf-diseases-detect"
.\.venv\Scripts\python.exe -m streamlit run main.py --server.port 8502
```

Wait until Streamlit starts (takes 30 seconds)

### **STEP 4: On Your Mobile Phone**

1. **Connect phone to SAME WiFi** as computer ✅
2. **Open browser** (Chrome, Edge, Firefox recommended)
3. **Type in address bar:**
   ```
   http://192.168.x.x:8502
   ```
   (Replace `192.168.x.x` with your actual IP from Step 1)

4. **Wait** for page to load (shows Leaf Disease Scanner)

### **STEP 5: Install as App**

**Android (Chrome/Edge/Firefox):**
- Tap Menu button (⋮) or (≡)
- Tap "**Install app**" or "**Add to Home Screen**"
- Tap "**Install**"
- ✅ **Done!** App appears on home screen

**iPhone (Safari):**
- Tap Share button (↗️ at bottom)
- Tap "**Add to Home Screen**"
- Tap "**Add**"
- ✅ **Done!** App on home screen

---

## 🎮 NOW TEST THE APP!

1. **Open app from home screen** 🏠
2. **Click "📸 Camera" tab** 📸
3. **Allow camera access** ✅
4. **Take photo of a leaf** 📷
5. **Click "🔍 Analyze"** 
6. **Wait for results!** ⏳

---

## 🔧 TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| Can't connect | Check WiFi is same on phone and computer |
| IP not working | Run `ipconfig` again, verify IP |
| App won't install | Try different browser (Chrome best) |
| Camera not working | Go to Settings → Apps → give camera permission |
| API Error | Make sure backend (port 8000) is running |
| Stuck loading | Wait 60+ seconds, refresh page |

---

## 📊 System Status Check

Run this to verify all services:

```powershell
# Check if ports are open
netstat -an | findstr "8000\|8502"

# Should show:
# LISTENING on 0.0.0.0:8000
# LISTENING on 0.0.0.0:8502
```

---

## 💻 YOUR COMPUTER IP

```powershell
ipconfig /all
```

Find the WiFi adapter (usually "Wireless LAN adapter WiFi"):
```
IPv4 Address . . . . . . . . . . . : 192.168.x.x
```

---

## 🚀 INTERNET SHARING (Optional - for outside WiFi)

To access from different networks:

1. Use ngrok tunnel:
```bash
pip install ngrok
python -c "from pyngrok import ngrok; print(ngrok.connect(8502))"
```

2. Share the generated URL with anyone!

---

## 📥 NATIVE APK DOWNLOAD

Want a real APK file?

**Option 1: Online Service (Easiest)**
- Go to: https://appsgeyser.com/
- Upload files from: `d:\My Desktop\Tech fest project\leaf-diseases-detect\`
- Build APK
- Download and install on phone

**Option 2: Local Build**
```bash
pip install buildozer kivy

cd "d:\My Desktop\Tech fest project\leaf-diseases-detect"
buildozer android debug

# Wait 15-30 minutes...
# APK in: bin/leafdiseasescanner-2.0.0-debug.apk
```

---

## ✨ FEATURES AVAILABLE NOW

✅ **📸 Camera Capture** - Take photos on mobile  
✅ **📁 Upload** - Select from gallery  
✅ **🤖 AI Analysis** - Instant disease detection  
✅ **💊 Treatment Info** - Get remedies  
✅ **⚡ Mobile Responsive** - Perfect on phone  
✅ **🔌 Offline Ready** - Works without internet (after first load)  

---

## 🎯 NEXT STEPS

1. ✅ Install as PWA (2 min)
2. ✅ Test camera on leaf
3. ✅ Check disease detection works
4. ✅ Download APK file (optional)
5. ✅ Share with friends!

**Start with step 1 and let me know if it works!** 🚀
