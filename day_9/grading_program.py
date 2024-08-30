student_scores = {"Harry": 88, "Ron": 78, "Hermione": 95, "Draco": 75, "Neville": 60}

student_grades = {}
for key, value in student_scores.items():
    if value <= 70:
        student_grades[key] = "Fail"
    if 70 < value <= 80:
        student_grades[key] = "Acceptable"
    if 80 < value <= 90:
        student_grades[key] = "Exceeds Expectations"
    if 90 < value <= 100:
        student_grades[key] = "Outstanding"


print(student_grades)
