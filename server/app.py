from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

# Simulate delays and states
START_TIME = time.time()
DELAY = random.randint(5, 15)  #  Random delay of 5 to 15 seconds

@app.route('/status', methods=['GET'])
def status():
    elapsed = time.time() - START_TIME
    if elapsed < DELAY:
        return jsonify({"result": "pending"})
    elif random.random() < 0.1:  # 10% Probability of returning an error
        return jsonify({"result": "error"})
    else:
        return jsonify({"result": "completed"})

if __name__ == '__main__':
    app.run(port=5000)
