from os.path import dirname

from manim import *
from code_video import CodeScene

example_dir = dirname(__file__)

REGULAR_FONT_AWESOME = f"{example_dir}/resources/font-awesome/svgs/regular"
SOLID_FONT_AWESOME = f"{example_dir}/resources/font-awesome/svgs/solid"
BRANDS_FONT_AWESOME = f"{example_dir}/resources/font-awesome/svgs/brands"


def get_svg_object(icon_file: str):
    return SVGMobject(icon_file)


class SvgLoadTransform(CodeScene):
    def construct(self):
        self.camera.background_color = WHITE
        svg = SVGMobject(f"{example_dir}/resources/app.svg")
        self.play(Create(svg))
        self.play(svg.animate.scale(0.3).to_edge(UL))
        company_label = Text("DeskRiders", color=BLACK).scale(0.5).next_to(svg, RIGHT)
        self.play(Write(company_label))

        self.play(Create(get_svg_object(f"{REGULAR_FONT_AWESOME}/bell.svg")))

        self.wait(1)
