import paho.mqtt.client as mqtt
from collections import deque

class MtlClient:

    def __init__(self, msg_stack):
        clientName = 'MQTT_MTL_Client'
        hostName = 'mqtt.cgmu.io'
        # self.heartbeatTopic = 'worldcongress2017/pilot_resologi/odtf1/ca/qc/mtl/mobil/infra/gateway/ipc0/gat-00000-01/heartbeat'
        self.heartbeatTopic = topic
        print('Creating a new client named test')
        self.client = mqtt.Client(clientName)
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.message_stack = msg_stack

        print('Connection to Montreal Mobility')
        self.client.connect(hostName)


    def start_client(self):
        self.client.loop_start()

    def stop_client(self):
        self.client.loop_stop()

    def on_message(self, client, userdate, message):
        print(f'Queue size : {len(self.message_stack)} Received the message{message.payload} on the topic: {message.topic}')
        self.message_stack.append(message.topic)

    def get_latest_message(self):
        print(f'Queue size : {len(self.message_stack)}')
        return self.message_stack.pop()

    def on_connect(self, client, userdata, flags, rc):
        print('Connected to Montreal Mobility with result code ' + str(rc))
        print('Listening to topic Heartbeat')
        client.subscribe(self.heartbeatTopic)
