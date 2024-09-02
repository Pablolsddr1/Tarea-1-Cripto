from scapy.all import *
from collections import Counter
from termcolor import colored

def load_spanish_dictionary():
    with open('/Users/pabloloressaavedra/Documents/VScode/Cripto/LAB1/espanol.txt', 'r', encoding='utf-8') as file:
        dictionary = set(word.strip().lower() for word in file)
    return dictionary

def caesar_cipher_decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            plaintext += chr(shifted)
        else:
            plaintext += char
    return plaintext

def capture_icmp_payload(target_ip, capture_time=30):
    captured_text = []
    
    def process_packet(packet):
        if packet.haslayer(ICMP):
            if packet[IP].src == target_ip and packet[ICMP].type == 8:  # ICMP Echo Request
                payload = bytes(packet[Raw].load)
                captured_text.append(chr(payload[8]))

    print(f"Capturando paquetes ICMP de {target_ip} durante {capture_time} segundos...")
    sniff(filter=f"icmp and src host {target_ip}", prn=process_packet, timeout=capture_time)

    return ''.join(captured_text)

def brute_force_caesar(ciphertext, dictionary):
    possibilities = {}
    for shift in range(26):
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        possibilities[shift] = decrypted_text
        print(f"Desplazamiento {shift}: {decrypted_text}")
    return possibilities

def highlight_most_likely(possibilities, dictionary):
    scores = {}
    for shift, text in possibilities.items():
        words = text.split()
        score = sum(1 for word in words if word.lower() in dictionary)
        scores[shift] = score
    
    best_shift = max(scores, key=scores.get)
    best_text = possibilities[best_shift]
    print(colored(f"\nPosible mensaje original (Desplazamiento {best_shift}): {best_text}", 'green'))

def main():
    dictionary = load_spanish_dictionary()

    # Solicitar la IP de destino al usuario
    target_ip = input("Ingrese la IP del remitente de los paquetes ICMP: ")

    # Capturar el texto cifrado
    ciphertext = capture_icmp_payload(target_ip, capture_time=30)  # 30 segundos de captura
    print(f"\nTexto cifrado capturado: {ciphertext}")

    # Realizar fuerza bruta para descifrar el texto
    possibilities = brute_force_caesar(ciphertext, dictionary)

    # Resaltar la opción más probable
    highlight_most_likely(possibilities, dictionary)

if __name__ == "__main__":
    main()
