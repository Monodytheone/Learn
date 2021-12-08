import numpy as np


A = np.mat([0, 0, 0,])
B = np.mat([2, 0, 0])
C = np.mat([2, 3, 0])
D = np.mat([0, 3, 0])
E = np.mat([0, 0, 2])
F = np.mat([2, 0, 2])
G = np.mat([2, 3, 2])
H = np.mat([0, 3, 2])

# print(A, B, C, D, E, F, G, H)
T_3d = np.mat([[0.5, 0, 0, 0],
               [0, 0.3333, 0, 0],
               [0, 0, 0.5, 0],
               [0, 0, 0, 1]])
print(T_3d)
resA = A * T_3d
print(resA)