# Marks and percentage calculator

subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))
subject5 = float(input("Enter marks for subject 5: "))

total = subject1 + subject2 + subject3 + subject4 + subject5

percentage = (total / 500) * 100
average = total / 5

print(f"Total marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Average marks: {average:.2f}")