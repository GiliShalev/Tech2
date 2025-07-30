from tkinter.font import names

# Declare and initialize
grades = [100, 95, 100]
# Access an item
print(grades[0])
# Access a range
print(grades[0:2:1])
# Update value
grades[0] = 101
# Replacing cells
grades[0:1] = [20, 30]

# Append to the end
grades.append(99)
# Append multiple values
grades.extend([100, 101])
# Insert at a specific position
grades.insert(1, 98)
# Remove a value (only the first occurrence)
grades.remove(98)
# Remove a specific value
grades.pop(1)

print(grades.count(100))


# Get list length
list_len = len(grades)
# Reverse the order
grades.reverse()
# Sort the list
grades.sort(reverse=True)
# Empty the list
# grades.clear()
# Get the number of occurrences of a value
num_of_100 = grades.count(100)

# Loop through the list with a for loop
for grade in grades:
    print(grade)

for i in range(0, len(grades), 1):
    print(grades[i])

# Declare and initialize
names = ('John', 'Jane', 'Jeremy')

# Declare and initialize
grades_by_name = {'John': 93, 'Jane': 95, 'Jeremy': 100}
# Access an item
# If it doesn't exist, it will return None
print(grades_by_name.get("John"))
# If it doesn't exist, it will throw an error
print(grades_by_name["John"])
# Change\Add key
grades_by_name["David"] = 100

