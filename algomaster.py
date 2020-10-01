from tkinter import *
from tkinter import colorchooser
from command import saveText

class AutoComplete:

	numTab = 0
	lastChar = ""
	symbols = {'{': '}', '[':']', '(':')'}
	char = [0, 0]
	line = 1

	def __init__(self):
		self.numTab = 0
		self.lastChar = ""
		self.symbols = {'{': '}', '[':']', '(':')'}


	def completeSymbol(self, c):
		
		
		self.textBox.insert(END, self.symbols[c])
		self.textBox.mark_set("insert", "{}.{}".format(self.line,self.char[self.line]))
		self.char[self.line] += 1


	def deleteLast(self, textBox):
		textBox.delete(END)

	def keyStroke(self, e):
		

		temp = str(e.char)
		
		if len(temp)==0:
			return

		if temp.isalnum():
			self.lastChar += temp
		else:
			print(self.lastChar)
			self.lastChar = ""

		if ord(e.char)==8: 
			if self.char[self.line]==0:
				if self.line<=1:
					self.line = 1
				else:
					self.line -= 1
			else:
				self.char[self.line] -= 1


		elif ord(e.char)==13:
			self.line +=1
			self.char.append(0)

		else: self.char[self.line] += 1

		
		if e.char in self.symbols:
			self.completeSymbol(e.char)

		#print(ord(e.char), self.char, self.line)



class GuiAlgoMaster5000(AutoComplete):

	ide = Tk()
	textBox = None
	background = "purple"
	foreground = "white"
	editor = None
	toolbox = None
	suggestion = None



	def __init__(self, title = "Your title"):
		self.ide.title(title)
		self.editor = PanedWindow()
		
		self.textBox = Text(font=("Consolas"), bg=self.background, fg=self.foreground)
			
		self.editor.add(self.textBox)

		self.toolbox = PanedWindow(self.editor, orient=VERTICAL)
		
		
		
		self.toolbox.add(Button(self.toolbox, text="Press it",
								width = 10, height=10,
								command=lambda:saveText(self.textBox),
								))
		self.toolbox.add(Button(self.toolbox, text="Choose background",
								width = 10, height=10,
								command=self.chooseColor))
		self.toolbox.add(Button(self.toolbox, text="Press it here", command=self.chooseColorfg))
		self.editor.add(self.toolbox)

		self.editor.pack(fill=BOTH, expand= True)
	
	def chooseColorfg(self): 
  
	    # variable to store hexadecimal code of color 
	    color_code = colorchooser.askcolor(title ="Choose color")
	    if color_code[0]:  
	    	#setting fore choosen by user
		    self.textBox['fg'] = color_code[1]
		    

	def chooseColor(self): 
  
	    # variable to store hexadecimal code of color 
	    color_code = colorchooser.askcolor(title ="Choose color")
	    if color_code[0]:  
	    	#setting background choosen by user
		    self.textBox['bg'] = color_code[1]

		    #inverting background color to use it as foreground
		    fg = "#" + "".join([hex(255-int(i))[2:].zfill(2) for i in color_code[0]])

		    #setting foreground
		    self.textBox['fg'] = fgs
	    

	def main(self):
		self.textBox.focus_set() #inital focus is set to Textbox
		self.ide.bind("<KeyPress>", self.keyStroke) 
		self.ide.mainloop()


GuiAlgoMaster5000("AlgoMaster5000").main()