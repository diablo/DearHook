import os, requests, time, sys
import json
import random
import string
from colorama import Fore, Style, init;
from threading import Thread, Lock
from time import sleep
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import win32gui
hwnd = win32gui.GetForegroundWindow()
win32gui.MoveWindow(hwnd, 100, 50, 600, 510, True)

init()

def anim():
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write('\r' + f'''                                {Fore.RED}Loading {Fore.RESET}'''+i)
        sys.stdout.flush()
        time.sleep(0.3)

def anim3():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write('\r' + f'''                                {Fore.RED}Exiting {Fore.RESET}'''+i)
        sys.stdout.flush()
        time.sleep(0.3)

def anim4():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write('\r' + f'''                                {Fore.RED}Loading {Fore.RESET}'''+i)
        sys.stdout.flush()
        time.sleep(0.3)

def anim5():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write('\r' + f'''                          Deleting {Fore.RED}Webhook(s) {Fore.RESET}'''+i)
        sys.stdout.flush()
        time.sleep(0.3)

def anim6():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write('\r' + f'''                            Deleting {Fore.RED}Webhook {Fore.RESET}'''+i)
        sys.stdout.flush()
        time.sleep(0.3)

def anim2():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write('\r' + f'''                             {Fore.RED}Sending Hooks {Fore.RESET}'''+i)
        sys.stdout.flush()
        time.sleep(0.3)
        os.system('cls')
        print(f'''{Fore.LIGHTWHITE_EX}
                     _____  ______          _____  
                    |  __ \|  ____|   /\   |  __ \ 
                    | |  | | |__     /  \  | |__) |
                    | |  | |  __|   / /\ \ |  _  / 
                    | |__| | |____ / ____ \| | \ \ 
                    |_____/|______/_/    \_\_|  \_\

{Fore.RESET}{Fore.RED}             _____  ____   _____ _____ ______ ________     __
            / ____|/ __ \ / ____|_   _|  ____|__  __\ \   / /
            | (___| |  | | |      | | | |__    | |   \ \_/ / 
            \___ \| |  | | |      | | |  __|   | |    \   /  
            ____) | |__| | |____ _| |_| |____  | |     | |   
            |_____/\____/ \_____|_____|______| |_|     |_|   
                            
                            {Fore.RESET}Webhook Spammer      

                                ''')
lock = Lock()
def Printer(color, past, text, proxy):
    lock.acquire()
    print(f'                  {Fore.LIGHTWHITE_EX}[{color}{past}{Fore.LIGHTWHITE_EX}] {text} - {proxy.split("://")[1]}')
    lock.release()

def random_number(digits):
    range_start = 10**(digits-1)
    range_end = (10**digits)-1
    return random.randint(range_start, range_end)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

os.system('cls && title Dear Society - Webhook Spammer' if os.name == 'nt' else 'clear')
anim()
os.system('cls')
print(f'''{Fore.LIGHTWHITE_EX}
                     _____  ______          _____  
                    |  __ \|  ____|   /\   |  __ \ 
                    | |  | | |__     /  \  | |__) |
                    | |  | |  __|   / /\ \ |  _  / 
                    | |__| | |____ / ____ \| | \ \ 
                    |_____/|______/_/    \_\_|  \_\

{Fore.RESET}{Fore.RED}             _____  ____   _____ _____ ______ ________     __
            / ____|/ __ \ / ____|_   _|  ____|__  __\ \   / /
            | (___| |  | | |      | | | |__    | |   \ \_/ / 
            \___ \| |  | | |      | | |  __|   | |    \   /  
            ____) | |__| | |____ _| |_| |____  | |     | |   
            |_____/\____/ \_____|_____|______| |_|     |_|   
                            
                            {Fore.RESET}Webhook Spammer                         
                                
                                ''')
                                          
print(f"      [{Fore.RED}1{Fore.RESET}] Default Settings [{Fore.RED}2{Fore.RESET}] Custom Settings [{Fore.RED}3{Fore.RESET}] Delete Webhook")
print('')
print(f'                                [{Fore.RED}4{Fore.RESET}] Exit')
print('')
inp = int(input(f'                                                                                                 Choose an {Fore.RED}option{Fore.RESET}: '))

validate = URLValidator()

