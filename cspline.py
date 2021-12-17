import numpy as np
from GaussianElimination import resolver

class cspline:
    def __init__(self, xp, yp):
        self.xp = np.asarray(xp)
        self.yp = np.asarray(yp)
        
        pendiente = np.empty(self.yp.shape)

        pendiente[0]    = 3*(self.yp[1] - self.yp[0])
        pendiente[1:-1] = 3*(self.yp[2:] - self.yp[:-2] )                                     
        pendiente[-1]   = 3*(self.yp[-1] - self.yp[-2])

        matriz = np.zeros((self.xp.size, self.xp.size))

        matriz[0,:2] = [2.0, 1.0]
        matriz[-1, -2:] = [1.0, 2.0]

        for i in range(1, self.xp.size-1):
            matriz[i, i-1:i+2] = [1.0, 4.0, 1.0]

        self.a = resolver(matriz, pendiente)

        self.b = 3*(self.yp[1:] - self.yp[:-1]) - 2*self.a[:-1] - self.a[1:]
        self.c = self.a[:-1] + self.a[1:] - 2*(self.yp[1:] - self.yp[:-1])

    def __call__(self, x):
        x = np.asarray(x)

        i = np.where( np.logical_and( self.xp[:-1,None] <= x[None,:],
                                            self.xp[1:,None]  >  x[None,:] ))[0]

        t = (x - self.xp[i]) / (self.xp[i+1] - self.xp[i]) 

        return self.yp[i] + t * ( self.a[i] + t * (self.b[i] + t * self.c[i])) 


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    
    xp = [0, 1, 2, 3, 4]
    yp = [0, 2, -4, 8, -16]
    
    sp = cspline(xp, yp) 

    x = np.linspace(np.min(xp), np.max(xp), 20, endpoint=False)
    y = sp(x)

    plt.plot(x, y, '.')
    plt.scatter(xp, yp)
    plt.show()

    
