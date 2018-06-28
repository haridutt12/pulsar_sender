import pulsar
import json

client = pulsar.Client('pulsar://localhost:6650')
data = {}

producer = client.create_producer('persistent://sample/standalone/ns1/my-topic')

for i in range(100):
    try:
        data['i'] = 'hello-Pulsar'
        json_data = json.dumps(data)
        producer.send(json_data)
    except Exception as e:
        print("Failed to send message: %s", e)

producer.close()
