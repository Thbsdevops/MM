from kafka import KafkaProducer
bootstrap_servers = ['localhost:9092']
topicName = 'Sample_producer_topic'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()
#producer.send(topicName, b'Hello World!!!!!!!!')
ack = producer.send(topicName, 'Hello World!!!!!!!!')
metadata = ack.get()
print(metadata.topic)
print(metadata.partition)
