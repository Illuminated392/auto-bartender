import customtkinter
import sys

sys.path.append("..")

from UserInterface.ModificationFrame import ModificationFrame as ModFrame


app = customtkinter.CTk()

app.geometry("500x500")

total=10
items=["a", "b", "c", "d", "e","f"]
values=[0,2,1,0,0,5]


mFrame = ModFrame(app, items, values, total)
mFrame.grid(row=0, column=0)



app.mainloop()



