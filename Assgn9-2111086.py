import random

#get inputs
m = int(input('input value of m :'))
n = int(input('input value of n :'))
p = int(input('input value of p :'))
q = int(input('input value of q :'))
A = []
B = []

#generate random matrix
for i in range(m):
  temp = []
  for j in range(n):
    temp.append(random.randint(0,10))
  A.append(temp)

for j in range(p):
  temp = []
  for k in range(q):
    temp.append(random.randint(0,10))
  B.append(temp)

#print matrices
print("A =",A)
print("B =",B)

#multiply and print result
if n!=p:
  print("multiplication not possible")
else:

  C = []
  for i in range(m):
    temp = []
    for k in range(q):
      summ=0
      for j in range(n):
          summ += A[i][j] * B[j][k]
      temp.append(summ)
    C.append(temp)
  
  print("A*B = C = ",C)
