#get input
print("This program prints the integration of (a2*x^2 + a1*x + a0) from limit x = lb to x = ub with the precision of interval p")

a2 = float(input("a2 = "))
a1 = float(input("a1 = "))
a0 = float(input("a0 = "))
lb = float(input("lb = "))
ub = float(input("ub = "))
p = float(input("p = "))

#function on x
def func(x):
	return (a2*x**2 + a1*x + a0)

#crx is the current value of x
crx = lb
integral = 0
while crx < ub:
  h = (func(crx) + func(crx + p))/2
  integral += h*p
  crx += p
print(integral)
