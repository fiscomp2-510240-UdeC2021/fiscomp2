from PolyClass import Poly

import numpy as np

class Lagrange(Poly):
    def __init__(self, xp, yp):
        super().__init__([0])
        
        self.xp = np.asarray(xp)
        self.yp = np.asarray(yp)

        L = [Poly([-xj,1]) for xj in xp]

        pol = Poly([0.0])

        # para cada valor de i, calcula polinomios de Lagrange
        for i,(xi,yi) in enumerate(zip(xp,yp)):
            tmp = np.prod(L[:i]) * np.prod(L[i+1:])
            tmp = tmp * (yi / tmp(xi))

            pol = pol + tmp

        self.coef = pol.coef

# esto es para testear el código directamente
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    
    xp = [1, 2, 5, 7, 8, 9]
    yp = [1, -2, -1, -2, 0, 2]
    # npoints = 20
    # xp = np.linspace(1, 9, npoints)
    # yp = np.random.randn(npoints)
    
    p = Lagrange(xp, yp)

    print(f"xp = {xp}")
    print(f"yp = {yp}")
    print(f"Polinomio interpolado: {p}")

    x = np.linspace(0.5, 9.5, 500)
    plt.plot(x, p(x), label="polinomio interpolado")
    plt.scatter(xp, yp, label="puntos interpolados")
    plt.legend()
    plt.title("Método de Lagrange")
    plt.xlabel(r"$x$")
    plt.ylabel(r"$y$")
    plt.ylim(-3,3)
    plt.show()


