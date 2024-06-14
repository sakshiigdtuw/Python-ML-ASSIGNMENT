from datetime import date
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


birth_date = date(2004,12,29)
print(f"Age: {calculate_age(birth_date)} years")
