from graphviz import *


class Node:

    dot = None
    name = ""

    def __init__(self, name):
        self.dot = Graph()
        self.name = name

    def drawbox(self, token, msg):
        self.dot.node(token, msg, shape="box")

    def drawOval(self, token, msg):
        self.dot.node(token, msg, shape="box")

    def showFlowChart(self):
        self.dot.render(self.name + ".gv", view=True)


class Complier(Node):

    code = ""

    block = {"for", "while", "if", "elif", "else", "def", "lambda"}

    stack = []
    flowChart = Node()
    lastToken = None
    currentToken = "0"

    def __init__(self, code=""):
        self.flowChart.drawOval(self.currentToken, "start")
        self.updateToken()

        self.code = code

    def updateToken(self):
        self.lastToken = self.currentToken
        self.currentToken = str(int(self.lastToken) + 1)
