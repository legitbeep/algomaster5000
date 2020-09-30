from tkinter import *
  
from tkinter import colorchooser   
# Function that will be invoked when the 
# button will be clicked in the main window 
def choose_color(): 
  
    # variable to store hexadecimal code of color 
    color_code = colorchooser.askcolor()  
    print(color_code) 
  
root = Tk() 
button = Button(root, text = "Select color", command = choose_color) 
button.pack() 
root.geometry("300x300") 
root.mainloop() 

'''

from tkinter import *
from command import *




editor = Tk()
editor.title("AlgoMaster 69")



maintext = PanedWindow()
maintext.pack(fill=BOTH)#, expand = 1)
textbox = Text()
maintext.add(textbox)

editor.bind("<KeyPress>", lambda e: getKey(e, textbox))
textbox.focus_set()

tools = PanedWindow(maintext, orient= VERTICAL)

maintext.add(tools)
t = Button(tools, text="Press")
b = Button(tools, text="Press again", command=lambda: saveText(textbox))
tools.add(t)
tools.add(b)

editor.mainloop()
'''