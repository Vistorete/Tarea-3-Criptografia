
if __name__ == "__main__":
    
    from Crypto.Cipher import DES
    from Crypto import Random

    key = b'-8B key-'
    iv = Random.new().read(DES.block_size)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    plaintext = b'sona si latine loqueris '
    msg = iv + cipher.encrypt(plaintext)
    
    ivhex = iv.hex()
    msghex = msg.hex()
    keyhex = key.hex()
    print(plaintext)
    print(ivhex)
    print(msghex)
    print(keyhex)
    
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
                <div class="deshex" id="%s"></div>
                <div class="ivhex" id="%s"></div>
                <div class="keyhex" id="%s"></div>
            </body>
        </html>
        ''' % (msghex, ivhex, keyhex))
    index.close()

