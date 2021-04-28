from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task
from .mtl_client import MtlClient
import paho.mqtt.client as mqtt
from collections import deque
from .topics import selectedTopic
from .agregators import *
import pickle
from queue import Queue
import datetime

TIMEOUT = 1

TESTQUEUE = Queue()

msg_stack = deque()
msg_list = Queue()
messages = Queue()
stats = None
heartbeatTopic = 'worldcongress2017/pilot_resologi/odtf1/ca/qc/mtl/mobil/infra/gateway/ipc0/gat-00000-01/heartbeat'

save_file = None

def on_message(client, userdata, message):
    print('Received the message' + str(message.payload) + 'on the topic: ' + message.topic)
    msg_stack.append(message)

def save_data(file, message):
    file.write(str(message) + "\n")

def check_health_on_connect(msg_topic):
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        msg_topic.put("connected")
        for i in selectedTopic:
            client.subscribe(i)
            
    return on_connect


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    for i in selectedTopic:
        client.subscribe(i)

def topic_to_multiple_topics(topics):
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        for i in topics:
            client.subscribe(i)
    return on_connect

def create_on_connect(topic_name):

    def connect(client, userdata, flags, rc):
        print('Connected to Montreal Mobility with result code ' + str(rc))
        print('Listening to topic Heartbeat')
        client.subscribe(topic_name)

    return connect

@shared_task
def start_client():
    clientName = 'test'
    hostName = 'mqtt.cgmu.io'
    print('Creating a new client named test')
    client = mqtt.Client(clientName)
    client.on_message = on_message
    client.on_connect = on_connect

    print('Connection to Montreal Mobility')
    client.connect(hostName)

    client.loop_start()

def check_health():
    clientName = 'test'
    hostName = 'mqtt.cgmu.io'
    print('Creating a new client named test')
    msg_q = Queue()
    client = mqtt.Client(clientName)
    client.on_message = on_message
    client.on_connect = check_health_on_connect(msg_q)

    print('Connection to Montreal Mobility')
    client.connect(hostName)

    client.loop_start()
    time.sleep(5)
    client.loop_stop()

    print(f"msgs : {list(msg_q.queue)}")

    return not msg_q.empty()

mtl: MtlClient = None
msg_stack = deque()



@shared_task
def run_mtl_client(topic):
    mtl = MtlClient(topic, msg_stack)
    mtl.start_client()

@shared_task
def get_latest_message():
    return msg_stack.pop()

def get_msg():
    return mtl.get_latest_message()

def compute_on_message(agregators: list):
    def on_message(client, userdata, message):

        save_file = open("save_file.txt", "a+")

        print(f'Message: {message.payload} topic: {message.topic}')
        val = parse_topic_msg(message.payload)["Value"]
        if isinstance(val, int) or isinstance(val, float):
            msg_list.put(val)
            messages.put(message)
            save_file.write(str(message.payload) + "\n")
            stats = Queue()
            for ag_func in agregators:
                stats.put(ag_func(list(msg_list.queue)))
    
        print(f"Statistics : {list(stats.queue)}")

    return on_message

def serizalise_msg_stack():
    pickle.dump(messages, open( "topic_msgs/msgs.p", "wb" ) )

def get_saved_msg_stack():
    return pickle.load(open("topic_msgs/msgs.p", "rb"))


@shared_task
def compute_stats_task(topics: list, agregator_names: list):
    agregators = []
    for ag in agregator_names:
        agregators.append(agregator_map[ag])

    clientName = 'test'
    hostName = 'mqtt.cgmu.io'
    print('Creating a new client named test')
    client = mqtt.Client(clientName)
    client.on_message = compute_on_message(agregators)
    client.on_connect = topic_to_multiple_topics(topics)

    print('Connection to Montreal Mobility')
    client.connect(hostName)

    client.loop_start()

def compute_stats_file_task(fileName: str):
    file = open(fileName, "r")
    lines = file.readlines()
    value_list = []

    for line in lines:
        if line[2:] == "b'" and line[-1:] == "'":
            value_list.append(parse_topic_msg(line[2: -4:])["Value"])
        else:
            value_list.append(parse_topic_msg(line)["Value"])

    stats = Queue()

    for ag_func in agregator_map.values():
        stats.put(ag_func(value_list))

    print(f"Statistics : {list(stats.queue)}")

    return list(stats.queue)

def compute_stats_file_upload_task(f):
    with open('temp_name.txt', 'wb+') as destination:
        destination.write(f)

    file = open('temp_name.txt', "r")
    lines = file.readlines()
    value_list = []

    for line in lines:
        if line[2:] == "b'" and line[-1:] == "'":
            value_list.append(parse_topic_msg(line[2: -4:])["Value"])
        else:
            value_list.append(parse_topic_msg(line)["Value"])

    stats = Queue()

    for ag_func in agregator_map.values():
        stats.put(ag_func(value_list))

    print(f"Statistics : {list(stats.queue)}")

    return str(list(stats.queue))




