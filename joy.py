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
    has_linux=1
except:
    print 'cant cd to /root/car'
    has_linux=0

pygame.init()

bind=  commands.getoutput("sudo rfcomm bind 0 00:0D:18:00:00:01")
print bind
   
try:
    connection = obd.OBD() # auto-connects to USB or RF port
    temp55=(connection.query(obd.commands.AMBIANT_AIR_TEMP).value.to("degF"))
    temp55=str(temp55)
    print temp55
except:
    has_linux=0
    temp55=''
    
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
song='A Things'
album='100'
artist='Alkaline Trio'
debug=True
pages=3

selection_t=10

pygame.mouse.set_visible(0)


######446=BOTTOM OF SCREEEN##########
######691=RIGHT OF SCREEN
BOTTOM=446
RIGHT=691



xpos=50

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





sm_total=5

speed=0




yellow_a=(250,055,250),(255,0,0),(0,0,250),(250,5,50),(255,255,255),(0,0,0),(125,125,125),(250,220,0),(127,255,0),(205,92,92),	(0,255,255),	(128,0,128)
color_t=len(yellow_a)-1


sm=1
font_size=90
font_select=27
selection=1
color=0
page=1
ypos=5
debug=True



largestx=0
spacex1=0
spacex2=0
spacex3=0
tot_space=0

yellow=yellow_a[color]
c=[page,debug,selection,color,font_select,sm,font_size,font_size,ypos,ypos]
c[5]=2




cr=random.randint(0,(color_t))
c[3]=cr

br=random.randint(0,len(bgs))
c[2]=br
#print len(c[3])
fr=random.randint(0,len(fonts))
c[4]=fr


    
def main():
    flagquit=0
    global done
    screen = pygame.display.set_mode((RIGHT,BOTTOM),pygame.NOFRAME)


    

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

        
        #print 'cant load', c[2]
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
        clock=True
        if clock==True:
            font_clock = pygame.font.Font('fonts/'+fonts[c[4]], 50)
            #clockd=time.strftime("%I:%M %p")
            clockd=time.strftime("%I:%M")
            if clockd[0]=='0':
                clockd=clockd[1:]
            clock



            #string_label = font_clock.render(clockd+temp55,True,(yellow),(0,0,0))
            string_label = font_clock.render(clockd+temp55,True,(0,0,0))
            aa =string_label.get_rect()
            mid= aa[2]
            mid2=mid
            real=RIGHT-mid2
            real=real/2

            
            button = pygame.image.load('image/button2.png')
            button= pygame.transform.scale(button, (mid+60,100))
            screen.blit(button,(real-30,BOTTOM-50))
            screen.blit(string_label,(real,BOTTOM-50))

            
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
            #RANDOM!!!     
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                #print c[3]
                cr=random.randint(0,(color_t))
                c[3]=cr

                br=random.randint(0,len(bgs))
                c[2]=br
                #print len(c[3])
                fr=random.randint(0,len(fonts))
                c[4]=fr

            #FONT#
            if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                c[4]=c[4]+1
                

            if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
                c[5]=c[5]+1
                





                    
            if event.type == pygame.KEYDOWN and event.key == pygame.K_2 and cycle==8:
                #ypos=ypos-5
                c[8]=c[8]-1
                

            if event.type == pygame.KEYDOWN and event.key == pygame.K_2 and cycle==9:
                c[8]=c[8]+1

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
    max_size=550
    #print 'omg'
    #global c
    
    font_size =c[6]
    #print font_size,' FONT'
    flag=0
    flag2=0
    flag3=1
    if c[0]==1:
        while len(string)<13:
            string=' '+string+' '
            #print string
        while flag==0:
            #font_music = pygame.font.Font('fonts/'+fonts[c[4]], font_size,background=(0,255,0))
            font_music = pygame.font.Font('fonts/'+fonts[c[4]], font_size)

        
            #string_label2 = font_music.render(string, True, (color),(0,0,0,250))
            string_label = font_music.render(string, True, (color))
            


            aa =string_label.get_rect()

            
            if aa[2]>max_size:
                font_size=font_size-5
            if aa[2]<=max_size:
                flag=1


        while flag2==0:
            #font_music = pygame.font.Font('fonts/'+fonts[c[4]], font_size,background=(0,255,0))
            font_music = pygame.font.Font('fonts/'+fonts[c[4]], font_size)

        
            #string_label2 = font_music.render(string, True, (color),(0,0,0,250))
            string_label = font_music.render(string, True, (color))


            aa =string_label.get_rect()

            
            if aa[2]<max_size:
                font_size=font_size+5
            if aa[2]>=max_size:
                flag2=1
        string_label=textOutline(font_music,string,(color),(125,125,125))
        
        '''
        while flag3==0:
            font_music = pygame.font.Font('fonts/'+fonts[c[4]], font_size,background=(0,255,0))
            string_label = font_music.render(string, True, (color),(0,0,0,250))
            string_label2 = font_music.render(string, True, (color))
            print aa[3]
            aa =string_label.get_rect()
            if aa[3]>200:
                font_size=font_size-10
                
            if aa[3]<=200:
                flag3=1'''
            
            

                
    if c[0]!=1:
        #font_size=60
        
        font_music = pygame.font.Font('fonts/'+fonts[c[4]], c[6]/2)

        
        string_label = font_music.render(string, True, (color),(0,0,0,255))
        string_label=textOutline(font_music,string,(0,255,255),color)
        string_label2 = font_music.render(string, True, (color),(0,0,0,255))
        string_label2=textOutline(font_music,string,(0,255,0),(255,0,0))


        aa =string_label.get_rect()
        




            
    #print aa.center
    #print aa
    mid= aa[2]
    mid2=mid
    real=RIGHT-mid2
    real=real/2
    

    if center==True:    
        screen.blit(string_label,(real,y))
        
    if center==False:
        screen.blit(string_label,(x,y))
    #screen.blit(*text_objects(font, message, color, screen_rect.center))
        '''
    if c[1]%2==1:
        screen.blit(bgc,(0,0))
        if center==True:    
            screen.blit(string_label2,(real,y))
        if center==False:
            screen.blit(string_label2,(x,y))
            '''


    return aa[3],aa[2]


