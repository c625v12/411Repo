from Crypto import Random
from Crypto.Cipher import AES
class aesEncrypt:


    def encrypt(self, data):
        key = b'jfkgltorpeywtsbfhdnyedouetqbdsjd'
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(data)
        print(ciphertext)

        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        plaintext = cipher.decrypt(ciphertext)
        try:
            cipher.verify(tag)
            print("The message is authentic:", plaintext)
        except ValueError:
            print("Key incorrect or message corrupted")

                
if __name__ == "__main__":
    a = aesEncrypt()
    payload = open('plaintextPayloadValko.json', 'rb')
    data = payload.read()
    print(data)
    encryptedData = a.encrypt(data)
    
