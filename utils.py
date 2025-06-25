def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


def greet_user():
    name = input("What is your name: ")
    print(f"Hi {name}!")
    print("Welcome aboard!")

def decimal_checker(x):
    if float(x) % 1 != 0:
        decimal = True
    else:
        decimal = False
    return decimal


def kg_lbs_converter():
    print("--Kg/Lbs weight converter--")
    num_error = False # "number error" to loop if anything other than a number is entered
    while not num_error:
        weight = input("Please, enter your weight: ")

        if weight.isnumeric():
            num_error = True
        elif decimal_checker(weight):
            num_error = True
        else:
            print("""
That is an invalid value for weight
Please enter a whole or decimal number value
            """)
    # char_error is "character error" being used to loop the program
    char_error = False
    while not char_error:
        k_or_l = input("(K)g or (L)bs? ")
        if k_or_l.upper() == "K":
            print(str(weight) + " Kilograms")
            weight = float(weight) / 0.453592
            print(str(weight) + " Pounds")
            char_error = True
        elif k_or_l.upper() == "L":
            print(str(weight) + " Pounds")
            weight = float(weight) * 0.453592
            print(str(weight) + " Kilograms")
            char_error = True
        else:
            print("""
That is an unsupported character
Please enter an L, l, K, or k
            """)
            char_error = False
    print("Thank you for using Jordan's Kg/Lbs weight converter")
