#take inputs
print("This program will take the number n of total votes and the number of\\
candidates k as input and declare the winner based on votes")
n = int(input("total number of votes is : "))
k = int(input("total number of candidates are : "))
data = {}

#loop to get name inputs
for i in range(n):
  name = input('enter name of candidate : ')
  if name not in data:
    data[name]=1
  else:
    data[name]+=1

#find max
flag = 0
maxx = 0
maxl = []
for key in data:
  if data[key]>maxx:
    maxn = key
    maxx = data[key]
    maxl = []
    maxl.append(key)
    flag = 0

  elif data[key]==maxx:
    maxl.append(key)
    flag = 1

#print result
if flag==0:
  print('the winner of the poll is '+maxn+' with a maximum vote of '+str(maxx))
else:
  print('there is a tie between ')
  for x in maxl:
    print(x + ' ')
  print('for the maximum vote of ',str(maxx))

