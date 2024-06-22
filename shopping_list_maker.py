# Task 1 -- Write a function that lets the user add items to a list

shopping_list = []

while True:
    add_items = input("What would you like to ADD to the shopping list? (type 'done' to finish) ")
    
    if add_items.lower() == 'done':
        break
    
    items = add_items.split(',')

    for item in items:
        shopping_list.append(item.strip())
    
    print("Updated shopping list:", shopping_list)


# Task 2 -- Include a feature to remove items from the list

while True:
    remove_items = input("What would you like to REMOVE from the shopping list? (type 'done' to finish) ")
    
    if remove_items.lower() == 'done':
        break
    
    items = remove_items.split(',')

    for item in items:
        item = item.strip()
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print(f"{item} is not in the shopping list.")
    
    print("Updated shopping list:", shopping_list)


# Task 3 --  Add a function that prints out the entire list in a formatted way

print("\nFinal Shopping List:")

print(shopping_list)