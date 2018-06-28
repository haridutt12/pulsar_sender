import pulsar
import time
time.sleep(10)
client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('persistent://sample/standalone/ns1/my-topic', 
	       "my-subscription")
fh = open("messages.txt", "a")

while True:
    try:
        msg = consumer.receive(timeout_millis=2000)
        messg = msg.data()
        fh.writelines(messg)
        print("Received message '{0}' id='{1}'".format(msg.data(), 
        msg.message_id()))
        consumer.acknowledge(msg)
    except Exception:
        print("No message recieved in 2 sec")
        break

fh.close()
client.close()
