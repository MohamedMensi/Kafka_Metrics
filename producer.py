import json
import time
import csv
from kafka import KafkaProducer


def producer():
    producer = KafkaProducer (
    bootstrap_servers=['your address ip:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    with open('C:/Users/chaou/Desktop/projet3/data.csv') as file:

        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            producer.send(topic='my_topic', value=row)
            time.sleep(1)
            print(row)
            producer.flush()

if __name__ == '__main__':

    #while 1 == 1:
    producer()
