from subprocess import Popen,PIPE
import psutil
import sys

def cls(): print('\n'*100)
        
def Table():
    print(*[line.decode('cp866','ignore') for line in Popen('tasklist',stdout = PIPE).stdout.readlines()])

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

choose = int(sys.argv[1])
if choose == 1:
    Table()
if choose == 2:
    progressbarr()
if choose == 3:
    Table()
    progressbarr()
