###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    num = ord(char)
    # add one to the character's code
    num = num + 1
    # replace new character code with its
    # corresponding character (use chr())
    code = chr(num)
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text + code

print(plain_text)
print(encrypted_text)