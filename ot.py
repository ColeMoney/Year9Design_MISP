from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

lst=[]
lstprint=""
totalpts=0
print("Downloading hockey data")
site=requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')

def update_lab():
    lstprint=""
    for item in lst:
        lstprint=lstprint+item+"\n"
    mylab.configure(text=lstprint)
  
  
# a function that adds item when called  
def addItem():
    item=entry.get()
    if(lst.count(item)==0):
        lst.append(item)
        entry.delete(0,END)
        update_lab()
def removeItem():
    item=entry.get()
    if lst.count(item)>0:
        lst.remove(item)
        entry.delete(0,END)
        update_lab()

def saveList():
    myfile=open("myplayers.txt","w")
    for player in lst:
        myfile.write(player+"\n")
    myfile.close()
    root.filename=filedialog.asksaveasfilename(initialdir="/", title="Select file")
    print(root.filename)
    messagebox.showinfo("myplayers/txt", "players saved to disk")

def scrape():
    if(messagebox.askyesno("Wait?", "This could take a few seconds. Wait?")==False):
        return
    if site.status_code is 200:
        content = BeautifulSoup(site.content, 'html.parser')
        totalpts=0
        for myplayer in lst:
            dTag=content.find(attrs={"csk": myplayer})
            parent=dTag.findParent("tr")
            if parent==False:
                break
            playerpts=int(parent.contents[8].text)
            totalpts=totalpts + playerpts
        mypts.configure(text=totalpts)
        

        


#makes a blank list that will be your players        

root=Tk()
root.geometry("500x380+0+0")
root.title("hockey pool")
#root.config(bg='deep sky blue')

instlab=Label(root,text="Input (e.g.McDavid,Connor):")
instlab.pack()

#makes an input for the user to type into
entry=Entry(root)
entry.pack()

#this creats a button and it calls the addItem function when clicked
addbutton=Button(root,text="Add",bg='deep sky blue',fg='lawn green', command=addItem)
addbutton.pack()

removebutton=Button(root, text="Remove", command=removeItem)
removebutton.pack()

savebutton=Button(root, text="Save", command=saveList)
savebutton.pack()

checkbutton=Button(root, text="Checkpoints", command=scrape)
checkbutton.pack()

mypts=Label(root, text=totalpts)
mypts.pack()

mylab=Label(root, text=lstprint, anchor=W, justify=LEFT)
mylab.pack()

mainloop(