import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))

channel = connection.channel()


def callback(ch, method, properties, body):
    print("Отримано: {}".format(body))
    time.sleep(str(body).count('.'))
    print("Виконано")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()