from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask CI/CD pipeline!. I am Muhsin shah and you are waching my CICD pipeline. and how are you ??"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
