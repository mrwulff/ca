# -*- coding: cp1252 -*-
#fuck2
###page 1=music
###page 2=obd






import pygame
import socket
from string import *
import random
import datetime
import time
import obd

import commands
import os,glob
import psutil
try:
    import udp
except:
    has_udp=False

connection = obd.OBD() # auto-connects to USB or RF port




pygame.init()
'''
screen = pygame.display.set_mode((720, 480),pygame.FULLSCREEN)

#screen = pygame.display.set_mode((640, 480))

'''
screen = pygame.display.set_mode((720,480))


clock2 = pygame.time.Clock()
done = False
font = pygame.font.SysFont("A", 60)
#font_music = pygame.font.Font("chiller", 90)
      #pygame.font.Font('redline.ttf', 16)
print pygame.font.get_fonts()
reset=0
song='All the Small Things'
album='Godamnit'
artist='Alkaline Trio'
debug=True

screen_rect = screen.get_rect()
page=3
pages=3

selection=1
selection_t=10

color=0


yellow_a=(250,055,250),(255,0,0),(0,0,250),(250,5,50),(255,255,255),(0,0,0),(125,125,125),(250,220,0),(127,255,0),(205,92,92),	(0,255,255),	(128,0,128)
yellow=yellow_a[color]


color_t=len(yellow_a)-1
xpos=50
ypos=50

fonts=[]
os.chdir("fonts")
for file in glob.glob("*.ttf"):
    fonts.append(file)
print fonts
font_select=0

font_size=90

sm=0
sm_total=5

speed=0





os.chdir("..")


font_music = pygame.font.Font('fonts/'+fonts[font_select], font_size)


def data(song):
    
    
    junk,song=split(song,"=")
    if len(song)>20:
        song= song[:20]+'...'
    return song

def lab(string,color,x,y,center,i):
    global font_size
    flag=0
    flag2=0
    if page==1:
        while flag==0:
            font_music = pygame.font.Font('fonts/'+fonts[font_select], font_size)

        
            string_label = font_music.render(string, True, (color))

            aa =string_label.get_rect()

            
            #print '               ',aa[2]
            if aa[2]>600:
                font_size=font_size-1
            if aa[2]<=600:
                flag=1


        while flag2==0:
            font_music = pygame.font.Font('fonts/'+fonts[font_select], font_size)

        
            string_label = font_music.render(string, True, (color))

            aa =string_label.get_rect()

            
            #print '               ',aa[2]
            if aa[2]<600:
                font_size=font_size+1
            if aa[2]>=600:
                flag2=1

                
    else:
        #font_size=60
        font_music = pygame.font.Font('fonts/'+fonts[font_select], font_size)

        
        string_label = font_music.render(string, True, (color))

        aa =string_label.get_rect()
        




            
    #print aa.center
    #print aa
    mid= aa[2]
    mid2=mid
    real=720-mid2
    real=real/2

    if center==True:    
        screen.blit(string_label,(real,y))
    if center==False:
        screen.blit(string_label,(x,y))
    #screen.blit(*text_objects(font, message, color, screen_rect.center))

    return aa[3]*.7

def rot_center(image, angle):
    print angle
    angle=angle*-1.85
    
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image




def speedmeter(connection):
    global speed
    global sm
    try:
        mph=connection.query(obd.commands.SPEED).value.to("mph")
        mph=mph.magnitude
        mph=str(rouund(mph,2))+' mph'
    except:
        'poop'


    try:
        bg = pygame.image.load('image/dj'+str(selection)+'.png')
        screen.blit(bg, (00, 0))
    except:
        'poop'

    try:    
        gage = pygame.image.load('image/speed'+str(sm)+'.png')
        screen.blit(gage, (00, 0))
    except:
        print 'cant find sm',sm


    needle = pygame.image.load('image/sneedle1.png')
    needle_rot=rot_center(needle,(speed+265))
    screen.blit(needle_rot, (120, 0))

      
    
def music():
    global song
    global album
    global artist
    global ypos
    sep=90
    #global color
    yellow=yellow_a[color]


    '''
    if selection==1 or selection==5 or selection==6 or selection==1:
        ypos=-61
    if selection==4:
        ypos=19
    if selection==2 or selection==0:
        ypos=-9
    if selection==3:
        ypos=33
    '''
    
    try:
        info=udp.get()
        if "song=" in info:
            song=data(info)

        if "album=" in info:
            album=data(info)
        if 'artist=' in info:
            artist=data(info)
    
        print info
    except:
        song= 'not connected to music  '
    

    ran=str(random.randint(600,4000))

    try:
        bg = pygame.image.load('image/dj'+str(selection)+'.png')
        screen.blit(bg, (00, 0))
    except:
        'poop'
    

    
    space1=lab(song,(yellow),50,ypos,True,1)
    
    space2=lab(artist,(yellow),50,ypos+space1,True,2)
    print '            ',space1,space2
    lab(album,(yellow),50,ypos+space1+space2,True,3)
    #if debug==True:
        #lab(str(selection)+' '+str(ypos),(yellow),50,330,False)

