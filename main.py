# Write a program to check whether the given number is greater than 15 or smaller than 15.

num = float(input("What number do you choose?"))

if num > 15:
    print(f"Your number was bigger than 15 by {num - 15}")
else:
    print(f"Your number was lesser than 15 by {15 - num}")