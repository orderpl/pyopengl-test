from model import *

class Scene(object):
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        
    def add_object(self, obj):
        self.objects.append(obj)
        
    def load(self):
        add = self.add_object
        app = self.app
        
        add(Cube(app, tex_id=0, pos=(2, 0, 0)))
        add(Cube(app, tex_id=1, pos=(0, 0, 0)))
        add(Cube(app, tex_id=2, pos=(-2, 0, 0)))
        
    def render(self):
        for obj in self.objects:
            print(f"rendering {obj}")
            obj.render()
            
    def update(self):
        for obj in self.objects:
            obj.update()