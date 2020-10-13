
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
    key64 = base64.b64encode(key)

    print(plaintext)
    print(iv64)
    print(msg64)
    print(key64)
    
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
                <div class="des" id="%s"></div>
                <div class="iv" id="%s"></div>
                <div class="key" id="%s"></div>
            </body>
        </html>
        ''' % (msg64.decode(), iv64.decode(), key64.decode()))
    index.close()

