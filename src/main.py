from src.input_handler import get_user_birthday
from src.birthday_calculator import calculate_days
from src.constellation import get_constellation
from src.fortune_exporter import get_fortune, export_fortune

def main():
    print("=== 生日查询小程序 ===")
    
    # 获取用户生日
    birthday = get_user_birthday()
    
    while True:
        print("\n请选择功能:")
        print("1. 查询距离下一个生日天数")
        print("2. 查询星座")
        print("3. 查询当日运势并导出")
        print("4. 退出")
        
        choice = input("请输入选项 (1-4): ")
        
        if choice == '1':
            days_until, days_lived = calculate_days(birthday)
            print(f"距离下一个生日还有: {days_until} 天")
            if days_lived:
                print(f"您已经出生了: {days_lived} 天")
                
        elif choice == '2':
            constellation = get_constellation(birthday)
            print(f"您的星座是: {constellation}")
            
        elif choice == '3':
            fortune = get_fortune(birthday)
            print(f"您今日的运势: {fortune}")
            export_fortune(fortune, birthday)
            print("运势已导出到文件!")
            
        elif choice == '4':
            print("感谢使用，再见!")
            break
            
        else:
            print("无效选项，请重新选择!")

if __name__ == "__main__":
    main()