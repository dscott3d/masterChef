from typing import ItemsView


FOODS = ["ice cream",
         "chocolate",
         "cheese cake",
         "burgers",
         "cheese"
         ]

FOODS = FOODS[0]

def bestFoods(FOODLIST):
    items = FOODLIST[::len(FOODLIST)-1]
    return(items)

def randomNewFunction(somethingIn):
    sorted_items = sorted(somethingIn)
    formatted_items = sorted_items[0] + "\n" + sorted_items[1]
    return (formatted_items)

if __name__ == "__main__":
    output = bestFoods(FOODS)
    # print (output)
    sorted_output = randomNewFunction(output)
    print (sorted_output)
