from confluent_kafka import Consumer
import json
import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
conf={
    "bootstrap.servers": '198.244.141.48:29092',
    "group.id": 0
    }
#initialiser le topic
topic_name='abdata'
#initialiser le Consumer 
consumer= Consumer(conf)
# Subscribe to topic
consumer.subscribe([topic_name])
# Process messages
total_count = 0
try:
    while True:
        msg = consumer.poll(0.01)
        
        if msg is None:
            # No message available within timeout.
            # Initial message consumption may take up to
            # `session.timeout.ms` for the consumer group to
            # rebalance and start consuming
            #print("Waiting for message or event/error in poll()")
            continue
        elif msg.error():
            logging.warning('error: {}'.format(msg.error()))
        else:
            # Check for Kafka message
            record_key = msg.key()
            record_value = msg.value()
            data = json.loads(record_value)
            Country = data['Country']
            Confirmed= data['Confirmed']
            Deaths= data['Deaths']
            Recovred= data['Recovred']
            logging.warning(Country)
            logging.warning("Consumed record with key {} and value {}, \
                  and updated total count to {}"
                  .format(record_key, record_value, record_value))
except KeyboardInterrupt:
    pass
finally:
    # Leave group and commit final offsets
    consumer.close()
