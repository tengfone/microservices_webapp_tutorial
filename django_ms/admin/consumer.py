# amqps://vkmgksap:TTg88Al9L4Yl5mAjNOdn_JllIL2QTH2X@poodle.rmq2.cloudamqp.com/vkmgksap

from products.models import Product
import pika
import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()


params = pika.URLParameters(
    'amqps://vkmgksap:TTg88Al9L4Yl5mAjNOdn_JllIL2QTH2X@poodle.rmq2.cloudamqp.com/vkmgksap')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(
    queue="admin", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
