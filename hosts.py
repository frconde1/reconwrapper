import re 

HOSTS_FILE = "/etc/hosts"

def agregarHost(ip,dominio): 
    entrada = f"{ip}\t{dominio}"

    with open(HOSTS_FILE,"r") as f:
        contenido = f.read()

    if dominio in contenido:
        print(f"[!] {dominio} ya existe en /etc/hosts") 
        return
    
    with open(HOSTS_FILE, "a") as f: 
        f.write(f"\n{entrada}")

    print(f"[+] Agregado: {entrada}")

def obtenerIpDeHosts(dominio):
    patron = re.compile(r'^\s*(\d{1,3}(?:\.\d{1,3}){3})\s+\S*' + re.escape(dominio))
    
    with open(HOSTS_FILE, "r") as f:
        for linea in f:
            if linea.startswith("#"):
                continue
            match = patron.match(linea)
            if match:
                return match.group(1)  # devuelve la IP
    
    return None  # no encontrado
