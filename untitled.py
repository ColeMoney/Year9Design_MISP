from tkinter import *
master = Tk()

def return_entry(en):
	"""Gets and prints the content of the entry"""
	content = entry.get()
	print(content)
	
Label(master, text="Input: ").grid(row=0, sticky=W)

entry = Entry(master)
entry.grid(row=0, column=1)

entry.bind('<Return>', return_entry)

mainloop()