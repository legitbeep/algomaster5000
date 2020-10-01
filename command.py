from tkinter import END, INSERT

sym = {'{': '}',
		'[':']',
		'(':')', 
		'numofTab': 0,
		'last': "1"}



def saveText(editor):
	StringResult = editor.get(1.0, 'end-1c')
	print(StringResult.split(" "))


def completeSymbols(editor, c):
	editor.insert(END, sym[c])


def completeIndentation(editor):
	editor.insert('end-1c', sym['numofTab']*'\t')


def getKey(e, editor):

	print(e.char, sym['numofTab'], sym['last'])
	sym['last'] = editor.get(END)

	if sym['last'] == e.char and sym['last'] in sym.items():
		editor.delete(END)
		sym['last'] = "1"

	if e.char == chr(13):
		completeIndentation(editor)
	if e.char in sym:
		completeSymbols(editor, e.char)
		sym['numofTab'] += 1
