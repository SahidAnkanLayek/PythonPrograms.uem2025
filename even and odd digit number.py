
number = input("Enter a 4-digit number: ")

even_digits = []
odd_digits = []
even_count = 0
odd_count = 0


for digit in number:
    if int(digit) % 2 == 0:
        even_digits.append(digit)
        even_count += 1
    else:
        odd_digits.append(digit)
        odd_count += 1

print(f"Even digits: {', '.join(even_digits)}")
print(f"Odd digits: {', '.join(odd_digits)}")
print(f"Total even digits: {even_count}")
print(f"Total odd digits: {odd_count}")



