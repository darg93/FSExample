from db import db
from main import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, threaded=True)
