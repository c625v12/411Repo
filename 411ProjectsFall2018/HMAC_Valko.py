# Project: HMAC Hashing
# Purpose Details: Hashing a message and comparing
# Course: 411
# Author: Chris Valko
# Date Developed: 10/21/2018
# Last Date Changed: 10/23/2018
# Rev: 1

import hashlib,  sys, base64, hmac

try:

	key = "This is a key"
	print(key)
	message = '{"payload":"hash"}'
	print(message)
	key = bytes(key, 'UTF-8')
	message = bytes(message, 'UTF-8')

	print("sha1 hmac")
	sha1_digester = hmac.new(key, message, hashlib.sha1)
	print("sha1 digester: ", sha1_digester)
	sha1_signature1 = sha1_digester.digest()
	print("sha1 signature 1: ", sha1_signature1)
	sha1_signature2 = base64.urlsafe_b64encode(sha1_signature1)
	print("sha1 signature 2: ", sha1_signature2)

	print("md5 hmac")
	md5_digester = hmac.new(key, message, hashlib.md5)
	print("md5 digester: ", md5_digester)
	md5_signature1 = md5_digester.digest()
	print("md5 signature 1: ", md5_signature1)
	md5_signature2 = base64.urlsafe_b64encode(md5_signature1)
	print("md5 signature 2: ", md5_signature2)
	compare_hmac = hmac.compare_digest(sha1_signature2, md5_signature2)
	print("The two signatures are ",compare_hmac)
except:
	print("Log exception: ", sys.exc_info()[0])


