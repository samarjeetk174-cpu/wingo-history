import requests
import json

# 1. API Endpoint URL (पूरे पैरामीटर्स के साथ)
url = "https://api.ar-lottery01.com/api/Lottery/GetTrendStatistics?gameCode=WinGo_1M&pageNo=1&pageSize=10&language=en&random=867075960099&signature=A1CD2A9F052644D9F0ED929EF6DE&timestamp=1790249652"

# 2. Token
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTYXpvSW4iOiIxNjA2NTkwIiwicm9sZSI6Im5vcm1hbCIsIklEcyI6WyIxMDMwMDIxOTUzNSIsInR5cGUiOjEsImFkIjowLCJpc3MiOiJhdXRoMCIsImV4cCI6MTc5MDI0OTY1Mn0.kxIrk26k0OWbRJ_4hscfWqd4"

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
