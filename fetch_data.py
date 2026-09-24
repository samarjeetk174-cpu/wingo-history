import os
import requests
import firebase_admin
from firebase_admin import credentials, firestore

# Firebase इनिशियलाइज़ेशन (बिना क्रेडेंशियल सीधे प्रोजेक्ट ID से या सर्विस की के जरिए)
# GitHub Actions Secrets से सर्विस अकाउंट JSON लिया जा सकता है
import json

firebase_key = os.environ.get("FIREBASE_SERVICE_ACCOUNT")
if firebase_key:
    cred = credentials.Certificate(json.loads(firebase_key))
    firebase_admin.initialize_app(cred)
else:
    # डिफ़ॉल्ट प्रोजेक्ट इनिशियलाइज़
    firebase_admin.initialize_app(options={"projectId": "wingo-d3f67"})

db = firestore.client()

def fetch_and_sync():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    # 1. 500 राउंड्स लाइव डेटा फेच
    combined = []
    for page in range(1, 11):
        try:
            url = f"https://draw.ar-lottery01.com/WinGo/WinGo_1M/GetHistoryIssuePage.json?pageNo={page}&pageSize=50"
            r = requests.get(url, headers=headers, timeout=10)
            data = r.json()
            items = data.get("data", {}).get("list", [])
            if items:
                combined.extend(items)
            else:
                break
        except Exception as e:
            print(f"Error on page {page}: {e}")
            break

    print(f"Total fetched records: {len(combined)}")

    # 2. Firestore में बैच राइट (Batch Write)
    batch = db.batch()
    batch_count = 0

    for item in combined:
        issue = str(item.get("issueNumber"))
        num = int(item.get("number"))
        size = "BIG" if num >= 5 else "SMALL"

        doc_ref = db.collection("wingo_history").document(issue)
        batch.set(doc_ref, {
            "issueNumber": issue,
            "number": num,
            "size": size,
            "status": "RECORDED",
            "timestamp": firestore.SERVER_TIMESTAMP
        }, merge=True)
        
        batch_count += 1
        if batch_count >= 400:  # Firestore 500 लिमिट सेफगार्ड
            batch.commit()
            batch = db.batch()
            batch_count = 0

    if batch_count > 0:
        batch.commit()
        
    print("Database sync complete!")

if __name__ == "__main__":
    fetch_and_sync()
