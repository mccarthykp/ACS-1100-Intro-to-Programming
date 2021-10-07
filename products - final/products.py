# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
# load data 

def load(path):
    list = []
    with open(path, 'r') as data:
        for line in data:
            info = line.split(',')
            list.append(info)
    return list


# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
# check if user search query is in product list

def check_product_list(search_query, product_list):
    search_match = []
    for item in product_list:
        if search_query.lower() in item[1].lower():
            search_match.append(item)
    return search_match


# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
# display result string

def display_product_info(products):
    # print(type(product))
    if products is None:
        print('\nItem not found\n')
        exit()

    # item[id, name, price, number of units]
    for index, _ in enumerate(products):
        name = products[index][1]
        price = products[index][2]
        count = products[index][3].replace('\n', '')
        total = round((float(count) * float(price)), 2)
        print(f'\nName: {name}\nPrice: {price}\nCount: {count}\nTotal: {total}\n')
    return


# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
# runs display function and asks user if they'd like to make another search

def product_lookup(user_searched):
    display_product_info(user_searched)
    continue_search = input('Search Again?: (y/n) ')
    
    if continue_search.lower() == 'y':
        return True
    else:
        return False


# load file and set list variable to loaded data file
input_file_name = 'products.txt'
product_list = load(input_file_name)
running = True

while running:
    # get user search query
    user_search = input('\nSearch: ')
    user_searched = check_product_list(user_search, product_list)
    continue_running = product_lookup(user_searched)

    if continue_running == False:
        running = False
