from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Merhaba! Bu benim OpenShift uygulamam!'

@app.route('/imza')
def signature():
    return 'İmza doğrulama servisi yakında burada olacak!'

# Ana blok dışında çalıştır
port = int(os.environ.get('PORT', 8080))
app.run(host='0.0.0.0', port=port) 