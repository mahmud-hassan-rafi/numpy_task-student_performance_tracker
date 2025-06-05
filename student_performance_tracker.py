import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Input & Basic Setup
student = int(input("How many students?: "))
subjects = ["Physics", "Chemistry", "Math", "Biology"]
heading_row = ["Student Roll"] + subjects
student_names = [f"Roll-{i+1:<3}" for i in range(student)]

# Create an object-type 2D array to hold data
data = np.empty((student + 1, len(heading_row)), dtype=object)
data[0] = heading_row
data[1:, 0] = student_names

# Fill in random marks (30–100) for each subject
for i in range(1, student + 1):
    for j in range(1, len(heading_row)):
        data[i][j] = np.random.randint(30, 101)

# Show Full Data
print("\nFull Student Data:\n")
print(data)

# Numeric Data Extraction
numeric_data = data[1:, 1:].astype(np.int32)
roll_list = data[1:, 0]

# Total Marks per Student
print("\nTotal Marks per Student:\n")
for i in range(student):
    total = np.sum(numeric_data[i])
    print(f"{roll_list[i]} → {total}")

# Average Marks per Subject
avg_marks = np.mean(numeric_data, axis=0)
print("\nAverage Marks per Subject:")
for i in range(len(subjects)):
    print(f"{subjects[i]:<10}: {avg_marks[i]:.2f}")

# Topper in Each Subject
print("\nTopper in Each Subject:")
topper_indices = np.argmax(numeric_data, axis=0)
for i, idx in enumerate(topper_indices):
    print(f"{subjects[i]:<10} → {roll_list[idx]} ({numeric_data[idx, i]} marks)")

# Students Who Failed (any subject < 40)
print("\nStudents Who Failed in Any Subject:")
failed_flags = np.any(numeric_data < 40, axis=1)
failed_students = roll_list[failed_flags]
if len(failed_students) > 0:
    for name in failed_students:
        print(name)
else:
    print("All students passed")

# Max & Min Marks
max_val = np.max(numeric_data)
min_val = np.min(numeric_data)
max_pos = np.unravel_index(np.argmax(numeric_data), numeric_data.shape)
min_pos = np.unravel_index(np.argmin(numeric_data), numeric_data.shape)

print(f"\nHighest Mark : {max_val} → {roll_list[max_pos[0]]} in {subjects[max_pos[1]]}")
print(f"Lowest Mark  : {min_val} → {roll_list[min_pos[0]]} in {subjects[min_pos[1]]}")
