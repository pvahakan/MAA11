import matplotlib.pyplot as plt
import numpy as np

# Määritellään funktio, joka ratkaistaan
def f(x):
    # return np.exp(-0.5*x) - 1
    # return -3*x**3 + 2*x**2 - 3*x + 5
    return x + np.log(x)


# Piirretään funktion kuvaaja
x = np.linspace(0.0001, 3, 100)
y = f(x)

plt.plot(x, y)
plt.grid(True)
plt.show()


# Annetaan ratkaistavan välin tiedot
alaraja = 0.0001 # float(input('Anna alaraja: '))
ylaraja = 4 # float(input('Anna yläraja: '))

virhemarginaali = 0.00000001
i = 0 # Laskuri iteraatioita varten

keskipiste = (ylaraja + alaraja) / 2

# Ratkaistaan yhtälö puolitusmenetelmällä
while abs(f(keskipiste) - 0) > virhemarginaali:
    i += 1
    if f(keskipiste) < 0 and f(alaraja) < 0:
        alaraja = keskipiste
    elif f(keskipiste) > 0 and f(ylaraja) > 0:
        ylaraja = keskipiste
    # # Edistyneempi ratkaisu
    # if f(keskipiste) * f(alaraja) > 0:
    #     alaraja = keskipiste
    # elif f(keskipiste) * f(ylaraja) > 0:
    #     ylaraja = keskipiste

    keskipiste = (ylaraja + alaraja) / 2

# Tulostetaan tiedot näkyviin
print(f'keskipiste: {keskipiste}')
print(f'f(keskipiste): {f(keskipiste)}')
print(f'Iteraatioita {i} kpl.')
    
# Piirretään funktion kuvaaja ja merkitään siihen ratkaisukohta
plt.plot(x, y)
plt.grid(True)
plt.plot(keskipiste, f(keskipiste), 'x', color='red')
plt.show()