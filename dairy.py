import favourites

print (favourites.FOODS)

food_dictionary = {"ice cream": "dairy", 
                   "chocolate": "dairy", 
                   "cheesecake": "dairy",
                   "burgers": "non-dairy",
                   "cheese": "dairy"}

def check_for_dairy(pass_in_foods):
    if food_dictionary[pass_in_foods] == "dairy":
        contains_dairy = True
    else:
        contains_dairy = False
    return contains_dairy
    
print(check_for_dairy(favourites.FOODS[3]))