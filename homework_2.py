from flask import Flask, render_template, request
from cryptography.fernet import Fernet


app = Flask(__name__)
generate_key = Fernet.generate_key()
key = Fernet(generate_key)


@app.route("/")
@app.route("/encrypt")
def encrypt():

    '''

    Encrypts the received text

    :param string: string for encrypt:str
    :return: encrypted result:bytes

    '''

    text = request.args.get("string")
    if text:
        convert = text.encode('utf-8')
        frase = "Encrypted result: "
        result = key.encrypt(convert)
    else:
        frase = "Enter your text to the url"
        result = ""
    return render_template("encrypt_and_decrypt.html", result=result, frase=frase)


@app.route("/decrypt")
def decrypt():

    '''

    Deccrypts the received text

    :param string: string for decrypt:str
    :return: decrypted result:str

    '''

    string = request.args.get("string")
    convert_to_bytes = bytes(string, encoding='utf8')
    result = key.decrypt(convert_to_bytes)
    return render_template('encrypt_and_decrypt.html', result=result.decode('utf-8'), frase="Decrypted result:")


app.run(debug=True)
