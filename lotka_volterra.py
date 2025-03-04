# -*- coding: utf-8 -*-
"""Lotka-Volterra.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D_ObSgxBM_pqII5FT6uv4G7EOsaI-eqR
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# parameter model
alpha = 0.5     # Laju pertumbuhan mangsa (rusa)
beta = 0.02     # tingkat perburuan oleh predator
delta = 0.01    # efisiensi konversi menjadi predator
gamma = 0.3     # tingkat kematian alami predator

# Persamaan diferensial Lotka-volterra
def lotka_volterra(y, t, alpha, beta, delta, gamma):
    x, y = y
    dxdt = alpha * x - beta * x * y   # pertumbuhan populasi rusa
    dydt = delta * x * y - gamma * y  # pertumbuhan populasi serigala
    return [dxdt, dydt]

# Kondisi awal: jumlah awal rusa dan serigala
y0 = [40, 9]

# Rentang waktu simulasi (0 sampai 200 unit waktu)
t = np.linspace(0, 200, 1000)

# Menyelesaikan persamaan diferensial
solution = odeint(lotka_volterra, y0, t, args=(alpha, beta, delta, gamma))
rusa, serigala = solution.T   # Memisahkan hasil ke dua variabel

# Membuat grafik simulasi
plt.figure(figsize=(10, 5))
plt.plot(t, rusa, label="Rusa(Prey)", color="blue", linewidth=2)
plt.plot(t, serigala, label="Serigala(Predator)", color="red", linewidth=2)
plt.xlabel("waktu")
plt.ylabel("populasi")
plt.title("Simulasi Model Lotka-Voltrra: Rusa vs Serigala")
plt.legend()
plt.grid()
plt.show()