import os 
import subprocess
import re
import sys
from hosts import agregarHost, obtenerIpDeHosts
from scanner import escaneo
from utils import check, checkDom, clear_screen, info, ok, error, warning

if os.geteuid() != 0:
    error("Ejecutar como root!")
    exit(1)

def main():
    opcion = input("¿La IP ya ha sido ingresada? (s/n): ")
    if opcion.lower() == "s":
        dominio = input("Ingrese el dominio correspondiente: ")
        ip = obtenerIpDeHosts(dominio)
        if ip is None:
            print(f"{dominio} no encontrado en /etc/hosts")
            sys.exit(1)


    else:
        while True:

            ip = input("Ingrese la IP para efectuar el reconocimiento: ")
            if check(ip):
                break
            print("IP inválida!")

        while True:

            dominio = input("Ingrese un dominio para la IP: ")
            if checkDom(dominio):
                break 
            error("Dominio inválido!")
        agregarHost(ip, dominio)
    while True:
        menu(ip, dominio)
        otra = input("¿Realizar otro escaneo? (s/n): ")
        if otra.lower() != "s":
            info("Saliendo...")
            break


def menu(ip, dominio): 
    clear_screen()
    info(f"Target: {ip} → {dominio}")
    print("─" * 30)
    info("[1] - Escaneo total")
    info("[2] - Escaneo de puertos")
    info("[3] - Escaneo Sigiloso")
    info("[4] - Escaneo UDP")
    while True: 
        modo = input("Seleccione el modo de reconocimiento: ")
        try: 

            valor = int(modo)
            if 1<=valor<=4:
                escaneo(valor, ip, dominio)
                break
            error("Valor inválido!")
        except ValueError:
            error("Valor inválido!")
            continue



if __name__ == "__main__":
    main()

