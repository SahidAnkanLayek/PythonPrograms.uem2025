my_tuple = (4, 8, 12, 16)

# Trying to modify the second element
try:
    my_tuple[1] = 10  # This will raise an error
except TypeError as e:
    print("Error:", e)
