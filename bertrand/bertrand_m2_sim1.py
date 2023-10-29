#
# This python code produces the starting video of the explaination video of
# Bertrand's paradox random chord selection method 2, i.e. # random radial 
# point method.
#
from manim import *

class BertrandExplain(Scene):
    def construct(self):
        # Load the logo (SVG format)
        c2e_logo = SVGMobject(file_name="C2E.svg").move_to(UP)  # move a littble bit higher 

        # Text under the logo
        c2e_t = Text("Code to Explore").next_to(c2e_logo, DOWN)    # put the text under the logo

        # Title of this episode
        title_t = Text("Bertrand's Paradox").move_to(UP)
        
        # FadeIn the logo of Code to Explore
        logo_g = Group(c2e_logo, c2e_t)
        self.play(FadeIn(logo_g), run_time=3)

        # Transiting to the title of the video
        self.play(Transform(logo_g, title_t), run_time=4)

        # Fade out the title 
        self.play(FadeOut(logo_g), run_time=3)


         # Sub titles
        sub_t1 = Text("Simulation of random chords selection method 2").next_to(logo_g, DOWN).scale(0.8)
        sub_t2 = Text("Random radial point", color=RED_A).next_to(sub_t1, DOWN).scale(0.8)

        title_g = Group(sub_t1, sub_t2).move_to(UP)
        self.play(FadeIn(title_g))

        ref_t = Text("Reference to").scale(0.3).next_to(sub_t2, 5*DOWN+2*LEFT)
        reflnk_t = Text("https://en.weikipedia.org/wiki/Bertrand_paradox_(probability)", color=GRAY).scale(0.3).next_to(ref_t)
        ref_g = Group(ref_t, reflnk_t)
        self.play(FadeIn(ref_g))
        self.wait()
        self.play(FadeOut(ref_g, title_g), run_time=3)


if __name__ == '__main__':
    from os import system
    system("manim -pqh {} BertrandExplain".format(__file__))
