# Lab 5 Vincent Pham

# step 1

def cat_greeting(word):
    print(f'Cat says {word}')

cat_greeting("meow")

#step 2

def generate_superhero_power():
    name = "Vincent"
    power = "Telekinesis"
    print(f'{name}, has {power}')

generate_superhero_power()

#step 3

def generate_superhero_power1():
    superpower = "flying"
    return superpower

print(f'returned super power is {generate_superhero_power1()}')

#step 4

def generate_superhero_power2(user, ability):
    return f"{user} has the ability of {ability}"

user = input("enter name: ")
ability = input("power: ")

result = generate_superhero_power2(user, ability)
print(result)

#step 5

def cat_greetings_loop():
    for i in range(5):
        print("meow")

cat_greetings_loop()

#step 6

def generate_multiple_powers(superpowers):
    for superpower in superpowers:
        print("Superpower:", superpower)


multiple_powers = ["flight", "super speed", "telekinesis", "invisibility", "fire"]

generate_multiple_powers(multiple_powers)

