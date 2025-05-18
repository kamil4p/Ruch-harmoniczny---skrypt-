#biblioteki
import numpy as np
import matplotlib as mat


def funkcjawar(prompt):
    while True:
        value = input(prompt)
        try: 
            value = float(value)
            if value <= 0:
                print ("Błąd - wartości muszą być większe od zera. Spróbuj ponownie.")
            else:
                return value
        except ValueError:
            print("Błąd. Podaj poprawne liczby.")
    
        
#Dane
omega = funkcjawar("Wprowadź prędkość kątową (rad/s^2): ")
A = funkcjawar("Wprowadź amplitudę A (m):" )
k = funkcjawar("Wprowadź współczynnik sprężystości k (N/m): ")



# Obliczenia
f = omega / (2 * np.pi)
T = 1 / f
E = 0.5 * k * A**2 

#Wyniki
print("-----Wyniki-----")
print(f"Częstotliwość: {f:.3f} Hz")
print(f"Okes: {T:.3f} s")
print(f"Okres: {E:.3f} J")


      




