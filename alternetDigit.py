# Input 10-digit number
number = input("Enter a 10-digit number: ")


if len(number) == 10 and number.isdigit():
    alternate_digits = number[::2]  
    print(f"Alternate digits: {alternate_digits}")
else:
    print("Please enter a valid 10-digit number.")
