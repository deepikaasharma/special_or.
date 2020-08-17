"""Complete the function called special_or.

special_or takes two boolean expressions as parameters, and returns True or False corresponding to the or operator.

Notes:

    Do not use the or operator
    Use 'not' and 'and' operators instead

output = special_or(True, False)
print(output) # --> True

"""

"""if not(expression1):
    if not(expression2):
      return False
    else:
      return True
  elif not(expression2):
    if not(expression1):
      return False
    else:
      return True"""

def special_or(expression1, expression2):
  if not(expression1) and not(expression2):
    return False
  else:
    return True

output= special_or(True, False)
print(output)