# -*- coding: utf-8 -*-
"""tugas_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Gvbv_usoPHRkdKdtx922WwtV7ABYxnv_

Tugasss
"""

import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung suhu berdasarkan Hukum Pendinginan Newton
def calculate_temperature(T0, Ta, k, t):
    """
    Menghitung suhu benda pada waktu tertentu menggunakan Hukum Pendinginan Newton.

    Parameter:
     T0: Suhu awal benda (°C)
     Ta: Suhu lingkungan stabil (°C)
     k: Konstanta laju perpindahan panas (1/detik)
     t: Array waktu (detik)

    Return:
    - Suhu benda (°C) pada setiap waktu dalam t
    """
    return np.exp(-k * t) * (T0 - Ta) + Ta

# Parameter awal
T0 = 120  # Suhu awal benda, misalnya suhu air panas (°C)
Ta = 30   # Suhu lingkungan stabil, misalnya suhu ruangan (°C)
k = 0.05  # Konstanta perpindahan panas
time = np.linspace(0, 100, 500)  # Rentang waktu (detik)

# Hitung suhu berdasarkan waktu
temperature = calculate_temperature(T0, Ta, k, time)

# Plot grafik suhu terhadap waktu
plt.figure(figsize=(8, 6))
plt.plot(time, temperature, label="Suhu $T(t)$", color="blue")
plt.axhline(y=Ta, color="red", linestyle="--", label="Suhu Lingkungan $T_a$")
plt.title("Grafik Suhu terhadap Waktu (Hukum Pendinginan Newton)")
plt.xlabel("Waktu (detik)")
plt.ylabel("Suhu (°C)")
plt.legend()
plt.grid()
plt.show()