import os,glob
from string import *
import search_google.api
#from google import search

import Tkinter 
import tkMessageBox
import shutil
from Tkinter import *
from tkSimpleDialog import askstring
#from tkSimpleDialog import askquestion

import lxml.etree
import lxml.builder
import xml.etree.ElementTree
import xml.etree.ElementTree as ET
from urllib import *
from PIL import Image, ImageTk


from Tkinter import Tk
s=0
oculus_dir='C:\Program Files\Oculus/'
steamapi='xxx'
picked=''
backup=True
master = Tk()
name=''
picture=''
steamid=''
games=[]
games_data=[]
games_json=[]
xmls=[]
game_file=''

current_name=''
current_id=''
current_steamid=''
games=[]
cwd=''
listbox=''
isgame=[]
v = IntVar()
value=''
def importo():
    a=''

    f=games_data[s]
    f[7]=current_name
    fi= xmls[s]
    junk=split(fi,'/')
    dirr='C:\Program Files\Oculus\Software\Manifests/'+ junk[len(junk)-1]
    w=open(dirr,'w')
    

    for i in range(len(f)):
        a=a+ f[i]+'"'
    a=a[:len(a)-1]
    w.write(a)
def save(f,path,cname):
    exists=False
    
    try:
        sfile=open(path,'r')
        exists=True
        return
    except:
        ''
    #b=raw_input("OVERWRITE? "+cname)
    b=''
    if b=='':
    
        
        sfile=open(path,'w')
        E = lxml.builder.ElementMaker()
        ROOT = E.root
        DOC = E.doc
        FIELD1 = E.exe
        FIELD2 = E.fileDir
        FIELD3 = E.steamid
        FIELD4 = E.images
        FIELD5 = E.isgame

        the_doc = ROOT(
                DOC(
                    FIELD1(name=cname),
                    FIELD2(name=path),
                    FIELD3(name=''),
                    FIELD4(name=''),
                    FIELD5(name='no')
                    )   
                )   

        a= lxml.etree.tostring(the_doc, pretty_print=True)
        sfile.write(a)
        sfile.close

def savefile():
    global current_id
    global current_name
    global s
    global v
    global value
    print v
    print value
    print current_id,'++ID++'
    tree = ET.parse(game_file)
    for rank in tree.iter('exe'):
        rank.text = str('')
        rank.set('name', current_name)
        ''

    for rank in tree.iter('steamid'):
        rank.text = str('')
        rank.set('name', current_id)
        ''

    for rank in tree.iter('isgame'):
        rank.text = str('')
        rank.set('name', value)
        ''


    tree.write(game_file)
    print current_id,current_name, 'current name and id'
    current_id=''
    

def searchg():
    global current_id
    flag=0
    for url in search(games_data[s][7], stop=10):
        if 'steam' in url and flag==0:
        
            surl=split(url,'/')
            for i in range(len(surl)):
                if 'app' in surl[i] and flag==0:
                    steamid= surl[i+1]
                    flag=1
            

    #results.download_links('downloads')
    try:                
        current_id=steamid
    except:
        print 'cant find id'
        #searchg(30)

    savefile()



    
    'oop'
def changename():
    global current_name
    current_name = askstring("Input", "Change Name")
    #return answer
    savefile()

def changeid():
    global current_id
    current_id = askstring("Input", "Change ID")
    print current_id,'cuurrentid'
    savefile()

def one():
    global value
    global s
    value='yes'
    listbox.itemconfig(s, {'bg':'white'})
def two():
    global value
    global s
    value='no'
    listbox.itemconfig(s, {'bg':'red'})
def CurSelet(event):
    global s
    global current_name
    global current_id
    global current_steamid
    global game_file
    global v
    global value
    widget = event.widget
    selection=widget.curselection()
    s=(selection[0])
    s=int(s)

    picked = widget.get(selection[0])
    game_file=games_json[s]




    e = xml.etree.ElementTree.parse(games_json[s]).getroot()
    #print e
    ef= e[0][0].attrib
    
    current_name= ef['name']


    ef= e[0][1].attrib
    
    current_fdir= ef['name']


    ef= e[0][2].attrib
    
    current_steamid= ef['name']

    ef= e[0][3].attrib
    
    current_images= ef['name']

    
    



    p = Canvas(master, width=700, height=900)
    p.pack()
    p.create_rectangle(10,10,330,50)
    p.place(x=150,y=000)



    w = Label(master, text=picked)
    w.pack()
    w.place(x=230,y=100)

    w = Label(master, text='Occulus Name')
    w.pack()
    w.place(x=130,y=100)

    

    w = Label(master, text=current_name)
    w.pack()
    w.place(x=230,y=130)

    b = Button(master, text="Change Name", command=changename)
    
    b.pack()
    b.place(x=130,y=130)
                                

    

    w = Label(master, text=current_steamid)
    w.pack()
    w.place(x=230,y=164)

    b1 = Button(master, text="Change Steam ID", command=changeid)
    #b1 = Button(master, text="Change Steam ID", command=changeid(game_file,e))

    b1.pack()
    b1.place(x=130,y=160)

    

    w = Label(master, text=current_images)
    w.pack()
    w.place(x=230,y=198)

    b2 = Button(master, text="Change Pic", command=changename)
    b2.pack()
    b2.place(x=130,y=190)

    #w = Label(master, text=current_steamid)
    #w.pack()
    #w.place(x=230,y=100)


    b3 = Button(master, text="Lookup ID", command=searchg)
    b3.pack()
    b3.place(x=130,y=220)

    b4 = Button(master, text="Save config", command=savefile)
    b4.pack()
    b4.place(x=130,y=250)

    b4 = Button(master, text="Import to Occulus", command=importo)
    b4.pack()
    b4.place(x=130,y=280)

    b5 = Button(master, text="Download Pictures", command=dlpics)
    b5.pack()
    b5.place(x=130,y=310)

    b5 = Button(master, text="Overwrite Pictures", command=opics)
    b5.pack()
    b5.place(x=130,y=340)

    
    b6=Radiobutton(master, text="Show", variable=v,command=one, value=1,)
    b6.pack(anchor=W)
    b7=Radiobutton(master, text="Hide", variable=v,command=two,value=2)
    b7.pack(anchor=W)
    b6.place(x=130,y=370)
    b7.place(x=130,y=390)
    
    

    
    try:

        image = Image.open(cwd+'/pics/'+current_steamid+'.jpg')
        photo = ImageTk.PhotoImage(image)

        label = Label(image=photo)
        label.image = photo # keep a reference!
        
        label.pack()
        label.place(x=500,y=500)
    except:
        print 'cant find photos'


