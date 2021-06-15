number_of_jury = int(input())
final_grades = 0
number_of_presentations_grades = 0
presentation_name = input()

while presentation_name != "Finish":
    presentation_average_grade = 0
    for presentation_grade in range(number_of_jury):
        current_grade = float(input())
        presentation_average_grade += current_grade
        final_grades += current_grade
        number_of_presentations_grades += 1
    presentation_average_grade /= number_of_jury
    print(f"{presentation_name} - {presentation_average_grade:.2f}.")
    presentation_name = input()
final_average_grade = final_grades / number_of_presentations_grades
print(f"Student's final assessment is {final_average_grade:.2f}.")

