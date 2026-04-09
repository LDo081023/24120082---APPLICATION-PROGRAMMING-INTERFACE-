import requests

BASE_URL = "http://127.0.0.1:8000"

def test_translation():
    test_cases = [
        "Can you tell me how to get to the nearest bus station?",
        "Have a nice day bro"
    ]
    
    for text in test_cases:
        print(f"Đang dịch: '{text}'")
        response = requests.post(f"{BASE_URL}/predict", json={"text": text})
        
        if response.status_code == 200:
            result = response.json()
            print(f"Kết quả dịch: {result['translated_text']}")
        else:
            print(f"Lỗi: {response.json()}")
        print("-" * 30)

if __name__ == "__main__":
    test_translation()
