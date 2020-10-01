import networkx as nx

class Complier:

	code = ""
	flowChat = nx.graph  
	def __init__(self, code=""):
		self.code = code

	def main():

		for i in code.split("\n"):
			for j in i:
				if "start"==j.lower():


