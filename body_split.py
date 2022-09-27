# -*- coding: utf-8 -*-
# author: WuYanRu
# motto: Literate Programming
# Time: 2022/9/2 8:22
# File: body_split.py

import random

def body_split(file_input, file_output, proportion, randm = False):
    with open(file_output,'a',encoding='utf8') as f1:
        with open(file_input,'r',encoding='utf8') as f:
            body_org = [sen.strip() for sen in f.readlines()]
            if randm:
                random.shuffle(body_org)
            lenght = len(body_org)
            body_new = body_org[:int(lenght*proportion)]
            for sen in body_new:
                f1.write(sen + '\n')

file_input = '../datasets/pretrain/susong/mlm_ss_data_512.txt'
file_output ='../datasets/pretrain/susong/mlm_ss_data_512(8_10).txt'
proportion = 0.8

body_split(file_input, file_output, proportion, randm = True)