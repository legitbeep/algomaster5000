import os
import subprocess
import black


class formatter:
        def __init__(self, filename):
                os.system("black "+filename)
