from manim import *

from code_video import CodeScene


class HighlightSnippets(CodeScene):
    def display(self, display_text):
        self.clear()
        title = Text(
            display_text,
            font="Source Code Pro",
        )
        title.to_edge(LEFT)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

    def construct(self):
        code_file = Path(
            "~/workspace/dev-rider-codesnippets/kt-snippets/app/src/main/kotlin/kt/snippets").expanduser() / "OpenAiCompletions.kt"
        self.animate_code_comments(
            code_file.as_posix(),
            keep_comments=False,
            title="Using OpenAI's GPT-3 API",
            title_font="Source Code Pro",
            title_font_size=30,
            reset_at_end=True,
            line_spacing=0.5,
            font_size=24,
            font="Input Mono",
            comment_font="Input Mono Compressed",
            comment_font_size=20,
        )
        self.wait(5)
        self.display("Thanks for watching! \nhttps://deskriders.dev")