if inp == 1: # default settings
    name = id_generator()
    avatar = ('https://picsum.photos/id/{}/200'.format(random.randint(1, 500)))
    message = (f'')
    tts = True
    anim2()

elif inp == 2:
    print('')
    name = input(f"                                                                                                   Webhook Name: ")
    print('')
    avatar = input(f"                                                                                                   Webhook Image: ")

    try:
        validate(avatar)
        print('')
        print(f'                                                                                             {Fore.GREEN}Image validated successfully!{Fore.RESET}')

    except ValidationError as exception:
        print('')
        print(f'                                                                                                [{Fore.RED}-{Fore.RESET}] {Fore.RED}Please provide a valid image URL{Fore.RESET}')
        time.sleep(3.00)
        os.system('cls && python fuck.py')
        exit()

    print('')
    message = input(f"                                                                                                  Webhook Message: ")
    os.system('cls')
    print(f'''{Fore.LIGHTWHITE_EX}
                     _____  ______          _____  
                    |  __ \|  ____|   /\   |  __ \ 
                    | |  | | |__     /  \  | |__) |
                    | |  | |  __|   / /\ \ |  _  / 
                    | |__| | |____ / ____ \| | \ \ 
                    |_____/|______/_/    \_\_|  \_\

{Fore.RESET}{Fore.RED}             _____  ____   _____ _____ ______ ________     __
            / ____|/ __ \ / ____|_   _|  ____|__  __\ \   / /
            | (___| |  | | |      | | | |__    | |   \ \_/ / 
            \___ \| |  | | |      | | |  __|   | |    \   /  
            ____) | |__| | |____ _| |_| |____  | |     | |   
            |_____/\____/ \_____|_____|______| |_|     |_|   
                            
                            {Fore.RESET}Webhook Spammer                             
                                
                                ''')
    anim2()

