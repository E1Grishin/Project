import pygame
import pygame as pg
import keyboard
import time
from tkinter import *
from tkinter import filedialog
root = Tk()
root.withdraw()
pygame.init()
Window = pg.display.set_mode((750, 450))

pg.mixer.init()
FPS = 30
clock = pg.time.Clock()
arial12 = pg.font.SysFont('arial', 12)
class Button:
    def __init__(self, widh, height, AColor , IaColor):
        self.widh =  widh
        self.height = height
        self.AColor = AColor
        self.IaColor = IaColor
    def draw(self, x, y, text):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if ( x < mouse[0] < x + self.widh ) and ( y < mouse[1] < y + self.height ) :

            pg.draw.rect(Window, self.AColor, (x, y, self.widh, self.height))
            if click[0]==1 :
                pg.draw.rect(Window,  (0, 150, 0), (x, y, self.widh, self.height))
                pg.display.update()
                pg.time.delay(500)
                return True

        else:
            pg.draw.rect(Window, self.IaColor, (x, y, self.widh, self.height ) )
        txt = arial12.render(text, 1, (255, 255, 255), None)
        Window.blit(txt, (x + 10, y + 19))

GREEN = (0, 200, 100)
RED = (255, 0, 0)

but1 = Button(100, 50, GREEN, RED)
but2 = Button(100, 50, GREEN, RED)
but3 = Button(100, 50, GREEN, RED)
but4 = Button(100, 50, GREEN, RED)
but5 = Button(100, 50, GREEN, RED)
but6 = Button(100, 50, GREEN, RED)
but7 = Button(100, 50, GREEN, RED)
but8 = Button(100, 50, GREEN, RED)
but9 = Button(100, 50, GREEN, RED)
but10 = Button(100, 50, GREEN, RED)
but11 = Button(100, 50, GREEN, RED)
but12 = Button(100, 50, GREEN, RED)
butpause = Button(50, 50, GREEN, RED)
butset = Button(50, 50, GREEN, RED)

file_path_binds = 'Content/Binds.txt'
file_path_sounds = 'Content/Sounds.txt'

def read_saves(dict,file_path):
    s = open(file_path)

    for i in range(1,15):
        a = str(i)
        dict[a] = s.readline().replace('\n','')
    s.close()
    return dict
def write_saves(dict, file_path ):
    s = open(file_path,'r+')
    n = ''
    for i in range(1,15):
        a= str(i)
        n += dict[a] + '\n'
    s.write(n)
    s.close()

sounds = {"1":'',"2":'',"3":'',"4":'',"5":'',"6":'',"7":'',"8":'',"9":'',
         "10":'',"11":'',"12":'',"13":'',"14":''}
binds = {"1":'',"2":'',"3":'',"4":'',"5":'',"6":'',"7":'',"8":'',"9":'',
         "10":'',"11":'',"12":'',"13":'',"14":''}

read_saves(sounds, file_path_sounds)
read_saves(binds,file_path_binds)

