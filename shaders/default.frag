# version 330 core

layout (location = 0) out vec4 fragColor;

in vec2 uv_0;
in vec3 normal;
in vec3 fragPos;

struct Light {
    vec3 pos; // position
    vec3 color;
    vec3 Ia; // ambient lighting intensity
    vec3 Id; // diffuse
    vec3 Is; // specular
};

uniform Light light;
uniform vec3 camPos;
uniform sampler2D u_texture_0;

vec3 calcLight(vec3 color) {
    vec3 ambient = light.Ia;

    vec3 lightDir = normalize(light.pos - fragPos);
    float diff = max(0, dot(lightDir, normal));
    vec3 diffuse = diff * light.Id;

    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0), 32);
    vec3 specular = spec * light.Is;
    
    return color * (ambient + diffuse + specular);
}

void main() {
    vec3 color = texture(u_texture_0, uv_0).rgb;
    color = calcLight(color);
    fragColor = vec4(color, 1.0);
}