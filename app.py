from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.errorhandler(Exception)
def handle_exception(e):
    # Log the error
    print(f"Error: {e}")
    return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(debug=True)