web: uvicorn app:app --host 0.0.0.0 --port $PORT
worker: python -m streamlit run main.py --server.port $PORT --server.address 0.0.0.0
