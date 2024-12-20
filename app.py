from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello, World!")

@app.errorhandler(Exception)
def handle_exception(e):
    # Log the error
    print(f"Error: {e}")
    return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run()