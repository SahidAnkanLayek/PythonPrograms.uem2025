def math_operations(a, b):
    return (a + b, a - b, a * b, a / b if b != 0 else "Undefined")

# Example usage
result = math_operations(10, 2)
print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])
print("Quotient:", result[3])
