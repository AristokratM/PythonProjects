import pyodbc
import json
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\1\Documents\lab7.accdb;')
cursor = conn.cursor()

def callback(ch, method, properties, body):
    json_message = json.loads(body)
    print(json_message)
    cursor.execute(
        '''INSERT INTO Users (login,password) VALUES('{}','{}')'''.format(json_message['login'],json_message['password'])
    )
    conn.commit()
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Повідомлення записано до БД")

channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()
conn.close()
