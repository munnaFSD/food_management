food_inventory = [] # initialize empty list for favourite foods

#Options section
def options():
    print("\n------------------------------\nFavourite Foods Manager\n------------------------------")
    choice_options = ["Add Foods", "Remove Foods", "Remove all Foods", "View favourite all foods", "Exit or Cancel"]

    for index, options in enumerate(choice_options, start=1):
        print(f"{index}. {options}")



#Adding food to inventory
def add_foods():
    print("\n\tSelect one from the options below\n\t------------------------------")
    print("\t1. Single Food")
    print("\t2. Multiple Food")
    ask = input("\t>>> What kind of food do you want to add (1/2) ? ")

    #Condition part
    if (ask == "1"):
        food = input("\n\t>>> Enter your favourite food name: ")
        food_inventory.append(food.title()) #Added item in food inventory
        print(f"\n\t{food.title()} added Successfully")
    else:
        if (ask == "2"):
            foods = input("\n\t>>> Enter your favourite foods name (Allowed multiple food name):")
            convert_list = foods.title().split(" ") #Convert food item in list
            food_inventory.extend(convert_list) #Added multiple item in food inventory
            print(f"\n\t{convert_list} added Successfully ")




#Removing food to inventory
def remove_foods():
    food = input("\n\t>>> Enter a food name which you want to remove: ")
    con_title_case = food.title()
    if (con_title_case in food_inventory) :
        food_inventory.remove(con_title_case)
        print(f"\n\t{con_title_case} remove Successfully")

    else:
        print(f"\n\t{food} does not exists")



#Removing all food in inventory
def removes_foods():
    ask = input("\n\t>>> Do you want to remove all items (yes/no) ? ")

    if (ask == "YES") or (ask == "Yes") or (ask == "yes") or (ask == "Y") or (ask == "y") or (ask == "1"):
        food_inventory.clear()
        print(f"\n\tAll items were removed successfully")
    else:
        if (ask == "NO") or (ask == "No") or (ask == "no") or (ask == "N") or (ask == "n") or (ask == "0"):
            options() #will show options again
        else:
            print("\n\tInvalid choice/input!")



#View all foods
def view_all_foods():
    if not food_inventory:
        print("\n\tFood List is empty or didn't added yet! ")
    else:
        if food_inventory:
            print("\n\tYour favourite foods:")
            print("\t------------------------------")
            for index, each_food in enumerate(food_inventory, start=1):
                print(f"\t{index}. {each_food}")
                

while True:
    options()
    #From taken user input
    choice = input("\nChoose an Option: ")

    if (choice == "1"):
        add_foods()

    elif (choice == "2"):
        remove_foods()

    elif (choice == "3"):
        removes_foods()

    elif (choice == "4"):
        view_all_foods()
    
    elif (choice == "5"):
        print("\n\tThanks for using Favourite Foods Manager")
        break

    else:
        print("\n\tInvalid choice!")
