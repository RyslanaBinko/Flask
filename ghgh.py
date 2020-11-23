from flask import Flask, render_template, request
from cryptography.fernet import Fernet


app = Flask(__name__)


@app.route("/")
@app.route("/encrypt")
def encrypt(string="string"):

    '''

    :param string: string for encrypt
    :return: encrypted string
    '''

    string = request.args["string"]
    by = string.encode('utf-8')
    return render_template("w.html", perem=f.encrypt(by), frase="Encrypted result: ")


@app.route("/decrypt")
def decrypt(string="string"):

    '''

    :param string: string for decrypt
    :return: decrypted string

    '''

    string = request.args["string"]
    byt = bytes(string, encoding='utf8')
    dec = f.decrypt(byt)
    return render_template('w.html', perem=dec.decode('utf-8'), frase="Decrypted result:")


key = Fernet.generate_key()
f = Fernet(key)

app.run(debug=True)
