import pulsar

client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer('persistent://sample/standalone/ns1/my-topic')

for i in range(10):
    try: 
        producer.send('hello-Pulsar-%d' % i)
    except Exception as e:
        print("Failed to send message: %s", e)

producer.close()
