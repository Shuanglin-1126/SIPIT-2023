import math
import numpy as np

def image_world(a, b):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    in_matrix = [[1885.8, 0, 791.6],
                 [0, 1877.1, 673.3],
                 [0, 0, 1]]
    out_r_matrix = [[0.99927543, -0.01742397, 0.03383805],
                  [0.02902416, 0.92397992, -0.38133805],
                  [-0.02462126, 0.38204387, 0.92381615]]
    out_t_matrix = [[-0.04947418], [-0.03458971], [0.14245446]]
    in_matrix = np.array(in_matrix)
    out_r_matrix = np.array(out_r_matrix)
    out_t_matrix = np.array(out_t_matrix)
    image_matrix = [[a], [b], [1.0]]
    image_matrix = np.array(image_matrix, dtype=object)
    world_matrix = np.dot(np.linalg.inv(np.dot(in_matrix, out_r_matrix)),
                          (image_matrix - np.dot(in_matrix, out_t_matrix)))
    world_matrix = world_matrix * 100
    world_matrix[0] = world_matrix[0] + 40.05470
    world_matrix[1] = world_matrix[1] - 3.46084

    world_x = 0.07225 * a
    world_y = 0.07225 * b
    return world_matrix[0], world_matrix[1], world_x, world_y

