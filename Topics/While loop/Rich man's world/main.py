principal = int(input())

interest_rate = 7.1
years = 0

while principal < 700000: # repeat until deposit is higher than 700K

    # calculate percentage of interest_rate
    interest = principal * interest_rate / 100

    # add this to the initial deposit
    principal += interest

    years += 1

print(years)


