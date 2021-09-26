from Modules.obj import obj
import pygame
from math import atan2,sqrt,degrees,radians,sin,cos

G = 6.673*10

class body(obj):

    def __init__(self,mass,radius,vel = [0,0],color = [255,0,0],pos = [0,0],cam = False):
        self.mass = mass
        self.radius = radius

        self.cam = cam

        assert isinstance(vel,list) and len(vel) == 2
        self.vel = vel

        self.color = color

        assert isinstance(pos,list) and len(pos) == 2
        self.pos = pos

        self.line = []

    def preUpdate(self,objs,time):
        accVecs = []

        for obj in objs:
            if obj == self:
                continue
            elif type(obj).__name__ != 'body':
                continue
            
            radius = sqrt((self.pos[1]-obj.pos[1])**2+(self.pos[0]-obj.pos[0])**2)
            angle = atan2(obj.pos[1]-self.pos[1],obj.pos[0]-self.pos[0])
            acc = ((obj.mass*G+self.mass*G)/radius**2)*time
            
            accVecs.append([cos(angle)*acc,sin(angle)*acc])

        for vec in accVecs:
            self.vel = [self.vel[0]+vec[0],self.vel[1]+vec[1]]

        
    def midUpdate(self,objs,time):
        
        '''for obj in objs:
            if obj == self:
                continue
            elif type(obj).__name__ != 'body':
                continue

            dist = sqrt((self.pos[0]-obj.pos[0]+self.vel[0])**2+(obj.pos[1]-obj.pos[1]+self.vel[1])**2)
            if dist < self.radius+obj.radius:
                angle = atan2(self.vel[1],self.vel[1])+radians(180)

                while dist < self.radius+obj.radius:
                    self.vel[0] -= cos(angle)
                    self.vel[1] -= sin(angle)
                    dist = sqrt((self.pos[0]-obj.pos[0]+self.vel[0])**2+(obj.pos[1]-obj.pos[1]+self.vel[1])**2)'''
        
        self.line.append((self.pos[0],self.pos[1]))
        if len(self.line) > 1000:
            del self.line[0]

    def postUpdate(self,objs,time):
        self.pos[0] = self.pos[0]+(self.vel[0]*time)
        self.pos[1] = self.pos[1]+(self.vel[1]*time)

    def draw(self,root,cam):
        if len(self.line) > 2:
            for i,line in enumerate(self.line[:-2]):
                pygame.draw.aaline(root,self.color,cam.getPos(line),cam.getPos(self.line[i+1]))

        pygame.draw.circle(root,self.color,cam.getPos(self.pos),self.radius)