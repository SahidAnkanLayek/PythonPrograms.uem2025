def check_membership(t, element):
    return element in t

# Example usage
sample_tuple = (10, 20, 30, 40, 50)
print(check_membership(sample_tuple, 30))  # True
print(check_membership(sample_tuple, 60))  # False
