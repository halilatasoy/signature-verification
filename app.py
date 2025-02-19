from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Merhaba! Bu benim OpenShift uygulamam!'

@app.route('/imza')
def signature():
    return 'İmza doğrulama servisi yakında burada olacak!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 