from yt_dlp.utils import age_restricted

user_name = str(input("What is your name? "))
user_age = int(input("What is your age? "))
def calculate_birth_year(name,age):
    from datetime import datetime
    current_year = datetime.now().year
    birth_year = current_year-age
    return f"Hi {name},you were born on {birth_year}"

result = calculate_birth_year(user_name,user_age)
print(result)

