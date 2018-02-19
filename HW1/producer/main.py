import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit',
                                                               port=5672))
channel = connection.channel()
channel.queue_declare(queue='msg')


with open('input') as r:
    for line in r:
        channel.basic_publish(exchange='',
                              routing_key='msg',
                              body=line)
        print(f'Pushed string {line}')

connection.close()