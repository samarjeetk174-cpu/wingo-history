import requests
import json

# 1. API Endpoint URL
url = "https://api.ar-lottery01.com/api/Lottery/GetTrendStatistics?gameCode=WinGo_1M&pageNo=1&pageSize=10&language=en"

# 2. Cleaned Authorization Token (बिना किसी स्पेस या लाइन ब्रेक के)
token = "eyJhbGciOiJlUzI1NilsInR5cCl6lkpXVCJ9.eyJUb2tlblR5cGUiOiJBY2Nlc3NfVG9rZW4iLCJUZW5hbnRJZCI6IjExMDIiLCJVc2VySWQiOiIxMTAyMDAwMDc1MzUxMilslkFnZW50Q29kZSI6IjExMDIwMSIsIIRIbmFudEFjY291bnQiOil3NTM1MTIiLCJMb2dpbklQljoiMjQwOT00MGU1OjExMmM6ZGZiYzpjNDU50jlkZmY6ZmVIMT02MjJmliwiTG9naW5UaW1lIjoiMTc5MDI0NzY3ODg4NCIsIIN5c0N1cnJlbmN5ljoiSU5SliwiU3IzTGFuZ3VhZ2UiOiJlbilsIkRldmljZVR5cGUiOiJBbmRyb2lkliwiTG90dGVyeUxpbWI0R3JvdXBfZW0iOilwliwiVXNICIR5cGUiOilwliwibmJmljoxNzkwMjQ30TA2LCJIeHAiOjE3OTAyNTE1MDYsImlzyl6lmp3dElzc3VlcilslmF1ZCI6ImxvdHRlcnlUaWNrZXQifQ.2-VXfjHdBfYs7Z2dQ1ofRzFdOj9kEelbYy1Aw0-q4uQ"

# 3. Request Headers
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://www.veergame17.com",
    "Referer": "https://www.veergame17.com/",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua": '"Chromium";v="139", "Not=A?Brand";v="99"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site"
}

def fetch_data():
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print("Status Code:", response.status_code)
        
        if response.status_code == 200:
            data = response.json()
            print("Response Data:")
            print(json.dumps(data, indent=2))
        else:
            print("Request Failed. Response text:")
            print(response.text)
            
    except requests.exceptions.RequestException as e:
        print("Network error:", e)

if __name__ == "__main__":
    fetch_data()
