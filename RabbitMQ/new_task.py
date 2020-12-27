import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))

channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
message = input() or '{"login":"Test", "password":"12345"}'
channel.basic_qos(prefetch_count=1)
channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print("Відправив повідомлення {}".format(message))
