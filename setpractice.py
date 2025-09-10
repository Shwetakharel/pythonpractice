# print 1st 10 numbers and their squares
result = {i: i**2 for i in range(1, 11)}
print(result)

# using zip
days = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]
temp_C = [30.5, 32.6, 31.8, 33.4, 29.8, 30.2, 29.9]
result = {key: value for key, value in zip(days, temp_C)}
print(result)


# using if condition . pull all the values greater than 0
products = {'phone': 10, 'laptop': 0, 'charger': 32, 'tablet': 0}
result = {key: value for key, value in products.items() if value > 0}
print(result)


# Nested Comprehension
# print tables of number from 2 to 4
result = {i: {j: j * i for j in range(1, 11)} for i in range(2, 5)}
print(result)
