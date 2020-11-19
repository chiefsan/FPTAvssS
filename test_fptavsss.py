import fptavsss
import numpy as np

def test_0d():
    assert 1==1

def test_1d():
    def distance(a,b):
        return np.linalg.norm(a-b)
    Y = [0, 2, 3, 4, 5, 6, 7]
    M = 2
    epsilon = 0.5
    solver = fptavsss.Solver(Y, M, epsilon, distance)
    print (solver.solve())

def test_2d():
    def distance(a,b):
        a = np.array(a)
        b = np.array(b)
        return np.linalg.norm(a-b)
    Y = [(0, 0), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]
    M = 2
    epsilon = 0.5
    solver = fptavsss.Solver(Y, M, epsilon, distance)
    print (solver.solve())

def test_3d():
    def distance(a,b):
        a = np.array(a)
        b = np.array(b)
        return np.linalg.norm(a-b)
    Y = [(0, 0, 0), (0, 2, 0), (0, 3, 0), (0, 4, 0), (0, 5, 0), (0, 6, 0), (0, 7, 0)]
    M = 2
    epsilon = 0.5
    solver = fptavsss.Solver(Y, M, epsilon, distance)
    print (solver.solve())