from confluent_kafka.admin import AdminClient, NewTopic

a = AdminClient({'bootstrap.servers': 'kafka:9092','debug': 'broker,admin'})

new_topics = [NewTopic(topic, num_partitions=3, replication_factor=1) for topic in ["coachs2", "abdata"]]
# Note : Dans un scénario de production multi-clusters, il est plus habituel d'utiliser un facteur de réplication de 3 pour la durabilité.

# Appelez create_topics pour créer des sujets de manière asynchrone. Un dict # de <topic,future> est renvoyé.
fs = a.create_topics(new_topics)

# Attendre la fin de chaque opération.
for topic, f in fs.items():
    try:
        f.result()  # Le résultat en lui-même est None
        print("Topic {} created".format(topic))
    except Exception as e:
        print(e)
        print("Failed to create topic {}: {}".format(topic, e))