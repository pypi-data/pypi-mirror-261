from flask import jsonify

from .pubsub import streaming_pull_future
from .health import app, is_healthy

@app.route('/shutdown', methods=['GET'])
def shutdown():
    print('Shutdown signal received')
    global streaming_pull_future

    streaming_pull_future.cancel()
    streaming_pull_future.result()

    global is_healthy
    is_healthy = False

    return jsonify(success=True, status_code=200)