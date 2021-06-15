incoming = float(input())
grade = float(input())
min_salary = float(input())
social_scholarship = int(min_salary * 0.35)
excellent_scholarship = int(grade * 25)

if grade >= 5.50:
    if social_scholarship > excellent_scholarship and incoming < min_salary:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
elif 4.50 < grade < 5.50:
    if incoming < min_salary:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print(f"You cannot get a scholarship!")
else:
    print(f"You cannot get a scholarship!")
