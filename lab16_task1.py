import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 11, 51)
y = np.sqrt(np.exp(x) + x**2)

plt.plot(x, y, 'r--', label='y = sqrt(e^x + x^2)')

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title('Графік функції')
plt.legend()

plt.savefig('quadrate.png', dpi=300)
plt.show()