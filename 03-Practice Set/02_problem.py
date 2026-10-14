name = input("enter  your name: ")
letter = '''
dear <|name|>
YOU ARE SELECTED!
<|DATE|>'''
print(letter.replace("<|name|>",name).replace("<|DATE|>"
 ,"06 june 2026"))