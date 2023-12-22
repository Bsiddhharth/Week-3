pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}

def create_recipe():
    print("Available recipes:")
    for i in recipes.keys():
        print(f"- {i}")
    
    r_name = input("Enter the name of the recipe you want to create: ")

    if r_name in recipes:
        r_ingr = recipes[r_name]
        for ingr in r_ingr:
            if ingr in pantry:
                qty = r_ingr.count(ingr)
                if pantry[ingr] >= qty:
                    pantry[ingr] -= qty
                else:
                    print(f"Insufficient {ingr} in the pantry.")
                    return
            else:
                print(f"{ingr} is not available in the pantry. so cant prepare {r_name}")
                return

        print(f"{r_name} has been prepared.")
    else:
        print("Recipe not found.")

while True:
    print("\nMenu:")
    print("1. Create Recipe")
    print("2. View Pantry")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        create_recipe()
    elif choice == "2":
        print("\nCurrent Pantry:")
        for item, qty in pantry.items():
            print(f"{item}: {qty} ")
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
