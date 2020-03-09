right_p = 0
right_loc_p = 0
p_loc = 0
y_loc = 0
all_lab = 0


states = ['B','M','E','O']
with open('/Users/zc/ztt/电力资料/dianli/dg_op_result.txt', 'r') as f:
    for line in f.readlines():
        if line.strip() == '':
            continue
        a = line.split()
        # print(a)
        if len(a) == 2:
            right_p += 1
            all_lab += 1
            continue
        w,y,p = a
        all_lab += 1
        if y == p:
            if y in states:
                right_loc_p += 1
            right_p += 1
        if y in states:
            y_loc += 1
        if p in states:
            p_loc += 1

'''
准确率（正确率）= 所有预测正确的样本/总的样本  （TP+TN）/总

精确率 = 将正类预测为正类 / 所有预测为正类 TP/（TP+FP）

召回率 = 将正类预测为正类 / 所有正真的正类 TP/（TP+FN）
'''

a = right_p/all_lab
p = 1.0*right_loc_p/p_loc
r = 1.0*right_loc_p/y_loc

print('a:{},p:{},r:{},f1:{}'.format(a,p,r,2*p*r/(p+r)))