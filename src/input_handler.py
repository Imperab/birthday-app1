from datetime import datetime

def get_users_birthday():
    while True:
        try:
            date_str = input("请输入您的出生日期 (格式: YYYY-MM-DD 或 MM-DD): ")
            
            if len(date_str.split('-')) == 2:
               
                month, day = map(int, date_str.split('-'))
                year = None
            else:
               
                year, month, day = map(int, date_str.split('-'))
                
           
            if year and (year < 1900 or year > datetime.now().year):
                print("年份无效，请重新输入!")
                continue
                
            if month < 1 or month > 12:
                print("月份无效，请重新输入!")
                continue
                
            if day < 1 or day > 31:
                print("日期无效，请重新输入!")
                continue
                
            return {"year": year, "month": month, "day": day}
            
        except ValueError:
            print("格式错误，请按照指定格式输入!")