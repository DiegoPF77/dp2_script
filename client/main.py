import json
import os
import time
import pandas as pd
import random
from confluent_kafka import Producer


user_id=1 #os.getenv('USER_ID')
topic_id=2 #os.getenv('TOPIC_ID')
time_lapse=3 #int(os.getenv('TIME_ID'))

config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}
producer = Producer(config)

TOPIC_ID = 'heart_rate'

counter=0
lines=[]

def generatedata():
    global counter
    counter=counter+1
    if counter>=len(lines):
        counter=0
    data={}
    data["userid"]=user_id
    data["timestamp"]=int(time.time())
    data["heart_rate"]=lines[counter]*100+random.randint(0,100)
    return json.dumps(data)

def senddata():
    producer.produce(topic=TOPIC_ID, value=generatedata(), key=key)
    producer.flush()

count=0
with open('client/data/data.csv', 'r') as file:
    lines = file.readlines()
    key = str(count)
    lines = [float(line.strip()) for line in lines]




while True:
    senddata()
    time.sleep(time_lapse)