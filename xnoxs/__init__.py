import requests
import urllib.parse
import json
import time
import os
import sys

p = "\033[1;97m"
m = "\033[1;31m"
h = "\033[1;32m"
k = "\033[1;33m"
c = "\033[1;36m"
b = "\033[1;34m"
mp = "\033[101m\033[1;37m"
n = "\n"
d = "\033[0m"
t = "\t"
r = "                  \r"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def msg(str, j=10):
    symbols = ['-', '/', '|', '\\']
    for i in range(j, 0, -1):
        for n, s in enumerate(symbols):
            print(f"{p}                 [{k}{s}{p}] {h}{str} {k}{'➤' * n}{r}", end='', flush=True)
            time.sleep(0.1)
    print("                           " + r, end='', flush=True)

def simpan(data_name):
    if os.path.exists(data_name):
        with open(data_name, 'r') as file:
            data = file.read().strip()
    else:
        bn(name)
        data = input(f"{p} Input {data_name} : {h}")
        with open(data_name, 'w') as file:
            file.write(data)
    return data

def line():
    return p + '─' * 55 

def get_time_zone():
    try:
        rpi = requests.get("http://ip-api.com/json").json()
        if rpi:
            tz = rpi["timezone"]
            os.environ['TZ'] = tz
            return rpi["country"]
    except:
        os.environ['TZ'] = 'UTC'
        return "UTC"

def bn(name):
    os.system('cls' if os.name == 'nt' else 'clear')
    zone = get_time_zone()
    date = time.strftime("%d-%b-%Y")
    current_time = time.strftime("%H:%M:%S")
    padding = 50 - len(zone + date + current_time)
    space = padding // 2
    location = f"{c}{zone}{' ' * space}{date}{' ' * space}{current_time}"
    if padding % 2 == 1:
        location += " "
    print(location)
    print(line())
    print(f"{m} ╭╮╱╱╱╱╭━━━┳━━━╮    {h}Create By  {k}: {p}BC06{n} {m}┃┃╱╱╱╱┃╭━╮┃╭━━╯    {h}Script     {k}: {p}{name}{n} {m}┃╰━┳━━┫┃┃┃┃╰━━╮    {h}Telegram   {k}: {p}t.me/BC060904{n} {p}┃╭╮┃╭━┫┃┃┃┃╭━╮┃    {h}Support By {k}: {p}IEWIL OFFICIAL{n} ┃╰╯┃╰━┫╰━╯┃╰━╯┃    {h}Thanks To  {k}: {p}BP12{n} ╰━━┻━━┻━━━┻━━━╯    {mp}Note : Script Not For Sell!!{d}")
    print(line())

def timer(duration, caption="please wait"):
    end_time = time.time() + duration
    while True:
        remaining_time = end_time - time.time()
        if remaining_time < 1:
            print("                      " + "\r", end='', flush=True)
            break
        print(f"{m}{caption} {p}{time.strftime('%M:%S', time.gmtime(remaining_time))}   \r", end='', flush=True)
        time.sleep(1)


def explode(awal, akhir, res, no):
    return res.split(awal)[no].split(akhir)[0]
    
