import subprocess, threading, requests, socket, pyfiglet, sys, os

from colorama import Fore

clear = lambda: os.system("clear")

verde, roxo, amarelo, reset = Fore.GREEN, Fore.MAGENTA, Fore.YELLOW, Fore.RESET

print(
        roxo + pyfiglet.figlet_format("Ippy") + reset
)

print(amarelo + "Criador: HunterDep" + reset)
print(amarelo + "Github: https://github.com/xHunterDepx\n" + reset)

try:
        host = "0.0.0.0"
        porta_http = int(sys.argv[1])
        porta_tcp = int(sys.argv[2])
except:
        print("Ultilize: python3 tracker.py [portaHTTP] [PortaTCP]")
        exit()

with open("index.php", "r+") as arqv:
        linhas = arqv.readlines()
        linhas[2] = f"$serverPort = '{porta_tcp}';\n"
        linhas = "".join(linhas)
        arqv.seek(0)
        arqv.write(linhas)

def ip_info(ip):
        print(f"{verde}ip {amarelo} => {verde}{ip}{reset}")
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        infos = []
        infos.append(f"ip => {ip}")

        for index in data:
                print(verde + index + f"{amarelo} => " + verde + str(data[index]) + reset)

                infos.append(
                        index + " => " + str(data[index])
                )
        with open(f"{ip}.txt", "w") as arqv:
                arqv.write("\n".join(infos))

def http():
        print(f"{verde}Servidor HTTP Ativo: {roxo}http://{host}:{porta_http}{reset}")
        subprocess.check_output(["php", "-S", f"0.0.0.0:{porta_http}"])

def tcp():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.bind((host, porta_tcp))
        s.listen()

        print(f"{verde}Servidor TCP Ativo: {roxo}{host}:{porta_tcp}{reset}")

        while True:
                cs, ca = s.accept()
                clear()
                ip = cs.recv(1024).decode()
                ip = ip.replace("\n", "")
                ip_info(ip)

t1 = threading.Thread(target=http)
t2 = threading.Thread(target=tcp)

t1.start()
t2.start()
t1.join()
t2.join()
