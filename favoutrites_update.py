FOODS = ["ice cream",
         "chocolate",
         "cheese cake",
         "burgers",
         "cheese"
         ]

def bestFoods(FOODLIST):
    items = FOODLIST[::len(FOODLIST)-1]
    first_last_items = items[0] + "\n" + items[1]
    return(items)

def randomNewFunction(somethingIn):
    return (sorted(somethingIn))

if __name__ == "__main__":
    output = bestFoods(FOODS)
    print (output)
    sorted_output = randomNewFunction(output)
    print (sorted_output)