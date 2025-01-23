from flask import Flask, request, abort
import hmac
import hashlib
from .git_operations import pull_changes

def verify_signature(secret, payload, signature):
    hashed = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={hashed}", signature)

app = Flask(__name__)
repo = None  # Initialize with your repo object later
secret = None

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    signature = request.headers.get('X-Hub-Signature-256')
    if not verify_signature(secret, request.data, signature):
        abort(403)
    pull_changes(repo)
    return "Webhook processed", 200
