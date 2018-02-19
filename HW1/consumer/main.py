import pika
import psycopg2

rabbit_conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit',
                                                                port=5672))
channel = rabbit_conn.channel()
channel.queue_declare(queue='msg')

db_conn = psycopg2.connect("dbname=db user=db password=db host=db port=5432")


def db_init():
    cur = db_conn.cursor()
    cur.execute("CREATE TABLE received (body TEXT)")
    db_conn.commit()


def callback(ch, method, properties, body):
    cur = db_conn.cursor()
    str_body = body.decode()
    cur.execute(f"INSERT INTO received(body) VALUES ('{str_body}')")
    db_conn.commit()
    print(f'Pushed {str_body} to db')



db_init()

channel.basic_consume(callback,
                      queue='msg',
                      no_ack=True,
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
