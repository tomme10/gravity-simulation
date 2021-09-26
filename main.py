import pygame
import sys
from Modules.camera import camera
from Modules.objectRoot import objectRoot
from Modules.body import body
from Modules.grid import grid
from math import ceil,floor

dis = (800,600)
root = pygame.display.set_mode(dis)

FPS = 60

def main(args):

    objRoot = objectRoot(
        [
            body(100,10,pos = [0,-300],vel=[10,0],color = (255,255,0)), # sun
            body(100,10,pos = [0,-200],vel = [-10,0],color = [0,255,0]), # earth
            body(100,10,pos = [0,300],vel = [-10,0],color = [0,255,0]),
        ]
    )
    clock = pygame.time.Clock()
    cam = camera(follow = objRoot.objects[2])
    speed = 1/60
    speed2 = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_PERIOD:
                    cam.zoom(0.25)
                elif event.key == pygame.K_COMMA:
                    cam.zoom(-0.25)

                elif event.key == pygame.K_LEFTBRACKET:
                    speed2 = ceil(1.25*speed2)
                elif event.key == pygame.K_RIGHTBRACKET:
                    if speed2//1.25 >= 1:
                        speed2 = floor(speed2/1.25)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            speed *= 1.01
        if keys[pygame.K_DOWN] and speed / 1.01 > 0:
            speed /= 1.01
        
        cam.update()

        for i in range(speed2):
            objRoot.update(speed)

        root.fill((0,0,0))
        objRoot.draw(root,cam)

        clock.tick(FPS)
        pygame.display.update()

    return

if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as e:
        pygame.quit()
        raise e

    pygame.quit()
    sys.exit()