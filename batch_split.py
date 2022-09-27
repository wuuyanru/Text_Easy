# -*- coding: utf-8 -*-
# author: WuYanRu
# motto: Literate Programming
# Time: 2022/9/1 17:07
# File: batch_split.py

def sens_split(body_sens,maxlen):
    line_split = []
    sen_temp = ''
    num = 0
    for i in range(len(body_sens)):
        # print((len(sen_temp) + len(body_sens[i])))
        if (len(sen_temp) + len(body_sens[i])) < maxlen:
            sen_temp += body_sens[i]
        else:
            if len(body_sens[i]) >= maxlen:
                if len(sen_temp) > 0:
                    line_split.append(sen_temp)
                line_split.append(body_sens[i])
                sen_temp = ''
            else:
                if len(sen_temp) >= 0:
                    line_split.append(sen_temp)
                sen_temp = body_sens[i]

            num += 1
    if len(sen_temp) > 0:
        line_split.append(sen_temp)
    return line_split

if __name__ == '__main__':

    file_read = '../datasets/pretrain/susong/mlm_ss_data_256.txt'
    file_write = '../datasets/pretrain/susong/mlm_ss_data_512.txt'
    with open(file_write, 'a', encoding='utf8') as f1:
        with open(file_read,'r',encoding='utf8') as f:
            body_sens = f.readlines()
            body_sens = [sen.strip() for sen in body_sens]
            line_split = sens_split(body_sens,510)

            for sen in line_split:
                f1.write(sen + '\n')


