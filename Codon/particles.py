from bindings import *
import random

MAX_PARTICLES = 5000

class Particle:
    def __init__(self, position, velocity, radius, color):
        self.position = position
        self.velocity = velocity
        self.radius = radius        
        self.color = color

def main():
    init_window(1280, 720, 'Random Particles')
    set_target_FPS(60)
    
    particles = [Particle(Vector2(random.randint(0, 1280), random.randint(0, 720)), Vector2(random.randint(-200, 200) / 100, random.randint(-200, 200) / 100), random.randint(1, 3), Color(random.randint(50, 255), random.randint(50, 255), 255, 255)) for i in range(MAX_PARTICLES)]

    while not window_should_close():
        begin_drawing()
        clear_background(black)

        for i in range(MAX_PARTICLES):
            particle = particles[i]

            if particle.position.x <= 0 or particle.position.x >= 1280:
                particle.velocity.x = -particle.velocity.x
            if particle.position.y <= 0 or particle.position.y >= 720:
                particle.velocity.y = -particle.velocity.y

            particle.position.x += particle.velocity.x
            particle.position.y += particle.velocity.y

            draw_circle(int(particle.position.x), int(particle.position.y), particle.radius, particle.color)

        draw_FPS(10, 10)
        end_drawing()

main()