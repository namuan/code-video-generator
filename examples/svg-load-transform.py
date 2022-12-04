from os.path import dirname

from manim import *
from code_video import CodeScene

example_dir = dirname(__file__)

class SvgLoadTransform(CodeScene):
    def construct(self):
        # load svg from resources/app.svg into manim object
        svg = SVGMobject(f"{example_dir}/resources/app.svg")
        self.play(Create(svg))
        self.play(svg.animate.scale(0.3).to_edge(UL))
        company_label = Text("DeskRiders", font="Montserrat").scale(0.5).next_to(svg, RIGHT)
        self.play(Create(company_label))

        # Wait 5 seconds before finishing
        self.wait(1)
