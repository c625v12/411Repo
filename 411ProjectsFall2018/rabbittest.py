import json, pika

try:
   print("Connecting to Localhost Queue")
   connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.145'))
   channel = connection.channel()
   print("Channel Connected")
   channel.queue_declare(queue='IST411')
   channel.basic_publish(exchange='', routing_key='IST411', body='Mostafa is a bitch')
   print(" [x] Sent 'msg!")
   connection.close()
except Exception as e:
   print(e)
