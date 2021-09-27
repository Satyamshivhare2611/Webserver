from flask import Flask
app= Flask(__name__)

@app.route("/")
def main():
    return "Hi, This is my First webserver!"

if __name__ == "__main__":
    app.run(debug=true, host="0.0.0.0", port=80)
