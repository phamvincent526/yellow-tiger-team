#task 1
food = "chicken tikka masala"
print(food)

print("the first 3 characters: ", food[:3])
print("the last 3 characters: ", food[-3:])
first_last = food[0] + food[-1]
print("the first and last characters: ", first_last)
split_str = food.split()
print("the split string: ", split_str)
print("the joined string: ", " ".join(split_str))

#task 2

number_list = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
number_list.append(9)
number_list.insert(3, 225)
number_list.pop()
number_list.remove(6)
print("the number list: ", number_list)

print("the first 3 numbers: ", number_list[:3])
print("the last 3 numbers: ", number_list[-3:])

#task 3

books = {"Elisabetta Dami" : "Four mice Deep in the Jungle", "Selina" : "Working in python", "Rabindranath Tagore" : "Gitanjali", 
         "J.K. Rowling" : "Harry Potter and the Philosopher's Stone" }
print(books.keys())
print(books.values())
print(books.get("Selina"))
books.pop("Rabindranath Tagore")
print(books)
del books["Elisabetta Dami"]
print(books)

