#get input
print("this program ges input of x and n prints the output x^n")
x = int(input("what is the value of x :"))
n =int(input("what is the value of n :"))

#iterative power
def itt(x,n):
  i=0
  power=1
  while i<n:
     power *= x
     i += 1
  return power

#recursive power
def rec(x,n):
  if n==0:
    power = 1
  elif n==1:
    power = x
  else:
    if n%2 == 0:
      power = (itt(x,n//2))**2
    else:
      power = ((itt(x,(n-1)//2))**2) * x
  return power

#output
print('itterative power calculation',x,'^',n,' = ',itt(x,n))
print('recurssive power calculation',x,'^',n,' = ',rec(x,n))
