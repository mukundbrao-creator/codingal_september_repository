basket1 = {"apple", "mango", "kiwi", "apple", "grape"}
basket2 = {"mango", "banana", "apple", "watermelon"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)

basket1.add("orange")
print("Basket 1 after adding orange:", basket1)

common_fruits = basket1.intersection(basket2)
print("Common Fruits Between Both Baskets:", common_fruits)

import array as arr
fruit_counts = arr.array("i", [2, 2, 1, 1, 1, 1])
print("Fruit Count Array:", fruit_counts)
fruit_counts.insert(1, 2)
fruit_counts.append(3)
print("Updated Array:", fruit_counts)

fruit_counting = fruit_counts.count(1)
print("Number of time 1 appears:", fruit_counting)
fruit_counts.reverse()
print("Reversed Fruit Count:", fruit_counts)

print()
print("===== CLASS FRUIT BASKET ORGANIZER =====")
print("Basket 1:", basket1)
print("Basket 2:", basket2)
print("Shared Fruits:", common_fruits)
print("Fruit Count:", fruit_counts)
print("=" * 25)