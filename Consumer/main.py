from kafka import KafkaConsumer
import threading
from json import loads
from prometheus_client import start_http_server, Counter

# Kafka Configuration (Replace with your Ubuntu VM's IP)
KAFKA_BOOTSTRAP_SERVERS = "192.168.124.181:9092"  # e.g., "192.168.1.100:9092"
KAFKA_EXPLORE_TOPIC = "exploreTopic"
KAFKA_BUY_TOPIC = 'buyTopic'

# Prometheus Metrics Setup
explore_counter = Counter('explore_messages_total', 'Total number of explore messages received')
buy_counter = Counter('buy_messages_total', 'Total number of buy messages received')

# Kafka Consumer Setup
consumer = KafkaConsumer(
    KAFKA_EXPLORE_TOPIC, KAFKA_BUY_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    auto_offset_reset='earliest',
    group_id='multi-topic-group',
    enable_auto_commit=True,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

def consume_messages():
    for message in consumer:
        if message.topic == KAFKA_EXPLORE_TOPIC:
            explore_counter.inc()
        elif message.topic == KAFKA_BUY_TOPIC:
            buy_counter.inc()

        print(f"Python Consumer Received: {message.topic}")

if __name__ == '__main__':
    start_http_server(8000)
    consume_messages()