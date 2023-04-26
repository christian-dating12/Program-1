# Chistian Dating | BSCPE 1-5

# Write a python program that reads a text file named numbers.txt that contains 20 integers. The program
# will create two other text file; the first text file will be named even.txt that will contains all even numbers 
# extracted from the numbers.txt. The second file will be named odd.txt that will contains all odd numbers 
# extracted from the numbers.txt.

input("\n\033[94mPress Any Key to Start...")
print("\033[90m=" * 80)

# Intro
import pyfiglet
greet = "GOOD DAY!"
print("\033[92m" + pyfiglet.figlet_format(greet, font = "Thin"))

# Pseudocode
import random
even = []
odd = []
# open numbers.txt (read), even.txt (append), odd.txt(append)
with open("numbers.txt", "w") as f:
    for i in range (20):
        num = random.randint(0,20)
        f.write(str(num) + "\n")

with open("numbers.txt", "r") as f:
    integers = f.readlines()
# read numbers.txt
# if even
for i in integers:
    if int(i) % 2 == 0:
        even.append(i)
# if odd
    else:
        odd.append(i)

# write to even.txt
with open("even.txt", "w") as f:
    for numbers in even:
        f.write(numbers)
# write to odd.txt
# START