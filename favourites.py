# from typing import ItemsView  # why did you add this, it's not being used?

FOODS = ["ice cream",
         "chocolate",
         "cheese cake",
         "burgers",
         "cheese"
         ]

# FOODS = FOODS[0] # this is wrong, as you're changing FOODS from the above list to just be a list of one item

def bestFoods(passed_in_list_of_foods):
    # If you refer to FOODLIST, then we ignore the argument we passed in
    # items = FOODLIST[::len(FOODLIST)-1]  # this is a bit overkill, with a list, can just use [-1]
    sorted_foods = sorted(passed_in_list_of_foods)
    items = [sorted_foods[0], sorted_foods[-1]]
    return items

def randomNewFunction(somethingIn):
    # sorted_items = sorted(somethingIn)  # have sorted in the best foods function
    sorted_items = somethingIn
    formatted_items = sorted_items[0] + "\n" + sorted_items[1]
    return formatted_items  # I remove the brackets, aka parentheses here, not needed

if __name__ == "__main__":
    #print (bestFoods())
    output = bestFoods(FOODS)  # this is good, you pass in our master list
    # print (output)
    sorted_output = randomNewFunction(output)
    print (sorted_output)
