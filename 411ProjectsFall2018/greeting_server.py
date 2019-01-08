# Project:SFTP Secure File Transfer
# Purpose Details: Send and receive file through SFTP
# Course: 411
# Author: Chris Valko
# Date Developed: 10/11/2018
# Last Date Changed: 10/11/2018
# Rev: 1

import time
import Pyro4

@Pyro4.expose
class CrazyMaker(object):
	def get_fortune(self, name, name2):
		return ("This is the weird one: {0}" \
			"This second one is insane: {1}".format(name, name2))
daemon = Pyro4.Daemon()
uri = daemon.register(CrazyMaker)

print("Turning on server")
print("Server Ready. Object uri =", uri)
time.sleep(10)
print("Don't forget to turn off the server")
daemon.requestLoop()


