# coding=utf-8
from math import *
import numpy as np
import matplotlib.pyplot as plt
from basic_shapes import Shape


# Sides must be an even number
# The number of triangles is sides/2 - 2
def createColorCircle(r, g, b, radius=1):
    sides = 32
    steps = pi / sides
    t = np.arange(-np.pi, np.pi, steps)
    x = radius * np.sin(t)
    y = radius * np.cos(t)
    # Defining locations and colors for each vertex of the shape
    vertices = []

    for i in range(len(x)):
        # Positions
        vertices.append(x[i])
        vertices.append(y[i])
        vertices.append(0.0)  # 2D
        # Colors
        vertices.append(r)
        vertices.append(g)
        vertices.append(b)

    # Defining connections among vertices
    indices = []
    nodos = len(x)
    for i in range(nodos):
        if (i != 0) and (i != (nodos - 1)):
            indices.append(0)
            indices.append(i)
            indices.append(i + 1)
    return Shape(vertices, indices)


# Sides must be an even number
# The number of triangles is sides/2 - 2
def createColorCircumference(r, g, b, radius=1):
    sides = 10
    steps = 0.01
    t = np.arange(-np.pi, np.pi, steps)
    x = radius * np.sin(t)
    y = radius * np.cos(t)
    radius2 = 0.99
    x2 = radius2 * np.sin(t)
    y2 = radius2 * np.cos(t)
    # Defining locations and colors for each vertex of the shape
    vertices = []

    for i in range(len(x)):
        # Outer circle
        # Positions
        vertices.append(x[i])
        vertices.append(y[i])
        vertices.append(0.0)  # 2D
        # Colors
        vertices.append(r)
        vertices.append(g)
        vertices.append(b)

    for i in range(len(x)):
        # Inner circle
        # Positions
        vertices.append(x2[i])
        vertices.append(y2[i])
        vertices.append(0.0)  # 2D
        # Colors
        vertices.append(r)
        vertices.append(g)
        vertices.append(b)

    # Defining connections among vertices
    indices = []
    nodos = len(x)
    for i in range(nodos):
        if i < nodos - 1:
            indices.append(i)
            indices.append(i + 1)
            indices.append(i + 629)
            indices.append(i + 629)
            indices.append(i + 629 + 1)
            indices.append(i + 1)
    return Shape(vertices, indices)


def createGradientQuad(r1, g1, b1, r2, g2, b2):
    # Defining locations and colors for each vertex of the shape
    vertices = [
        #   positions        colors
        -0.5, -0.5, 0.0, r1, g1, b1,
        0.5, -0.5, 0.0, r1, g1, b1,
        0.5, 0.5, 0.0, r2, g2, b2,
        -0.5, 0.5, 0.0, r2, g2, b2]

    # Defining connections among vertices
    # We have a triangle every 3 indices specified
    indices = [
        0, 1, 2,
        2, 3, 0]

    return Shape(vertices, indices)


# The number of triangles is sides/2 - 2
def createColorSphere(r, g, b, sides=32):
    t = np.linspace(-np.pi, np.pi, sides+1)
    z = np.linspace(-1, 1, sides+1)
    angle = np.linspace(0, np.pi, sides+1)
    radius = np.sin(angle)

    # Defining locations and colors for each vertex of the shape
    vertices = []
    for j in range(sides + 1):
        if j == 0 or j == sides:
            vertices += [0, 0, z[j]]
            vertices += [r, g, b]
        else:
            x = radius[j] * np.sin(t)
            y = radius[j] * np.cos(t)

            for i in range(sides):
                vertices += [x[i], y[i], z[j]]  # Positions
                vertices += [r, g, b]  # Colors

    # Defining connections among vertices
    indices = []
    nodes = len(vertices)//6
    #for i in range(nodes):
    #    if i == 0:  # Triangulos inferiores
    #        #for j in range(i+1, sides):
    #        #    indices += [i, j, (j+1) % (sides+1)]
    #        #indices += [i, sides, 1]
    #        continue
    #    elif i == nodes - 1:  # Triangulos superiores
    #        #for j in range(i-sides, i-1):
    #        #    indices += [i, j, j+1]
    #        #indices += [i, i-1, i-sides]
    #        continue
    #    elif i <= 4:
    #        indices += [i, i+1, i+sides]
    #        indices += [i+1, i+sides, i+1+sides]

# Cheking every level
    for i in range(sides):
        print(f"level = {i}")
        if i == 0:  # Triangulos inferiores
            print("Case 1")
            for j in range(i+1, sides):
                indices += [i, j, (j+1) % (sides+1)]
                print(f"{i} {j} {(j+1) % (sides+1)}")
            indices += [i, sides, 1]
            print(f"{i} {sides} {1}")
        elif i == sides - 1:  # Triangulos superiores
            print("Case 2")
            for j in range(0, sides):
                k = (sides - 1) * i + j
                if j == sides - 1:
                    indices += [nodes - 1, k, (sides - 1) * i]
                    print(f"{nodes - 1} {k} {(sides - 1) * i}")
                else:
                    indices += [nodes - 1, k, k+1]
                    print(f"{nodes - 1} {k} {k+1}")
        else:
            print("Case 3")
            for j in range(1, sides+1):
                k = (i - 1) * sides + j
                if j == sides + 1:
                    indices += [k, k + 1, k + sides]
                    print(f"{k} {k + 1} {k + sides}")
                    indices += [k + 1, (i - 1) * sides + 1, k + 1 + sides]
                    print(f"{k + 1} {(i - 1) * sides + 1} {k + 1 + sides}")
                else:
                    indices += [k, k+1, k+sides]
                    print(f"{k} {k+1} {k + sides}")
                    indices += [k+1, k+sides, k+1+sides]
                    print(f"{k+1} {k + sides} {k+1+sides}")

    #for i in range(0, len(indices), 3):
    #    print(f"{indices[i]} {indices[i+1]} {indices[i+2]}")

    #print(X)
    #print(Y)
    #print(Z)

    return Shape(vertices, indices)
