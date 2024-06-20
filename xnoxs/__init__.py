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
        clear()
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

def bn(name=None):
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

def antibot(response, api_key, hostcap):
    bot1 = response.split('rel=\\"')[1].split('\\"')[0]
    bot2 = response.split('rel=\\"')[2].split('\\"')[0]
    bot3 = response.split('rel=\\"')[3].split('\\"')[0]
    main = response.split('data:image/png;base64,')[1].split('\\"')[0]
    img1 = response.split('data:image/png;base64,')[2].split('\\"')[0]
    img2 = response.split('data:image/png;base64,')[3].split('\\"')[0]
    img3 = response.split('data:image/png;base64,')[4].split('\\"')[0]

    if not bot1:
        raise ValueError("Bot information missing.")

    data = {
        'key': api_key,
        'method': 'antibot',
        'main': main,
        bot1: img1,
        bot2: img2,
        bot3: img3
    }

    url = f'http://{hostcap}/in.php'
    headers = {'Content-type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=data, headers=headers)
    response_text = response.text

    try:
        task = response_text.split('OK|')[1]
    except IndexError:
        return 0

    if task:
        while True:
            res_url = f'http://{hostcap}/res.php?key={api_key}&id={task}'
            r2 = requests.get(res_url).text
            try:
                hasil = r2.split('OK|')[1]
            except IndexError:
                if r2 == "CAPCHA_NOT_READY":
                    print("BYPASS ANTIBOT     \r", end="")
                    time.sleep(3)
                else:
                    return 0
                continue

            antb = hasil.split(',')
            return "+" + "+".join(antb)
    else:
        return 0

    print("\r                            \r", end="")


def hcaptcha(sitekey, pageurl, apikey, hostcap):
    while True:    
        response = requests.get(f"http://{hostcap}/in.php?key={apikey}&method=hcaptcha&sitekey={sitekey}&pageurl={pageurl}")
        task = response.text.split('OK|')[1] if 'OK|' in response.text else None
        time.sleep(5)
        
        if task:
            while True:
                response_check = requests.get(f"http://{hostcap}/res.php?key={apikey}&action=get&id={task}")
                if 'OK|' in response_check.text:
                    hasil = response_check.text.split('OK|')[1]
                    return hasil
                elif response_check.text == "ERROR_CAPTCHA_UNSOLVABLE":
                    print(f"{response_check.text}\r")
                    break 
                else:
                    print(f"{response_check.text}\r", end='')
                    time.sleep(3)
        else:
            continue 

def recaptcha(key, url, apikey, hostcap):
    while True:        
        response = requests.get(f"https://{hostcap}/in.php?key={apikey}&method=userrecaptcha&googlekey={key}&pageurl={url}")
        task = response.text.split('OK|')[1] if 'OK|' in response.text else None
        time.sleep(10)
        
        if task:
            while True:
                response_check = requests.get(f"https://{hostcap}/res.php?key={apikey}&action=get&id={task}")
                if 'OK|' in response_check.text:
                    hasil = response_check.text.split('OK|')[1]
                    return hasil
                elif response_check.text == "ERROR_CAPTCHA_UNSOLVABLE":
                    print(f"{response_check.text}\r")
                    break 
                else:
                    print("BYPASS RECAPTCHA         \r", end='')
                    time.sleep(3)
        else:
            continue 

def gp_captcha(res):
    cap = res.split('class="text-color text-capitalize">')[1].split('<')[0]
    c1 = res.split('name="captcha_code" value="')[1].split('"')[0]

    icon_paths = {
        "flag": 'M349.565',
        "tree": 'M377.33',
        "heart": 'M414.9',
        "car": 'M499.991',
        "cup": 'M192',
        "star": 'M259.3',
        "house": 'M488',
        "plane": 'M472',
        "key": 'M512',
        "truck": 'M624'
    }

    if cap in icon_paths:
        opr = res.split(icon_paths[cap])[1].split('</div>')[0]
        c2 = opr.split('class="icons" value="')[1].split('"')[0]
        return {'captcha_code': c1, 'icons_value': c2}
    else:
        raise ValueError("Unexpected captcha type")
        

def curl(url, headers=None, data=None):
    try:
        if data:
            response = requests.post(url, headers=headers, data=data)
        else:
            response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def head(url):
   host = urllib.parse.urlparse(url).hostname
   headers = {
     'Host': host,
     'upgrade-insecure-requests': '1',
     'user-agent': simpan('user-agent'),
     'cookie': simpan('cookie'),
   }
   return headers


def fly(url):
   data = {'main': url}
   return requests.post('https://mcm-faucet.biz.id/index.php',headers={}, data=data).text

import os

def file_get_contents(filename):
    with open(filename, 'r') as file:
        return file.read()

def file_put_contents(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def choice():
    options = {
        1: {'host': 'api.multibot.in', 'apikey_file': 'apikey-multibot'},
        2: {'host': 'goodxevilpay.pp.ua', 'apikey_file': 'apikey-xevil'}
    }
    
    print(h + '['+ k+ '1' + h + ']' + k + ' Multibot')
    print(h + '['+ k+ '2' + h + ']' + k + ' Xevil')
    
    while True:
        try:
            cap = int(input(h + "Input Number: " + p))
            if cap in options:
                option = options[cap]
                apikey_file = option['apikey_file']
                
                if os.path.exists(apikey_file):
                    apikey = file_get_contents(apikey_file)
                else:
                    apikey = input(f"API key for {option['host']} : ")
                    file_put_contents(apikey_file, apikey)
                
                option['apikey'] = apikey
                return option
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

