import os, re
import threading

received_packages = re.compile(r'(\d) received')
status = ("no response", "alive but losses", "alive")

def call_ip(ip):
    ip = "192.168.178." + str(ip + 20)
    ping_out = os.popen("ping -q -c2 " + ip, "r")
    print("... pinging ", ip)
#for suffix in range(20, 30):
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])

threads = [threading.Thread(target=call_ip, args=(i,)) for i in range(40)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()