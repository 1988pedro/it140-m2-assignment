# Name: Anayo Pedro Okafor
# Course: IT 140 Module Two Assignment
# Description: Prompts user for name and age, then calculates birth year.

user_name = input("What is your name? ")
user_age = int(input("How old are you? "))

current_year = 2026
birth_year = current_year - user_age

print(f"\nHello {user_name}! You were born in {birth_year}.")
