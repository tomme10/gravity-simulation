
class objectRoot():

    def __init__(self,objects = []):
        assert isinstance(objects,list)

        self.objects = objects
        
    def update(self,time):
        objs = []
        for obj in self.objects:
            objs.append(obj.getElements())

        objs = sorted(objs,key = lambda obj:obj.updateOrder)

        for obj in objs:
            obj.preUpdate(objs,time)
        
        for obj in objs:
            obj.midUpdate(objs,time)

        for obj in objs:
            obj.postUpdate(objs,time)

    def draw(self,root,cam):
        objs = []
        for obj in self.objects:
            objs.append(obj.getElements())

        for obj in sorted(objs,key = lambda obj:obj.drawOrder):
            obj.draw(root,cam)