import math

# ask the user for input number
n = int(input("Enter the number for mod 10007 to find power of 1234: "))
# performing mod operation
n = n % 10007

# handing error
if n == 0:
    print("Error input! cannot find value with mod function")

else:

    ans = math.log(n, 1234)

# print ans. value

print("The value of x is", ans)