Window.fill((150, 150, 150))
pg.display.update()
running = True
settings = False
pause = False
while running:
    clock.tick(FPS)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            running = False
    if butpause.draw(50,50,'Pause'):
        pause = True
        Window.fill((150, 150, 150))
        pg.display.update()
        while pause:
            clock.tick(FPS)
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    running = False
                    pause = False
            if butpause.draw(50, 50, "Play"):
                pause = False
                Window.fill((150, 150, 150))
            pg.display.update()
    if butset.draw(50, 150, 'set'):
        settings = True
        while settings:
            Window.fill((150, 150, 150))
            clock.tick(FPS)
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    running = False
                    settings = False
            if butset.draw(50, 150, 'set'):
                settings = False
            if but1.draw(200, 50, binds['1'], ):
                sounds['1'] = filedialog.askopenfilename(filetypes=[("mp3 files", ".mp3")])
            if but2.draw(350, 50, binds['2'], ):
                sounds['2'] = filedialog.askopenfilename(filetypes=[("mp3 files", ".mp3")])
            if but3.draw(500, 50, binds['3'], ):
                sounds['3'] = filedialog.askopenfilename(filetypes=[("mp3 files", ".mp3")])
            if but4.draw(200, 150, binds['4'], ):
                sounds['4'] = filedialog.askopenfilename(filetypes=[("mp3 files", ".mp3")])
            if but5.draw(350, 150, binds['5'], ):
                sounds['5'] = filedialog.askopenfilename(filetypes=[("mp3 files", ".mp3")])
            if but6.draw(500, 150, binds['6'], ):
                sounds['6'] = filedialog.askopenfilename(filetypes=[("mp3 files", ".mp3")])
            if but7.draw(200, 250, binds['7'], ):
                sounds['7'] = filedialog.askopenfilename(filetypes=[("mp3 files", ".mp3")])
            if but8.draw(350, 250, binds['8'], ):
                sounds['8'] = filedialog.askopenfilename(filetypes=[("mp3 files", ".mp3")])
            if but9.draw(500, 250, binds['9'], ):
                sounds['9'] = filedialog.askopenfilename(filetypes=[("mp3 files", ".mp3")])
            if but10.draw(200, 350, binds['10'], ):
                sounds['10'] = filedialog.askopenfilename(filetypes=[("mp3 files", ".mp3")])
            if but11.draw(350, 350, binds['11'], ):
                sounds['11'] = filedialog.askopenfilename(filetypes=[("mp3 files", ".mp3")])
            if but12.draw(500, 350, binds['12'], ):
                sounds['12'] = filedialog.askopenfilename(filetypes=[("mp3 files", ".mp3")])
            pg.display.update()
        Window.fill((150, 150, 150))
        pg.display.update()
    if but1.draw(200, 50, binds['1'], ):
        i=0
        b1=''
        while(i==0):
            time.sleep(0.3)
            b1 = keyboard.read_key()
            time.sleep(0.3)
            if b1!='':
                i=1
        binds["1"] = b1
    if but2.draw(350, 50, binds['2'], ):
        i = 0
        b2 = ''
        while (i == 0):
            time.sleep(0.3)
            b2 = keyboard.read_key()
            time.sleep(0.3)
            if b2 != '':
                i = 1
        binds["2"] = b2
    if but3.draw(500, 50, binds['3'], ):
        i = 0
        b3 = ''
        while (i == 0):
            time.sleep(0.3)
            b3 = keyboard.read_key()
            time.sleep(0.3)
            if b3 != '':
                i = 1
        binds["3"] = b3
    if but4.draw(200, 150, binds['4'], ):
        i = 0
        b4 = ''
        while (i == 0):
            time.sleep(0.3)
            b4 = keyboard.read_key()
            time.sleep(0.3)
            if b4 != '':
                i = 1
        binds["4"] = b4
    if but5.draw(350, 150, binds['5'], ):
        i = 0
        b5 = ''
        while (i == 0):
            time.sleep(0.3)
            b5 = keyboard.read_key()
            time.sleep(0.3)
            if b5 != '':
                i = 1
        binds["5"] = b5
    if but6.draw(500, 150, binds['6'], ):
        i = 0
        b6 = ''
        while (i == 0):
            time.sleep(0.3)
            b6 = keyboard.read_key()
            time.sleep(0.3)
            if b6 != '':
                i = 1
        binds["6"] = b6
    if but7.draw(200, 250, binds['7'], ):

        i = 0
        b7 = ''
        while (i == 0):
            time.sleep(0.3)
            b7 = keyboard.read_key()
            time.sleep(0.3)
            if b7 != '':
                i = 1
        binds["7"] = b7
    if but8.draw(350, 250, binds['8'], ):
        i = 0
        b8 = ''
        while (i == 0):
            time.sleep(0.3)
            b8 = keyboard.read_key()
            time.sleep(0.3)
            if b8 != '':
                i = 1
        binds["8"] = b8
    if but9.draw(500, 250, binds['9'], ):
        i = 0
        b9 = ''
        while (i == 0):
            time.sleep(0.3)
            b9 = keyboard.read_key()
            time.sleep(0.3)
            if b9 != '':
                i = 1
        binds["9"] = b9
    if but10.draw(200, 350, binds['10'], ):
        i = 0
        b10 = ''
        while (i == 0):
            time.sleep(0.3)
            b10 = keyboard.read_key()
            time.sleep(0.3)
            if b10 != '':
                i = 1
        binds["10"] = b10
    if but11.draw(350, 350, binds['11'], ):
        i = 0
        b11 = ''
        while (i == 0):
            time.sleep(0.3)
            b11 = keyboard.read_key()
            time.sleep(0.3)
            if b11 != '':
                i = 1
        binds["11"] = b11
    if but12.draw(500, 350, binds['12'], ):
        i = 0
        b12 = ''
        while (i == 0):
            time.sleep(0.3)
            b12 = keyboard.read_key()
            time.sleep(0.3)
            if b12 != '':
                i = 1
        binds["12"] = b12
    if keyboard.is_pressed(binds['1']):
        sound1 = pg.mixer.Sound(sounds['1'])
        sound1.play()
        time.sleep(0.2)
    if keyboard.is_pressed(binds['2']):
        sound2 = pg.mixer.Sound(sounds['2'])
        sound2.play()
        time.sleep(0.2)
    if keyboard.is_pressed(binds['3']):
        sound3 = pg.mixer.Sound(sounds['3'])
        sound3.play()
        time.sleep(0.2)
    if keyboard.is_pressed(binds['4']):
        sound4 = pg.mixer.Sound(sounds['4'])
        sound4.play()
        time.sleep(0.2)
    if keyboard.is_pressed(binds['5']):
        sound5 = pg.mixer.Sound(sounds['5'])
        sound5.play()
        time.sleep(0.2)
    if keyboard.is_pressed(binds['6']):
        sound6 = pg.mixer.Sound(sounds['6'])
        sound6.play()
        time.sleep(0.2)
    if keyboard.is_pressed(binds['7']):
        sound7 = pg.mixer.Sound(sounds['7'])
        sound7.play()
        time.sleep(0.2)
    if keyboard.is_pressed(binds['8']):
        sound8 = pg.mixer.Sound(sounds['8'])
        sound8.play()
        time.sleep(0.2)
    if keyboard.is_pressed(binds['9']):
        sound9 = pg.mixer.Sound(sounds['9'])
        sound9.play()
        time.sleep(0.2)
    if keyboard.is_pressed(binds['10']):
        sound10 = pg.mixer.Sound(sounds['10'])
        sound10.play()
        time.sleep(0.2)
    if keyboard.is_pressed(binds['11']):
        sound11 = pg.mixer.Sound(sounds['11'])
        sound11.play()
        time.sleep(0.2)
    if keyboard.is_pressed(binds['12']):
        sound12 = pg.mixer.Sound(sounds['12'])
        sound12.play()
        time.sleep(0.2)
    pg.display.update()
write_saves(binds,file_path_binds)
write_saves(sounds, file_path_sounds)