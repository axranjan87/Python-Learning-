"""@WAP to fill template given below with name and date
letter = '''Dear <|Name|>,
You are Selected
<|Date|>'''
"""


letter = '''Dear <|Name|>,
You are Selected
<|Date|>'''

print(letter.replace("<|Name|>","Ayush").replace("<|Date|>","22 March 2026"))