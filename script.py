

import camellia


if __name__ == "__main__":

    c1 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
    c2 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)

    mensaje = "mi mensaje secre" # El mensaje que se encriptara
    plain = mensaje.encode("utf-8") # Codifica los caracteres a bytes
    encrypted = c1.encrypt(plain) # Encripta los caracteres
    
    mensaje_codificado = encrypted.hex() # Pasa los bytes a caracteres
    print( encrypted)
    print(bytes.fromhex(mensaje_codificado))
    decripted = c2.decrypt(encrypted) # Desencripta los bytes
    mensaje_decodificado = decripted.decode("utf-8") # Pasa los bytes a caracteres
    
    print("mensaje:", mensaje)
    # >>>> mensaje: mi mensaje secre
    print("mensaje codificado:", mensaje_codificado)
    # >>>> mensaje: Fxï-Ú)RU;Ôå
    print("mensaje decodificado:", mensaje_decodificado)
    # >>>> mensaje: mi mensaje secre 
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
                <div class="camellia" id="%s"></div>
            </body>
        </html>
        ''' % mensaje_codificado)
    index.close()

