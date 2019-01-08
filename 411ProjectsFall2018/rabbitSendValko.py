# Project: RabbitMQ
# Purpose Details: Send Message through rabbit
# Course: 411
# Author: Chris Valko
# Date Developed: 11/4/2018
# Last Date Changed: 11/6/2018
# Rev: 1

import pika

class rabbitSend:

	def send_rabbit(self):

		try:
                        print("Opening Json file to compress and decompress!!")
                        payload = open('json.json', 'rb')
                        data = payload.read()
                        print("Json file opened and read!")
                        print("Connecting to Localhost Queue")
                        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
                        channel = connection.channel()
                        print("Channel Connected")
                        channel.queue_declare(queue='ist411')
                        channel.basic_publish(exchange='',routing_key='ist411', body=data)
                        print(" [x] Sent 'JSON file!'")
                        connection.close()
		except Exception as e:
			print(e)

if __name__ == "__main__":

	r = rabbitSend()
	r.send_rabbit()
