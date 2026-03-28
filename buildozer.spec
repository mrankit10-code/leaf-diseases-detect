# buildozer.spec - Build configuration for Leaf Disease Detection APK

[app]
title = Leaf Disease Scanner
package.name = leafdiseasescanner
package.domain = org.techfest

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 2.0.0

requirements = python3,kivy,requests,pillow,python-dotenv,groq,plyer

orientation = portrait
fullscreen = 0
android.permissions = CAMERA,INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,ACCESS_FINE_LOCATION

# Android specific settings
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Gradle options
android.gradle_dependencies = androidx.appcompat:appcompat:1.3.1

# App icon
android.icon = 
android.presplash = 

# Build options
android.release_artifact = apk
p4a.source_dir = 
p4a.local_recipes = ./recipes/

[buildozer]
log_level = 2
warn_on_root = 1
