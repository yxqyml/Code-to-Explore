from manim import *

class MonteCarloExplain(Scene):
    def construct(self):
        NUM = 100
        axes = Axes()
        circle=Circle(radius=3)
        square = Square(side_length = 6)
        #self.set_camera_orientation(phi=75 * DEGREES, theta=60 * DEGREES)

        self.add(axes)
        self.wait()
        self.add(square)
        self.wait()
        self.add(circle)
        self.wait()
        tex = MathTex(r"\pi = 4 \times {\frac{area\ of\ circle}{area\ of\ square}}")
        tex2 = MathTex(r"\pi = 4 \times \frac{\pi R^2}{{(2R)}^2}")
        tg = VGroup(tex, tex2).arrange(DOWN)
        tg.scale(0.6)
        tg.to_corner(UR)
        self.play(Write(tg))
        
        dot_in = Dot([1, 2, 0], color=RED)
        self.add(dot_in)
        self.wait()
        arrow1 = Arrow(ORIGIN, dot_in, buff=0, color=RED)
        in_text = Text("dot in the circle, in red").next_to(arrow1.get_end(),UP)
        in_text.scale(0.5)
        self.add(arrow1, in_text)
        self.wait()
        dot_out = Dot([-2.5, -2.5, 0], color=BLUE)
        arrow2 = Arrow(ORIGIN, dot_out, buff=0, color=BLUE)
        out_text = Text("dot outsides the circle, in blue").next_to(arrow2.get_end(),UP)
        out_text.scale(0.5)
        self.add(dot_out, arrow2, out_text)
        self.wait()

        x = np.random.uniform(-3, 3, NUM)
        y = np.random.uniform(-3, 3, NUM)
        colors = np.where(np.sqrt(x**2 + y**2) < 3, 'red', 'blue')
        g = VGroup()
        g.add(axes, circle, square, dot_in, dot_out, arrow1,arrow2, in_text, out_text)
            
        for i in range(NUM):
            dot = Dot([x[i], y[i], 0], color=colors[i])
            self.add(dot)
            g.add(dot)
        self.play(g.animate.shift(RIGHT), g.animate.scale(0.7))
        self.wait()
        tex = MathTex(r"\pi = 4* {\frac{num\ of\ red\ dots}{total\ num\ of\ dots}}")
        tex.to_edge(UL)
        self.play(Write(tex))
        self.wait()
