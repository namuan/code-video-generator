from os.path import dirname

from manim import DOWN
from manim import Text
from manim import UP
from manim.animation.creation import Create

from code_video import AutoScaled
from code_video import CodeScene
from code_video import SequenceDiagram
from code_video.widgets import DEFAULT_FONT


class SequenceDiagramsScene(CodeScene):
    def construct(self):
        example_dir = dirname(__file__)
        self.add_background(f"{example_dir}/resources/blackboard.jpg")
        diagram = AutoScaled(SequenceDiagram())
        browser, web, app = diagram.add_objects("Browser", "Web", "App")

        browser.to(web, "Make a request")
        web.to(app, "Do a quick thing")
        web.to(app, "Retrieve a json object")
        app.to(app, "Call itself")
        app.note("Do lots and lots and lots of thinking")
        app.to(web, "Value from db")
        web.to(browser, "HTML response")

        title = Text("Sequence Diagram", font=DEFAULT_FONT, font_size=24)
        title.to_edge(UP)
        self.add(title)
        diagram.next_to(title, DOWN)

        self.play(Create(diagram))
        for interaction in diagram.get_interactions():
            self.play(Create(interaction))

        self.wait(5)
