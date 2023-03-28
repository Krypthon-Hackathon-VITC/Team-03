from tkinter import *
root = Tk()
root.title('Auto Select/Search')
root.iconbitmap('c:/gui/icon.ico')
root.geometry("500x300")
def update(data):
	my_list.delete(0, END)
	for item in data:
		my_list.insert(END, item)
def fillout(e):
	my_entry.delete(0, END)
	my_entry.insert(0, my_list.get(ANCHOR))
def check(e):
	typed = my_entry.get()

	if typed == '':
		data = toppings
	else:
		data = []
		for item in toppings:
			if typed.lower() in item.lower():
				data.append(item)
	update(data)
my_label = Label(root, text="Start Typing...",
	font=("TimesNewRoman", 14), fg="grey")
my_label.pack(pady=20)
my_entry = Entry(root, font=("TimesNewRoman", 20))
my_entry.pack()
my_list = Listbox(root, width=50)
my_list.pack(pady=40)
toppings = ["Shoe", "Shampoo", "Bottle",
	"Camera", "Balloon"]
update(toppings)
my_list.bind("<Button-2>", fillout)
my_entry.bind("<Button-1>", check)
root.mainloop()