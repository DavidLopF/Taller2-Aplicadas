mensaje = "THZEIPHMRRRGOSRKRUDWVLKNUSITAGSOKOEPHMRRRG"
clave = "EDGAR"

##desencriptar el mensaje transfromando a en a 
def desencriptar(mensaje, clave):
    mensaje_desencriptado = ""
    for i in range(len(mensaje)):
        letra_mensaje = mensaje[i]
        letra_clave = clave[i % len(clave)]
        letra_desencriptada = chr((ord(letra_mensaje) - ord(letra_clave)) % 26 + ord('A'))
        mensaje_desencriptado += letra_desencriptada
    return mensaje_desencriptado

mensaje_desencriptado = desencriptar(mensaje, clave)
print("El mensaje desencriptado es:", mensaje_desencriptado)