###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''
x = 0
y = ''

for char in plain_text:
    # read the character's code (use ord())
    x = ord(char)
    # add one to the character's code
    x = x + 1
    # replace new character code with its
    # corresponding character (use chr())
    y = chr(x)
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text + y
    x = 0
    y = ''

print(plain_text)
print(encrypted_text)