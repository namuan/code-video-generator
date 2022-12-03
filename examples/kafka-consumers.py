from manim import DOWN
from manim import FadeIn
from manim import Scene

from code_video.extended_widgets import Box


class KafkaScene(Scene):
    def construct(self):
        box1 = Box(
            text="Kafka Consumer Group",
            height=5.0,
            width=2.0,
            text_alignment_to_border=DOWN,
            text_attrs={
                "font_size": 16,
                "font": "Consolas"
            },
        )

        self.play(FadeIn(box1))

        self.wait(5)
