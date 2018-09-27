'''
testgui.py -basic ugly gui
acoleman - original coding, Sept. 21, 2018
'''
from tkinter import *
master = Tk()
master.config(backround="black")
label = Label(master, text="Hockey Pool")
label.config(backround="black")
label.config(foreground="white")
label.pack()
button + Button(master, text="QUIT", fg="red", command=quit)
button.pack(side=BOTTOM)
listbox = Listbox(master)
listbox.config(backround="black'")
listbox.config(foreground="white")
listbox.pack()
listbox.insert(END, "Player, Goals")
lst = {{"conner mcdavid,208"}, {"sidney crosby", 234}, {"steven stamkos", 187}, {"austen matthews", 70}}
for item in list:  
    listbox.insert(END, item(0) + "-" + str(item[1]))
    
mainloop()
