
# biblioteki
import numpy as np
import matplotlib.pyplot as plt

# Obsługa błędnych danych
def funkcjawar(dane):
    while True:
        value = input(dane)
        try: 
            value = float(value)
            if value <= 0:
                print ("Błąd - wartości muszą być większe od zera. Spróbuj ponownie.")
            else:
                return value
        except ValueError:
            print("Błąd. Podaj poprawne liczby.")
    
        
# Zmienne
omega = funkcjawar("Wprowadź prędkość kątową (rad/s^2): ")
A = funkcjawar("Wprowadź amplitudę A (m):" )
k = funkcjawar("Wprowadź współczynnik sprężystości k (N/m): ")



# Obliczenia na zmiennych
f = omega / (2 * np.pi)
T = 1 / f
E = 0.5 * k * A**2 

# Wyniki
print("-----Wyniki-----")
print(f"Częstotliwość: {f:.3f} Hz")
print(f"Okes: {T:.3f} s")
print(f"Okres: {E:.3f} J")


# Obliczenia na zmiennych v2
t = np.linspace(0, 2*T, 1000)
x = A * np.sin(omega * t)
v = A * omega * np.cos(omega * t)
a = -A * omega**2 * np.sin(omega * t)

      
# Wykresy
fig, axs = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle(f"Pełna analiza ruchu harmonicznego (ω = {omega:.2f} rad/s², A = {A:.2f} m)", fontsize=16)


# 1. x(t)
axs[0, 0].plot(t, x, color='red')
axs[0, 0].set_title("Położenie x(t)")
axs[0, 0].set_xlabel("Czas t [s]")
axs[0, 0].set_ylabel("Położenie x [m]")
axs[0, 0].grid(True)


# 2. v(t)
axs[0, 1].plot(t, v, color='orange')
axs[0, 1].set_title("Prędkość v(t)")
axs[0, 1].set_xlabel("Czas t [s]")
axs[0, 1].set_ylabel("Prędkość v [m/s]")
axs[0, 1].grid(True)



# 3. a(t)
axs[0, 2].plot(t, a, color='yellow')
axs[0, 2].set_title("Przyspieszenie a(t)")
axs[0, 2].set_xlabel("Czas t [s]")
axs[0, 2].set_ylabel("Przyspieszenie a [m/s²]")
axs[0, 2].grid(True)

# 4. v(x)
axs[1, 0].plot(x, v, color='purple')
axs[1, 0].set_title("Prędkość od polożenia v(x)")
axs[1, 0].set_xlabel("Położenie x [m]")
axs[1, 0].set_ylabel("Prędkość v [m/s]")
axs[1, 0].grid(True)

# 5. a(x)
axs[1, 1].plot(x, a, color='blue')
axs[1, 1].set_title("Przyspieszenie od polożenia a(x)")
axs[1, 1].set_xlabel("Położenie x [m]")
axs[1, 1].set_ylabel("Przyspieszenie a [m/s²]")
axs[1, 1].grid(True)

# 6. a(v)
axs[1, 2].plot(v, a, color='green')
axs[1, 2].set_title("Przyspieszenie od prędkości a(v)")
axs[1, 2].set_xlabel("Prędkość v [m/s]")
axs[1, 2].set_ylabel("Przyspieszenie a [m/s²]")
axs[1, 2].grid(True)

# Wykresy v2
plt.tight_layout()
plt.show()
