from tkinter import *
from tkinter import colorchooser
from math import floor




class AutoComplete:

	numTab = 0
	lastChar = ""
	symbols = {'{': '}', '[':']', '(':')'}

	def __init__(self):
		self.numTab = 0
		self.lastChar = ""
		self.symbols = {'{': '}', '[':']', '(':')'}


	def CompleteSymbol(self, textBox, c):
		textBox.insert(END, self.symbols[c])


	def DeleteLast(self, textBox):
		textBox.delete(END)


class Editor(AutoComplete):

	pass


class GuiAlgoMaster5000:

	ide = Tk()
	textBox = None
	background = "purple"
	foreground = "white"
	editor = None
	toolbox = None



	def __init__(self, title = "Your title"):
		self.ide.title(title)
		self.editor = PanedWindow()
		
		self.textBox = Text(font=("Consolas"), bg=self.background, fg=self.foreground)
		self.editor.add(self.textBox)

		self.toolbox = PanedWindow(self.editor, orient=VERTICAL)
		a = Button(self.toolbox, text="Press it here")
		a.pack(side=BOTTOM)
		
		self.toolbox.add(Button(self.toolbox, text="Press it"))
		self.toolbox.add(Button(self.toolbox, text="Choose background", command=self.choose_color))
		self.toolbox.add(a)
		self.editor.add(self.toolbox)

		self.editor.pack(fill=BOTH, expand= True)
		self.ide.mainloop()

	def choose_color(self): 
  
	    # variable to store hexadecimal code of color 
	    color_code = colorchooser.askcolor(title ="Choose color")
	    if color_code[0]:  
		    self.textBox['bg'] = color_code[1]
		    s = "#" + "".join([hex(255-int(i))[2:].zfill(2) for i in color_code[0]])
		    self.textBox['fg'] = s
	    

	def main(self):
		pass


GuiAlgoMaster5000().main()