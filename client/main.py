import json
import os
import time
import pandas as pd
import random

user_id=os.getenv('USER_ID')
topic_id=os.getenv('TOPIC_ID')
time_lapse=int(os.getenv('TIME_ID'))

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

    # Coloca el código para enviar los datos a tu sistema de mensajería
    # Utiliza la variable topic id para especificar el topico destino
    print(generatedata())


with open('data/data.csv', 'r') as file:
    lines = file.readlines()

lines = [float(line.strip()) for line in lines]
    
print(lines)


while True:
    senddata()
    time.sleep(time_lapse)