def obd2(connection,):
    yellow=yellow_a[color]
    try:

        bar=str(connection.query(obd.commands.BAROMETRIC_PRESSURE))

        temp=(connection.query(obd.commands.AMBIANT_AIR_TEMP).value.to("degF"))
        #print temp
        #print type(temp)
        temp=temp.magnitude
        temp = str(round(temp, 2)+'°F')

        load=str(connection.query(obd.commands.ENGINE_LOAD))
        load,junk=split(load,' ')
        load=load+'%'

        oiltemp=connection.query(obd.commands.COOLANT_TEMP).value.to("degF")
        oiltemp=oiltemp.magnitude
        oiltemp = str(round(oiltemp, 2))+'°F'

        mph=connection.query(obd.commands.SPEED).value.to("mph")
        mph=mph.magnitude
        mph=str(rouund(mph,2))+' mph'

        rpm=str(connection.query(obd.commands.RPM))
        rpm=split(rpm,' ')
        rpm=rpm[0]+'rpm'

        throt=connection.query(obd.commands.THROTTLE_POS)
        throt=throt.value
        throt=round(throt,1)
        throt=str(throt)+'%'

        runtime=str(connection.query(obd.commands.RUN_TIME))

        gas=connection.query(obd.commands.FUEL_LEVEL)
        gas=gas.value
        gas=round(gas,1)
    except:        


        bar='500 kilop'
        temp='69°F'
        load='50.1%'
        oiltemp='200°F'
        mph='99 mph'
        rpm='1233 rpm'
        throt=10.5
        runtime='4444 seconds'
        gas=12.4

    i=0

    lab(bar,(yellow),50,10,False,i)

        
    lab(temp,(yellow),50,60,False,i)

    
    lab(load,(yellow),50,110,False,i)

        
    lab(oiltemp,(yellow),50,160,False,i)


    lab(str(mph),(yellow),50,210,False,i)

    
    lab(rpm,(yellow),50,260,False,i)

    lab(str(throt),(yellow),50,310,False,i)

                
    lab(runtime,(yellow),50,360,False,i)

    
    lab(str(gas)+'%',(yellow),50,410,False,i)


    #lab(str(connection.query(obd.commands.DISTANCE_SINCE_DTC_CLEAR).value.to("mile")),(yellow),350,60,False)
    #lab(str(connection.query(obd.commands.STATUS_DRIVE_CYCLE)),(yellow),350,160,False)
    #print str(connection.query(obd.commands.STATUS_DRIVE_CYCLE))
    #lab(str(connection.query(obd.commands.THROTTLE_POS_B)),(yellow),350,210,False)
    #lab(str(connection.query(obd.commands.THROTTLE_POS_C)),(yellow),350,260,False)
    #lab(str(connection.query(obd.commands.FUEL_TYPE)),(yellow),350,310,False)
    #lab(str(connection.query(obd.commands.ETHANOL_PERCENT)),(yellow),350,360,False)
    #lab(str(connection.query(obd.commands.FUEL_RATE)),(yellow),350,410,False)
    #lab(str(connection.query(obd.commands.FUEL_PRESSURE)),(yellow),50,210,False)
    







def info():
    yellow=yellow_a[color]

    ip = commands.getoutput("hostname -I")
    

    temp = commands.getoutput("/opt/vc/bin/vcgencmd measure_temp")
    try:

        junk,temp=split(temp,'/vcgencmd:')
    except:
        temp=str(temp)


    cpu=(psutil.cpu_percent())
    ram=(psutil.virtual_memory())
    print ram[2]
    ram= ram[2]
    ram=str(ram)



    i=0

    lab(ip,(yellow),50,60,True,i)
    lab(temp,(yellow),50,150,True,i)
    lab(str(psutil.cpu_percent()),(yellow),50,250,True,i)
    lab(ram,(yellow),50,350,True,i)
    


    
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            udp.close()
            pygame.display.quit()
            done = True
            screen.close()
            pee
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
            
            pygame.display.quit()
            pygame.quit()
            udp.close()
            poop

        #PAGE
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            page=page+1
            if page>pages:
                page=0
                
        #DEBUG
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            if debug==True:
                debug=False
            else:
                debug=True
        #BG#
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            selection=selection+1
            if selection>selection_t:
                selection=0
        #COLOR        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            color=color+1
            if color>color_t:
                color=0
        #FONT#
        if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
            font_select=font_select+1
            if font_select>(len(fonts)-1):
                font_select=0

        if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
            sm=sm+1
            if sm>sm_total:
                sm=0






                
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            ypos=ypos-5

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            ypos=ypos+4

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            font_size=font_size+3

        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            font_size=font_size-2

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            speed=speed+10

        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            speed=speed-10


            


    bg = pygame.image.load('image/bg.png')
    screen.blit(bg, (00, 0))

    if page==1:
        music()
    if page==0:
        info()
    if page==2:
        obd2(connection)
    if page==3:
        speedmeter(connection)




      
       
    
    clock2.tick(10)
    if debug==True:
        #print page,'page'
        #print selection,'selection'
        #print color,'color'
        #print font_size,'font_size'
        #string=str(fonts[font_select])+str(font_select)
        if page==3:
            string=str(speed)+' '+str(sm)
        #print yellow
        string_label = font.render(string,True,(yellow))
        screen.blit(string_label,(5,5))

    pygame.display.flip()

