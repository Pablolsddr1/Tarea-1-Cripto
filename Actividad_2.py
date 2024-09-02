from scapy.all import *
import os
import time

def send_icmp_request(ip, message):
    # Configuración del paquete ICMP
    icmp_id = 12345  # Identificador ICMP
    icmp_seq = 1  # Número de secuencia ICMP

    # Generar un payload real de 48 bytes utilizando bytes aleatorios
    payload_base = os.urandom(48)  # 48 bytes de datos reales

    # Posición fija dentro del payload donde se inyectará el carácter
    injection_position = 8  # Por ejemplo, la posición 8 (después de los primeros 8 bytes)

    if len(message) > 48:
        raise ValueError("El mensaje es demasiado largo. Debe ser de hasta 48 caracteres.")

    for i, char in enumerate(message):
        # Construir el payload ICMP con el carácter inyectado en la posición fija
        payload = payload_base[:injection_position] + char.encode() + payload_base[injection_position+1:]
        
        # Crear el paquete ICMP
        packet = IP(dst=ip) / ICMP(id=icmp_id, seq=icmp_seq) / Raw(load=payload)
        
        # Enviar el paquete
        send(packet)
        print(f"Paquete ICMP enviado con carácter '{char}' en la posición {injection_position} del payload")

        # Esperar antes de enviar el siguiente carácter para evitar congestión
        time.sleep(1)

def main():
    # Solicitar IP y mensaje al usuario
    ip = input("Ingrese la IP de destino: ")
    message = input("Ingrese el mensaje a enviar (hasta 48 caracteres): ")

    send_icmp_request(ip, message)
    print("Todos los caracteres han sido enviados en paquetes ICMP.")

if __name__ == "__main__":
    main()
