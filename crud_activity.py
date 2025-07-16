cookbook = []

def create(recipe):
    cookbook.append(recipe)
    print(f'"{recipe}" was added.')

def read(index):
    if index >= len(cookbook) or index < 0:
        print("invalid")
    else:
        print(f"at {index}, there is '{cookbook[index]}'.")

def update(index, recipe):
    if index >= len(cookbook):
        print ("invalid")
    else:
        old_recipe = cookbook[index]
        cookbook[index] = recipe
        print(f'"{old_recipe}" was changed to "{recipe}".')

def destroy(index):
    if index >= len(cookbook) or index < 0:
        print("invalid")
    else:
        removed = cookbook.pop(index)
        print(f'"{removed}" was removed.')

def list_all_recipes():
    if len(cookbook) == 0:
        print("the cookbook is empty")
    else:
        print("cookbook includes:")
        i = 0
        for recipe in cookbook:
            print(i, ":", recipe)
            i = i + 1

def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()

