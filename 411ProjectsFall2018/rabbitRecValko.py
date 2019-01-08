# Project: RabbitMQ
# Purpose Details: Send a message with RabbitMQ
# Course: 411
# Author: Chris Valko
# Date Developed: 11/4/2018
# Last Date Changed: 11/6/2018
# Rev: 1

import pika
from Crypto import Random
from Crypto.Cipher import AES
import json
import base64


try:
        print("Connection to local host")
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        print("Queue hello created")
        channel.queue_declare(queue='ist411')
        #callback function that will receive the message
        def callback(ch, method, properties, body):
                print(" [x] Received %r" % body)
                key = b'th byte key i am the key of life'
                cipher = AES.new(key, AES.MODE_EAX)
                nonce = cipher.nonce
                cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
                plaintext = cipher.decrypt(body)
                try:
                    print("The message is authentic:", plaintext)
                except ValueError:
                    print("Key incorrect or message corrupted")
        channel.basic_consume(callback,queue='ist411', no_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
except Exception as e:
        print(e)

