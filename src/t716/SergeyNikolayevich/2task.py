from subprocess import Popen,PIPE
import psutil

def cls(): print('\n'*100)

from threading import Thread
try:
    from msvcrt import getch
except ImportError:
     import sys
     import tty, termios
     def getch():
         fd = sys.stdin.fileno()
         old_settings = termios.tcgetattr(fd)
         try:
             tty.setraw(sys.stdin.fileno())
             ch = sys.stdin.read(1)
         finally:
             termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
         return ch
        
def Table():
    print(*[line.decode('cp866','ignore') for line in Popen('tasklist',stdout = PIPE).stdout.readlines()])
    print('Press 1 to update or any other key to change type\n')
    decision = int(getch())
    if decision==1:
        cls()
        Table()
    else:
        main()

def progressbarr():
    cpu=psutil.cpu_percent(interval = 1,percpu=False)
    ram = psutil.virtual_memory()
    ram = ram[2]
    counter = 0
    cpubarr=""
    rambarr=""
    while counter<50:
        if counter<=cpu/2:
            cpubarr+='|'
            counter+=1
        else:
            cpubarr+='.'
            counter+=1
        if counter<ram/2:
            rambarr+='|'
        else:
            rambarr+='.'       
    print(' one | = 0-2%')
    print('{0}({1}% CPU usage)'.format(cpubarr,cpu))
    print('{0}({1}% RAM usage)'.format(rambarr,ram))
    print('Press 1 to update or any other key to change type\n')
    decision = int(getch())
    if decision==1:
        cls()
        progressbarr()
    else:
        main()

def Both():
    print(*[line.decode('cp866','ignore') for line in Popen('tasklist',stdout = PIPE).stdout.readlines()])
    cpu=psutil.cpu_percent(interval = 1,percpu=False)
    ram = psutil.virtual_memory()
    ram = ram[2]
    counter = 0
    cpubarr=""
    rambarr=""
    while counter<50:
        if counter<=cpu/2:
            cpubarr+='|'
            counter+=1
        else:
            cpubarr+='.'
            counter+=1
        if counter<ram/2:
            rambarr+='|'
        else:
            rambarr+='.'       
    print(' one | = 0-2%')
    print('{0}({1}% CPU usage)'.format(cpubarr,cpu))
    print('{0}({1}% RAM usage)'.format(rambarr,ram))
    print('Press 1 to update or any other key to change type\n')
    decision = int(getch())
    if decision==1:
        cls()
        Both()
    else:
        main()
        
def main():
    print('1. Processes Table\n2. Ram and CP\n3. Both\n')
    choose = int(getch())
    if choose == 1:
        Table()    
    if choose == 2:
        progressbarr()
    if choose == 3:
        Both()
main()
        

