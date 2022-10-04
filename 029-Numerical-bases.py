number = int(input("Type an integer: "))
print("What will be the conversion basis?")
print("[1] to binary;")
print("[2] to octal;")
print("[3] to hexadecimal.")
base = int(input())
while base < 1 or base > 3:
    print("Try again.")
    print("[1] to binary;")
    print("[2] to octal;")
    print("[3] to hexadecimal.")
    base = int(input())
if base == 1:
    print(f"Your number in binary is: {bin(number)[2:]}")
elif base == 2:
    print(f"Your number in octal is: {oct(number)[2:]}")
else:
    print(f"Your number in hexadecimal is: {hex(number)[2:]}")