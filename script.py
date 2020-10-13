
if __name__ == "__main__":
    
    from Crypto.Cipher import DES
    from Crypto import Random
    import base64
    key = b'-8B key-'
    iv = Random.new().read(DES.block_size)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    plaintext = b'sona si latine loqueris '
    msg = iv + cipher.encrypt(plaintext)
    
    iv64 = base64.b64encode(iv)
    msg64 = base64.b64encode(msg)
    print(plaintext.decode())
    print(iv64.decode())
    print(msg64.decode())
    index = open("index.html","w")
    index.write('''
        <html>
            <head>

            </head>
            <title>
                Tarea cripto
            </title>
            <body>
                <p>Este sitio contiene un mensaje secreto</p>
                <div class="des64" id="%s"></div>
                <div class="iv64" id="%s"></div>
                <div class="key" id="%s"></div>
            </body>
        </html>
        ''' % (msg64.decode(), iv64.decode(), key.decode()))
    index.close()

