def age_assignment(*names, **ages):
    age_dict = {name: 0 for name in names}

    for first_letter, age in ages.items():
        for name in age_dict:
            if name.startswith(first_letter):
                age_dict[name] = age

    return age_dict


print(age_assignment('Peter', 'George', G=26, P=19))