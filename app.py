from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'AIATUS Signature Verification OpenShift Dünyasına Hoşgeldiniz!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 