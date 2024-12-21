import subprocess
import time

from client_ import VideoStatusClient

def test_integration():
    # 启动服务器
    server_process = subprocess.Popen(['python', 'server/app.py'])
    time.sleep(2)  # 等待服务器启动

    try:
        client = VideoStatusClient("http://127.0.0.1:5000", max_retries=10)
        status = client.get_status()
        print(f"Final Status: {status}")
    finally:
        server_process.terminate()
        server_process.wait()

if __name__ == "__main__":
    test_integration()
