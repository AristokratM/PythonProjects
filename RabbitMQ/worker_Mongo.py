import pika
import pymongo
import json
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))

channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

client = pymongo.MongoClient('localhost', 27017)
db = client['lab7']
users_collection = db['users']


def callback(ch, method, properties, body):
    json_message = json.loads(body.decode("utf-8"))
    print(json_message)
    print("ID повідомлення в БД {}".format(users_collection.insert_one(json_message).inserted_id))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()