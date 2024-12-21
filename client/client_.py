import requests
import time

class VideoStatusClient:
    def __init__(self, server_url, max_retries=5, initial_delay=1, max_delay=5):
        self.server_url = server_url
        self.max_retries = max_retries
        self.initial_delay = initial_delay
        self.max_delay = max_delay

    def get_status(self):
        delay = self.initial_delay
        retries = 0

        while retries < self.max_retries:
            try:
                response = requests.get(f"{self.server_url}/status")
                response.raise_for_status()
                result = response.json().get("result")

                if result == "completed":
                    print("✅ Video translation completed!")
                    return "completed"
                elif result == "error":
                    print("❌ Video translation failed.")
                    return "error"
                else:
                    print(f"⏳ Status: {result}. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay = min(delay * 2, self.max_delay)  # 指数退避
                    retries += 1

            except requests.exceptions.RequestException as e:
                print(f"⚠️ Error: {e}")
                retries += 1
                time.sleep(delay)
        
        print("❌ Max retries reached. Exiting.")
        return "timeout"
