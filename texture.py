import pygame as pg
import moderngl as mgl
import glm


class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/big.png')
        self.textures[1] = self.get_texture(path='textures/smol.png')
        self.textures[2] = self.get_texture(path='textures/noisy.png')
        
    def get_texture(self, path):
        texture = pg.transform.flip(
            pg.image.load(path).convert(), 
            flip_x=False, flip_y=True)
        
        return self.ctx.texture(size=texture.get_size(), components=3, 
                                data=pg.image.tostring(texture, "RGB"))
        
    def destroy(self):
        [tex.release() for tex in self.textures.values()]