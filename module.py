class Data:
	def __init__(self, KEY = "", VAL = "", DEPTH  = 0):
		self.key = KEY
		self.val = VAL
		self.depth = DEPTH
	def __str__(self):
		return self.key + " " + self.val + " " + str(self.depth)

class Blocker:

	def __init__(self):
		self.states = []
		self.token = { 'for', 'while', 'if', 'elif', 'else' }
		self.useless = { 'class' , 'def' }
		self.curDepth = 0 
		self.flagUseless = 0

	def splitter(self, code):

		for line in code.split('\n'):

			newLine = Data()
			cntTab = line.count('\t')
			line = line.replace('\t','')

			if len(line) == 0:
				continue

			key = self.getToken(line)
			self.curDepth = cntTab
			newLine.val = line
			newLine.key = key
		#	print(self.getToken(line) , self.flagUseless , self.checkToken(key))

			if self.checkToken(key) or self.flagUseless : 

				if cntTab == 0 and not self.checkToken(key):
					self.flagUseless = 0

			if self.flagUseless == 0 :

				if cntTab > self.curDepth:
					newLine.depth = self.curDepth

				elif cntTab < self.curDepth:
					newLine.depth = self.curDepth

				else :
					newLine.depth = self.curDepth

				self.states.append(newLine)
				

	def getToken(self,line):

		line = line.split()
		if line[0] in self.token :
			return line[0]
		elif line[0] in self.useless:
			return line[0]
		return "None"

	def checkToken(self,token):

		if token in self.useless:
			self.flagUseless = 1
			return True
		return False