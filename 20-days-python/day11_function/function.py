# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def sum(a,b):
    return a+b

print(sum(5,6))
# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    sum = 0
    for i in args:
        if not isinstance(i,(int,float)):
            return f"Error: '{i}' is not a number. Please provide only numeric values."
        sum += i   
    return sum
print(add_all_nums(2,5,6))
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_seasons(month):
    if month == "march" or month == "april" or month == "may":
        return "spring"
    if month == "june" or month == "july" or month == "augest":
        return "summmer"
    if month == "september" or month == "october" or month == "november":
        return "fall"
    if month == "december" or month == "january" or month == "feburary":
        return "winter"
print(check_seasons("september"))
# Write a function called calculate_slope which return the slope of a linear equation
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050
# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.