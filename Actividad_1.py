def cifrado_cesar(texto, corrimiento):
    cifrado = ""
    
    for char in texto:
        if char.isalpha():  # Verifica si el carácter es una letra
            desplazamiento = corrimiento % 26  # Ajusta el corrimiento al rango de 0-25
            if char.islower():  # Verifica si el carácter es una letra minúscula
                base = ord('a')
                cifrado += chr((ord(char) - base + desplazamiento) % 26 + base)
            elif char.isupper():  # Verifica si el carácter es una letra mayúscula
                base = ord('A')
                cifrado += chr((ord(char) - base + desplazamiento) % 26 + base)
        else:
            cifrado += char  # Mantiene los caracteres no alfabéticos sin cambios
    
    return cifrado

# Solicitar datos al usuario
def solicitar_datos():
    texto = input("Introduce el texto a cifrar: ")
    corrimiento = int(input("Introduce el valor de corrimiento (número entero): "))
    return texto, corrimiento

# Bloque de evidencia
def prueba_cifrado_cesar():
    texto, corrimiento = solicitar_datos()
    texto_cifrado = cifrado_cesar(texto, corrimiento)
    print(f"Texto original: {texto}")
    print(f"Texto cifrado: {texto_cifrado}")

# Ejecutar la prueba
prueba_cifrado_cesar()
