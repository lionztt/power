count = 0
split_rate = 0.1
test_file = open('/Users/zc/ztt/电力资料/dianli/src/code2/data/NER_data/op_test.txt','w')
train_file = open('/Users/zc/ztt/电力资料/dianli/src/code2/data/NER_data/op_train.txt','w')
input_file = open('/Users/zc/ztt/电力资料/dianli/src/code2/result/op_label.txt','r')

# 数文件行数
file_count = 0
while True:
    buffer = input_file.read(1024 * 8192)
    if not buffer:
        break
    file_count += buffer.count('\n')
input_file.close()

split_point = int(file_count*split_rate)
print(split_point)

input_file = open('/Users/zc/ztt/电力资料/dianli/src/code2/result/op_label.txt','r')
for line in input_file.readlines():
    count+=1
    if count<=split_point:
        test_file.write(line)
    else:
        train_file.write(line)
    if count%1000==0:
        print('处理条数：', count)
input_file.close()
test_file.close()
train_file.close()
