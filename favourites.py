FOODS = ["ice cream",
         "chocolate",
         "cheese cake",
         "burgers",
         "cheese"
         ]

FOODS = FOODS[0]

def bestFoods():
    return randomNewFunction(FOODS)

def randomNewFunction(somethingIn):
    return sorted(somethingIn)

if __name__ == "__main__":
    print (bestFoods())
