prices = [10, 20, 30, 50]
total = 0
for item in prices:
    total += item
print(f"Your total is: {total}")

numbers = [2, 2, 2, 2, 7]
x_count = 0
x_string = ""
for count in numbers:
    while count > x_count:
        x_string += "X"
        x_count += 1
    x_count = 0
    print(x_string)
    x_string = ""


numbers = [1, 2, 2, 5, 4, 3, 4, 8, 9, 10]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)




