import os 
import subprocess
import re
import sys

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


