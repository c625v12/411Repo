from base64 import b64encode
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import json
from base64 import b64decode
from Crypto.Util.Padding import unpad
class encrypt_decrypt:
    
    def encrypt(self, data):
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))
        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')
        result = json.dumps({'iv':iv, 'ciphertext':ct})
        print(result)
        b64 = json.loads(result)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        print("The message was: ", pt)

    def Main(self):
        payload = open('plaintextPayloadValko.json', 'rb')
        data = payload.read()
        encryptedObject = self.encrypt(data)

if __name__ == "__main__":
    e = encrypt_decrypt()
    e.Main()

