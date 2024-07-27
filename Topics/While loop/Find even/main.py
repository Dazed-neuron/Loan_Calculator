n = int(input())

# print all positive even numbers less than n
current_even = 2
even_list = []

while current_even < n:

    even_list.append(current_even)

    current_even += 2

even_list.sort()

for i in even_list:
    print(i)