__all__ = ["interp_vandermonde"]

import numpy as np
from GaussianElimination import resolver



class interp_vandermonde:
    def __init__(self, xi, yi):
        """Encuentra los coeficientes a[n] de un polinomio p(x)=sum( a[n]*x^n,
        n=0,N), con N el número de puntos {xi,yi}."""

        xi = np.asarray(xi)
        yi = np.asarray(yi)
        
        self.dim = xi.size
        
        # crea una matriz de Vandermonde
        V = np.vander(xi, increasing=True)

        # usa eliminacion gaussiana para encontrar los coeficientes a[n]
        # luego, guarda cada coeficiente en una lista
        self.coefs = resolver(V, yi)

        
    def __call__(self, x):
        """evalúa el polinomio interpolado en un punto x"""
        x = np.asarray(x)
        
        value = self.coefs[-1]
        for i in range(2,self.dim+1):
            value = self.coefs[-i] + value * x

        return value
        
        
        
