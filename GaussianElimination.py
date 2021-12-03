__all__ = ["resolver", "det", "inversa"]

import numpy as np

def _forward_elimination(M):
    L0 = M[0] / M[0,0]

    for i in range(1,len(M)):
        M[i] = M[i] - M[i,0] * L0


def _backward_elimination(M):
    n = len(M)-1

    M[n] = M[n] / M[n,n]

    for i in range(len(M)-1):
        M[i] = M[i] - M[i,n] * M[n]
    
        
def Gaussian_elimination(M):
    """retorna M en forma escalonada o triangular superior"""

    for i in range(len(M)-1):
        _forward_elimination(M[i:,i:])


def GaussJordan_elimination(M):
    """retorna M en forma escalonada reducida"""
    _backward_elimination(M)

    for i in range(1,len(M)):
        _backward_elimination(M[:-i])
        

def resolver(A, b):
    aumentada = np.hstack( (A, b[:,None]) )
    Gaussian_elimination(aumentada)
    GaussJordan_elimination(aumentada)

    return aumentada[:, -1]


def det(M):
    A = M.copy()

    Gaussian_elimination(A)

    return np.prod( A.diagonal() )


def inversa(M):
    dim = len(M)
    
    aumentada = np.hstack( (M, np.identity(dim)) )
    
    Gaussian_elimination(aumentada)
    GaussJordan_elimination(aumentada)

    return aumentada[:, -dim:]
        
# A = np.array([[1, 1, 1], [-1, 2, 0], [2, 0, 1]], dtype="float64")
# b = np.array([6,3,5])

# print( resolver(A, b) )

