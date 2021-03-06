"""
Dibuja --> main
"""


import json
import basic_shapes as bs
from controller import *
import numpy as np
import transformations2 as tr2


def main(*args):
    return 0


if __name__ == "__main__":
    # Initialize glfw
    if not glfw.init():
        sys.exit()

    width  = 650
    height = 650

    window = glfw.create_window(width, height, "Sistema Planetario", None, None)

    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)

    controller = Controller()

    # Connecting the callback function 'on_key' to handle keyboard events
    glfw.set_key_callback(window, controller.on_key)

    # Assembling the shader program (pipeline) with both shaders
    pipeline = es.SimpleTransformShaderProgram()
    pipeline2 = es.SimpleTextureTransformShaderProgram()
    # Creating shader programs for textures and for colores
    textureShaderProgram = es.SimpleTextureModelViewProjectionShaderProgram()
    colorShaderProgram = es.SimpleModelViewProjectionShaderProgram()

    # Telling OpenGL to use ou shader program
    glUseProgram(pipeline.shaderProgram)

    # Setting up the clear screen color
    glClearColor(23 / 255, 9 / 255, 54 / 255, 1.0)

    # Profundidad: activa la camara 3D
    #glEnable(GL_DEPTH_TEST)

    # Our shapes here are always fully painted
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    gpuShape = es.toGPUShape(bs.createTextureQuad("starry_sky.png", 1, 1), GL_REPEAT, GL_LINEAR)

    # Creamos la camara y la proyección
    projection = tr2.ortho(-1, 1, -1, 1, 0.1, 100)
    view = tr2.lookAt(
        np.array([10, 10, 5]),  # Donde está parada la cámara
        np.array([0, 0, 0]),  # Donde estoy mirando
        np.array([0, 0, 1])  # Cual es vector UP
    )

    sphere = Sphere([1, 1, 1], 0.2)
    axis = Axis()

    # Acá se dibuja
    while not glfw.window_should_close(window):
        # Using GLFW to check for input events
        glfw.poll_events()

        # Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT)

        # Background
        glUseProgram(pipeline2.shaderProgram)
        glUniformMatrix4fv(glGetUniformLocation(pipeline.shaderProgram, "transform"), 1, GL_TRUE, tr.uniformScale(2))
        pipeline2.drawShape(gpuShape)

        # Dibujar modelos
        sphere.draw(colorShaderProgram, textureShaderProgram, projection, view)
        axis.draw(colorShaderProgram, projection, view)

        # Once the render is done, buffers are swapped, showing only the complete scene.
        glfw.swap_buffers(window)

    glfw.terminate()
