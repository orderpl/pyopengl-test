import pygame as pg
import moderngl as gl
import sys
import pygame as pg

from model import *
from camera import Camera
from light import Light
from mesh import Mesh

class GraphicsEngine(object):
    def __init__(self, win_resolution:tuple[int, int]):
        pg.init()
        self.clock = pg.time.Clock()
        self.WIN_RESOLUTION = win_resolution
        self.time = 0
        self.max_tick_time = 1 / 60.0
        
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        
        pg.display.set_mode(self.WIN_RESOLUTION, flags=pg.OPENGL | pg.DOUBLEBUF)

        self.ctx = gl.create_context()
        self.ctx.enable(flags=gl.DEPTH_TEST | gl.CULL_FACE)
        
        self.camera = Camera(self)
        
        self.light = Light((3, 3, -3))
        
        self.mesh = Mesh(self)
        self.scene = Cube(self)
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.end()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.end()
                    
    def render(self):
        self.time = pg.time.get_ticks() * 0.001
        self.ctx.clear(color=(0.15, 0.15, 0.2))
        self.scene.render()
        pg.display.flip()
        
    def update(self):
        self.camera.update()
        self.scene.update()
        
    def run(self):
        dt = 0.0
        pg.mouse.set_visible(False)
        pg.event.set_grab(True)
        while True:
            dt += self.clock.tick() * 0.001
            self.check_events()
            self.render()
            while dt > self.max_tick_time:
                self.update()
                dt -= self.max_tick_time
            
    def end(self):
        self.mesh.destroy()
        sys.exit(0)
        
            
if __name__ == '__main__':
    app = GraphicsEngine((1280, 720))
    app.run()