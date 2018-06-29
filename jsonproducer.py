import pulsar
import json

client = pulsar.Client('pulsar://localhost:6650')
data = {}

producer = client.create_producer('persistent://sample/standalone/ns1/my-topic')
i=0
while True:
    try:
#        data['i'] = i+1
#        json_data = json.dumps(data)
        i=i+1
        producer.send("%d" %i)
        if i == 1000:
            break
    except Exception as e:
        print("Failed to send message: %s", e)

producer.close()
