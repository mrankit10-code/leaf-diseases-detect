import requests
import json

# Test API endpoint
url = "http://localhost:8000/disease-detection-file"
image_path = "Media/brown-spot-4 (1).jpg"

print("=" * 60)
print("TESTING BACKEND API")
print("=" * 60)

with open(image_path, 'rb') as f:
    files = {'file': (image_path, f, 'image/jpeg')}
    print(f"\n✓ Image file: {image_path}")
    print(f"✓ API Endpoint: {url}")
    print(f"\nSending request to backend...")
    print("-" * 60)
    
    response = requests.post(url, files=files, timeout=30)
    
print(f"\nResponse Status: {response.status_code}")
print("-" * 60)
print("\nResponse Body:")
print(json.dumps(response.json(), indent=2))
print("\n" + "=" * 60)

if response.status_code == 200:
    data = response.json()
    print("✓ API WORKING SUCCESSFULLY!")
    print(f"\nDisease Detected: {data.get('disease_detected')}")
    print(f"Disease Name: {data.get('disease_name')}")
    print(f"Disease Type: {data.get('disease_type')}")
    print(f"Severity: {data.get('severity')}")
    print(f"Confidence: {data.get('confidence')}%")
else:
    print("❌ API ERROR - Check backend logs")
print("=" * 60)
