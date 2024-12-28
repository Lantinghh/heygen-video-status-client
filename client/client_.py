import requests
import time
import logging
from security import safe_requests

# Configure logging
logging.basicConfig(
    filename='video_status_client.log',  # Log file name
    level=logging.INFO,  # Log level (INFO and above)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

class VideoStatusClient:
    def __init__(self, server_url, max_retries=5, initial_delay=1, max_delay=5):
        self.server_url = server_url
        self.max_retries = max_retries
        self.initial_delay = initial_delay
        self.max_delay = max_delay
        logging.info("Initialized VideoStatusClient with server URL: %s", server_url)

    def get_status(self):
        delay = self.initial_delay
        retries = 0

        while retries < self.max_retries:
            try:
                response = safe_requests.get(f"{self.server_url}/status")
                response.raise_for_status()
                result = response.json().get("result")

                if result == "completed":
                    logging.info("✅ Video translation completed!")
                    print("✅ Video translation completed!")
                    return "completed"
                elif result == "error":
                    logging.error("❌ Video translation failed.")
                    print("❌ Video translation failed.")
                    return "error"
                else:
                    logging.warning("⏳ Status: %s. Retrying in %s seconds...", result, delay)
                    print(f"⏳ Status: {result}. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay = min(delay * 2, self.max_delay)  # 指数退避
                    retries += 1

            except requests.exceptions.RequestException as e:
                logging.error("⚠️ RequestException: %s", e)
                print(f"⚠️ Error: {e}")
                retries += 1
                time.sleep(delay)
        
        logging.error("❌ Max retries reached. Exiting.")
        print("❌ Max retries reached. Exiting.")
        return "timeout"
