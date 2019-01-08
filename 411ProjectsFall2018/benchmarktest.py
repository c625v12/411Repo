import json
from benchmark import AesDecrypt
from benchmark import AESEncrypt

key = b'teyrhfbqteutorpe'
iv_string = b'gsfdgsfdgsfdgsfd'
data = ''

def get_file():
    with open('plaintext.json', 'r') as f:
        payload = json.load(f)
        #data = json.load(f)
        return payload

def test_encryption(benchmark):
    try:
        iv_string = b'gsfdgsfdgsfdgsfd'
        encrypt = AESEncrypt(key, iv_string)
        payload = get_file()
        benchmark(encrypt.encrypt, payload)

    except Exception as e:
        print("Error %s" % e.args[0])

def test_decryption(benchmark):
    try:
        decrypt = AesDecrypt(key, iv_string)
        payload = decrypt.get_file()
        decrypted_result = benchmark(decrypt.decrypt, payload)
    except Exception as e:
        print("Error %s" % e.args[0])
