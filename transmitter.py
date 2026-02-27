from confluent_kafka import Producer
import json

config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'región-sensorial-01'
}

producer = Producer(config)

def emitir_impulso(region, valor):
    mensaje = {'data': valor, 'metadata': {'type': 'asociativo'}}
    producer.produce('impulso-cerebral',
                     key=region,
                     value=json.dumps(mensaje))
    producer.flush()
    print(f"Propagando señal desde {region}...")

emitir_impulso('Corteza_Visual', 0.95)