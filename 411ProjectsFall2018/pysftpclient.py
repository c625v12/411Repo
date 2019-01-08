# Project:SFTP Secure File Transfer
# Purpose Details: Send and receive file through SFTP
# Course: 411
# Author: Chris Valko
# Date Developed: 10/11/2018
# Last Date Changed: 10/11/2018
# Rev: 1

import	pysftp, sys
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts':cnopts, 'host':'oz-ist-linux-fa18-411', 'username':'ftpuser', 'password':'test1234', 'port':103}
try:
	with pysftp.Connection(**cinfo) as sftp:
		print("Connection made")
		try:
			print("getting payloadValko.json file")

			print("File got")
			print("putting payloadValko.json file")
			sftp.put('payloadValko.json', 'ChrisValkoPayload.json')
			print("file was put")
			sftp.get('ChrisValkoPayload.json')
		except:
			print("Log exception 1: ", sys.exc_info()[0])
except:
	print("Log exception 2: ", sys.exc_info()[0])
