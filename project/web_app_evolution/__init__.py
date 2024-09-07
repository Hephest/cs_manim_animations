from manim import *


def use_appleberry_font():
    appleberry_font = TexTemplate()
    appleberry_font.add_to_preamble(r"\usepackage{appleberry}")


class WebAppBuildingBlocks1(Scene):
    def construct(self):
        use_appleberry_font()

        html_text = Text("HTML", color=WHITE, font="appleberry").scale(0.8)
        html_description = Text("Гіпертекстовий документ", color=WHITE, font="appleberry").scale(0.5)
        html_content = VGroup(html_text, html_description).arrange(DOWN, buff=0.1)
        html_block = SurroundingRectangle(html_content, buff=0.3, color=WHITE, fill_opacity=0.2, corner_radius=0.2)
        html = VGroup(html_block, html_content)

        html.move_to(ORIGIN)

        self.play(FadeIn(html))
        self.wait(2)

        self.play(html.animate.move_to(DOWN * 3))
        self.wait(1)

        image = ImageMobject("screenshots/web_app_evolution/001.png")
        image.scale_to_fit_width(config.frame_width * 0.9)
        image.move_to(UP * 0.5)

        self.play(FadeIn(image))
        self.wait(5)
        self.play(FadeOut(image))
        self.wait(0.5)

        self.play(html.animate.move_to(ORIGIN))



class WebAppBuildingBlocks2(Scene):
    def construct(self):
        use_appleberry_font()

        html_text = Text("HTML", color=WHITE, font="appleberry").scale(0.8)
        html_description = Text("Гіпертекстовий документ", color=WHITE, font="appleberry").scale(0.5)
        html_content = VGroup(html_text, html_description).arrange(DOWN, buff=0.1)
        html_block = SurroundingRectangle(html_content, buff=0.3, color=WHITE, fill_opacity=0.2, corner_radius=0.2)
        html = VGroup(html_block, html_content)

        html.move_to(ORIGIN)

        self.play(FadeIn(html))
        self.wait(2)
        
        self.play(html.animate.move_to(ORIGIN + UP * 1.1))

        css_text = Text("CSS", color=WHITE, font="appleberry").scale(0.8)
        css_description = Text("Каскадні таблиці стилів", color=WHITE, font="appleberry").scale(0.5)
        css_content = VGroup(css_text, css_description).arrange(DOWN, buff=0.1)
        css_block = SurroundingRectangle(css_content, buff=0.3, color=WHITE, fill_opacity=0.2, corner_radius=0.2)
        css = VGroup(css_block, css_content)

        css.next_to(html, DOWN, buff=0.2)

        self.play(FadeIn(css))
        self.wait(1)

        brace = Brace(VGroup(html, css), direction=RIGHT)
        brace_label = Text("Static Page", font="appleberry").scale(0.6)
        brace_description = Text("Статична сторінка", font="appleberry").scale(0.4)
        brace_text = VGroup(brace_label, brace_description).arrange(DOWN, buff=0.1).next_to(brace, RIGHT)
 
        self.play(
            GrowFromCenter(brace),
        )
        self.wait(0.2)
        self.play(Write(brace_text))
        self.wait(3)
        self.play(FadeOut(brace), FadeOut(brace_text))
        self.wait(2)


class WebAppBuildingBlocks3(Scene):
    def construct(self):
        use_appleberry_font()

        html_text = Text("HTML", color=WHITE, font="appleberry").scale(0.8)
        html_description = Text("Гіпертекстовий документ", color=WHITE, font="appleberry").scale(0.5)
        html_content = VGroup(html_text, html_description).arrange(DOWN, buff=0.1)
        html_block = SurroundingRectangle(html_content, buff=0.3, color=WHITE, fill_opacity=0.2, corner_radius=0.2)
        html = VGroup(html_block, html_content)

        css_text = Text("CSS", color=WHITE, font="appleberry").scale(0.8)
        css_description = Text("Каскадні таблиці стилів", color=WHITE, font="appleberry").scale(0.5)
        css_content = VGroup(css_text, css_description).arrange(DOWN, buff=0.1)
        css_block = SurroundingRectangle(css_content, buff=0.3, color=WHITE, fill_opacity=0.2, corner_radius=0.2)
        css = VGroup(css_block, css_content)

        html.move_to(ORIGIN + UP * 1.1)

        js_text = Text("JS", color=WHITE, font="appleberry").scale(0.8)
        js_description = Text("Інтерактивні сценарії", color=WHITE, font="appleberry").scale(0.5)
        js_content = VGroup(js_text, js_description).arrange(DOWN, buff=0.1)
        js_block = SurroundingRectangle(js_content, buff=0.3, color=WHITE, fill_opacity=0.2, corner_radius=0.2)
        js = VGroup(js_block, js_content)

        css.next_to(html, DOWN, buff=0.2)
        js.next_to(css, DOWN, buff=0.2)

        self.add(html, css)
        
        self.play(
            FadeIn(js),
            html.animate.move_to(ORIGIN + UP * 1.6),
            css.animate.move_to(ORIGIN),
            js.animate.move_to(ORIGIN + DOWN * 1.6),
            run_time=1
        )
        self.wait(1)

        brace = Brace(VGroup(html, css, js), direction=RIGHT)
        brace_label = Text("Dynamic Page", font="appleberry").scale(0.6)
        brace_description = Text("Динамічна сторінка", font="appleberry").scale(0.4)
        brace_text = VGroup(brace_label, brace_description).arrange(DOWN, buff=0.1).next_to(brace, RIGHT)
 
        self.play(
            GrowFromCenter(brace),
        )
        self.wait(0.2)
        self.play(Write(brace_text))
        self.wait(3)
        self.play(FadeOut(brace), FadeOut(brace_text))
        self.wait(2)