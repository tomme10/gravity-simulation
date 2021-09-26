import pygame
from Modules.obj import obj

class grid(obj):
    drawOrder = -1

    wh = 20

    def draw(self,root,cam):
        print(f'800/{cam.rect.width}')
        zoom = 800/cam.rect.width

        wh = int(self.wh*zoom)

        for i in range((root.get_width()//wh)+2):
            pos = [i*wh+(cam.rect.center%wh),i*wh+(cam.rect.center%wh),800]

            pygame.draw.line(root,(100,100,100),((i*wh-(cam.rect.left%wh)),0),((i*wh-(cam.rect.left%wh)),600))

        for j in range((root.get_height()//round(wh+0.5))+2):
            pygame.draw.line(root,(100,100,100),(0,(j*wh-(cam.rect.top%wh))),(800,(j*wh-(cam.rect.top%wh))))