def textHollow(font, message, fontcolor):
    notcolor = [c^0xFF for c in fontcolor]
    base = font.render(message, 0, fontcolor, notcolor)
    size = base.get_width() + 18, base.get_height() + 18
    img = pygame.Surface(size, 50)
    img.fill(notcolor)
    base.set_colorkey(0)
    img.blit(base, (0, 0))
    img.blit(base, (2, 0))
    img.blit(base, (0, 2))
    img.blit(base, (2, 2))
    base.set_colorkey(0)
    base.set_palette_at(1, notcolor)
    img.blit(base, (1, 1))
    img.set_colorkey(notcolor)
    return img




def textOutline(font, message, fontcolor, outlinecolor):
    base = font.render(message, 0, fontcolor)
    outline = textHollow(font, message, outlinecolor)
    img = pygame.Surface(outline.get_size(), 16)
    img.blit(base, (1, 1))
    img.blit(outline, (0, 0))
    img.set_colorkey(0)
    return img


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
        mph=speed
        print mph,'no good'

        


    try:
        bg = pygame.image.load('image/dj'+str(selection)+'.png')
        #screen.blit(bg, (00, 0))
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
    lab(screen,bg,bgc,str(mph),yellow,50,400,True,3)

    screen.blit(needle_rot, (120, 0))

      
    
def music(screen,bg,bgc):
    global song
    #global HEIGHT
    global album
    global artist
    global ypos
    global c
    sep=90
    global font_size
    #global color
    yellow=yellow_a[c[3]]
    #print c[3]
    #print "C{#}"
    #global bgc

    global spacex1
    global spacex2
    global spacex3
    global tot_space


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
        #while len(song)<5:
          #  song=' '+song+' '
            

        if "album=" in info:
            
            album=data(info)
            #while len(album)<5:
               # album=' '+album+' '
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




    largestx=spacex1
    if spacex2>largestx:
        spacex2=largestx
    if spacex3>largestx:
        spacex3=largestx
    left=(RIGHT-largestx)/2
    trans=125
    #screen.fill((trans, trans, trans), (left,c[8],largestx,tot_space), pygame.BLEND_RGBA_MULT)
    





    
    space1,spacex1=lab(screen,bg,bgc,song,yellow,50,c[8],True,1)
    
    space2,spacex2=lab(screen,bg,bgc,artist,yellow,50,c[8]+space1,True,2)
    space3,spacex3=lab(screen,bg,bgc,album,yellow,50,c[8]+space1+space2,True,3)
    tot_space= space1+space2+space3
    tot_x_space=spacex1+spacex2+spacex3
    #print tot_space,'tot_space'
    c[8]=(BOTTOM-tot_space)/2





    

def obd2(screen,bg,bgc,connection,):
    yellow=yellow_a[c[3]]
    global arduino
    yellow=yellow_a[c[3]]
    if has_linux==1:

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
    if has_linux==0:        


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
