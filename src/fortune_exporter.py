import random
import json
from datetime import datetime


FORTUNES = [
    "今天是你幸运日，大胆尝试新事物吧!",
    "保持耐心，好事即将发生。",
    "注意健康，适当休息。",
    "财运亨通，有机会获得意外之财。",
    "人际关系和谐，适合社交活动。",
    "工作上有突破，抓住机会展示自己。"
]

def get_fortune(birthday):

    return random.choice(FORTUNES)

def export_fortune(fortune, birthday):
    filename = f"fortune_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=== 今日运势 ===\n")
        f.write(f"查询时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        if birthday["year"]:
            f.write(f"出生日期: {birthday['year']}年{birthday['month']}月{birthday['day']}日\n")
        else:
            f.write(f"出生日期: {birthday['month']}月{birthday['day']}日\n")
        f.write(f"运势内容: {fortune}\n")
    
  
    data = {
        "query_time": datetime.now().isoformat(),
        "birthday": birthday,
        "fortune": fortune
    }
    
    json_filename = f"fortune_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
