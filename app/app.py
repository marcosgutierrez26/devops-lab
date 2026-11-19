import shutil
from flask import Flask, jsonify

app = Flask(__name__)


def clasificar(uso):
    if uso >= 90:
        return "CRITICAL"
    elif uso >= 80:
        return "WARNING"
    else:
        return "normal"


@app.route("/")
def home():
    return jsonify({"message": "DevOps Lab API", "status": "ok"})


@app.route("/disk")
def disk():
    total, used, free = shutil.disk_usage("/")
    percent = used / total * 100
    return jsonify({
        "total_gb": round(total / (1024 ** 3), 2),
        "used_gb": round(used / (1024 ** 3), 2),
        "usage_percent": round(percent, 1),
        "level": clasificar(percent),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