def dlpics():

    url ='http://store.steampowered.com/app/'+current_steamid
    pic= 'http://cdn.akamai.steamstatic.com/steam/apps/'+current_steamid+'/header.jpg'

    try:
        pi=cwd+'/pics/'+current_steamid+'.jpg'
        pio=open(pi,'r')
    except:
        
        urlretrieve(pic,cwd+'/pics/'+current_steamid+'.jpg')
        print 'done downloading'
    landscape='cover_landscape_image.jpg'
    cover_squuare='cover_square_image.jpg'
    icon_image='icon_image.jpg'
    logo_trans='logo_transparent_image.png'
    orig='original.jpg'
    small_landscape='small_landscape_image.jpg'

def opics():
    
    a=oculus_dir
    b='Software\Software\StoreAssets/'
    c= games_data[s][3]
    d='_assets'
    imdir= a+b+c+d
    ''
    os.chdir(imdir)
    newpic=cwd+'/pics/'+current_steamid+'.jpg'
    print newpic
    landscape='cover_landscape_image.jpg'
    cover_squuare='cover_square_image.jpg'
    icon_image='icon_image.jpg'
    logo_trans='logo_transparent_image.png'
    orig='original.jpg'
    small_landscape='small_landscape_image.jpg'
    pics=[]
    pics.append(landscape)
    pics.append(cover_squuare)
    pics.append(icon_image)
    pics.append(logo_trans)
    pics.append(orig)
    pics.append(small_landscape)
    for i in range(len(pics)):
        shutil.copy(newpic, pics[i])


    

        
def findpics(game):
  
    'test'



def make_grid():
    global listbox
    global picked
    global games
    
    
    sizex = 1200
    sizey = 800
    posx  = 40
    posy  = 20
    master.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

    listbox = Listbox(master,height=len(games))
    listbox.pack()
    listbox.bind('<<ListboxSelect>>',CurSelet,master)
    

    #listbox.insert(END, "a list entry")
    listbox.place(x=0,y=0)
    

    i=0
    for item in games:
        
        
        listbox.insert(END, item)
        if isgame[i]=='no':
            listbox.itemconfig(i, {'bg':'red'})
        i=i+1
    w = Canvas(master, width=200, height=100)
    
    w.pack()
    

    mainloop()
    
def lookup_if_game(f):
    global isgame
    print f
    e = xml.etree.ElementTree.parse(f).getroot()
    ef= e[0][4].attrib
    
    ef= ef['name']
    print ef
    isgame.append(ef)
    
def main(redo):
    global games
    global xmls
    global cwd
    

    root=Tk()
    
    cwd=os.getcwd()
    print cwd
    files=[]
    di='C:\Program Files\Oculus\Software\Manifests/'
    os.chdir(di)
    for file in glob.glob("*.*"):
        files.append(file)
    for i in range(len(files)):
        full_file=di+files[i]
        backup_file=di+'/backup/'+files[i]
        b=open(full_file,'r')
        if backup==True:
            shutil.copyfile(full_file, backup_file)
        for line in b.readlines():
            if 'displayName' in line:
                root.withdraw()
                

                
                xmldir=cwd+'/ids/'+files[i]
                xmls.append(xmldir)
                #s=open(xmldir,'w')
                games_json.append(xmldir)
                junk=split(line,'"')
                games_data.append(junk)

                findpics(junk[7])
                games.append(junk[7])
                #print files[i],xmldir,junk[7],'woop',xmldir
                
                #xx=raw_input('')
                if redo==True:
                    save(files[i],xmldir,junk[7])
                lookup_if_game(xmldir)
                    
    make_grid()
    
                         
main(True)


