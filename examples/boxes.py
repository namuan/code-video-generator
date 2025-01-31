from manim import DOWN
from manim import FadeIn
from manim import LEFT
from manim import RIGHT
from manim import Scene
from manim.animation.creation import Create

from code_video import Connection
from code_video import TextBox


class BoxesScene(Scene):
    def construct(self):

        comp1 = TextBox("Component A", shadow=False)
        comp2 = TextBox("Component B", shadow=False)
        comp3 = TextBox("Component C", shadow=False)
        comp1.to_edge(LEFT)
        comp2.next_to(comp1, DOWN, buff=1)
        comp3.next_to(comp1, RIGHT, buff=4)
        arrow1 = Connection(comp2, comp1, label="Do something")
        arrow2 = Connection(comp1, comp3, label="Another thing")

        self.play(FadeIn(comp2))
        self.play(Create(arrow1))
        self.play(FadeIn(comp1))
        self.play(Create(arrow2))
        self.play(FadeIn(comp3))

        self.wait(5)
