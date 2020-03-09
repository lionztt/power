


print('主程序执行开始...')
# input_file = open('/Users/zc/ztt/电力资料/dianli/src/asserts/data3.csv','r')
# input_file = open('/Users/zc/ztt/电力资料/dianli/src/asserts/test.csv','r')
# out_file = open('/Users/zc/ztt/电力资料/dianli/src/code2/result/op_label.txt','w')
# input_dict = open('/Users/zc/ztt/电力资料/dianli/src/code2/data/op.csv', 'r')


def read_need_label_file(input_file_path, out_file_path, dict_path):

    out_file = open(out_file_path, 'w')
    input_file = open(input_file_path, 'r')
    print('开始读入数据文件...')
    input_lines = input_file.readlines()
    print('读入数据文件结束！')
    window_size, power_dict = read_dict(dict_path)
    label_file(window_size, input_lines,)
    input_file.close()
    out_file.close()


def read_dict(dict_path):
    print('开始读入字典文件...')
    input_dict_file = open(dict_path, 'r')
    dict_lines = input_dict_file.readlines()
    power_dict = set()
    max_len = 0
    for word_line in dict_lines:
        word_line = word_line.strip('\n')
        word, label = word_line.split('\t')
        if len(word) > max_len:
            max_len = len(word)
        # if word_line not in power_dict:
        power_dict.add({'word': word, 'label': label})
    print('读入数据文件结束！')
    input_dict_file.close()
    return max_len, power_dict


def label_file(window_size, input_lines, out_file, power_dict, labels):
    print('标注程序执行开始...')
    count = 0
    # window_size = 14
    for line in input_lines:
        sentence = line.strip()
        index = len(sentence)
        count += 1
        if index < 2:
            continue
        result = label(sentence, window_size, power_dict, labels)
        for item in result:
            out_file.write(item)
        out_file.write('\n')
        # print(result)

        if count% 1000 == 0:
            print('已处理{}条数据'.format(count))
    print('标注程序执行结束！')


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
                        result.append(piece[i] + '\t' + labels[0] + '\n')
                    elif i == len(piece) - 1:
                        result.append(piece[i] + '\t' + labels[1] + '\n')
                    else:
                        result.append(piece[i] + '\t' + labels[2] + '\n')
                break
            tmp = piece
        if tmp == '':
            pass
        elif tmp == ' ':
            pass
        elif len(tmp) == 1:
            result.append(tmp + '\t' + 'O' + '\n')
        index = index - 1
    result.reverse()
    return result


test_sentence = '干式变压器绕组温度达到启动定值时，应能启动风机，且工作正常。'
power_dict = ['干式变压器绕组','风机']
test_result = label(test_sentence,7,power_dict,['B-DEC','E-DEC','M-DEC'])
print(test_result)