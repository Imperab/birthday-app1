from datetime import datetime, date

def calculate_days(birthday):
    today = date.today()
    year = birthday["year"]
    month = birthday["month"]
    day = birthday["day"]
    
    # 计算下一个生日
    next_birthday = date(today.year, month, day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, month, day)
    
    days_until = (next_birthday - today).days
    
    # 计算已出生天数（如果有年份）
    days_lived = None
    if year:
        birth_date = date(year, month, day)
        days_lived = (today - birth_date).days
    
    return days_until, days_lived