strang = input('''Gimme a string, and I'll reverse it.
''')
reversestrang = ''
def strang_reversal(strang, reversestrang):
  newchar = strang[-1]
  reversestrang = reversestrang + newchar
  # following line based on code from https://stackoverflow.com/questions/15478127/remove-final-character-from-string
  strang = strang[:-1]
  if len(strang) >= 1:
    strang_reversal(strang, reversestrang)
    return
  else:
    print(reversestrang)
    return
strang_reversal(strang, reversestrang)