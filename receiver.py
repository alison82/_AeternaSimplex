from confluent_kafka import Consumer

config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'procesamiento-central',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(config)
consumer.subscribe(['impulso-cerebral'])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None: continue
        print(f"Recibido en Asociación: {msg.value().decode('utf-8')} de {msg.key().decode('utf-8')}")
except KeyboardInterrupt:
    consumer.close()