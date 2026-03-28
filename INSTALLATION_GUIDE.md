# 🚀 INSTALLATION GUIDE - Leaf Disease Scanner

## **Option 1: PWA (EASIEST - Recommended)**

### What is a PWA?
A Progressive Web App works like an native app but doesn't require Google Play Store. It installs directly from your browser!

### ✅ Installation Steps (30 seconds)

**On Android:**
1. Open your phone's browser (Chrome, Edge, Firefox)
2. Go to: `http://YOUR_COMPUTER_IP:8502`
   - Find your computer IP: Open Command Prompt and type `ipconfig` (look for IPv4 like `192.168.x.x`)
3. You'll see the **🌿 Leaf Disease Scanner** page
4. Click **"🚀 App Launcher"** button
5. Click **"Install app"** when browser asks
6. ✅ Done! App appears on your home screen

**On iPhone (iOS):**
1. Open Safari browser
2. Go to: `http://YOUR_COMPUTER_IP:8502`
3. Tap Share button (↗)
4. Tap "Add to Home Screen"
5. Tap "Add"
6. ✅ Done! App on home screen

### **Advantages of PWA:**
✅ No store submission required
✅ Works on all devices (Android, iPhone, Windows, Mac)
✅ Auto-updates when changes made
✅ Offline support (can work without internet)
✅ Fast and responsive
✅ Can use camera and other device features

---

## **Option 2: Native APK (COMPLEX)**

### Method A: Online APK Builder (Easiest for APK)
Use online services to convert your web app to APK:

**Services:**
- 🔗 https://www.phonegap.com/
- 🔗 https://appsgeyser.com/
- 🔗 https://www.appshopper.com/

**Steps:**
1. Go to one of the above services
2. Upload your web app files (we'll provide)
3. Click "Build APK"
4. Download the APK file
5. Transfer to phone and install (.apk files)

---

### Method B: Local Build with Android Studio (HARDEST)

**Requirements:**
- Windows/Mac/Linux computer
- 15+ GB free disk space
- Java Development Kit (JDK)
- Android Studio
- Android SDK (API 31+)
- Android NDK
- Buildozer (Python tool)

**Installation Steps:**

```bash
# Step 1: Install dependencies
pip install buildozer cython

# Step 2: Configure buildozer
cd "d:\My Desktop\Tech fest project\leaf-diseases-detect"
buildozer android debug

# Step 3: Wait 15-20 minutes for build...
# APK will be created in: bin/leafdiseasescanner-2.0.0-debug.apk

# Step 4: Transfer APK to mobile
# Connect phone via USB or email the APK file

# Step 5: Open APK on phone
# Navigate to Downloads folder → tap APK file → Install
```

---

## **Option 3: Web App Native Build (MODERATE - Recommended Alternative)**

Use **Kivy + PyDroid** to convert directly:

```bash
# Install kivy
pip install kivy

# Run on Android via PyDroid app:
# 1. Download "Pydroid 3" app from Google Play
# 2. Open app and create new project
# 3. Copy our code into Pydroid
# 4. Run it from PyDroid app
```

---

## **🎯 RECOMMENDED: Start with PWA**

For fastest testing, use **PWA** (30 seconds to install):

```powershell
# Make sure backend is running
cd "d:\My Desktop\Tech fest project\leaf-diseases-detect"

# Terminal 1: Backend
.\.venv\Scripts\python.exe -m uvicorn app:app --reload --host 0.0.0.0 --port 8000

# Terminal 2: Frontend
.\.venv\Scripts\python.exe -m streamlit run main.py --server.port 8502

# Terminal 3: Open index.html (PWA launcher)
# In browser: http://localhost:8502/index.html
# Or on mobile: http://192.168.x.x:8502/index.html
```

---

## **📱 Testing on Mobile**

### **Step 1: Find Your Computer IP**
```powershell
ipconfig
```
Look for line: `IPv4 Address . . . . . . : 192.168.x.x`

### **Step 2: On Mobile Browser**
```
Go to: http://192.168.x.x:8502
```

### **Step 3: Install as App**
- Android Chrome: Menu (⋮) → "Install app"
- iOS Safari: Share (↗) → "Add to Home Screen"

### **Step 4: Allow Permissions**
- Camera ✅
- Storage ✅

---

## **📦 Files We Created For You**

✅ **manifest.json** - PWA configuration
✅ **sw.js** - Service worker (offline support)
✅ **index.html** - PWA launcher page
✅ **buildozer.spec** - APK build config
✅ **main.py** - Updated with mobile UI
✅ **app.py** - Updated with CORS for mobile

---

## **🚀 Quick Start (Copy-Paste)**

```powershell
# Navigate to project
cd "d:\My Desktop\Tech fest project\leaf-diseases-detect"

# Activate venv
.\.venv\Scripts\Activate.ps1

# Start backend in Terminal 1
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000

# Start frontend in Terminal 2  
python -m streamlit run main.py --server.port 8502

# On mobile:
# Open browser → http://192.168.1.xxx:8502
# Click "Install App" 
# ✅ Done!
```

---

## **❓ Troubleshooting**

**Q: Can't connect from mobile?**
- A: Check computer and phone are on same WiFi
- A: Verify IP address is correct (ipconfig)
- A: Disable Windows Firewall temporarily

**Q: Camera not working?**
- A: Allow camera permissions when prompted
- A: Check browser has camera access

**Q: App crashes on mobile?**
- A: Clear browser cache
- A: Try different browser (Chrome recommended)

---

## **What We Recommend:**

1. **For Quick Testing:** PWA (30 seconds setup) ⭐⭐⭐⭐⭐
2. **For App Store:** Native APK via online service ⭐⭐⭐⭐
3. **For Full Control:** Local Buildozer build ⭐⭐⭐

---

**Start with PWA! It's the fastest way to test on mobile.** 🚀
