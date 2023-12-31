import pygame
import sys
import os
from pygame.locals import *
import numpy as np

# 1. Define colors
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
COLORS = [
        (255, 0, 0),    # RED
        (0, 255, 0),    # GREEN
        (0, 0, 255),    # BLUE
        (255, 255, 0),  # YELLOW
        (0, 255, 255),  # CYAN
        (255, 0, 255),  # MAGENTA
        ]
# 2. Pygmae initialization
pygame.init()

# 3. Windows size and position
window_size = (800, 600)
os.environ['SDL_VIDEO_WINDOW_POS'] = '20, 50'

# 4. Pygame init with resizeable flag
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption("Happy New Year!")
CLOCK = pygame.time.Clock()
FPS = 60

# 5. Fireworks constants
MAX_FIREWORKS = 50
AVG_FIREWORKS_PER_SECOND = 100
GRAVITY_FORECE = -10.0/FPS

# 6. Greeting setup, font and text, you can customize it
font = pygame.font.Font(None, 100)
text = font.render("Happy New Year! 2024", True, COLORS[0]) # Red text

text_alpha = 0
fade_in = 120           # 2 seconds to fade in
fade_out_start = 180    # Fade out starts after 3 seconds
fade_out = 120          # 2 seconds to fade out

# 7. Class for Fireworks Particals 
class FireWorkParticale:
    LAG = 5
    MIN_SPEED = 1
    MAX_SPEED = 5
    FADE_SPEED = 5

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.angle = np.random.randint(0, 360)*np.pi/180
        self.speed = np.random.randint(self.MIN_SPEED, self.MAX_SPEED)
        self.x_speed = np.cos(self.angle)*self.speed
        self.y_speed = np.sin(self.angle)*self.speed
        self.points = [(self.x, self.y)]
        self.color = color

    def evolve(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.y_speed -= GRAVITY_FORECE
        self.points.append([self.x, self.y])

        if len(self.points) > self.LAG:
            self.points.pop(0)
        self.color = [c - self.FADE_SPEED if c > self.FADE_SPEED else 0 for c in self.color]

    def draw(self):
        pygame.draw.aalines(screen, self.color, False, self.points, True)


# 8. Class for Fireworks
class Firework:
    MIN_PARTICALS = 20
    MAX_PARTICALS = 50

    def __init__(self):
        self.particles = []
        x = np.random.randint(0, window_size[0])
        y = np.random.randint(0, window_size[1])
        color = COLORS[np.random.randint(0, len(COLORS))]

        for _ in range(np.random.randint(self.MIN_PARTICALS, self.MAX_PARTICALS+1)):
            self.particles.append(FireWorkParticale(x, y, color))

    def evolve(self):
        for particle in self.particles:
            particle.evolve()

    def draw(self):
        for particle in self.particles:
            particle.draw()

def generate_firework():
    if np.random.random() > 1 - (AVG_FIREWORKS_PER_SECOND/FPS):
        FIREWORKS.append(Firework())
        if len(FIREWORKS) > MAX_FIREWORKS:
            FIREWORKS.pop(0)

def update_and_draw_fireworks():
    for firework in FIREWORKS:
        firework.evolve()
        firework.draw()

def handle_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

# 9. Main function
def main():
    global screen, text_alpha
    frame_count = 0

    while True:
        screen.fill(BLACK)
    
        generate_firework()
        update_and_draw_fireworks()

        # Greeting!
        text.set_alpha(text_alpha)
        text_rect = text.get_rect(center=(window_size[0]//2, window_size[1]//2))
        screen.blit(text, text_rect)

        # Fading in and out
        if frame_count < fade_in:
            text_alpha += 255 / fade_in
        elif frame_count >= fade_out_start:
            text_alpha -= 255/fade_out

        pygame.display.update()

        CLOCK.tick(FPS)
        handle_events()
        frame_count += 1

# 10. call the main function
if __name__ =='__main__':
    FIREWORKS = [Firework()]
    main()

