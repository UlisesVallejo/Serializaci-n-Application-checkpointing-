import psutil
import os, time
from colorama import Fore, Style

while True:
    procesos = 0
    for proc in psutil.process_iter():

        if proc.name().lower() == 'main.exe' or proc.name().lower() == 'python.exe':
            procesos += 1
        
    if procesos == 1:
        # todo: ejecutar la app si esta caida
        opc = input(Style.BRIGHT + Fore.RED +'\nLa aplicación está cerrada, desea abrirla? (s/n): ' + Style.RESET_ALL)
        if opc == 's' or opc == 'S':
            print('Abriendo...')
            time.sleep(2)
            os.system('python main.py')
        elif opc == 'n' or opc == 'N':
            break
    
    else:
        print(Style.BRIGHT + Fore.GREEN + 'La aplicación principal se esta ejecutando correctamente' + Style.RESET_ALL)
        
            