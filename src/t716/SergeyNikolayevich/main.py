import time
import thread
def Action():
    while 1:
        cls()
        if Object.Type=='Dog':
            print('\r  _    _  \n\r / / \__/ \ \ \n\r \/| /\/\ |\/\n\r  _||o o ||_\n\r /. .\__/. .\ \n\r/ . .(__) . .\ \n\r\ .  /__\  . / \n\r \__/\__/\__/')
        Object.State()
        Object.Cycle()
        print('\r##### ACTIVITIES ##### \n\r1 Feed\n\r2 Sleep\n\r3 Clean\n\r4 Play')
        if Object.Cheerfulness<=0 or Object.Satiety<=0 or Object.Mood<=0 or Object.Purity<=0:
            print('\r######GAME OVER######\n\rPress any key to restart')
            break
        time.sleep(1)
            
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

def cls(): print("\n" * 100)

class Animal:
    Type = 'default'
    Name = 'default'
    Cheerfulness = 0
    Satiety = 0
    Purity = 0
    Mood = 0
    def Start(self):
        self.Cheerfulness=100
        self.Satiety=100
        self.Purity=100
        self.Mood=100
    def State(self):
        print('\rName {}\n\rCheerfulness {}\n\rSatiety {}\n\rPurity {}\n\rMood {}'.format(self.Name,self.Cheerfulness,self.Satiety,self.Purity,self.Mood))
    def Cycle(self):
        self.Cheerfulness-=1
        self.Satiety-=1
        self.Purity-=1
        self.Mood-=1
    def Feed(self):
        print('\rFeeding...')
        self.Cheerfulness+=8
        if self.Cheerfulness>100:
            self.Cheerfulness=100
    def Sleep(self):
        print('\rSleaping...')
        self.Satiety+=8
        if self.Satiety>100:
            self.Satiety=100
    def Clean(self):
        print('\rCleaning...')
        self.Purity+=8
        if self.Purity>100:
            self.Purity=100
    def Play(self):
        print('\rPlaying...')
        self.Mood+=8
        if self.Mood>100:
            self.Mood=100
         
Alive = True
Game = True
Object=Animal()
while Game==True:
    Object.Start()
    print('\rFor starting game you should choose a character\n\r1 Cat\n\r2 Dog')
    choose=int(getch())
    if choose==1:
        Object.Type='Cat'
    elif choose==2:
        Object.Type='Dog'
    Object.Name=input('\rPerfect choose! Now you should name your pet\nName: ')
    print('\r{},what a wonderful name!The game will start right now'.format(Object.Name))
    counter=5
    while counter>0:
        print('{}...'.format(counter))
        time.sleep(1)
        counter-=1
    thread.start_new_thread(Action,())
    while Alive:
        choose=int(getch())
        if Object.Cheerfulness<=0 or Object.Satiety<=0 or Object.Mood<=0 or Object.Purity<=0:
            break
        if choose==1:
            Object.Feed()
        if choose==2:
            Object.Sleep()
        if choose==3:
            Object.Clean()
        if choose==4:
            Object.Play()
