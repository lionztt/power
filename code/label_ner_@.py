myType = {
    1: ['发电机', '罐式断路器', '断路器', '电流电压互感器', '变压器', '避雷器', '六氟化硫电气设备', 'SF6设备', '气体绝缘设备', '高压电缆', 'SF6断路器', 'GIS开关设备', '干式变压器绕组', '站用变', '高压开关柜'],
    2: ['继电器', '控制开关', '指示灯', '测量仪表', '气体管路', '测量管路', '气体管道', '测量管道', '都标装置', '尾气回收装置', '电阻电容式湿度计', '电解式湿度计', '湿度计', '冷凝式露点仪', '取样管道',
        'SF6气体检漏仪', '密度监视器', '接地引线', '仪器管路', 'SF6气体检漏仪', '皂膜流量计', '吹洗仪器', '保护盖帽', '密度监视器', '色谱仪', '同轴电缆', '二次线缆', '检测仪器', '取气阀门', '气体采集装置',
        '气体采样容器', '采样器', '接地线', '尾气回收装置', 'SF6新气对检测仪', '调节针型阀', '保护盖帽', '铁心'],
    3: ['国家电网公司', '国家电网公司国家电力调度中心', '省公司运检部', '省评价中心', '国网评价中心', '省检修公司'],
    # 4: ['小时', '天', '年', '月', '秒'],
    5: ['SF6气体湿度', '电缆外护层接地电流', '气体密封性', '直流参考电压', 'UnmA', 'μL/L', '氢气', '总烃', 'kV', '风速', '环境温湿度', '红外热像', '放电信号', '放电频次', '管道无渗漏', '管道壁厚',
        '测量准确度', '测量时间', '取样总流量', '气体湿度', '气体压力', '露点值', '设备压力', '湿度', '测量流量', '气样湿度', 'SF6气体', '含氧量', 'CO气体', 'SO2', 'H2S气体', '检测量程', '气体流量', '限流电阻',
        '直流电阻', '保护硅堆', '电阻值', '电流', '功率', '密度', '界面张力', '电阻', '质量'],
    6: ['带电检测记录', 'PMS系统', '检测日期', '停电试验报告', '不锈钢管', '铜管', '聚四氟乙烯管', '管道内壁', '高弹性材料管道', '橡皮管', '聚氯乙烯管', '气体收集袋标', '接头', '吹风机', '带电检测', '测量尾气',
        '标准化作业工艺卡', '移相', '波形图', '趋势图', '冷凝露点式', '三相', '仪器排气口', '辅助气', '分子筛', '档案分析判断法', '干燥氮气', '杂质微粒', '油污', '真空泵', '真空压力表', 'DL/T', 'VY', 'VX',
        '带电检测', '采样容器', '气体采样', '工作站', '数据分析系统', '色谱柱', '聚四氟乙烯垫片', 'SF6气体分解产物', '气体收集袋', '真空压力表', '取样阀', '针阀', '调节阀', '管道内壁', '高压电源', '通风设备',
        '分子筛', '湿敏元件', '针型阀门', '三通阀', 'TCD检测器', '合闸线圈', '分闸线圈', '绝缘拉杆', '电容器', '微安表', '交流高电压', '变径活塞泵', '脱气容器', '磁力搅拌器', '喷淋系统', '气体灭火装置', 'GIS',
        '消弧线圈', '隔离开关', '分闸行程曲线测试', '合闸阀', '阀针', '铂丝圆环', '直流高电压', '恒温定时振荡器', '自动顶空进样器', '污水泵', '潜水泵', '排水泵', '控制电源', '空气开关', '接地引下线', '顶空色谱法原理',
        '绝缘油', '高频阻波器', '高压绕组', '主变冷却系统', '不间断电源系统']
}


def read_need_label_file(input_file_path, out_file_path):

    out_file = open(out_file_path, 'w')
    input_file = open(input_file_path, 'r')
    print('开始读入数据文件...')
    input_lines = input_file.readlines()
    print('读入数据文件结束！')
    count = 0
    for line in input_lines:
        sentence = line.strip()
        count += 1
        for key in myType:
            window_size, power_dict = read_dict(key)
            labels = ['@'+str(key), '@', '']
            sentence = label_file(window_size, sentence, power_dict, labels)
        sentence += '\n'
        out_file.write(sentence)
        if count % 1000 == 0:
            print('已处理{}条数据'.format(count))
    input_file.close()
    out_file.close()


def read_dict(key):
    # print('开始读入字典文件...')
    power_dict = []
    max_len = 0
    for word in myType[key]:
        if len(word) > max_len:
            max_len = len(word)
        power_dict.append(word)
    # print('读入字典文件结束！')
    return max_len, power_dict


def label_file(window_size, line, power_dict, labels):
    # print('标注程序执行开始...')
    sentence = line
    result = label(sentence, window_size, power_dict, labels)
    # if len(result) > 0:
    #     result += '\n'
    # print(result)
    # print('标注程序执行结束！')
    return result


def label(sentence, window_size, power_dict, labels):
    index = len(sentence)
    result = []
    while index > 0:
        tmp = ''
        for size in range(index - window_size, index):
            piece = sentence[size:index]
            if piece in power_dict:
                index = size + 1
                for i in range(len(piece) - 1, -1, -1):
                    if i == 0:
                        result.append(labels[0] + piece[i])
                    elif i == len(piece) - 1:
                        result.append(piece[i] + labels[1])
                    else:
                        result.append(piece[i] + labels[2])
                break
            tmp = piece
        if tmp == '':
            pass
        elif tmp == ' ':
            pass
        elif len(tmp) == 1:
            result.append(tmp)
        index = index - 1
    result.reverse()
    myResult = ''
    for item in result:
        myResult += item
    return myResult


# test_sentence = '干式变压器绕组温度达到启动定值时，应能启动风机，且工作正常。'
# power_dict = ['干式变压器绕组','风机']
# test_result = label(test_sentence,7,power_dict,['B-DEC','E-DEC','M-DEC'])
# print(test_result)
# print('主程序执行开始...')
input_file_path = '/Users/zc/ztt/GitHub/power/data/text_label_part_0.csv'
out_file_path = '/Users/zc/ztt/GitHub/power/data/text_label_part_0_label.csv'
read_need_label_file(input_file_path, out_file_path)