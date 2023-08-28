import pygame as pg
import moderngl as gl
import sys

from model import *
from camera import Camera


class GraphicsEngine(object):
    def __init__(self, win_resolution:tuple[int, int]):
        pg.init()
        self.clock = pg.time.Clock()
        self.WIN_RESOLUTION = win_resolution
        self.time = 0
        
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        
        pg.display.set_mode(self.WIN_RESOLUTION, flags=pg.OPENGL | pg.DOUBLEBUF)

        self.ctx = gl.create_context()
        
        self.camera = Camera(self)
        
        self.scene = Cube(self)
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.end()
            if event == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.end()
   
                        
    def render(self):
        self.time = pg.time.get_ticks() * 0.001
        self.ctx.clear(color=(0.1, 0.1, 0.1))
        self.scene.render()
        print(self.time)
        pg.display.flip()
        
    def run(self):
        while True:
            self.check_events()
            self.render()
            self.clock.tick()
            
    def end(self):
        self.scene.destroy()
        sys.exit(0)
            
if __name__ == '__main__':
    app = GraphicsEngine((1280, 720))
    app.run()