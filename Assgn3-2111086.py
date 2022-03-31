"""converts input base 10 into base i given by user"""

bs10 = int(input("Inout the number in base 10: "))
i = int(input("Input the base of output: "))
out = 0
counter = 0

while bs10 > 0:
  dig = bs10 % i
  bs10 = bs10 // i
  out += (10**counter) * dig
  counter += 1

print(out)
