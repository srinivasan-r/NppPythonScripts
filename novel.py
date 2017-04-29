console.clear()
text = editor.getText()
console.write(text)
editor.addText("\n")
for i in range(139,150):
	editor.addText(text + str(i)+'-1'+"\n")
	editor.addText(text + str(i)+'-2'+"\n")
	editor.addText(text + str(i)+'-3'+"\n")
console.write("DOne")