import subprocess
import time
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from client.client_ import VideoStatusClient

def test_integration():
    # start sercver
    server_process = subprocess.Popen(['python', 'server/app.py'])
    time.sleep(2)  # waiting for server to start

    try:
        client = VideoStatusClient("http://127.0.0.1:5000", max_retries=10)
        status = client.get_status()
        print(f"Final Status: {status}")
    finally:
        server_process.terminate()
        server_process.wait()

if __name__ == "__main__":
    test_integration()
