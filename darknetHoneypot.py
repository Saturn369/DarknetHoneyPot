from flask import Flask, render_template, request, jsonify
import logging
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Set up logging to capture all access attempts and activity
logging.basicConfig(filename='honeypot_log.txt', level=logging.INFO)

# List of fake card entries (simulated)
cards = [
    {"name": "VISA Gold", "bin": "426398", "country": "Germany", "price": 35},
    {"name": "MasterCard Classic", "bin": "512345", "country": "US", "price": 25},
    {"name": "Discover Platinum", "bin": "601151", "country": "UK", "price": 30},
]

# Log each attempt
def log_attempt(endpoint, ip):
    log_message = f"{datetime.now()} - Attempted access to {endpoint} from {ip}"
    logging.info(log_message)

# Home page route
@app.route('/')
def home():
    return render_template('index.html', cards=cards)

# Fake login page (just logs attempts)
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    log_attempt("/login", request.remote_addr)
    
    # Always deny access to simulate a failed login
    return jsonify({"message": "Access denied. Must be invited."})

# Fake buy button route (logs any clicks)
@app.route('/buy/<bin>', methods=['POST'])
def buy(bin):
    log_attempt(f"/buy/{bin}", request.remote_addr)
    
    # Always deny access to simulate a failed purchase
    return jsonify({"message": "You must be logged in to purchase."})

# Start the app on port 5000
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
