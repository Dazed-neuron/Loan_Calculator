# Read a number from the user

# Initialize variables

# TODO: Write a while loop that calculates the sum of the first n positive odd integers
# Hint: In each iteration, add the current odd number to the sum and update the current odd number

# Print the sum
n = int(input())

sum = 0
i = 1

while n > 0:
    sum += i
    i += 2
    n -= 1

print(sum)
