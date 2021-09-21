import os
checklist = list()
running = True

# CREATE
def create(item):
    if item == 'x':
        return True
    else:
        checklist.append(item)

# READ
def read(index):
    print(checklist[index])

# UPDATE
def update(index, item):
    if index == 'x':
        return True
    else:
        checklist[index] = item

# DESTROY
def destroy(index):
    if index == 'x':
        return True
    else:
        checklist.pop(int(index))

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def list_all_items():
    print('\n')
    print('_______________________________')
    for i, item in enumerate(checklist):
        print('{}.) {}'.format(i, item))
        i += 1
    print('_______________________________')
    print('\n')

def mark_completed(index):
    if index == 'x':
        return True
    else:
        update(int(index), '√ ' + checklist[int(index)])
        read(int(index))
        return 
    return True
        

def select(function_code):
    # Create item
    if function_code == "a":
        input_item = user_input("Add item (x to cancel): ").lower()
        create(input_item)
        os.system('clear')
        return True

    # Remove item
    elif function_code == "r":
        item_index = user_input("Index Number (x to cancel): ").lower()
        destroy(item_index)
        os.system('clear')
        return True

    elif function_code == "m":
        item_index = user_input("Index Number (x to cancel): ").lower()
        mark_completed(item_index)
        os.system('clear')
        return True

    elif function_code == "q":
        os.system('clear')
        return False

    # Catch all
    else:
        os.system('clear')
        print("Unknown Option")
        return True

while running:
    list_all_items()
    selection = user_input('A to Add\nR to Remove\nM to Mark Item as Completed\nQ to Exit checklist.py\n\n').lower()
    running = select(selection)
    







# def test():
#     create("orange shirt")
#     create("red cloak")
#     update(0, "purple socks")

#     mark_completed(1)

#     user_value = user_input('Please enter a value: ')
#     print(user_value)
# test()