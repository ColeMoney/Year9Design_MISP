from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import webbrowser
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

#Functions
def openwebsite():
    webbrowser.open_new('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')
    
def saveList():
    myfile=open("myplayers.txt","w")
    for player in lst:
        myfile.write(player+"---")
    myfile.close()
    messagebox.showinfo("myplayers/txt", "players saved to disk")   

def saveasList():
    myfile=open("myplayers.txt","w")
    for player in lst:
        myfile.write(player+"\n")
    myfile.close()
    root.filename=filedialog.asksaveasfilename(initialdir="/", title="Select file")
    print(root.filename)
    messagebox.showinfo("myplayers/txt", "players saved to disk")
    
def update_lab():
    lstprint=""
    for item in lst:
        lstprint=lstprint+item+"\n"
    mylab.configure(text=lstprint)

def readfile():
    f=open("myplayers.txt","r")
    cont=f.read().split("---")
    for a in cont:
        if cont!=0:
            listbox.insert(END,a)
            lst.append(a)
    f.close()
    
def scrape():
    if(messagebox.askyesno("Wait/Espere?", "This could take a few seconds/esto podría tomar unos segundos. Wait?/Espere")==False):
        return
    if site.status_code is 200:
        totalpts=0
        for myplayer in lst:
            dTag=content.find(attrs={"csk": myplayer})
            parent=dTag.findParent("tr")
            if parent==False:
                break
            playerpts=int(parent.contents[8].text)
            totalpts=totalpts + playerpts
        mypts.configure(text=totalpts)
def addplayers(value):
    var.get
    if lst.count(value)!=0:
        pass
    else:
        listbox.insert(END,value)
        lst.append(value)
        
def remplayers(value):
    var=listbox.get(ACTIVE)
    listbox.delete(listbox.index(ACTIVE))
    lst.remove(var)
    
def makeList():
    if content !=-99:
        names=content.findAll(attrs={"data-stat":"player"})
        for player in names:
            if (player.get("csk")!=None or player.get("csk")!=""):
                playerlist.append(player.get('csk'))
        return playerlist


'''def readList():
    try'''
    
def createlistbox(value):  
    
    var=listbox.get(ANCHOR)
    print(var)
    if content!=-99:
        if var!=type(NONE):
            if var!=None:
                dTag=content.find(attrs={"csk":var})
                parent=dTag.findParent("tr")
                points=int(parent.contents[8].text)
                goals=int(parent.contents[6].text)
                assists=int(parent.contents[7].text)
                games=int(parent.contents[5].text)
                minutes=int(parent.contents[21].text)
                team=parent.contents[3].text
                position=parent.contents[4].text
                age=int(parent.contents[2].text)
                average=float(parent.contents[20].text)
                plusminus=int(parent.contents[9].text)
                #record=parent.contents[12].text
                #current=parent.contents[1].text
                #fanpts=parent.contents[11].text
                listbox2=Listbox(root,bg='SpringGreen2')
                listbox2.grid(row=1,column=0,sticky=N,padx=0,pady=0)
                listbox2.insert(END,"Position: "+str(position))
                listbox2.insert(END,"Team: "+str(team))
                listbox2.insert(END, "Age: "+ str(age))
                listbox2.insert(END,"Points: " + str(points))
                listbox2.insert(END,"Goals: " + str(goals))
                listbox2.insert(END,"Assists: "+str(assists))
                listbox2.insert(END,"Games Played: "+str(games))
                listbox2.insert(END,"Minutes Played: "+str(minutes))
                listbox2.insert(END,"+/-: "+str(plusminus))
                listbox2.insert(END,"Shooting %: "+str(average))
                #listbox2.insert(END,"Record: "+str(record))
                #listbox2.insert(END,"Fan Pts: "+str(fanpts))
                #listbox2.insert(END,"Pre Season Ranking: "+str(current))
        
            
          

assistlist=[]
pointlist=[]
playerlist=[]
goallist=[]
lst=[]
lstprint=""
totalpts=0
print("Downloading Hockey Data")
site=requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')
if site.status_code is 200:
    content = BeautifulSoup(site.content, 'html.parser')
else:
    content=-99

    

root=Tk()
root.title("Hockey Pool")
root.geometry("600x600+0+0")
root.config(bg='orange')


can=Canvas(root,width=570, height=320)
can.grid(row=0,column=0, padx=10,pady=5)
image1=Image.open("HP.jpg")
photo=ImageTk.PhotoImage(image1)
can.create_image(0,0,anchor=NW, image=photo)

can.create_oval(5,15,200,130, fill="white", outline="#DDD", width=2)
can.create_line(75,50,160,50, fill="purple", width=6)
can.create_line(55,60,160,60, fill="blue", width=6)
can.create_line(65,87,160,87, fill="red", width=6)
can.create_line(85,97,160,97, fill="gold", width=6)
can.create_text(103,73, text="Hockey Pool", fill="black")

listbox=Listbox(root,bg='lightblue')
listbox.grid(row=1, column=0, sticky=NW,padx=10)


listbox.bind("<Button-1>", createlistbox)
listbox.bind('<<ListboxSelect>>',createlistbox)

add=Label(root,text="Add Players Below",bg='white')
add.grid(row=1,column=0,sticky=NE,padx=10)

remove1=Label(root,text="Delete a Player",bg='white')
remove1.grid(row=1,column=0,sticky=NE,padx=10,pady=49)
remove2=Label(root,text="= Double Click",bg='white')
remove2.grid(row=1,column=0,sticky=NE,padx=10,pady=73)

listbox.bind('<Double-Button-1>',remplayers)

add=Label(root,text="Created and Published by Austin Coleman",bg='lightblue')
add.grid(row=6,column=0,sticky=SE,padx=10)



OPTIONS=makeList()
var=StringVar(root)
var.set(OPTIONS[0])
w=OptionMenu(root,var,*OPTIONS,command=addplayers)
w.grid(row=1,column=0, padx=30, sticky=NE,pady=25)

readfile()


save=Button(root,text="Save", fg='black', command=saveList)
save.grid(row=4, column=0, sticky=W,padx=10)

checkpts=Button(root,text="Total Points", bg='white', fg='black',command=scrape)
checkpts.grid(row=2,column=0,sticky=W, padx=10)

mypts=Label(root,text=totalpts,bg='white')
mypts.grid(row=3,column=0,sticky=W, padx=10)

website=Button(root,text="Hockey Refrence Player List",command=openwebsite)
website.grid(row=6,column=0, sticky=SW, padx=10)

mainloop()