# flask_web/app.py

print("starting file")
from flask import Flask
print("successfully imported Flask")
app = Flask(__name__)

@app.route("/")
def foo():
    return "Hey, we have Flask in a Docker container!"

if __name__ == "__main__":
    print("[RUNNING]")
    app.run(debug=True, host="0.0.0.0", port=1286)
