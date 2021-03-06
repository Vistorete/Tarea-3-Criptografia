import pyDes # pyDes.des(key, [mode], [IV], [pad], [padmode])
    
if __name__ == "__main__":

    data = "DES Algorithm Implementation"
    key = "DESCRYPT"
    iv = "abcd1234"
    k = pyDes.des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)
    encrypted_data = k.encrypt(data)
    decrypted_data = k.decrypt(encrypted_data)
    
    print ("Texto plano: %r" % data)
    print ("Key: %r" % key)
    print ("IV: %r" % iv)
    print ("Encrypted bytes: %r" %encrypted_data)
    print ("Encrypted hex:   %r" %encrypted_data.hex())
    print ("Decrypted: %r" % decrypted_data)


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
        ''' % (encrypted_data.hex(), iv, key))
    index.close()

