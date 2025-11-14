string_raw = "Alice:82,Bob:91,carol:74,dan:91,ellen:59"

list_top_students = []
failed_students = []
passed_students = {}

first_ = string_raw.split(",")
# Result: ['Alice:82', 'Bob:91', 'carol:74', 'dan:91', 'ellen:59']

# Split each student by colon to separate name from grade
second_step = [x.split(":") for x in first_]
# Result: [['Alice', '82'], ['Bob', '91'], ['carol', '74'], ['dan', '91'], ['ellen', '59']]

result = dict(second_step)

# Capitalize all student names
list_keys = list(result.keys())
for i in range(len(list_keys)):
    list_keys[i] = list_keys[i].capitalize()
# Result: ['Alice', 'Bob', 'Carol', 'Dan', 'Ellen']

# Convert all grade values from strings to integers
list_values = list(result.values())
for i in range(len(list_values)):
    list_values[i] = int(list_values[i])
# Result: [82, 91, 74, 91, 59]

# Update the dictionary with corrected names and integer grades
result.clear()
result.update(zip(list_keys, list_values))
# Result: {'Alice': 82, 'Bob': 91, 'Carol': 74, 'Dan': 91, 'Ellen': 59}

print("Number of valid students:", len(result))

avg_grade = float(sum(list_values) / len(result))
print("Average grade:", f"{avg_grade:.2f}") # avg to 2 decimal places

max_grade = max(list_values)
print("Maximum grade:", max_grade)

# Categorize students based on their grades
for key, value in result.items():
    if value == max_grade:
        list_top_students.append(key)
    if value < 60:
        failed_students.append(key)
    else:
        passed_students[key] = value

print(list_top_students)
print("Failed students:", failed_students)

# Sort passing students by grade in descending order
sorted_students = sorted(passed_students.items(), key=lambda x: x[1], reverse=True)
"""
key parameter tells how to sort
lambda function before colon input, after colon output,in this case value
"""
# Result: [('Bob', 91), ('Dan', 91), ('Alice', 82), ('Carol', 74)]

try:
    with open("passing.txt", "w") as file:
        for name, grade in sorted_students:
            file.write(f"{name}:{grade}\n")
    print(f"Saved {len(sorted_students)} passing students to passing.txt")
except Exception as e:
    print(f"Error writing to file: {e}")