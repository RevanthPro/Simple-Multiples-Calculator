'''This is a Python code that takes input and gives all the multiples of the number below 100'''
number = list(range(1, 101)) #Creating range for the calcultor to find multiples
input = int(input("Please enter the number which you want the multiples of")) #Taking input from the user

for item in number:
    remainder = item % input
    if remainder == 0:
        print(item)