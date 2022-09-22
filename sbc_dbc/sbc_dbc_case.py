# -*- coding: utf-8 -*-
# author: WuYanRu
# motto: Literate Programming
# Time: 2022/9/22 23:01
# File: sbc_dbc_case.py
# Function:全半角转换和各类全半角元素判断
# Transfomer self.ustring = ustring
class SbcDbcJudge(object):
    def __init__(self, uchar):#第一个参数是self，实例化时不用实际传参，self在__init__里面代表实例的本身，后面的参数正常传递
        self.uchar = uchar
    def is_chinese(self):
        """判断一个unicode是否是汉字"""
        if self.uchar >= u'\u4e00' and self.uchar<=u'\u9fa5':
            return True
        else:
            return False

    def is_number(self):
        """判断一个unicode是否是半角数字"""
        if self.uchar >= u'\u0030' and self.uchar <= u'\u0039':
            return True
        else:
            return False

    def is_Qnumber(self):
        """判断一个unicode是否是全角数字"""
        if self.uchar >= u'\uff10' and self.uchar <= u'\uff19':
            return True
        else:
            return False

    def is_alphabet(self):
        """判断一个unicode是否是半角英文字母"""
        if (self.uchar >= u'\u0041' and self.uchar <= u'\u005a') or (self.uchar >= u'\u0061' and self.uchar <= u'\u007a'):
            return True
        else:
            return False

    def is_Qalphabet(uchar):
        """判断一个unicode是否是全角英文字母"""
        if (uchar >= u'\uff21' and uchar <= u'\uff3a') or (uchar >= u'\uff41' and uchar <= u'\uff5a'):
            return True
        else:
            return False

    #拆分为全角与半角，增加函数
    def is_other(self):
        """判断是否汉字，数字和英文字符"""
        if self.is_chinese() or self.is_number() or self.is_alphabet():
            return True
        else:
            return False

    def B2Q(uchar):
        """单个字符 半角转全角"""
        inside_code = ord(uchar)
        if inside_code < 0x0020 or inside_code > 0x7e:  # 不是半角字符就返回原来的字符
            return uchar
        if inside_code == 0x0020:  # 除了空格其他的全角半角的公式为: 半角 = 全角 - 0xfee0
            inside_code = 0x3000
        else:
            inside_code += 0xfee0
        return chr(inside_code)

    def Q2B(uchar):
        """单个字符 全角转半角"""
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
            return uchar
        return chr(inside_code)



if __name__ == '__main__':
    uchar = 'A'
    SDT = SbcDbcJudge(uchar)
    print(SDT.is_other())


