def life_in_weeks(age):
    lifespan_weeks = 90 * 52
    age_weeks = age * 52
    weeks_left = lifespan_weeks - age_weeks
    print(f"You have {weeks_left} weeks left.")


life_in_weeks(56)
