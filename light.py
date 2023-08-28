import glm

class Light(object):
    def __init__(self, position, color=(1, 1, 1)) -> None:
        self.pos = glm.vec3(position)
        self.color = glm.vec3(color)
        
        self.Ia = 0.1 * self.color  # ambient
        self.Id = 0.8 * self.color  # diffuse
        self.Is = 1.0 * self.color  # specular