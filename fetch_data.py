import os
import json
import requests
import firebase_admin
from firebase_admin import credentials, db

# 1. Firebase Realtime Database कनेक्शन सेटअप
firebase_key = os.environ.get("FIREBASE_SERVICE_ACCOUNT")
database_url = "https://wingo-history-fa620-default-rtdb.firebaseio.com"

if firebase_key:
    try:
        key_dict = json.loads(firebase_key)
        cred = credentials.Certificate(key_dict)
    except Exception:
        cred = credentials.Certificate(firebase_key)
    firebase_admin.initialize_app(cred, {"databaseURL": database_url})
else:
    firebase_admin.initialize_app(options={"databaseURL": database_url})

def fetch_and_sync():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    combined = []
    # 500 रिकॉर्ड्स के लिए 10 पेज तक लूप
    for page in range(1, 11):
        url = f"https://draw.ar-lottery01.com/WinGo/GetHistoryIssuePage.json?pageNo={page}&pageSize=50"
        try:
            r = requests.get(url, headers=headers, timeout=10)
            data = r.json()
            items = data.get("data", {}).get("list", [])
            if not items:
                break
            combined.extend(items)
        except Exception as e:
            print(f"Error on page {page}: {e}")
            break

    print(f"Total fetched records: {len(combined)}")

    if not combined:
        print("No data to update.")
        return

    # 2. Realtime Database में 'wingo_history' नोड में डेटा सेव करना
    ref = db.reference("wingo_history")
    updates = {}

    for item in combined:
        issue = str(item.get("issueNumber"))
        num = int(item.get("number", 0))
        color = item.get("color", "")
        size = "BIG" if num >= 5 else "SMALL"

        updates[issue] = {
            "issueNumber": issue,
            "number": num,
            "color": color,
            "size": size,
            "premium": item.get("premium", ""),
            "status": "RECORDED"
        }

    # एक साथ बल्क अपडेट
    ref.update(updates)
    print("Database sync complete!")

if __name__ == "__main__":
    fetch_and_sync()
