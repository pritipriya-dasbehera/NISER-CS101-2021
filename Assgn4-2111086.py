def factorise(n):
  """takes a number as input and returns the faactorisation"""
  div = 2
  string = ""
  while n > 1:
    divp = 0
    while n%div == 0:
      n=n//div
      divp += 1
    if divp > 0:
      string += str(div)+"^"+str(divp)+" * "
    div += 1
  return string


#get the input
n = int(input("what is the number you want to factorise: "))

#print output
print(factorise(n))
