from manim import Rectangle

from code_video.widgets import BoxBase


class Box(BoxBase):
    def __init__(self, text, height, width, text_alignment_to_border, text_attrs, **kwargs):
        super(Box, self).__init__(text=text, text_attrs=text_attrs, **kwargs)
        self._box(
            text=text,
            border_builder=lambda _: Rectangle(
                height=height + 0.2,
                width=width + 0.2
            ),
            text_alignment_to_border=text_alignment_to_border,
        )
