# def pick_fruits(list of strings, num of fruits to return)

# function should return new list of strings with count number of fruits 
# in it from the fruits input list. Output should not contain fruit whose 
# name starts with a vowel (A, E, I, O, U)

# SET listOfFruits to [banana, apple, mange, orange, pineapple, honeydew]

# FUNCTION pick_fruits(fruitList, numFruits)
    # SET vowels to [a, e, i, o, u, A, E, I, O, U]
    # SET outputList to []
    # SET count to 0

    # FOR fruit in fruitList
        # IF numFruits is equal to 0
            # RETURN
        
        # IF length of fruitList is equal to 0
            # RETURN

        # IF fruit is in outputList
            # CONTINUE

        # IF fruit[0] is in vowels
            # PASS
        # ELSE
            # APPEND fruit to outputList
            # COUNT += 1

        # IF count is less than numFruits
            # IF fruit is equal to fruitList[-1]
                # RETURN outputList

        # IF count is equal to numFruits
            # RETURN outputList
    # ENDLOOP


listOfFruits = ['banana', 'banana', 'apple', 'mango', 'orange', 'pineapple', 'honeydew']
# emptyFruitList = []

def pick_fruits(fruitList, numFruits):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    outputList = []
    count = 0

    for fruit in fruitList:
        if numFruits == 0:
            print('Pick at least one fruit!')
            return

        if len(fruitList) == 0:
            print('Your list is empty..')
            return

        if fruit in outputList:
            continue

        if fruit[0] in vowels:
            pass
        else:
            outputList.append(fruit)
            count += 1

        if count < numFruits:
            if fruit == fruitList[-1]:
                return outputList
        
        if count == numFruits:
            return outputList
        

print(pick_fruits(listOfFruits, 3))
# print(pick_fruits(listOfFruits, 'one'))
# print(pick_fruits(emptyFruitList, 4))