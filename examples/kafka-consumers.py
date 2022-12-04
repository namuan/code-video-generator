"""
Demonstrating Kafka consumer re-balancing

Generate high resolution video
$ manim render -qh -p examples/kafka-consumers.py

Generate low resolution video
$ manim render -ql -p examples/kafka-consumers.py

"""
from manim import *

from code_video import TextBox, Connection
from code_video.extended_widgets import Box

CUSTOM_FONT = "Consolas"


class KafkaScene(Scene):
    def construct(self):
        self.display("Kafka: Re-balancing in consumer groups")
        self.heading("Producer sending messages to a topic with 3 partitions")

        producer = self.setup_producer()

        topic = self.setup_topic()
        partitions = self.setup_partitions(topic)

        self.heading("One consumer in a consumer group")

        consumer_group = self.setup_consumer_group(group_title="Consumer Group 1", edge_placement=UR)
        consumers_in_group_1 = []
        consumer_1 = self.setup_consumer_in_group(consumer_group)
        consumers_in_group_1.append(consumer_1)

        self.connect_producer_to_partition(partitions, producer)

        self.heading("Consumer will receive messages from all partitions")
        partition_0_to_consumer_a = Connection(
            partitions[0],
            consumers_in_group_1[0],
            text_attrs={"font": CUSTOM_FONT, "font_size": 14},
        )
        self.play(Create(partition_0_to_consumer_a))
        partition_1_to_consumer_a = Connection(
            partitions[1],
            consumers_in_group_1[0],
            text_attrs={"font": CUSTOM_FONT, "font_size": 14},
        )
        self.play(Create(partition_1_to_consumer_a))
        partition_2_to_consumer_a = Connection(
            partitions[2],
            consumers_in_group_1[0],
            text_attrs={"font": CUSTOM_FONT, "font_size": 14},
        )
        self.play(Create(partition_2_to_consumer_a))

        self.heading("Now we add another consumer in the same consumer group")
        consumer_2 = TextBox(
            text=f"Consumer 2",
            text_attrs={"font": CUSTOM_FONT, "font_size": 14},
        )
        consumer_2.next_to(consumer_group, UP, buff=-3.0)
        self.play(FadeIn(consumer_2))
        consumers_in_group_1.append(consumer_2)

        self.heading("Adding consumer in a consumer group will trigger re-balancing")
        self.play(FadeOut(partition_2_to_consumer_a))
        self.heading("Kafka will re-assign partitions and both consumers will start receiving messages")
        partition_2_to_consumer_a = Connection(
            partitions[2],
            consumers_in_group_1[1],
            text_attrs={"font": CUSTOM_FONT, "font_size": 14},
        )
        self.play(Create(partition_2_to_consumer_a))

        self.heading("Adding another consumer group")
        consumer_group_2 = self.setup_consumer_group(group_title="Consumer Group 2", edge_placement=DR, box_height=2.0)
        consumers_in_group_2 = []
        consumer_gr_2_1 = self.setup_consumer_in_group(consumer_group_2)
        consumers_in_group_2.append(consumer_gr_2_1)

        # Single consumer in the new consumer group gets all the messages
        self.heading("New consumer will receive messages from all partitions")
        partition_0_to_consumer_a = Connection(
            partitions[0],
            consumers_in_group_2[0],
            arrow_color=YELLOW_A,
            text_attrs={"font": CUSTOM_FONT, "font_size": 14},
        )
        self.play(Create(partition_0_to_consumer_a))
        partition_1_to_consumer_a = Connection(
            partitions[1],
            consumers_in_group_2[0],
            arrow_color=YELLOW_A,
            text_attrs={"font": CUSTOM_FONT, "font_size": 14},
        )
        self.play(Create(partition_1_to_consumer_a))
        partition_2_to_consumer_a = Connection(
            partitions[2],
            consumers_in_group_2[0],
            arrow_color=YELLOW_A,
            text_attrs={"font": CUSTOM_FONT, "font_size": 14},
        )
        self.play(Create(partition_2_to_consumer_a))
        self.wait(2)
        self.display("Thanks for watching! \n@deskriders_twt")

    def display(self, display_text):
        self.clear()
        title = Text(
            display_text,
            font=CUSTOM_FONT
        )
        title.to_edge(LEFT)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

    def heading(self, text):
        header = Text(text, font=CUSTOM_FONT, font_size=20).scale(1.1)
        header.to_edge(DOWN)
        self.play(Create(header))
        self.wait(1)
        self.play(FadeOut(header))

    def connect_producer_to_partition(self, partitions, producer):
        publish_to_topic = Connection(
            producer,
            partitions[0],
            text_attrs={"font": CUSTOM_FONT, "font_size": 14},
        )
        self.play(Create(publish_to_topic))

    def setup_consumer_in_group(self, consumer_group, consumer_title=f"Consumer 1", buffer=-1.5):
        consumer = TextBox(
            text=consumer_title,
            text_attrs={"font": CUSTOM_FONT, "font_size": 14},
        )
        consumer.next_to(consumer_group, UP, buff=buffer)
        self.play(FadeIn(consumer))
        return consumer

    def setup_consumer_group(self, group_title, edge_placement, box_height=3.0):
        consumer_group = Box(
            text=group_title,
            height=box_height,
            width=2.0,
            text_alignment_to_border=DOWN,
            text_attrs={
                "font": CUSTOM_FONT, "font_size": 16
            },
        )
        consumer_group.to_edge(edge_placement)
        self.play(FadeIn(consumer_group))
        return consumer_group

    def setup_partitions(self, topic):
        partitions = []
        for i in range(1, 4):
            partition = TextBox(
                text=f"Partition {i}",
                text_attrs={"font": CUSTOM_FONT, "font_size": 14},
            )
            partition.next_to(topic, UP, buff=i * -1.5)
            self.play(FadeIn(partition))
            partitions.append(partition)
        return partitions

    def setup_topic(self):
        topic = Box(
            text="Topic",
            height=5.0,
            width=2.0,
            text_alignment_to_border=UP,
            text_attrs={
                "font": CUSTOM_FONT, "font_size": 16
            },
        )
        self.play(FadeIn(topic))
        return topic

    def setup_producer(self):
        producer = TextBox(
            text="Producer",
            text_attrs={"font": CUSTOM_FONT, "font_size": 14},
        )
        producer.to_edge(LEFT)
        self.play(FadeIn(producer))
        return producer
