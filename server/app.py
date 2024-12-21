from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

# 模拟延迟和状态
START_TIME = time.time()
DELAY = random.randint(5, 15)  # 随机延迟5到15秒

@app.route('/status', methods=['GET'])
def status():
    elapsed = time.time() - START_TIME
    if elapsed < DELAY:
        return jsonify({"result": "pending"})
    elif random.random() < 0.1:  # 10% 概率返回错误
        return jsonify({"result": "error"})
    else:
        return jsonify({"result": "completed"})

if __name__ == '__main__':
    app.run(port=5000)
