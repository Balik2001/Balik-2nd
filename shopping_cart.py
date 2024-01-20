Shopping_list = []

while True:
    user1 = input("Please enter an item")
    Shopping_list.append(user1)

    choice = input("Would you like to continue? y/n")
    if choice == "n":
        break

for i in Shopping_list:
    print("This is your current shopping list ",i)

while True:
    choice2 = input("Would you like to remove anything from the list? y/n")
    if choice2 == "y":
        pattern = input("What is the item you want to remove?")
        deleted_item = Shopping_list.remove(pattern)
    else:
        break

for i in Shopping_list:

    print("This is the updated shopping list \n :", Shopping_list)







