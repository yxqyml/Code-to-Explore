#
# This python code is about to explain the method 3 of the Bertrand's Paradox,  i.e. the random midpoint method.
# I use manim to produce the animations which will help you to understand it easily.
#

from manim import *
from os import system

class M3Exp(Scene):
    def construct(self):
        # First of all, let's create a circle with radius of 2
        R = 2
        circle = Circle(radius=R, stroke_width=1)
        self.play(FadeIn(circle))
        self.play(Create(Dot([0,0,0])))

        # Draw a triangle with in the circle
        triangle = RegularPolygon(3, radius=R, color=GRAY, stroke_width=1)
        self.play(FadeIn(triangle))

        self.wait()

        # Choose a point randomly within the area of the circle
        
        # point 1
        x = 1.5*np.cos(PI/3)
        y = 1.5*np.sin(PI/3)
        random_point = np.array([x,y,0])

        t0 = Text("Randomly select a point in the circle").scale(0.6).move_to(3*DOWN)
        self.play(FadeIn(t0))
        self.wait(2)

        self.chord_from_midpoint(random_point, circle)
        self.play(FadeOut(t0))

        t0 = Text('''
                    Draw a chord across the random point.
                  And, let the chord perpendicular to the radius
                  across it
                  ''').scale(0.6).move_to(DOWN*3)
        self.play(FadeIn(t0))
        self.wait(3)
        self.play(FadeOut(t0))

        # Here is the point 2
        x = -0.8*np.cos(PI/3)
        y = 0.8*np.sin(PI/3)
        random_point = np.array([x, y, 0])
        self.chord_from_midpoint(random_point, circle)

        t1 = Text('''
                        If we draw a concentric circle of radius of R/2
                      i.e. half of the larger circle
                      ''').scale(0.6).move_to(DOWN*3)
        self.play(FadeIn(t1))
        inner_c = Circle(radius=R/2, stroke_width=1)
        self.play(FadeIn(inner_c))
        self.wait(2)
        self.play(FadeOut(t1))       
        t2 = Text('''
                        Obviously, the chord is longer than a side of the inscribed
                      triangle if the chosen random point falls within the concentric
                      circle of radius of 1/2 the radius of te larger circle. The
                      area of the samller circle is one fourth the area of the larger circle
                      ''').scale(0.6).move_to(DOWN*3)
        self.play(FadeIn(t2))
        self.wait(3)
        conclusion_t = Text('''
                                Therefor the probability a random chord is longer
                                than a side of the inscribed triangle is:
                              ''').scale(0.6).move_to(3.2*UP)
        result_t = MathTex(r'\frac{1}{4}').scale(2).move_to(1.8*UP+3*RIGHT)
        result_t.set_color(RED)
        self.play(Write(conclusion_t))
        self.play(GrowFromCenter(result_t)) 
        self.wait(2)

        # Now we need some calculations to draw the chord across the random point (midpoint of the chord)
    def chord_from_midpoint(self,midpoint, circle):
        middot = Dot(midpoint, radius=0.05)
        self.play(Create(middot))

        # Draw a line between the center of the circle and the randm dot.
        orign = np.array([0,0,0])
        line0 = DashedLine(orign, midpoint, fill_color=YELLOW)
        self.play(Create(line0))
        self.wait()

        # Construct a chord with the chosen point as its midpoint
        slope = line0.get_slope()
        k = -1.0/slope
        x = midpoint[0]
        y = midpoint[1]
        line1 = Line(midpoint, [0, y-k*x, 0])

        # Calculate the intersection points
        int_points = self.get_intersection(circle, line1)    # we will define it later

        # and draw the intersection points on the circle
        dots = VGroup(*[Dot(point, radius=0.05) for point in int_points])

        # Connect the two points
        if len(int_points) == 2:
            d = np.sqrt(midpoint[0]**2 + midpoint[1]**2)
            if d > 1:
                color = BLUE
            else:
                color = RED
            conn_line = Line(int_points[0], int_points[1])
            conn_line.set_color(color)
            self.add(conn_line)
            self.add(dots)
            self.play(FadeOut(line0))



    def get_intersection(self, circle, line):
        x1, y1 = line.get_start()[:2]
        x2, y2, = line.get_end()[:2]
        r = circle.radius 

        dx = x2 - x1
        dy = y2 - y1 
        dr = np.sqrt(dx**2 + dy**2)
        D = x1*y2 + x2*y1
        d = r**2*dr**2 - D**2
        if d<0:
            return []
        sqrt_d = np.sqrt(d)
        sign_dy = np.sign(dy) if dy != 0 else 1
        x_plus = (D*dy + sign_dy*dx*sqrt_d)/(dr**2)
        x_minus= (D*dy - sign_dy*dx*sqrt_d)/(dr**2)

        y_plus = (-D*dx + np.abs(dy)*sqrt_d)/(dr**2)
        y_mius= (-D*dx - np.abs(dy)*sqrt_d)/(dr**2)

        return [np.array([x_plus, y_plus, 0]), np.array([x_minus, y_mius,0])]


if __name__ == "m__main__":
    system("manim -pql {} M3Exp".format(__file__))