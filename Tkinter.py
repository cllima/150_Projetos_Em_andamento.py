from tkinter import *



janela = Tk()
listbox = Listbox(janela)
listbox.pack(side=LEFT, fill=BOTH)
scrollbar = Scrollbar(janela)
scrollbar.pack(side=RIGHT, fill=BOTH)
for values in range(100):
    listbox.insert(END, values)


listbox.config(yscrollcommand=scrollbar.set)

scrollbar.config(command=listbox.yview)

janela.mainloop()
