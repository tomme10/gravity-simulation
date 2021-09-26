from Modules.obj import obj
import pygame

class camera(obj):

    def __init__(self,follow = None):
        self.pos = [0,0]
        self.z = 1
        self.follow = follow

    def update(self):
        if self.follow:
            self.pos = self.follow.pos

        else:
            keys = pygame.key.get_pressed()

            speed = 2/self.z
            if keys[pygame.K_LSHIFT]:
                speed = 5/self.z

            if keys[pygame.K_d]:
                self.pos[0] += -speed
            if keys[pygame.K_a]:
                self.pos[0] += speed
            if keys[pygame.K_w]:
                self.pos[1] += speed
            if keys[pygame.K_s]:
                self.pos[1] += -speed

        #print(self.rect.center,self.rect.size)

    def zoom(self,amount):
        self.z *= 1+amount

    def getPos(self,pos):
        transPos = [pos[0]+self.pos[0],pos[1]+self.pos[1]]
        transPos[0] *= self.z
        transPos[1] *= self.z
        transPos[0] += 400
        transPos[1] += 300
        return [int(transPos[0]),int(transPos[1])]
