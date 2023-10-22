#
# This python code is about to explain the method 2, i.e. random radial point
# method to the Bertrand's Paradox.
#
# For the sake of deugging, I use Manim Sideview - a Visual Studio code extension
#

from manim import *
from os import system 

class BertrandM2Explain(Scene):
    def construct(self):
        
        # First all let's create a circle with radius of 2 
        R = 2 
        LINEWIDTH = 1
        circle = Circle(radius=R, stroke_width=LINEWIDTH)
        self.add(circle)
        self.add(Dot([0,0,0]))

        # Draw a equilateral triangle inscribed in the circle
        triangle = RegularPolygon(3, 
                                  radius=circle.radius, 
                                  color=GRAY, 
                                  stroke_width=LINEWIDTH)
        self. play(Create(triangle))

        # Now we choose a random radius
        # Generate a random agle first
        angle = np.random.uniform(0, 2*PI)

        t0 = Text("Choose a random radius").scale(0.6).move_to(3*DOWN)
        self.play(FadeIn(t0))
        # and then draw a radius at that angle
        radius = Line(circle.get_center(), circle.point_at_angle(angle))
        self.add(radius)
        dotA = Dot(radius.get_end()) 
        self.add(dotA)
        pointA = Text("A").scale(0.5).next_to(radius.get_end())
        pointO = Text("O").scale(0.5).next_to(radius.get_start())

        midpoint = (radius.get_start() + radius.get_end())/2
        self.play(Write(pointA), Write(pointO))
        self.wait(2)
        self.play(FadeOut(t0))

        
        # Construct a chord (this is actually a kind of placehold,
        # we do not show the chord at first. It will be used in the following
        # animation)
        chord = Line(circle.get_right(), circle.get_left())
        chord.set_opacity(0)
        self.add(chord)

        # Rotate the triangle, then it is easier to compare the 
        # length of the chord with the side of triangle
        self.play(Rotate(triangle, angle+PI/2, about_point=circle.get_center()))

        # Create a dot moving alongt the radius
        dot = Dot(color=RED)
        self.add(dot)

        t1 = Text("Randomly select a point on the radius").scale(0.6).move_to(3*DOWN)
        self.play(FadeIn(t1))
        self.play(dot.animate.move_to(radius.get_start()), run_time=2)
        self.play(dot.animate.move_to(radius.get_end()), run_time=2)

        #self.play(dot.animate.move_to(radius.get_end()), run_time=2)
        self.play(FadeOut(t1))
        # Now we want to construct the chord through the moving point and 
        # perpendicular to the radius. Of course in an animated way.
        def update_chord(chord): # this is the chord we've already created but haven't shown
            # Obtain the position of the point on the radius
            t = np.dot(dot.get_center() - radius.get_start(), radius.get_unit_vector()) 

            # Calculate the coordinations of the chord's endpoints
            d = np.sqrt(circle.radius**2 - t**2)
            end1 = dot.get_center() + d * rotate_vector(radius.get_unit_vector(), PI/2)
            end2 = dot.get_center() - d * rotate_vector(radius.get_unit_vector(), PI/2)
            distance = np.linalg.norm(end1-end2)

            if np.sqrt(3)*R > distance:
                color = RED
            else:
                color = BLUE
            chord.set_color(color)
            chord.set_opacity(1)

            # Update the position of the chord
            chord.put_start_and_end_on(end1, end2)

        chord.add_updater(update_chord)

        dotM = Dot(midpoint)
        pointM = Text("M").scale(0.5).next_to(midpoint) 
        self.add(dotM)
        self.play(Write(pointM))

        t2 = Text(
                '''
                When the random point is at line OM, where M is the midpoint of AO 
                the chord length is longer (in blue) than the side-length of the triangle,
                otherwise when th e random point is at line AM, the chord length is shorter
                (in red) than the side-length of the triangle.
                '''
                ).scale(0.6).move_to(3*DOWN)
        self.play(FadeIn(t2))
        self.play(dot.animate.move_to(radius.get_start()), run_time=5)
        self.play(dot.animate.move_to(radius.get_end()), run_time=5)

        conclusion = Text(
        '''Therefor the probality a random chord is longer 
        than a side of the inscribed triangle is:
        '''
        ).scale(0.6).move_to(3.2*UP)
        result_t = MathTex(r"\frac{1}{2}").scale(2).move_to(1.8*UP+3*RIGHT)
        result_t.set_color(RED) 
        self.play(Write(conclusion))
        self.play(GrowFromCenter(result_t))
        self.wait(2)
 

if __name__ == "__main__":
    system("manim -pql {} BertrandM2Explain".format(__file__))
    # Change to '-pqh' for high definition video