elif inp == 3:
    os.system('cls')
    print(f'''{Fore.LIGHTWHITE_EX}
                     _____  ______          _____  
                    |  __ \|  ____|   /\   |  __ \ 
                    | |  | | |__     /  \  | |__) |
                    | |  | |  __|   / /\ \ |  _  / 
                    | |__| | |____ / ____ \| | \ \ 
                    |_____/|______/_/    \_\_|  \_\

{Fore.RESET}{Fore.RED}             _____  ____   _____ _____ ______ ________     __
            / ____|/ __ \ / ____|_   _|  ____|__  __\ \   / /
            | (___| |  | | |      | | | |__    | |   \ \_/ / 
            \___ \| |  | | |      | | |  __|   | |    \   /  
            ____) | |__| | |____ _| |_| |____  | |     | |   
            |_____/\____/ \_____|_____|______| |_|     |_|   
                            
                            {Fore.RESET}Webhook Spammer                         
                                
                                ''')
    anim4()
    os.system('cls')
    print(f'''{Fore.LIGHTWHITE_EX}
                     _____  ______          _____  
                    |  __ \|  ____|   /\   |  __ \ 
                    | |  | | |__     /  \  | |__) |
                    | |  | |  __|   / /\ \ |  _  / 
                    | |__| | |____ / ____ \| | \ \ 
                    |_____/|______/_/    \_\_|  \_\

{Fore.RESET}{Fore.RED}             _____  ____   _____ _____ ______ ________     __
            / ____|/ __ \ / ____|_   _|  ____|__  __\ \   / /
            | (___| |  | | |      | | | |__    | |   \ \_/ / 
            \___ \| |  | | |      | | |  __|   | |    \   /  
            ____) | |__| | |____ _| |_| |____  | |     | |   
            |_____/\____/ \_____|_____|______| |_|     |_|   
                            
                            {Fore.RESET}Webhook Spammer                         
                                
                                ''')
    print(f"                 [{Fore.RED}1{Fore.RESET}] Use webhooks file [{Fore.RED}2{Fore.RESET}] Enter webhook")
    inp = int(input(f'                                                                                                 Choose an {Fore.RED}option{Fore.RESET}: '))

    if inp == 1:
        os.system('cls')
        print(f'''{Fore.LIGHTWHITE_EX}
                     _____  ______          _____  
                    |  __ \|  ____|   /\   |  __ \ 
                    | |  | | |__     /  \  | |__) |
                    | |  | |  __|   / /\ \ |  _  / 
                    | |__| | |____ / ____ \| | \ \ 
                    |_____/|______/_/    \_\_|  \_\

{Fore.RESET}{Fore.RED}             _____  ____   _____ _____ ______ ________     __
            / ____|/ __ \ / ____|_   _|  ____|__  __\ \   / /
            | (___| |  | | |      | | | |__    | |   \ \_/ / 
            \___ \| |  | | |      | | |  __|   | |    \   /  
            ____) | |__| | |____ _| |_| |____  | |     | |   
            |_____/\____/ \_____|_____|______| |_|     |_|   
                            
                            {Fore.RESET}Webhook Spammer                         
                                
                                ''')
        anim5()
        os.system('cls')
        print(f'''{Fore.LIGHTWHITE_EX}
                     _____  ______          _____  
                    |  __ \|  ____|   /\   |  __ \ 
                    | |  | | |__     /  \  | |__) |
                    | |  | |  __|   / /\ \ |  _  / 
                    | |__| | |____ / ____ \| | \ \ 
                    |_____/|______/_/    \_\_|  \_\

{Fore.RESET}{Fore.RED}             _____  ____   _____ _____ ______ ________     __
            / ____|/ __ \ / ____|_   _|  ____|__  __\ \   / /
            | (___| |  | | |      | | | |__    | |   \ \_/ / 
            \___ \| |  | | |      | | |  __|   | |    \   /  
            ____) | |__| | |____ _| |_| |____  | |     | |   
            |_____/\____/ \_____|_____|______| |_|     |_|   
                            
                            {Fore.RESET}Webhook Spammer                         
                                
                                ''')
        url_list   = []
        with open('./url.txt', 'r') as url_file:
            for webhook in url_file:
                response = requests.delete(webhook.split('\n')[0])
                if response.status_code == 404:
                    print(f'                    Webhook has {Fore.RED}already{Fore.RESET} been {Fore.RED}deleted{Fore.RESET}')
                    exit()
                print(f'                            Webhook {Fore.RED}Deleted{Fore.RESET}')
                time.sleep(3.00)
                os.system('cls && python fuck.py')
                exit()
    elif inp == 2:
        os.system('cls')
        print(f'''{Fore.LIGHTWHITE_EX}
                     _____  ______          _____  
                    |  __ \|  ____|   /\   |  __ \ 
                    | |  | | |__     /  \  | |__) |
                    | |  | |  __|   / /\ \ |  _  / 
                    | |__| | |____ / ____ \| | \ \ 
                    |_____/|______/_/    \_\_|  \_\

{Fore.RESET}{Fore.RED}             _____  ____   _____ _____ ______ ________     __
            / ____|/ __ \ / ____|_   _|  ____|__  __\ \   / /
            | (___| |  | | |      | | | |__    | |   \ \_/ / 
            \___ \| |  | | |      | | |  __|   | |    \   /  
            ____) | |__| | |____ _| |_| |____  | |     | |   
            |_____/\____/ \_____|_____|______| |_|     |_|   
                            
                            {Fore.RESET}Webhook Spammer                         
                                
                                ''')
        webhook = input(f'                             Webhook {Fore.RED}Link:{Fore.RESET} ')
        os.system('cls')
        print(f'''{Fore.LIGHTWHITE_EX}
                     _____  ______          _____  
                    |  __ \|  ____|   /\   |  __ \ 
                    | |  | | |__     /  \  | |__) |
                    | |  | |  __|   / /\ \ |  _  / 
                    | |__| | |____ / ____ \| | \ \ 
                    |_____/|______/_/    \_\_|  \_\

{Fore.RESET}{Fore.RED}             _____  ____   _____ _____ ______ ________     __
            / ____|/ __ \ / ____|_   _|  ____|__  __\ \   / /
            | (___| |  | | |      | | | |__    | |   \ \_/ / 
            \___ \| |  | | |      | | |  __|   | |    \   /  
            ____) | |__| | |____ _| |_| |____  | |     | |   
            |_____/\____/ \_____|_____|______| |_|     |_|   
                            
                            {Fore.RESET}Webhook Spammer                         
                                
                                ''')
        anim6()
        os.system('cls')
        print(f'''{Fore.LIGHTWHITE_EX}
                     _____  ______          _____  
                    |  __ \|  ____|   /\   |  __ \ 
                    | |  | | |__     /  \  | |__) |
                    | |  | |  __|   / /\ \ |  _  / 
                    | |__| | |____ / ____ \| | \ \ 
                    |_____/|______/_/    \_\_|  \_\

{Fore.RESET}{Fore.RED}             _____  ____   _____ _____ ______ ________     __
            / ____|/ __ \ / ____|_   _|  ____|__  __\ \   / /
            | (___| |  | | |      | | | |__    | |   \ \_/ / 
            \___ \| |  | | |      | | |  __|   | |    \   /  
            ____) | |__| | |____ _| |_| |____  | |     | |   
            |_____/\____/ \_____|_____|______| |_|     |_|   
                            
                            {Fore.RESET}Webhook Spammer                         
                                
                                ''')
        response = requests.delete(webhook)
        if (response.status_code == 404):
            print(f'                    Webhook has {Fore.RED}already{Fore.RESET} been {Fore.RED}deleted{Fore.RESET}')
            time.sleep(3.00)
            os.system('cls && python fuck.py')
            exit()
        print(f'                            Webhook {Fore.RED}Deleted{Fore.RESET}')
        time.sleep(3.00)
        os.system('cls && python fuck.py')
        exit()

