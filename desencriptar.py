mensaje = "THZEIPHMRRRGOSRKRUDWVLKNUSITAGSOKOEPHMRRRG"
clave = "EDGAR"

mensaje_descifrado = ""
for i in range(len(mensaje)):
    letra_mensaje = ord(mensaje[i]) - ord('A')
    letra_clave = ord(clave[i % len(clave)]) - ord('A')
    letra_descifrada = chr(((letra_mensaje + letra_clave) % 26) + ord('A'))
    mensaje_descifrado += letra_descifrada

print("El mensaje descifrado es:", mensaje_descifrado)
