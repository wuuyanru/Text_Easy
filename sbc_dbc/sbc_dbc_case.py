# -*- coding: utf-8 -*-
# author: WuYanRu
# motto: Literate Programming
# Time: 2022/9/22 23:01
# File: sbc_dbc_case.py
# Function:全半角转换和各类全半角元素判断

#  self.ustring = ustring
class SbcDbcJudge():
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

    def is_Qalphabet(self):
        """判断一个unicode是否是全角英文字母"""
        if (self.uchar >= u'\uff21' and self.uchar <= u'\uff3a') or (self.uchar >= u'\uff41' and self.uchar <= u'\uff5a'):
            return True
        else:
            return False

    def is_sbc_cna(self):
        """判断是否汉字，半角数字和半角英文字符"""
        if self.is_chinese() or self.is_number() or self.is_alphabet():
            return True
        else:
            return False

    def is_dbc_cna(self):
        """判断是否汉字，全角数字和全角英文字符"""
        if self.is_chinese() or self.is_Qnumber() or self.is_Qalphabet():
            return True
        else:
            return False

    def B2Q(self):
        """单个字符 半角转全角"""
        inside_code = ord(self.uchar)
        if inside_code < 0x0020 or inside_code > 0x7e:  # 不是半角字符就返回原来的字符
            return uchar
        if inside_code == 0x0020:  # 除了空格其他的全角半角的公式为: 半角 = 全角 - 0xfee0
            inside_code = 0x3000
        else:
            inside_code += 0xfee0
        return chr(inside_code)

    def Q2B(self):
        """单个字符 全角转半角"""
        inside_code = ord(self.uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
            return uchar
        return chr(inside_code)

class SbcDbcTransfomer():
    def __init__(self, uchars):  # 第一个参数是self，实例化时不用实际传参，self在__init__里面代表实例的本身，后面的参数正常传递
        self.uchars = uchars


    def stringQ2B(self):
        """把字符串全角转半角"""
        all_ele = []
        for uchar in self.uchars:
            print('uchar0',uchar)
            inside_code = ord(uchar)
            if inside_code == 0x3000:
                inside_code = 0x0020
            else:
                inside_code -= 0xfee0
            if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
                all_ele.append(uchar)
            else:
                all_ele.append(chr(inside_code))
        return ''.join(all_ele)

    def stringB2Q(self):
        """把字符串全角转半角，包括数字、字符，各种符号"""
        all_ele = []
        for uchar in self.uchars:
            # print('uchar0',uchar)
            inside_code = ord(uchar)
            if inside_code < 0x0020 or inside_code > 0x7e:  # 不是半角字符就返回原来的字符
                all_ele.append(uchar)
            else:
                if inside_code == 0x0020:  # 除了空格其他的全角半角的公式为: 半角 = 全角 - 0xfee0
                    inside_code = 0x3000
                    all_ele.append(chr(inside_code))
                else:
                    inside_code += 0xfee0
                    all_ele.append(chr(inside_code))

        return ''.join(all_ele)

    def stringNAQ2B(self):
        """
        把字符串中数字和字母全角转半角

        Returns:

        """
        all_ele = []
        for uchar in self.uchars:
            if (uchar >= u'\uff10' and uchar <= u'\uff19') or (uchar >= u'\uff21' and uchar <= u'\uff3a') or (uchar >= u'\uff41' and uchar <= u'\uff5a'):
                inside_code = ord(uchar)
                if inside_code == 0x3000:
                    inside_code = 0x0020
                else:
                    inside_code -= 0xfee0
                if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
                    all_ele.append(uchar)
                else:
                    all_ele.append(chr(inside_code))
            else:
                all_ele.append(uchar)
        return ''.join(all_ele)

    def stringNAB2Q(self):
        """
        把字符串中数字和字母半角转全角

        Returns: 结果字符串

        """
        all_ele = []
        for uchar in self.uchars:
            if (uchar >= u'\u0030' and uchar <= u'\u0039') or (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
                inside_code = ord(uchar)
                if inside_code < 0x0020 or inside_code > 0x7e:  # 不是半角字符就返回原来的字符
                    all_ele.append(uchar)
                else:
                    if inside_code == 0x0020:  # 除了空格其他的全角半角的公式为: 半角 = 全角 - 0xfee0
                        inside_code = 0x3000
                        all_ele.append(chr(inside_code))
                    else:
                        inside_code += 0xfee0
                        all_ele.append(chr(inside_code))
            else:
                all_ele.append(uchar)
        return ''.join(all_ele)

if __name__ == '__main__':
    uchar = 'Ｊ'
    SDJ = SbcDbcJudge(uchar)
    print(SDJ.Q2B())

    ustrin = r'电影《２０１２》讲述了２０１２年１２月２１日的世界末日，主人公Ｊａｃｋ以及世'
    SDT = SbcDbcTransfomer(ustrin)
    print(SDT.stringQ2B())

    ustrin_b = '电影《2012》讲述了2012年12月21日的世界末日,主人公Jack以及世'
    SDT = SbcDbcTransfomer(ustrin_b)
    print(SDT.stringB2Q())

    ustrin_c = '电影《２０１２》讲述了２０１２年１２月２１日的世界末日，主人公Ｊａｃｋ以及世'
    SDT = SbcDbcTransfomer(ustrin_c)
    print(SDT.stringNAQ2B())

    ustrin_d = '电影《2012》讲述了2012年12月21日的世界末日,主人公Jack以及世'
    SDT = SbcDbcTransfomer(ustrin_d)
    print(SDT.stringNAB2Q())