elif inp == 4:
    os.system('cls')
    print(f'''{Fore.LIGHTWHITE_EX}
                     _____  ______          _____  
                    |  __ \|  ____|   /\   |  __ \ 
                    | |  | | |__     /  \  | |__) |
                    | |  | |  __|   / /\ \ |  _  / 
                    | |__| | |____ / ____ \| | \ \ 
                    |_____/|______/_/    \_\_|  \_\

{Fore.RESET}{Fore.RED}             _____  ____   _____ _____ ______ ________     __
            / ____|/ __ \ / ____|_   _|  ____|__  __\ \   / /
            | (___| |  | | |      | | | |__    | |   \ \_/ / 
            \___ \| |  | | |      | | |  __|   | |    \   /  
            ____) | |__| | |____ _| |_| |____  | |     | |   
            |_____/\____/ \_____|_____|______| |_|     |_|   
                            
                            {Fore.RESET}Webhook Spammer                         
                                
                                ''')
    anim3()
    os.system('cls')
    exit()

response_headers = {
  'username': name,
  'avatar_url': avatar,
  'content': message,
  'tts': True
}

class DearSociety:
    def __init__(self):
        self.proxy_list = []
        self.url_list   = []

        self.attempt = 0
        self.send = 0
        self.initialize()
    
    def initialize(self):

        with open('proxy.txt', 'r') as proxy_file:
            for proxy in proxy_file:
                self.proxy_list.append(proxy.split('\n')[0])

        with open('./url.txt', 'r') as url_file:
            for url in url_file:
                self.url_list.append(url.split('\n')[0])
        
        self.proxy_list = list(set(self.proxy_list))
        self.url_list   = list(set(self.url_list))

    def worker(self, webhook, proxy):
        alive = True

        while alive:
            
            os.system(f'title Hooks Sent: {self.send} - Retry Attempts: {self.attempt}')

            try:

                response = requests.post(webhook, headers= {'content-type': 'application/json'}, proxies= {'http': proxy, 'https': proxy}, json=response_headers)

                if response.status_code == 204:
                    self.send += 1
                    Printer(Fore.GREEN, '+', f'{Fore.GREEN}Hook sent{Fore.RESET}', proxy)

                elif response.status_code == 429:
                    self.attempt += 1
                    timeout = int(str(response.json()['retry_after'])[2:])
                    Printer(Fore.RED, '-', f'{Fore.RED}Rate limited{Fore.RESET} ({Fore.RED}{timeout}{Fore.RESET}s)', proxy)
                    time.sleep(30.0)
                    
                    
                elif response.status_code == 404:
                    Printer(Fore.RED, '-', f'{Fore.RED}Hook deleted{Fore.RESET}', proxy)
                    alive = False
                    break
            
            except:
                pass
    
    def start_worker(self):
        thread_list = []

        for url in self.url_list:
            for proxy in self.proxy_list:
                thread_list.append(Thread(target=self.worker, args=(url, proxy)))
        
        for thread in thread_list:
            thread.start()
        
        for thread in thread_list:
            thread.join()

DearSociety().start_worker()