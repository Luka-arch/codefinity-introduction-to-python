# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

apple_count = shelf.count("apples")
print("Number of Apples:", apple_count)

if apple_count < 5:
    print("Apples need to be restocked.")

else:
    print("Apples are sufficiently stocked.")

banana_index = shelf.index("bananas")
print("First Banana Index:", banana_index)

grapes_count = shelf.count("grapes")

if grapes_count <= 1:
    print("Grapes need to be restocked.")

else:
    print("Grapes are sufficiently stocked.")

storage_index = shelf.index("oranges")

if "oranges" in shelf:
    print("Oranges are at index:", storage_index)

else:
    print("Oranges are out of stock.")