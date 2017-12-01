# -*- coding: utf-8 -*-
#fuck2
###page 1=music
###page 2=obd




import serial


import pygame,sys
from pygame.locals import *

import socket
from string import *
import random
import datetime
import time
import obd
import subprocess

import commands
import os,glob
import psutil
#import s
try:
    import udp
except:
    has_udp=False


try:
    os.chdir("/home/pi/car")
except:
    print 'cant cd to /root/car'

pygame.init()

bind=  commands.getoutput("sudo rfcomm bind 0 00:0D:18:00:00:01")
print bind
   

connection = obd.OBD() # auto-connects to USB or RF port
temp=(connection.query(obd.commands.AMBIANT_AIR_TEMP).value.to("degF"))
print temp

'''

bind=  commands.getoutput("sudo rfcomm bind 0 00:0D:18:00:00:01")
print bind



'''


'''
screen = pygame.display.set_mode((720, 480),pygame.FULLSCREEN)

#screen = pygame.display.set_mode((640, 480))

'''


clock2 = pygame.time.Clock()
done = False
font = pygame.font.SysFont("A", 60)

reset=0
song='All the Small Things'
album='Godamnit'
artist='Alkaline Trio'
debug=True
page=1
pages=3

selection=1
selection_t=10

color=0






xpos=50
ypos=25

fonts=[]
os.chdir("fonts")
for file in glob.glob("*.ttf"):
    fonts.append(file)
os.chdir("..")
os.chdir("image/bg/")
bgs=[]
for file in glob.glob("*.*"):
    bgs.append(file)
os.chdir("..")
os.chdir("..")


    
#print fonts
font_select=27

font_size=90


sm_total=5

speed=0


sm=1

