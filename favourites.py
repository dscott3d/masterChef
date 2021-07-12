FOODS = ["ice cream",
         "chocolate",
         "cheese cake",
         "burgers",
         "cheese"
         ]

def bestFoods(passed_in_list_of_foods):
    sorted_foods = sorted(passed_in_list_of_foods)
    items = [sorted_foods[0], sorted_foods[-1]]
    return items

if __name__ == "__main__":
    output = bestFoods(FOODS)
    print (output)

testing