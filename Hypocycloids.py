from manim import *
import numpy as np

# Settings for vertical video output
config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920

class Hypocycloids(Scene):
    def construct(self):
        title = Text("Hypocycloids", font_size=62, weight=BOLD).set_color(RED)
        Full_text = VGroup(title)
        Full_text.arrange(DOWN, 1, True).to_edge(UP, buff=1)
        self.add(title)

        Acircle = Circle(radius=3.5, color=GRAY, stroke_width=2)
        ShadowCircle = Circle(radius=2.5, stroke_width=0)
        Bcircle = always_redraw(lambda: Circle(radius=1, color=RED, stroke_width=2).move_to(ShadowCircle.point_at_angle(0*PI/180)))

        GCircles = VGroup(Acircle,Bcircle,ShadowCircle)
        GCircles.to_edge(DOWN, buff=3)

        self.play(Create(GCircles))

        ALine = LabeledLine(label="a", label_position=0.75, font_size=72, label_color=YELLOW, label_frame=False, start=Acircle.get_center(), end = Acircle.point_at_angle(45*PI/180), stroke_width=1, buff=0)

        BLine = LabeledLine(label="b", label_position=0.5, font_size=64, label_color=YELLOW, label_frame=False, start=Bcircle.get_center(), end = Bcircle.point_at_angle(0*PI/180), stroke_width=1, buff=0)

        self.play(Write(ALine), Write(BLine))
        self.wait(0.25)

        def drawHypocloids(ACradius, BCradius, angleMultiplier=1, runTimeMultiplier=2, rotationDirection=-1, BCircleSlip=1, clear=False):
            colors = ["#0000ff","#8bff26","#26e9ff","#ff3c00","#ffa600"]
            if BCradius != 1:
                rRatio = MathTex(fr"\frac{{a}}{{b}} = {ACradius}/{BCradius}",font_size=54).to_edge(UP, buff=3)
            else:
                rRatio = MathTex(fr"\frac{{a}}{{b}} = {ACradius}",font_size=54).to_edge(UP, buff=3)
            rRatio[0][4:].set_color(YELLOW)
            angleDeg = ValueTracker(0)
            totalAngle = 360 * BCradius * angleMultiplier
            runTime = runTimeMultiplier * totalAngle / 360
            
            # To constrain the bigger circle inside the screen
            Aradius = 3.5
            Bradius = BCradius * Aradius / ACradius
            # Number of rotations when Bcircle follows Acircle
            dotRotateBcircle = BCircleSlip * (Aradius/Bradius) - 1

            Acircle = Circle(radius=Aradius, color=GRAY, stroke_width=1)
            ShadowCircle = Circle(radius=Aradius-Bradius, color=BLUE, stroke_width=0)
            Bcircle = always_redraw(lambda: Circle(radius=Bradius, color=RED, stroke_width=1).move_to(ShadowCircle.point_at_angle(angleDeg.get_value()*PI/180)))

            guideLine = always_redraw(lambda: Line(start=Bcircle.get_center(), end = Bcircle.point_at_angle(rotationDirection*dotRotateBcircle*angleDeg.get_value()*PI/180), stroke_width=0.5, buff=0))

            dot = always_redraw(lambda: Dot(color=YELLOW).move_to(Bcircle.point_at_angle(rotationDirection*dotRotateBcircle*angleDeg.get_value()*PI/180)))
            
            trace = TracedPath(dot.get_start).set_color_by_gradient(colors)

            allGroup = VGroup(Acircle,Bcircle, ShadowCircle,dot, guideLine)
            allGroup.to_edge(DOWN, buff=3)
            self.add(allGroup, trace)
            self.play(Write(rRatio), run_time=0.2)
            slipText = Text("Slipping circle", font_size=22, weight=LIGHT).set_color(GRAY_E).to_edge(UP, buff=5)
            rotationText = Text("Reverse rotation", font_size=22, weight=LIGHT).set_color(GRAY_E).to_edge(UP, buff=5)
            if BCircleSlip>1:
                self.add(slipText)
                self.play(angleDeg.animate.set_value(totalAngle), rate_func=rate_functions.linear, run_time=runTime)
            elif rotationDirection==1:
                self.add(rotationText)
                self.play(angleDeg.animate.set_value(totalAngle), rate_func=rate_functions.linear, run_time=runTime)
            else:
                self.play(angleDeg.animate.set_value(totalAngle), rate_func=rate_functions.linear, run_time=runTime)
                
            if clear:
                self.remove(Bcircle, trace, guideLine,rRatio, dot, slipText, rotationText)

        # Remove the initial descriptions
        self.play(FadeOut(ALine), FadeOut(BLine))
        self.remove(Bcircle)

        drawHypocloids(3.5, 1, 2, 2, -1, 1, True)
        drawHypocloids(6.2, 1, 3.1, 2, -1, 1, True)
        drawHypocloids(5.1, 1, 9, 2, -1, 1.35, True)
        drawHypocloids(4.3, 1, 10, 2, 1, 1, False)
        self.wait(1)


        