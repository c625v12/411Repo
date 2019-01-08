import json, time
import cProfile
import re
from Crypto.Cipher import AES

class AESEncrypt:
    def __init__(self, key, iv_string):
        self.__key = key
        self.__iv_string = iv_string

    def save_file(self, name, data):

        with open((name + ".aes"), 'wb') as outfile:
            outfile.write(data)

    def encrypt(self, payload):
        pad = b' '
        plaintext = str(payload).encode('utf-8')
        length = 16 - (len(plaintext) % 16)
        plaintext += length * pad

        aes = AES.new(self.__key, AES.MODE_CBC, self.__iv_string)
        cipher = aes.encrypt(plaintext)
        return cipher

class AesDecrypt():

    def __init__(self, key, iv_string):

        self.__key = key
        self.__iv_string = iv_string

    def get_file(self):

        with open('encryptedfile.aes', 'rb') as f:
            data = f.read()
            return data

    def decrypt(self, ciphertext):

        aes = AES.new(self.__key, AES.MODE_CBC, self.__iv_string)
        plaintext = aes.decrypt(ciphertext)
        return plaintext

if __name__ == '__main__':

    try:
        print("||||Opening file to encrypt||||")
        payload = open('plaintext.json', 'rb')
        data = payload.read()
        #print(data)
        key = b'teyrhfbqteutorpe'
        iv_string = b'gsfdgsfdgsfdgsfd'
        encrypt = AESEncrypt(key, iv_string)
        decrypt = AesDecrypt(key, iv_string)
        print("||||Starting to encrypt||||")
        cipher = encrypt.encrypt(data)
        print("||||Encrypted Cipher||||")
        #print(cipher)
        print("||||Ciper text being saved||||")
        encrypt.save_file('encryptedfile', cipher)
        print("||||Decrypt class opening file||||")
        file_to_decrypt = decrypt.get_file()
        print("||||File to be decrypted||||")
        #print(file_to_decrypt)
        print("||||Decrypting File||||")
        decrypted_data = decrypt.decrypt(file_to_decrypt)
        print("||||Decrypted File||||")
        print(decrypted_data)


    except Exception as e:
        print("Error %s" % e.args[0])

