# find languages which start with letter p
languages = ['java', 'python', 'php', 'c', 'javascript', 'c++']
result = [i for i in languages if i[0] == 'p']
print(result)


# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'
basket = ['apple', 'guava', 'cherry', 'banana']
my_fruits = ['apple', 'kiwi', 'grapes', 'banana']
new_list = [i for i in my_fruits if i in basket if i.startswith("a")]
print(new_list)


# Example : accepts items with the small letter “o” in the new list
# Example : accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
result = [i for i in names if "o" in i]
result1 = [i for i in names if (len(i) > 4)]
print(f"Items with small letter 'o' in the list : {result}")
print(f"Items which have more than 4 letters : {result1}")
