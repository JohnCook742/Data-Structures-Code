def sumManual(n):
  partialSum = 0
  for i in range(0, n+1):
    partialSum += i
  return partialSum

def sumRecursive(n):
  if n <= 0:
    return 0
  return n + sumRecursive(n-1)

# def sumFast(n):
#   return n * (n+1)/2

print(sumManual(10))

#print(sumRecursive(10))

# print(sumFast(10))
