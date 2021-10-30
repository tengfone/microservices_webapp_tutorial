# amqps://vkmgksap:TTg88Al9L4Yl5mAjNOdn_JllIL2QTH2X@poodle.rmq2.cloudamqp.com/vkmgksap

import pika,json

params = pika.URLParameters(
    'amqps://vkmgksap:TTg88Al9L4Yl5mAjNOdn_JllIL2QTH2X@poodle.rmq2.cloudamqp.com/vkmgksap')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key="admin",
                          body=json.dumps(body), properties=properties)
