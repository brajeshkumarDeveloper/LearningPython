# {expression for item in iterable if condition}

favourite_chais= ["masala Chai", "ginger tea", "lemon tea", "black tea", "green tea", "masala Chai", "ginger tea"]

unique_favourite_chais= {my_tea for my_tea in favourite_chais if "tea" in my_tea}
print(unique_favourite_chais)


recipes= {
    "masala Chai": ["water", "milk", "sugar", "tea leaves", "spices"],
    "ginger tea": ["water", "milk", "sugar", "tea leaves", "ginger"],
    "lemon tea": ["water", "lemon", "sugar", "tea leaves"],
    "black tea": ["water", "tea leaves"],
    "green tea": ["water", "green tea leaves"]
}

unique_spices={spice for ingredients in recipes.values()
               for spice in ingredients }
print(unique_spices)