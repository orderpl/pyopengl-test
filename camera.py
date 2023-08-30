import glm
import pygame as pg

FOV = 90
NEAR = 0.001
FAR = 100

SPEED = 0.075
BOOST_MP = 1.5

SENSITIVITY = 0.2

UP = glm.vec3(0, 1, 0)

class Camera(object):
    def __init__(self, app, position=(0, 0, 4), yaw=-90, pitch=0) -> None:
        self.app = app
        self.aspect_ratio = app.WIN_RESOLUTION[0] / app.WIN_RESOLUTION[1]
        
        self.pos = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0) # direction that top of the camera is pointing to
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        
        self.yaw, self.pitch = yaw, pitch
        
        self.m_view = self.get_view_matrix()
        self.m_proj = self.get_projection_matrix()
        
    def update(self):
        self.move()
        
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()
        
    def move(self):
        keys = pg.key.get_pressed()
        vel = SPEED * 1 if not keys[pg.K_LCTRL] else BOOST_MP
        if keys[pg.K_w]:
            self.pos += self.forward * vel
        if keys[pg.K_s]:
            self.pos -= self.forward * vel
        if keys[pg.K_d]:
            self.pos += self.right * vel
        if keys[pg.K_a]:
            self.pos -= self.right * vel
        if keys[pg.K_SPACE]:
            self.pos += UP * vel
        if keys[pg.K_LSHIFT]:
            self.pos -= UP * vel
            
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch += -rel_y * SENSITIVITY
        self.pitch = max(-90, min(90, self.pitch))
        
    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))
                
    def get_view_matrix(self):
        return glm.lookAt(self.pos, self.pos + self.forward, self.up)
        
    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)