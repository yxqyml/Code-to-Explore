# In this program, I'd like to explain the Bertrand's Pradox with manim animations.
from manim import * 

# for the sake of debugging, I use ipython as interactive debugging tool.
from os import system 

class BertrandExplain(Scene):
    def construct(self):
        # Load the logo of video channel (SVG format)
        c2e_logo = SVGMobject(file_name="C2E.svg").move_to(UP)

        # Text under the logo
        c2e_t = Text("Code to Explore").next_to(c2e_logo, DOWN)  # This text should be under the logo

        # Title of this vide 
        title_t = Text("Bertrand's Paradox").move_to(UP)
        # Fade in the logo 
        logo_g = Group(c2e_logo, c2e_t)
        self.play(FadeIn(logo_g), run_time=3)

        # Let the logo transfer to the tile of the video 
        self.play(Transform(logo_g, title_t), run_time=4)

        # Then fade out the title 
        self.play(FadeOut(logo_g), run_time=3)

        # Now show some text about the Bertrand's Paradox
        prob_t = Text("The Bertrand's Paradox goes as follows:").move_to(UP)
        prob_t[0:len("The Bertrand's Paradox".replace(' ', ''))].set_color(RED)
        self.play(FadeIn(prob_t))

        proble_formulation_t = Text(
                '''
                Consider a equilateral triangle inscribed in a circle.
                Suppose a chord of the circle is chosen at random. What
                is the probability that the chord is longer than a side
                of the triangle?
                '''
                , font="Open Sans", weight=THIN, line_spacing=1.1
                ).move_to(UP)
        arg_t = Text(
                '''
                Bertrand gave three arguments, all apparently valide,
                yet yielding different results.
                ''', color=BLUE
                ).scale(0.8).move_to(2*UP)
        m1_t = Text("Method 1: Random endpoints method").scale(0.6)
        m2_t = Text("Method 2: Random radial method").scale(0.6)
        m3_t = Text("Method 3: Random midpoints method").scale(0.6)
        method_g = VGroup(m1_t, m2_t, m3_t).move_to(UP)
        method_g.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.5)
        proble_formulation_t.scale(0.6).next_to(prob_t, DOWN)
        self.play(FadeIn(proble_formulation_t))
        self.wait(3)
        self.play(FadeOut(proble_formulation_t, prob_t))
        self.play(FadeIn(arg_t))
        self.play(FadeIn(method_g))
        self.wait(3)
        self.play(FadeOut(arg_t,method_g))

        # sub titles
        sub_t1 = Text("Random chords selection method 1").next_to(logo_g, DOWN).scale(0.8)
        sub_t2 = Text("Random endpoints", color=RED_A).next_to(sub_t1, DOWN).scale(0.8)

        title_g = Group(sub_t1, sub_t2).move_to(UP)
        self.play(FadeIn(title_g))
        
        ref_t = Text("Reference to").scale(0.3).next_to(sub_t2, 5*DOWN+2*LEFT)
        reflink_t = Text("https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)",
                       color=GRAY).scale(0.3).next_to(ref_t)
        ref_g = Group(ref_t, reflink_t)
        self.play(FadeIn(ref_g))
        self.wait()
        self.play(FadeOut(ref_g, title_g), run_time=3)

        # Now let's explain the 'random endpoint' method via animations
        LINEWIDTH=0.5

        # Draw a circle with radius of 2 
        circle = Circle(radius=2, stroke_width=1)

        d1 = Dot([2*np.sin(2), 2*np.cos(2), 0]).set_color(ORANGE)
        d2 = Dot([-2, 0, 0]).set_color(ORANGE)

        temp_line = Line(d1.get_center(), d2.get_center(), stroke_width=LINEWIDTH)

        # Draw a equilateral triangle inscribed in the circle 
        poly = Polygon([-np.sqrt(3), -1, 0], [np.sqrt(3), -1, 0], [0, 2, 0], stroke_width=1)

        # Draw three arcs between the points of the triangle 
        arc1 = ArcBetweenPoints([-np.sqrt(3), -1, 0], [np.sqrt(3), -1, 0], angle=2*PI/3, stroke_width=1)
        arc2 = ArcBetweenPoints([np.sqrt(3), -1, 0], [0, 2, 0], angle=2*PI/3, stroke_width=1)
        arc3 = ArcBetweenPoints([0, 2, 0], [-np.sqrt(3), -1, 0], angle=2*PI/3, stroke_width=1)

        # Gropup the above shapes 
        g = Group(circle, poly, arc1, arc2, arc3)

        # Add some text for method 1 
        method1_t = Text('''
                        The 'random endpoints' method says that to choose two random points on the 
                        circumference of the circle and draw the chord jointing them. To calculate 
                        the probability in question, the triangle rotated so its vertex conicides 
                        with one of the chord endpoints.
                         ''').scale(0.4).next_to(g, DOWN)
        self.play(FadeIn(method1_t))

        self.add(g)
        self.wait(2)

        self.add(d1, d2)
        self.wait(2)

        self.play(GrowFromPoint(temp_line, [-2,0,0]))
        self.wait(2) 

        # Rotate the group for -PI/6 degree
        self.play(Rotate(g, -PI/6))
        self.wait(2)

        self.remove(temp_line) 

        # Create an dot in orange
        line = VMobject(stroke_width=1)
        self.add(d1, d2, line)


        # Animate the random chord selection method
        # Method 1 - random endpoints
        m1_title = Text("Method 1: Random endpoints").scale(0.5).next_to(g, RIGHT)
        m1_text = Text('red = longer than triangle side, yellow - short').scale(0.25).next_to(m1_title, DOWN)
        self.add(m1_title, m1_text)

        short_t = Text(
                '''
                The chord is shorter than the side of the triangle,
                when the random endpoint is onhis part of the circle.
                '''
                ).scale(0.6).move_to(3*UP)
        self.play(FadeIn(short_t))
        line.add_updater(lambda x: x.become(Line([-2, 0, 0], d1.get_center(),
                                            stroke_width=LINEWIDTH).set_color(YELLOW)))
        self.play(MoveAlongPath(d1, arc1), rate_func=linear, run_time=5)
        line.add_updater(lambda x: x.become(Line([-2, 0, 0], d1.get_center(),
                                            stroke_width=LINEWIDTH).set_color(RED)))
        self.play(FadeOut(short_t))
        longer_t = Text('''
                       The chord is longer than the side of triangle,
                       when the random endpoint is on this part of the circle.
                       ''').scale(0.6).move_to(3*UP)
        self.play(FadeIn(longer_t))
        self.play(MoveAlongPath(d1, arc2), rate_func=linear, run_time=5)
        line.add_updater(lambda x: x.become(Line([-2, 0, 0], d1.get_center(),
                                            stroke_width=LINEWIDTH).set_color(YELLOW)))
        self.play(FadeOut(longer_t))
        self.play(FadeIn(short_t))
        self.play(MoveAlongPath(d1, arc3), rate_func=linear, run_time=5)
        self.wait()

        self.play(FadeOut(short_t))
        solution_t = Text('''
                          Therefore the probability that a random chord is longer
                          than a side of the inscribed triangle is:
                          ''').scale(0.6).move_to(3.2*UP)
        result_l = MathTex(r"\frac{1}{3}").scale(2).move_to(2*UP+2.5*RIGHT)
        result_l.set_color(RED)
        self.play(Write(solution_t))
        self.play(GrowFromCenter(result_l))
        self.wait(2)

 
    
    
if __name__ == "__main__":
    system("manim -pqh {} BertrandExplain".format(__file__))