yellow_a=(250,055,250),(255,0,0),(0,0,250),(250,5,50),(255,255,255),(0,0,0),(125,125,125),(250,220,0),(127,255,0),(205,92,92),	(0,255,255),	(128,0,128)
color_t=len(yellow_a)-1
yellow=yellow_a[color]
c=[page,debug,selection,color,font_select,sm,font_size,font_size,ypos,ypos]
c[5]=2




    
def main():
    flagquit=0
    global done
    screen = pygame.display.set_mode((720,480),pygame.NOFRAME)


    

    screen_rect = screen.get_rect()
    




    font_music = pygame.font.Font('fonts/'+fonts[font_select], font_size)




    cycle=0
    

    while not done:
        
        if c[0]>pages:
            c[0]=0
        if c[2]>(len(bgs)-1):
            c[2]=0
        if c[3]>color_t:
            c[3]=0
        if c[4]>(len(fonts)-1):
            c[4]=0
        if c[5]>sm_total:
                c[5]=0
        if cycle>(len(c)-1):
            cycle=0
        if c[1]%2==1:
            debug=True
        else:
            debug=False


        
            

        #print bgs
        #print selection
        #print c[2]
        bg = pygame.image.load('image/bg/'+bgs[c[2]]).convert_alpha()
        bg= pygame.transform.scale(bg, (720,480))
        bgc=bg.copy()
        bgc.fill((255, 255, 255, 50), None, pygame.BLEND_RGBA_MULT)

        
        print 'cant load', c[2]
        #screen.blit(bg, (00, 0))
        
        screen.blit(bg, (00, 0))


        #print c
        #print c[0]
        #print type(c[0])
        if c[0]==1:
            music(screen,bg,bgc)
        if c[0]==0:
            
            info(screen,bg,bgc)
        if c[0]==2:
            obd2(screen,bg,bgc,connection)
        if c[0]==3:
            speedmeter(screen,bg,bgc,connection,c)





        #cst=['page','debug','selection','color','font_select','sm','ypos','font_size']
        cst=['page','debug','bg','color','font_select','sm','font up','font down','y pos+','ypos --']
        
        
        if debug==True:
            #s.send(c[0],False,arduino)
            c[7]=c[6]
            c[9]=c[8]
            font_debug = pygame.font.Font('fonts/'+fonts[37], 30)

            #print page,'page'
            #print selection,'selection'
            #print color,'color'
            #print font_size,'font_size'
            #string=str(fonts[font_select])+str(font_select)
            #if page==3:
            #    string=str(speed)+' '+str(sm)

            #print yellow
            string=str(c[cycle])

            string_label = font_debug.render(string,True,(yellow))
            screen.blit(string_label,(5,50))


            string=cst[cycle]
            #22print string
            string_label = font_debug.render(string,True,(yellow))
            screen.blit(string_label,(5,400))

        pygame.display.flip()




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    
                    udp.close()
                except:
                    'poo'
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_7:
                
                c[0]=c[0]+1
                



            if event.type == pygame.KEYDOWN and event.key == pygame.K_3: 
                cycle=cycle+1


            if event.type == pygame.KEYDOWN and event.key == pygame.K_2 :
                c[cycle]=c[cycle]+1





                    
            #DEBUG
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                if debug==True:
                    debug=False
                else:
                    debug=True
            #BG#
            if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                c[2]=c[2]+1
               
            #COLOR        
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                #print c[3]
                subprocess.call("shutdown -h now", shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                #print c[3]
                cr=random.randint(0,(color_t))
                c[3]=cr

                br=random.randint(0,len(bgs))
                c[2]=br
                #print len(c[3])
                fr=random.randint(0,len(fonts))
                c[4]=fr
            '''

woop
            '''
            #FONT#
            if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                c[4]=c[4]+1
                

            if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
                c[5]=c[5]+1
                





                    
            if event.type == pygame.KEYDOWN and event.key == pygame.K_2 and cycle==8:
                #ypos=ypos-5
                c[8]=c[8]-5
                

            if event.type == pygame.KEYDOWN and event.key == pygame.K_2 and cycle==9:
                c[8]=c[8]+5

            if event.type == pygame.KEYDOWN and event.key == pygame.K_2 and cycle==6:
                c[6]=c[6]+3

            if event.type == pygame.KEYDOWN and event.key == pygame.K_2 and cycle==7:
                c[6]=c[6]-2

            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                speed=speed+10

            if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                speed=speed-10
    clock2.tick(60)


def data(song):
    
    
    junk,song=split(song,"=")
    if len(song)>20:
        song= song[:20]+'...'
    return song

def lab(screen,bg,bgc,string,color,x,y,center,i):
    #print 'omg'
    #global c
    font_size =c[6]
    flag=0
    flag2=0
    if c[0]==1:
        while flag==0:
            font_music = pygame.font.Font('fonts/'+fonts[c[4]], font_size,background=(0,255,0))

        
            string_label = font_music.render(string, True, (color),(0,0,0,250))
            string_label2 = font_music.render(string, True, (color))


            aa =string_label.get_rect()

            
            if aa[2]>600:
                font_size=font_size-1
            if aa[2]<=600:
                flag=1


        while flag2==0:
            font_music = pygame.font.Font('fonts/'+fonts[c[4]], font_size,background=(0,255,0))

        
            string_label = font_music.render(string, True, (color),(0,0,0,250))
            string_label2 = font_music.render(string, True, (color))


            aa =string_label.get_rect()

            
            if aa[2]<600:
                font_size=font_size+1
            if aa[2]>=600:
                flag2=1

                
    if c[0]!=1:
        #font_size=60
        
        font_music = pygame.font.Font('fonts/'+fonts[c[4]], c[6]/2)

        
        string_label = font_music.render(string, True, (color),(0,0,0,255))
        string_label2 = font_music.render(string, True, (color),(0,0,0,255))


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
    if c[1]%2==1:
        screen.blit(bgc,(0,0))
        if center==True:    
            screen.blit(string_label2,(real,y))
        if center==False:
            screen.blit(string_label2,(x,y))


    return aa[3]
def run_quit(screen,bg):
    screen.blit(bg, (00, 0))
    bind=  commands.getoutput("sudo rfcomm bind 0 00:0D:18:00:00:01")

def rot_center(image, angle):
    #print angle
    angle=angle*-1.85
    
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image




def speedmeter(screen,bg,bgc,connection,c):
    global speed
    #global c
    try:
        mph=connection.query(obd.commands.SPEED).value.to("mph")
        mph=mph.magnitude
        mph=(rouund(mph,2))
	print mph
    except:
        print mph,'no good'


    try:
        bg = pygame.image.load('image/dj'+str(selection)+'.png')
        screen.blit(bg, (00, 0))
    except:
        'poop'

    try:
        #print c[5]
        gage = pygame.image.load('image/speed'+str(c[5])+'.png')
        screen.blit(gage, (00, 0))
    except:
        print 'cant find sm',sm


    needle = pygame.image.load('image/sneedle1.png')
    needle_rot=rot_center(needle,(mph+265))
    screen.blit(needle_rot, (120, 0))

      
    
def music(screen,bg,bgc):
    global song
    global album
    global artist
    global ypos
    global c
    sep=90
    #global color
    yellow=yellow_a[c[3]]
    #print c[3]
    #print "C{#}"
    #global bgc


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
    
        #print info
    except:
        song= 'not connected to music  '
    

    #ran=str(random.randint(600,4000))

    try:
        bg = pygame.image.load('image/dj'+str(c[2])+'.png')
        screen.blit(bg, (00, 0))
    except:
        'poop'


    
    space1=lab(screen,bg,bgc,song,yellow,50,c[8],True,1)
    
    space2=lab(screen,bg,bgc,artist,yellow,50,c[8]+space1,True,2)
    lab(screen,bg,bgc,album,yellow,50,c[8]+space1+space2,True,3)
    #if debug==True:
        #lab(str(selection)+' '+str(ypos),(yellow),50,330,False)

def obd2(screen,bg,bgc,connection,):
    yellow=yellow_a[c[3]]
    global arduino
    yellow=yellow_a[c[3]]
    if 1==1:

        bar=str(connection.query(obd.commands.BAROMETRIC_PRESSURE))

        temp=(connection.query(obd.commands.AMBIANT_AIR_TEMP).value.to("degF"))
        #print temp
        #print type(temp)
        temp=temp.magnitude
        temp = str(round(temp, 2))+('*F')

        load=str(connection.query(obd.commands.ENGINE_LOAD))
        load,junk=split(load,' ')
        load=load+'%'

        oiltemp=connection.query(obd.commands.COOLANT_TEMP).value.to("degF")
        oiltemp=oiltemp.magnitude
        oiltemp = str(round(oiltemp, 2))+('*F')

        mph=connection.query(obd.commands.SPEED).value.to("mph")
        mph=mph.magnitude
        mph=str(round(mph,2))+' mph'

        rpm=str(connection.query(obd.commands.RPM))
        rpm=split(rpm,' ')
        rpm=rpm[0]+'rpm'

        throt=connection.query(obd.commands.THROTTLE_POS)
        throt=throt.value
        throt=round(throt,1)
        throt=str(throt)+'%Throttle'

        runtime=str(connection.query(obd.commands.RUN_TIME))

        gas=connection.query(obd.commands.FUEL_LEVEL)
        gas=gas.value
        gas=round(gas,1)
        gas=str(gas)+'% Gas'
    if 1==2:        


        bar='500 kilop'
        temp='69�F'
        load='50.1%'
        oiltemp='200�F'
        mph='99 mph'
        rpm='1233 rpm'
        throt='10.5'
        runtime='4444 seconds'
        gas=12.4
    
    

    i=0
    c[8]
    gap=50
    st=10
    ooo=[bar,temp,load,oiltemp,mph,rpm,throt,runtime,gas]
    for z in range(len(ooo)):
        print ooo[z]
        print type(ooo[z])
        lab(screen,bg,bgc,str(ooo[z]),(yellow),50,st+(gap*z),False,i)
    '''
        
    lab(bar,(yellow),50,10,False,i)

        
    lab(temp,(yellow),50,60,False,i)

    
    lab(load,(yellow),50,110,False,i)

        
    lab(oiltemp,(yellow),50,160,False,i)


    lab((mph),(yellow),50,210,False,i)

    
    lab(rpm,(yellow),50,260,False,i)

    lab((throt),(yellow),50,310,False,i)

                
    lab(runtime,(yellow),50,360,False,i)

    
    lab(gas,(yellow),50,410,False,i)
    '''


    #lab(str(connection.query(obd.commands.DISTANCE_SINCE_DTC_CLEAR).value.to("mile")),(yellow),350,60,False)
    #lab(str(connection.query(obd.commands.STATUS_DRIVE_CYCLE)),(yellow),350,160,False)
    #print str(connection.query(obd.commands.STATUS_DRIVE_CYCLE))
    #lab(str(connection.query(obd.commands.THROTTLE_POS_B)),(yellow),350,210,False)
    #lab(str(connection.query(obd.commands.THROTTLE_POS_C)),(yellow),350,260,False)
    #lab(str(connection.query(obd.commands.FUEL_TYPE)),(yellow),350,310,False)
    #lab(str(connection.query(obd.commands.ETHANOL_PERCENT)),(yellow),350,360,False)
    #lab(str(connection.query(obd.commands.FUEL_RATE)),(yellow),350,410,False)
    #lab(str(connection.query(obd.commands.FUEL_PRESSURE)),(yellow),50,210,False)
    



4



def info(screen,bg,bgc):
    yellow=yellow_a[c[3]]

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

    lab(screen,bg,bgc,ip,(yellow),50,60,True,i)
    lab(screen,bg,bgc,temp,(yellow),50,150,True,i)
    lab(screen,bg,bgc,str(psutil.cpu_percent()),(yellow),50,250,True,i)
    lab(screen,bg,bgc,ram,(yellow),50,350,True,i)
    


main()
