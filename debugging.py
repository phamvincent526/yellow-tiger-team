#code snipper 1
x = 10
y = 1 # was 0, cannot divide by 0
result = x/y
print("Result:", result)

#code snippet 2

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i]) #cannot have a +1 here, as it would attempt to print the number spot 5, while there is none

#code snippet 3

def calculate_area(radius): #missing colon
    area = 3.14 * radius ** 2
    return area

radius = 5
print(calculate_area(radius))

#code snippet 4

def is_even(number):
    if number % 2 == 0: #missing colon
        return True
    else: # missing colon
        return False

print(is_even(4))
print(is_even(7))

#code snippet 5
for i in range(5): # missing colon
    print(i)

#code snippet 6
def greet(name):
    return "Hello, " + name  # missing +

print(greet("Alice"))

# code snippet 7

numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number #missing indent here
print("Sum of numbers:", sum)

#code snippet 8
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) # shouldnt be + 1 
    
print (factorial(5))

# code snippet 9

name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
    print("Hello," +  name)
else:
    print("Hello, stranger!")

#code snippet 10

def divide_numbers(x, y):
    result = x / y
    return result

num1 = 10
num2 = 5
print(divide_numbers(num1, num2))