import paho.mqtt.client as mqtt


def on_message(client, userdate, message):
    print('Received the message' + str(message.payload) + 'on the topic: ' + message.topic)


def on_connect(client, userdata, flags, rc):
    print('Connected to Montreal Mobility with result code ' + str(rc))
    print('Listening to topic Heartbeat')
    client.subscribe(heartbeatTopic)


clientName = 'test'
hostName = 'mqtt.cgmu.io'
heartbeatTopic = 'worldcongress2017/pilot_resologi/odtf1/ca/qc/mtl/mobil/infra/gateway/ipc0/gat-00000-01/heartbeat'
print('Creating a new client named test')
client = mqtt.Client(clientName)
client.on_message = on_message
client.on_connect = on_connect

print('Connection to Montreal Mobility')
client.connect(hostName)

client.loop_forever()