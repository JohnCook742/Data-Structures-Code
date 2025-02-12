def sum(n):
    partialSum = 0
    for i in range(n + 1):
        partialSum += i
    return partialSum

def smartSum(n):
    numerator = n * (n + 1)
    return numerator/2

print(sum(100))

print (smartSum(100))

## sum                      # smartSum
# call sum(0)               call smartSum
# initialize partialSum     initialize numerator
# start a for loop          calculate numerator
# check i against 0         return result
# increase partialSum       print result
# return partialSum
# print the result          5 calls for all numbers O(1)

# 0: 7 calls

# call sum(1)
# initialize partialSum
# start for loop
# check i against 1
# increase partial sum
# check i against 1
# increase partialSum
# return partial sum
# print the result

# 1: 9

# 5 steps always run only once
# f(n) = 5 + 2(n + 1)       O(n)
