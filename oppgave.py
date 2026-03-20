import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x / 4) * np.arctan(x)

def g(x):
    return np.arctan(x) - 4 / (1 + x**2)

# vet nullpunktet ligger mellom [1,2]. Sjekk arket for utregning
a = 1.0
b = 2.0
pres = 0.00001 # stopper når intervallet er mindre enn dette

# halveringsmetoden
while (b - a) / 2 > pres:   # gjentas til det er mindre enn pres
    c = (a + b) / 2         # finner midtpunktet av intervallet

    if g(a) * g(c) < 0:     # sjekker om np ligger mellom a og c
        b = c               
    else:
        a = c

x_max = (a + b) / 2        # x-koordinat til tp
y_max = f(x_max)           # y-koordinat til tp

x = np.linspace(0, 5, 500)
y = f(x)

plt.plot(x, y)
plt.plot(x_max, y_max, 'ro', label=f"Toppunkt ({x_max:.4f}, {y_max:.4f})")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funksjonen f(x) med toppunkt funnet med halveringsmetoden")
plt.grid(True)
plt.show()

print(f"Toppunkt: x = {x_max:.4f}, f(x) = {y_max:.4f}")

