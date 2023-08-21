# Cierto texto en inglés fue cifrado utilizando un cifrado de Vigenere. El siguiente
# criptograma corresponde al texto cifrado:
# THZEIPHMRRRGOSRKRUDWVLKNUSITAGSOKOEPHMRRRG
# - ¿Cuál es la clave utilizada para cifrar el texto?
# - ¿Cuál es el mensaje en texto claro?

from collections import Counter


mensaje = "THZEIPHMRRRGOSRKRUDWVLKNUSITAGSOKOEPHMRRRG"
mensaje_size = len(mensaje)

# calcular el IC para diferentes longitudes de clave y comparar los resultados con el IC esperado para el idioma inglés.
ic_ingles = 0.0667


def calcular_ic(texto):
    if not texto:
        return 0
    frecuencias = {}
    for letra in texto:
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
    ic = 0
    n = len(texto)
    for letra in frecuencias:
        ic += frecuencias[letra] * (frecuencias[letra] - 1)
    ic /= n * (n - 1)
    return ic


def calcular_ic_para_longitudes_de_clave(texto_cifrado, longitudes_de_clave):
    resultados = {}
    for longitud in longitudes_de_clave:
        segmentos = [texto_cifrado[i:i+longitud] for i in range(0, len(texto_cifrado), longitud)]
        ic_total = 0
        for segmento in segmentos:
            ic_total += calcular_ic(segmento)
        resultados[longitud] = ic_total / len(segmentos)
    return resultados



# Cierto texto en inglés fue cifrado utilizando un cifrado de Vigenere. El siguiente
# criptograma corresponde al texto cifrado:
# THZEIPHMRRRGOSRKRUDWVLKNUSITAGSOKOEPHMRRRG
# - ¿Cuál es la clave utilizada para cifrar el texto?
# - ¿Cuál es el mensaje en texto claro?

from collections import Counter


mensaje = "THZEIPHMRRRGOSRKRUDWVLKNUSITAGSOKOEPHMRRRG"
mensaje_size = len(mensaje)

# calcular el IC para diferentes longitudes de clave y comparar los resultados con el IC esperado para el idioma inglés.
ic_ingles = 0.0667


def calcular_ic(texto):
    if not texto:
        return 0
    frecuencias = {}
    for letra in texto:
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
    ic = 0
    n = len(texto)
    for letra in frecuencias:
        ic += frecuencias[letra] * (frecuencias[letra] - 1)
    ic /= n * (n - 1)
    return ic



def calcular_ic_para_longitudes_de_clave(texto_cifrado, longitudes_de_clave):
    resultados = {}
    for longitud in longitudes_de_clave:
        segmentos = [texto_cifrado[i:i+longitud] for i in range(0, len(texto_cifrado), longitud)]
        ic_total = 0
        for segmento in segmentos:
            ic_total += calcular_ic(segmento)
        resultados[longitud] = ic_total / len(segmentos)
    return resultados

ic_final = {}


for longitud in range(2, 41):
    ic = calcular_ic_para_longitudes_de_clave(mensaje, [longitud])[longitud]
    ic_final[longitud] = ic



print(ic_final)

# #tomar solo los que tengan el ic mas cercano arriba de 0.06
# ic_final = {k: v for k, v in ic_final.items() if v > 0.06}
# print(ic_final)


#probar con las longitudes de clave que quedaron
for longitud in ic_final:
    print("Longitud de clave:", longitud)
    clave = ""
    for i in range(longitud):
        subcadena = mensaje[i::longitud]
        frecuencias = Counter(subcadena)
        letra_mas_comun = frecuencias.most_common(1)[0][0]
        clave += chr((ord(letra_mas_comun) - ord('E')) % 26 + ord('A'))
    print("La clave es:", clave)
    

def descript_vigerene(mensaje, clave):
    mensaje_descifrado = ""
    for i in range(len(mensaje)):
        letra_mensaje = ord(mensaje[i]) - ord('A')
        letra_clave = ord(clave[i % len(clave)]) - ord('A')
        letra_descifrada = chr(((letra_mensaje - letra_clave) % 26) + ord('A'))
        mensaje_descifrado += letra_descifrada
    return mensaje_descifrado

for longitud in ic_final:
    clave = ""
    for i in range(longitud):
        subcadena = mensaje[i::longitud]
        frecuencias = Counter(subcadena)
        letra_mas_comun = frecuencias.most_common(1)[0][0]
        clave += chr((ord(letra_mas_comun) - ord('E')) % 26 + ord('A'))
    print("______________________________________________________________")
    print("Longitud de clave:", longitud)
    print("La clave es:", clave)
    print("El mensaje descifrado es:", descript_vigerene(mensaje, clave))
    print("______________________________________________________________")

    
