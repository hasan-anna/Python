# Project: Python Gradebook 
# Lists
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Attach to lists 
subjects.append("computer science")
grades.append(100)

# Combine 2 lists 
gradebook = list(zip(subjects,grades))
gradebook.append(("visual arts", 93))
print(gradebook)

# Add 2 list together 
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)
