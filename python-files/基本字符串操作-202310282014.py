week_str = 0
week_id = input('退出按t\n请输入星期数字（1-7）')
while week_id not in ['T', 't']:
    week_str = "星期一星期二星期三星期四星期五星期六星期天"
    pos = (eval(week_id) - 1) * 3
    print(week_str[pos:pos+3], len(week_str[pos:pos+3]))
    week_id = input('请输入星期数字（1-7）')
