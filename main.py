import os 
import subprocess
import re
import sys
from hosts import agregarHost

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
domregex = r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
if os.geteuid() != 0:
    print("Ejecutar como root!")
    exit(1)

def main():
    while True:

        ip = input("Ingrese la IP para efectuar el reconocimiento: ")
        if check(ip):
            break
        print("IP inválida!")
    while True:

        dominio = input("Ingrese un dominio para la IP: ")
        if checkDom(dominio):
            break 
        print("Dominio inválido!")
    agregarHost(ip, dominio)
    while True:
        menu(ip, dominio)
        otra = input("¿Realizar otro escaneo? (s/n): ")
        if otra.lower() != "s":
            print("Saliendo...")
            break


def clear_screen():
    # For Windows (os.name is 'nt')
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux (os.name is 'posix')
    else:
        _ = os.system('clear')

def menu(ip, dominio): 
    clear_screen()
    print("[1] - Escaneo total")
    print("[2] - Escaneo de puertos")
    print("[3] - Escaneo Sigiloso")
    print("[4] - Escaneo UDP")
    while True: 
        modo = input("Seleccione el modo de reconocimiento: ")
        try: 

            valor = int(modo)
            if 1<=valor<=4:
                escaneo(valor, ip, dominio)
                break
            print("Valor inválido!")
        except ValueError:
            print("Valor inválido!")
            continue




def escaneo(modo, ip, dominio):
    output_file = f"recon{dominio}"

    match modo:
        case 1:
            flags = ["-sV", "-sC", "--top-ports", "1000", "-oN", f"{output_file}_común.txt"]
        case 2:
            flags = ["-sV", "-sC", "-p-", "-oN", f"{output_file}_total.txt"]
        case 3:
            flags = ["-sS", "-p-", "-oN", f"{output_file}_sigiloso.txt"]
        case 4:
            flags = ["-sU", "--top-ports", "200", "-oN", f"{output_file}_udp.txt"]
    print(f"[*] Iniciando escaneo sobre {ip}...")
    subprocess.run(["nmap"] + flags + [ip])
    print(f"[+] Resultado guardado en {output_file}...")

def check(ip):

    return re.search(regex,ip) is not None

def checkDom(dominio):
    return re.search(domregex, dominio) is not None


if __name__ == "__main__":
    main()

