from collections import Counter
import math

def friedman_test(ciphertext, max_key_length):
    # Calcular el índice de coincidencia para cada longitud de clave
    ic_values = []
    for key_length in range(1, max_key_length + 1):
        ic_sum = 0
        for i in range(key_length):
            segment = ciphertext[i::key_length]
            freqs = Counter(segment)
            ic = sum([n * (n - 1) for n in freqs.values()]) / (len(segment) * (len(segment) - 1))
            ic_sum += ic
        ic_values.append(ic_sum / key_length)
    
    # Encontrar la longitud de clave más probable
    most_likely_key_length = ic_values.index(max(ic_values)) + 1
    
    return most_likely_key_length

# Ejemplo de uso
ciphertext = "THZEIPHMRRRGOSRKRUDWVLKNUSITAGSOKOEPHMRRRG"
max_key_length = 6

def indice_de_coincidencia(cadena):
    n = len(cadena)
    frecuencias = Counter(cadena)
    suma = 0
    for letra in frecuencias:
        suma += frecuencias[letra] * (frecuencias[letra] - 1)
    indice = suma / (n * (n - 1))
    return indice

def encontrar_clave(cadena, longitud_clave):
    clave = ""
    for i in range(longitud_clave):
        subcadena = cadena[i::longitud_clave]
        frecuencias = Counter(subcadena)
        letra_mas_comun = frecuencias.most_common(1)[0][0]
        clave += chr((ord(letra_mas_comun) - ord('E')) % 26 + ord('A'))
    return clave



most_likely_key_length = friedman_test(ciphertext, max_key_length)

print(f"La longitud de clave más probable es: {most_likely_key_length}")

indice = indice_de_coincidencia(ciphertext)
print("El índice de coincidencia es:", indice)

clave = encontrar_clave(ciphertext, most_likely_key_length)
print("La clave es:", clave)




