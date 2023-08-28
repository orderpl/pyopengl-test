import glm

FOV = 90 
NEAR = 0.1
FAR = 100

class Camera(object):
    def __init__(self, app) -> None:
        self.app = app
        self.aspect_ratio = app.WIN_RESOLUTION[0] / app.WIN_RESOLUTION[1]
        
        self.pos = glm.vec3(2, 3, 3)
        self.up = glm.vec3(0, 1, 0) # direction that top of the camera is pointing to
        
        self.m_view = self.get_view_matrix()
        self.m_proj = self.get_projection_matrix()
        
    
    def get_view_matrix(self):
        return glm.lookAt(self.pos, glm.vec3(0), self.up)
        
    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)