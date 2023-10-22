# This python code is about to explain the random radial point
# method (a.k.a. the method 2 as explained by wikipedia) to the 
# Bertrand's paradox.
# For the sake of debugging, I use Main Sideview, a Visual Studio
# code extension.

# To save time, I reuse some piece of code from the previous one, i.e.
# the code for method 1 (random endpoints)
from manim import * 
from os import system

class BertrandMethod2(Scene):
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
        sub_t1 = Text("Random chords selection method 2").next_to(logo_g, DOWN).scale(0.8)
        sub_t2 = Text("Random radial points", color=RED_A).next_to(sub_t1, DOWN).scale(0.8)

        title_g = Group(sub_t1, sub_t2).move_to(UP)
        self.play(FadeIn(title_g))
        
        ref_t = Text("Reference to").scale(0.3).next_to(sub_t2, 5*DOWN+2*LEFT)
        reflink_t = Text("https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)",
                       color=GRAY).scale(0.3).next_to(ref_t)
        ref_g = Group(ref_t, reflink_t)
        self.play(FadeIn(ref_g))
        self.wait()
        self.play(FadeOut(ref_g, title_g), run_time=3)




if __name__ == "__main__":
    system("manim -pqh {} BertranMethod2".format(__file__))
    # TO GENRATE HIGH DEFINITION VIDEO, change the commond parameter
    # to -pqh
