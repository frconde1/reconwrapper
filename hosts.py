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

