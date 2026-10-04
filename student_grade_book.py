grades = {"Kyle": 79, "Jagadish": 99, "Charles": 93, "Molly": 96, "Phail": 49}
sum = 0
scores = []
for grade in grades:
    specific_grades = grades.get(grade)
    sum += specific_grades
    scores.append(specific_grades)
print("Scores List:", scores)
print("Sum of all grades:", sum)
class_average = sum / 5
print("Class Average:", class_average)

highest_grade = max(scores)
print("Highest grade:", highest_grade)
lowest_grade = min(scores)
print("Lowest grade:", lowest_grade)
print(f"The names of the students are:")
for names in grades:
    print(names, end= ", ")
name = input("\nEnter the name of the student you want to see the grade of: ")
names_searched = grades.get(name, "Sorry, student not here.")
print(names_searched)