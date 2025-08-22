from datetime import datetime, date

def calculate_days(birthday):
    today = date.today()
    year = birthday["year"]
    month = birthday["month"]
    day = birthday["day"]
    

    next_birthday = date(today.year, month, day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, month, day)
    
    days_until = (next_birthday - today).days
    
    
    day_lived = None
    if year:
        birth_date = date(year, month, day)
        days_lived = (today - birth_date).days
    
    return days_until, days_lived