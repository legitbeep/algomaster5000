import os
import black

class CodeExtractor:
        
        def __init__(self, file, stringFormat = False):
                if stringFormat:
                        __StringtoCode(self, code)
                        Formatter("flowchart$algomaster.py")
                else:
                        Formatter(file)

        def __StringtoCode__(self, code):
                file = open("flowchart$algomaster.py", "w")
                file.write(code)
                file.close()

        def __delete(self):
                os.system("rm flowchart$algomaster.py")


obj = CodeExtractor()

class Formatter:
        def __init__(self, filename):
                os.system("black -l 1000 "+filename)
