
import streamlit as st
import requests
from datetime import datetime
import json
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="🌿 Leaf Disease Scanner",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items=None
)


st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #e3f2fd 0%, #f7f9fa 100%); }
    main { padding: 1rem !important; }
    .stButton > button { width: 100%; font-size: 1.1em; padding: 1em 0; border-radius: 12px; font-weight: 600; }
    .result-card { background: rgba(255,255,255,0.95); border-radius: 16px; padding: 1.5em; border-left: 4px solid #1b5e20; }
    .disease-title { color: #1b5e20; font-size: 1.8em; font-weight: 700; }
    .severity-mild { background: #c8e6c9; color: #1b5e20; }
    .severity-moderate { background: #fff9c4; color: #f57f17; }
    .severity-severe { background: #ffccbc; color: #d84315; }
    </style>
""", unsafe_allow_html=True)

api_url = os.getenv('BACKEND_URL', 'http://localhost:8000')

if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = None

st.markdown("""<div style="text-align: center;">
    <h1 style="color: #1565c0;">🌿 Leaf Disease Scanner</h1>
    <p style="color: #616161;">Detect diseases with AI + Camera</p>
</div>""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📸 Camera", "📁 Upload"])

with tab1:
    st.markdown("### Take Photo")
    camera_image = st.camera_input("", key="camera")
    if camera_image:
        st.image(camera_image, use_column_width=True)
        if st.button("🔍 Analyze", use_container_width=True, key="cam_btn"):
            with st.spinner("🔬 Analyzing..."):
                try:
                    image_bytes = camera_image.getvalue()
                    files = {'file': ('image.jpg', image_bytes, 'image/jpeg')}
                    response = requests.post(f"{api_url}/disease-detection-file", files=files, timeout=30)
                    if response.status_code == 200:
                        st.session_state.analysis_result = response.json()
                    else:
                        st.error("Analysis failed")
                except Exception as e:
                    st.error(f"Error: {e}")

with tab2:
    st.markdown("### Upload Image")
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.image(uploaded_file, use_column_width=True)
        if st.button("🔍 Analyze", use_container_width=True, key="upload_btn"):
            with st.spinner("🔬 Analyzing..."):
                try:
                    image_bytes = uploaded_file.getvalue()
                    files = {'file': ('image.jpg', image_bytes, 'image/jpeg')}
                    response = requests.post(f"{api_url}/disease-detection-file", files=files, timeout=30)
                    if response.status_code == 200:
                        st.session_state.analysis_result = response.json()
                    else:
                        st.error("Analysis failed")
                except Exception as e:
                    st.error(f"Error: {e}")

if st.session_state.analysis_result:
    result = st.session_state.analysis_result
    st.divider()
    st.markdown("### 📊 Results")
    
    disease_type = result.get('disease_type', 'unknown')
    disease_name = result.get('disease_name', 'Unknown')
    confidence = result.get('confidence', 0)
    severity = result.get('severity', 'unknown')
    
    if result.get('disease_detected') and disease_type != 'invalid_image':
        st.markdown(f"""
            <div class="result-card">
                <div class="disease-title">🚨 {disease_name}</div>
                <strong>Confidence:</strong> {confidence}%<br>
                <strong>Severity:</strong> {severity.title()}
            </div>
        """, unsafe_allow_html=True)
        
        if result.get('symptoms'):
            st.markdown("**🔍 Symptoms:**")
            for s in result['symptoms']:
                st.write(f"• {s}")
        
        if result.get('treatment'):
            st.markdown("**💊 Treatment:**")
            for t in result['treatment']:
                st.write(f"✓ {t}")
    else:
        st.success("✅ Leaf is Healthy!")
    
    st.divider()
    if st.button("👈 Back", use_container_width=True):
        st.session_state.analysis_result = None
        st.rerun()

st.caption("🌱 Powered by Groq AI")
