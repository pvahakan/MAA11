import numpy as np
import matplotlib.pyplot as plt

# Ratkaistaan yhtälö x - cox(x) = 0
def f(x):
    # return np.cos(x)
    return np.sqrt(x + 4)

x = np.linspace(-3, 9, 100)
y = f(x)

plt.plot(x, y)
plt.plot(x, x)
plt.grid(True)
plt.show()

x_i = 1 # float(input('Anna alkuarvaus: '))
i = 0
virhemarginaali = 0.00001

while abs(x_i - f(x_i)) > virhemarginaali:
    x_i = f(x_i)
    i += 1

print(f'Yhtälön ratkaisu on x = {x_i}')
print(f'f(x_i) = {f(x_i)}')
print(f'Iteraatioita: {i} kpl.')

plt.plot(x, y)
plt.plot(x, x)
plt.grid(True)
plt.plot(x_i, f(x_i), 'x', color='red')
plt.show()