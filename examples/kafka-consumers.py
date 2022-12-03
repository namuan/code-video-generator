from manim import FadeIn
from manim import Create
from manim import Scene
from manim.constants import *

from code_video import TextBox, Connection
from code_video.extended_widgets import Box


class KafkaScene(Scene):
    def construct(self):
        producer = TextBox(
            text="Producer",
            text_attrs={"font_size": 14},
        )
        producer.to_edge(LEFT)
        self.play(FadeIn(producer))

        topic = Box(
            text="Topic",
            height=5.0,
            width=2.0,
            text_alignment_to_border=UP,
            text_attrs={
                "font_size": 16
            },
        )
        self.play(FadeIn(topic))
        partitions = []
        for i in range(1, 4):
            partition = TextBox(
                text=f"Partition {i}",
                text_attrs={"font_size": 14},
            )
            partition.next_to(topic, UP, buff=i * -1.5)
            self.play(FadeIn(partition))
            partitions.append(partition)

        consumer_group = Box(
            text="Kafka Consumer Group",
            height=5.0,
            width=2.0,
            text_alignment_to_border=DOWN,
            text_attrs={
                "font_size": 16
            },
        )
        consumer_group.to_edge(RIGHT)
        self.play(FadeIn(consumer_group))
        consumers = []
        for i in range(1, 3):
            consumer = TextBox(
                text=f"Consumer {i}",
                text_attrs={"font_size": 14},
            )
            consumer.next_to(consumer_group, UP, buff=i * -1.5)
            self.play(FadeIn(consumer))
            consumers.append(consumer)

        publish_to_topic = Connection(
            producer,
            partitions[0],
            "Publishes messages to topic",
            text_attrs={"font_size": 14},
        )
        self.play(Create(publish_to_topic))

        # Single consumer in the consumer group gets all the messages
        partition_0_to_consumer_a = Connection(
            partitions[0],
            consumers[0],
            "0",
            text_attrs={"font_size": 14},
        )
        self.play(Create(partition_0_to_consumer_a))
        partition_1_to_consumer_a = Connection(
            partitions[1],
            consumers[0],
            "1",
            text_attrs={"font_size": 14},
        )
        self.play(Create(partition_1_to_consumer_a))
        partition_2_to_consumer_a = Connection(
            partitions[2],
            consumers[0],
            "2",
            text_attrs={"font_size": 14},
        )
        self.play(Create(partition_2_to_consumer_a))

        self.wait(5)
