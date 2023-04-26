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
# if odd
# write to even.txt
# write to odd.txt
# START