x = 10
y = 10
z = 10
print(x)
print(y)
print(z)

#find max
if x > y:
  maxx = x
  if z > x:
    maxx = z
else:
  maxx = y
  if z > y:
    maxx = z
print(maxx)

#find min
if x < y:
  minn = x
  if z < x:
    minn = z
else:
  minn = y
  if z < y:
    minn = z
print(minn)
