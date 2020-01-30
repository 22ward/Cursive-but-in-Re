#Inquiring for user input
strang = input('''Gimme a string, and I'll reverse it.
''')
#Template for reversed string to be added to because you can't add stuff to a variable that doesn't exist
reversestrang = ''
def strang_reversal(strang, reversestrang):
  #Last var in char stored to var "newchar"
  newchar = strang[-1]
  #Adds "newchar" to what was on the existing reversed string (starts off as null on line 5)
  reversestrang = reversestrang + newchar
  # following line deletes last character and is based on code from https://stackoverflow.com/questions/15478127/remove-final-character-from-string
  strang = strang[:-1]
  #Determinator of whether or not to keep program going because if length is 0, there's nothing to reverse
  if len(strang) >= 1:
    strang_reversal(strang, reversestrang)
    return
  else:
    print(reversestrang)
    return
strang_reversal(strang, reversestrang)