// ==UserScript==
// @name         Tarea 3 Cripto
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://vistorete.github.io/Tarea-3-Criptografia/
// @require      https://code.jquery.com/jquery-3.5.1.min.js
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js
// @grant        none
// ==/UserScript==

(function() {
  /**
     * Decryption
   */
  function des_decrypt(ciphertext, key, iv) {
    key = CryptoJS.enc.Utf8.parse(key)
    iv = CryptoJS.enc.Utf8.parse(iv)
    let hex_string = CryptoJS.enc.Hex.parse(ciphertext)
    let srcs = CryptoJS.enc.Base64.stringify(hex_string)
    let decrypt = CryptoJS.DES.decrypt(srcs, key, {
      iv: iv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    })
    decrypt = decrypt.toString(CryptoJS.enc.Utf8)
    return decrypt.toString();
  }

    var msg = $('.des').attr("id");
    var iv = $('.iv').attr("id");
    var key = $('.key').attr("id");
    console.log("Mensaje encriptado(hex): " + msg);
    alert("Mensaje encriptado(hex): " + msg);
    console.log("Llave: " + key);
    alert("Llave: " + key);
    console.log("IV: " + iv);
    alert("IV: " + iv);
    $('#'+key).html("Mensaje encriptado(hex): " +  msg);
    $('#'+iv).html("IV: " + iv)
    $('#'+key).html("Llave: " + key)

    var decrypted_text = des_decrypt(msg, key, iv);
    console.log(decrypted_text);
    alert("Mensaje desencriptado: " + decrypted_text);
    var $div = $('<div />').appendTo('body');
    $div.attr('id', 'append');
    $('#append').html("Mensaje desencriptado: " + decrypted_text)

    
})();