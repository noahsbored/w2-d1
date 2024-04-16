def add_items_to_list():
    """Function to add items to a list until user replies 'stop'"""
    my_list = []

    while True:
        item = input("Enter an item to add to the list (or type 'stop' to finish): ")
        
        if item == 'stop':
            break
        else:
            my_list.append(item)
    
    return my_list

def remove_item_from_list(my_list):
   
    
    print("Current list:", my_list)
    item_to_remove = input("Enter the item you want to remove: ")
    
    if item_to_remove in my_list:
        my_list.remove(item_to_remove)
        print(f"'{item_to_remove}' has been removed from the list.")
    else:
        print(f"'{item_to_remove}' is not in the list.")

def print_formatted_list(my_list):
    """Function to print the list in a formatted way"""
    if not my_list:                                              #i kinda struggled with formating this whole thing so i got help on this part, but i understand it now, enumerating just generates a pair of index and item for each item in the list, we made it start at 1 instead of 0, everyhting else i did myself
        
        print("The list is empty.")
    else:
        print("Your list:")
        for index, item in enumerate(my_list, start=1):
            print(f"{index}. {item}")


my_list = add_items_to_list()
print_formatted_list(my_list)
remove_item_from_list(my_list)
print_formatted_list(my_list)
