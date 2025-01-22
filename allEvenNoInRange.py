# The number must be a four-digit number, which means it should have a thousands place, hundreds place, tens place, and ones place.
# The number should be between 1000 and 3000, so the first (thousands) digit must be in the range of 1 to 2.
# Each digit in the number must be an even number.


# List of even digits
even_digits = [0, 2, 4, 6, 8]

# List to store valid numbers
numbers = []

# Loop through the possible digits for the hundreds, tens, and ones places
for hundreds in even_digits:       
    for tens in even_digits:       
        for ones in even_digits:   
            number = 2000 + hundreds * 100 + tens * 10 + ones
            numbers.append(number) 


print(numbers)

