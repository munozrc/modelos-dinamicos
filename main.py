import matplotlib.pyplot as plt
import np

# Ejemplo: Aproximando el valor de pi - área de un círculo de
# radio = 1.

N = 10000
plt.figure("Área de un círculo de radio = 1 by Carlos Muñoz ", figsize=(8,8))  # tamaño de la figura

x, y = np.random.uniform(-1, 1, size=(2, N))
interior = (x**2 + y**2) <= 1
pi = interior.sum() * 4 / N
error = abs((pi - np.pi) / pi) * 100
exterior = np.invert(interior)

plt.plot(x[interior], y[interior], 'b.')
plt.plot(x[exterior], y[exterior], 'r.')
plt.plot(0, 0, label='$\hat \pi$ = {:4.4f}\nerror = {:4.4f}%'.format(pi,error), alpha=0)
plt.axis('square')
plt.legend(frameon=True, framealpha=0.9, fontsize=16)
plt.show()
