import numpy as np
import numpy.linalg as la

class Bilinear:
    def inverseMatrix(self, points):
        B = np.zeros((len(points), 3))

        for pointi, point in enumerate(points):
            B[pointi, 0] = 1
            B[pointi, 1] = point[0]
            B[pointi, 2] = point[1]

        return la.pinv(B)

    def gradient(self, Binv, values):
        a_2 = np.dot(Binv[1], values) # d/dx
        a_3 = np.dot(Binv[2], values) # d/dz

        return (a_2, a_3)

class BilinearCross:
    def inverseMatrix(self, points):
        B = np.zeros((len(points), 4))

        for pointi, point in enumerate(points):
            B[pointi, 0] = 1
            B[pointi, 1] = point[0]
            B[pointi, 2] = point[1]
            B[pointi, 3] = point[0]*point[1]

        return la.pinv(B)

    def gradient(self, Binv, values):
        a_2 = np.dot(Binv[1], values) # d/dx
        a_3 = np.dot(Binv[2], values) # d/dz

        return (a_2, a_3)

class Quadratic:
    def inverseMatrix(self, points):
        B = np.zeros((len(points), 5))

        for pointi, point in enumerate(points):
            B[pointi, 0] = 1
            B[pointi, 1] = point[0]
            B[pointi, 2] = point[1]
            B[pointi, 3] = point[0]**2
            B[pointi, 4] = point[1]**2

        return la.pinv(B)

    def gradient(self, Binv, values):
        a_2 = np.dot(Binv[1], values) # d/dx
        a_3 = np.dot(Binv[2], values) # d/dz

        return (a_2, a_3)

