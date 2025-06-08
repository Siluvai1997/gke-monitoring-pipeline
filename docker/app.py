from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
visits = Counter('app_visits', 'Number of visits to the Flask app')

@app.route('/')
def home():
    visits.inc()
    return "Hello from DevOps Flask App!"

@app.route('/metrics')
def metrics():
    return generate_latest(visits), 200, {'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
