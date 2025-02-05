#  Storing Employee Information

# Problem Statement: You are managing a small office. For every new employee, you store their personal details like name, age, and joining year. Since this data does not change, you want to use an immutable data structure.

#Tasks:

# Create a tuple for an employee named "John" who is 30 years old and joined the company in 2015.
# You later realize that his age is incorrect. You want to store a corrected version of his details, but remember that you can’t modify the tuple directly. You need to create a new tuple.
# Print the employee's updated details.

employees = []

employees.append(("sahid",22,2026))
employees.append(("sahidLayek",23,2026))
employees.append(("sahidAnkan",24,2026))
print("/n the detailes of the employee :")
for emp in employees:
    name, age, joiningDate=emp
    print(f"name of the employee is : {name} ,age is : {age},joining date is :{joiningDate}")    


employees[1] = ("Bob", 36, 2010)  # directly update an existing tuple in the list by assigning a new tuple to a specific index

print("\n Updated version :")
for emp in employees:
    name, age, joiningDate=emp
    print(f"name of the employee is : {name} ,age is : {age},joining date is :{joiningDate}") 