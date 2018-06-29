import pulsar
import csv
f = open("Iris.csv", "rb") 
reader = csv.reader(f)

client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer('persistent://sample/standalone/ns1/my-topic')

# for i in range(10):
#     try: 
#         producer.send('hello-Pulsar-%d' % i)
#     except Exception as e:
#         print("Failed to send message: %s", e)
for row in reader:
    d = json.dumps(row)
    producer.send(d)

producer.close()
