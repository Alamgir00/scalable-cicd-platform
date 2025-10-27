---

## 2) Sample app (app/app.py)
A tiny Flask app that returns service name and commit SHA (via env).
```python
# app/app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    commit = os.environ.get("GIT_COMMIT", "local")
    return f"Hello from Scalable CI/CD Platform! Commit: {commit}\n", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
