from PolyClass import Poly

import numpy as np

class Neville(Poly):
    def __init__(self, xp, yp):
        super().__init__([0])
        
        self.xp = np.asarray(xp)
        self.yp = np.asarray(yp)

        p = [Poly([yi]) for yi in yp]
        
        for j in range(1,len(yp)):
            for i in range(len(yp)-j):
                factor = 1.0/(xp[i]-xp[i+j])
                pol1 = Poly([-xp[i+j], 1])
                pol2 = Poly([-xp[i], 1])

                p[i] = factor*( pol1*p[i] - pol2*p[i+1])

        self.coef = p[0].coef


# esto es para testear el código directamente
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    
    # xp = [1, 2, 5, 7, 8, 9]
    # yp = [1, -2, -1, -2, 0, 2]
    npoints = 100
    xp = np.linspace(1, 9, npoints)
    yp = np.random.randn(npoints)
    
    p = Neville(xp, yp)

    print(f"xp = {xp}")
    print(f"yp = {yp}")
    print(f"Polinomio interpolado: {p}")

    x = np.linspace(0.5, 9.5, 500)
    plt.plot(x, p(x), label="polinomio interpolado")
    plt.scatter(xp, yp, label="puntos interpolados")
    plt.legend()
    plt.title("Método de Neville")
    plt.xlabel(r"$x$")
    plt.ylabel(r"$y$")
    plt.ylim(-3,3)
    plt.show()


