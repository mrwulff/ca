import serial
import time
import random
def send(zz,randomn,arduino):
    
    
    
    i=1
    a=chr(1)*3
    r=1
    b=1
    g=1
    ro=127
    bo=127
    go=127

    for q in range(1):
        zz=24-zz
        if randomn==True:
            zz=random.randint(1,24)
        print zz , '             zz  ',zz
            
        #print arduino.read(100),'opp'
        for z in range(1):
            
            if zz<8:
                ro=127
                bo=1
                go=1
            if zz<16 and z>7:
                ro=1
                bo=127
                go=1
            if zz>16:
                ro=1
                bo=1
                go=127
            col=chr(r)+chr(g)+chr(b)
            coloff=chr(ro)+chr(go)+chr(bo)
            p=(col*zz)+coloff*(24-zz)
            #print len(p),'len p'
            #print p
            if len(p)==72:
                #print len(p)
                command = str.encode(p)
                arduino.write(command)   
                time.sleep(.8)


            #print 'ok'
#arduino = serial.Serial('COM5', 2000000, timeout=0)                
#send(100,True,arduino)
