text = 'Hello world'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
""" 
index = alphabet.find(text[0].lower())
shifted = alphabet[index + shift]
print (shifted)
"""
encrypted_text =''

for char in text.lower():
  index = alphabet.find(char)
  new_index = index + shift
  encrypted_text += alphabet[new_index]
  print ('char:', char, 'encrypted_text:', encrypted_text)