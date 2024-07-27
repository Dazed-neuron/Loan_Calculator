# Function to test if a number is Positive, Negative, or Zero
def check_num(n):
    # Define your if-statement here to check the value of n and return "Positive", "Negative", or "Zero"
    if n > 0:
        print('Positive')
    elif n == 0:
        print('Zero')
    else:
        print('Negative')
# Testing your function with inputs
n = int(input())
# Remember to call the check_num function with a number as argument.
check_num(n)