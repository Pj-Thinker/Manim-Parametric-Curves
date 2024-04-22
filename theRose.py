from manim import *
import numpy as np

# Settings for vertical video output
config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920

class theRose(Scene):
    def construct(self):
        screen_width = config.frame_width
        screen_height = config.frame_height
        border_width = 2
        
        border_rect = Rectangle(
            width=screen_width,
            height=screen_height,
            stroke_width=border_width,
            stroke_color = WHITE
        )

        self.add(border_rect)

        def func(t, k):
            x = np.cos(k*t)*np.cos(t)
            y = np.cos(k*t)*np.sin(t)
            return np.array([x,y,0])
        
        colors = ["#0000ff","#8bff26","#26e9ff","#ff3c00","#ffa600"]

        title = Text("The Rose", font_size=62, weight=BOLD).set_color(RED)
        formula_text = MathTex(r"x = cos(k\theta) \, cos(\theta) \\ y = cos(k\theta) \,sin(\theta)",font_size=54).set_color(BLUE)
        c = MathTex(r"k = \frac{n}{d}",font_size=54).set_color(YELLOW)
        c1 = MathTex(r"k = \frac{n}{d} = \frac{5}{4}",font_size=54) 
        c2 = MathTex(r"k = \frac{n}{d} = \frac{8}{5}",font_size=54)
        c3 = MathTex(r"k = \frac{n}{d} = \frac{7}{3}",font_size=54)
        c4 = MathTex(r"k = \frac{n}{d} = \frac{3}{5}",font_size=54)
        c5 = MathTex(r"k = \frac{n}{d} = \frac{8}{7}",font_size=54)
        c6 = MathTex(r"k = \frac{n}{d} = \frac{4}{6}",font_size=54)
        c7 = MathTex(r"k = \frac{n}{d} = \frac{8}{1}",font_size=54)
        c8 = MathTex(r"k = \frac{n}{d} = \frac{10}{9}",font_size=54)

        cArray = [c1, c2, c3, c4, c5, c6, c7, c8]
        cValuesArray = [5/4, 8/5, 7/3, 3/5, 8/7, 4/6, 8/1, 10/9]

        for item in cArray:
            item[0][6:].set_color(YELLOW)


        cg = VGroup(c, *cArray)
        Full_text = VGroup(title, formula_text, cg)
        Full_text.arrange(DOWN, 0.5, True)
        Full_text.to_edge(UP, buff=1)

        self.play(Write(title), Write(formula_text)) 
        self.play(Indicate(formula_text[0][6]), Indicate(formula_text[0][21]))
        self.play(TransformFromCopy(formula_text, c))


        f1 = Circle(1).set_color_by_gradient(colors).set_stroke(width=2).scale(3).to_edge(DOWN, buff=3)
        self.play(Write(f1))

        for i in range(len(cArray)):
            self.play(ReplacementTransform(c, cArray[i]))
            f2 = ParametricFunction(lambda t: func(t, cValuesArray[i]), t_range = [0, 5*TAU + i*TAU], fill_opacity=0).set_color_by_gradient(colors).set_stroke(width=2).scale(3).to_edge(DOWN, buff=3)
            self.play(ReplacementTransform(f1, f2), Indicate(cArray[i][0][-3:]), run_time=2)
            self.wait(0.5)
            f1 = f2
            c = cArray[i]

        self.wait(3)