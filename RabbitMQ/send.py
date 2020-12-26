import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(50):
    channel.basic_publish(exchange="",
                           routing_key='hello',
                           body='Checker{}'.format(i))

    print(i, "Повідомлення було відправлене!")

connection.close()