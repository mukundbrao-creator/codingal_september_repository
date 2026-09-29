name_score_pairs = {"Jagganath": 96, "Bhima": 97, "Vishnu": 98, "Krishna": 99, "Narayana": 100}
sum = 0
scores = []
for names in name_score_pairs:
    stored_scores = name_score_pairs.get(names)
    sum += stored_scores
    scores.append(stored_scores)
print("Scores List:", scores)
print("Sum of all grades:", sum)
class_average = sum / 5
print("Class Average:", class_average)

highest_grade = max(scores)
print("Highest grade:", highest_grade)
lowest_grade = min(scores)
print("Lowest grade:", lowest_grade)
name = input("Enter the name of the student you want to see the grade of: ")
names_searched = name_score_pairs.get(name, "Sorry, student not here.")
print(names_searched)