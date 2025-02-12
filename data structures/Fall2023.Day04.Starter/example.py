# Write a function that captures the run time of this program in terms of n.
# You can assume that each statement takes 1 unit of time.
n = 6
time = 0
print("You have 2 " + str(n) + "-sided dice.")
print("The values that each die can show are:")
for i in range(n):
    print(str(i + 1))
    time += 1

print("The values that each pair of dice can be are:")

for j in range(n):
    for k in range(n):
        print(str(j + 1) + " and " + str(k + 1))
        time += 1
print("Time taken: " + str(time))
