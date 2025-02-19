from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Merhaba! Bu benim OpenShift uygulamam!'

@app.route('/imza')
def signature():
    return 'İmza doğrulama servisi yakında burada olacak!'

if __name__ == '__main__':
    # OpenShift'in PORT environment variable'ını kullan
    port = int(os.environ.get('PORT', 8080))
    # Host'u 0.0.0.0 olarak ayarla
    app.run(host='0.0.0.0', port=port, debug=False) 