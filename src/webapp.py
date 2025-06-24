from flask import Flask, render_template_string, request, redirect, session, url_for
from datetime import datetime
import os
import string

app = Flask(__name__)
app.secret_key = os.environ.get("CHAT_SECRET_KEY", "change_this_secret")  # Set a strong secret in production

# Simple shared password for you and your friend
CHAT_PASSWORD = "pass123"  # Change this!

# In-memory message store (reset on server restart)
messages = []

# Cipher dictionaries
lorem_cipher = {
    'A': 'Lorem', 'B': 'Ipsum', 'C': 'Dolor', 'D': 'Sit', 'E': 'Amet',
    'F': 'Consectetur', 'G': 'Adipiscing', 'H': 'Elit', 'I': 'Sed', 'J': 'Do',
    'K': 'Eiusmod', 'L': 'Tempor', 'M': 'Incididunt', 'N': 'Ut', 'O': 'Labore',
    'P': 'Et', 'Q': 'Dolore', 'R': 'Magna', 'S': 'Aliqua', 'T': 'Enim',
    'U': 'Ad', 'V': 'Minim', 'W': 'Veniam', 'X': 'Quis', 'Y': 'Nostrud', 'Z': 'Exercitation'
}
lorem_cipher_reversed = {v.lower(): k for k, v in lorem_cipher.items()}

def encrypt_message(message):
    words = message.split()
    encrypted_words = []
    for word in words:
        encrypted_letters = []
        for char in word:
            if char.isalpha():
                enc = lorem_cipher[char.upper()].capitalize()
                encrypted_letters.append(enc)
            else:
                encrypted_letters.append(char)
        encrypted_words.append(' '.join(encrypted_letters))
    return '   '.join(encrypted_words)  # Triple space between words

def decrypt_message(encrypted_message):
    decrypted_message = []
    words = encrypted_message.split('   ')  # Triple space between words
    for word in words:
        tokens = word.split()
        decrypted_letters = []
        for token in tokens:
            stripped = token.strip(string.punctuation)
            key = stripped.lower()
            if key in lorem_cipher_reversed:
                prefix = token[:len(token)-len(stripped)] if token.startswith(stripped) == False else ''
                suffix = token[len(stripped):] if token.endswith(stripped) == False else ''
                decrypted_letters.append(prefix + lorem_cipher_reversed[key] + suffix)
            else:
                decrypted_letters.append(token)
        decrypted_message.append(''.join(decrypted_letters))
    return ' '.join(decrypted_message)

CHAT_HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Private Chat</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { background: #f8f9fa; }
    .chat-box { height: 400px; overflow-y: auto; background: #fff; border: 1px solid #ddd; padding: 1em; }
    .msg-me { text-align: right; }
    .msg-other { text-align: left; }
    .msg-meta { font-size: 0.8em; color: #888; }
  </style>
</head>
<body>
  <div class="container mt-4">
    <h2 class="mb-4 text-center">🔒 Private Chat</h2>
    <div class="chat-box mb-3" id="chatbox">
      {% for m in messages %}
        <div class="{{ 'msg-me' if m['user'] == user else 'msg-other' }}">
          <div><b>{{ m['user'] }}</b>: {{ m['text']|e }}</div>
          <div class="msg-meta">{{ m['time'] }}</div>
        </div>
      {% endfor %}
    </div>
    <form method="post" autocomplete="off">
      <div class="input-group mb-3">
        <input type="text" name="msg" class="form-control" placeholder="Type a message..." autofocus autocomplete="off" required>
        <button class="btn btn-primary" type="submit">Send</button>
      </div>
    </form>
    <form method="post" action="{{ url_for('logout') }}">
      <button class="btn btn-outline-danger btn-sm">Logout</button>
    </form>
  </div>
  <script>
    // Auto-scroll chat to bottom
    var chatbox = document.getElementById('chatbox');
    chatbox.scrollTop = chatbox.scrollHeight;
  </script>
</body>
</html>
"""

LOGIN_HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Login - Private Chat</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-5" style="max-width:400px;">
    <h3 class="mb-4 text-center">🔒 Private Chat Login</h3>
    {% if error %}
      <div class="alert alert-danger">{{ error }}</div>
    {% endif %}
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Your Name</label>
        <input type="text" name="user" class="form-control" required>
      </div>
      <div class="mb-3">
        <label class="form-label">Password</label>
        <input type="password" name="pw" class="form-control" required>
      </div>
      <button class="btn btn-primary w-100" type="submit">Login</button>
    </form>
  </div>
</body>
</html>
"""

ALLOWED_USERS = {"Ahmed", "Malek"}  # Add your allowed names here

@app.route("/", methods=["GET", "POST"])
def chat():
    if "user" not in session:
        return redirect(url_for("login"))
    user = session["user"]
    if request.method == "POST":
        msg = request.form.get("msg", "").strip()
        if msg:
            messages.append({
                "user": user,
                "text": msg,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    return render_template_string(CHAT_HTML, messages=messages, user=user)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        user = request.form.get("user", "").strip()
        pw = request.form.get("pw", "")
        if pw == CHAT_PASSWORD and user:
            session["user"] = user
            return redirect(url_for("chat"))
        else:
            error = "Invalid password or missing name."
    return render_template_string(LOGIN_HTML, error=error)

@app.route("/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# For local testing only
if __name__ == "__main__":
    app.run(debug=True)