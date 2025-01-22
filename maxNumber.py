

number = input("Enter a 10-digit number: ")


if len(number) == 10 and number.isdigit():
    max_digit = '0' 
    
    for digit in number:
       
        if digit > max_digit:
            max_digit = digit
    
    print(f"The maximum digit is: {max_digit}")
else:
    print("Please enter a valid 10-digit number.")

