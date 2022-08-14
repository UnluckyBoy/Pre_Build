# ---************************************************---
# @coding: utf-8
# @Time : 2022/8/14 0014 11:21
# @Author : Matrix
# @File : Pre_Remove_Hundred_Ten_One_Bit.py
# @Software: PyCharm
# ---************************************************---

####################################################和值尾数去个十百方法模块#################################################
def BySum_Remove_Hundred_Bit(num_list,sum_end):
    """
    #通过和尾去百位
    #规则:和尾加减2(偶数+2，奇数-2),去百位同值
    :param num_list:
    :param sum_end:
    :return:
    """
    if Get_Odd_Even(sum_end)>0:
        #为偶数
        sum_key =str(sum_end+2)
        pass
    else:
        sum_key = (abs(sum_end - 2))#取绝对值
        pass
    # print('num_list_re_hundred:',num_list)
    # print('sum_end:',sum_end,'sum_key:',sum_key)
    # print(num_list[0][0])#第一个元素第一个字符
    result_re_hundred=[]
    for i in range(len(num_list)):
        if i==len(num_list)-1:
            break
            pass
        if num_list[i][0]!=sum_key:
            # print(num_list[i])
            result_re_hundred.append(num_list[i])
            pass
        pass

    return result_re_hundred
    pass
def BySum_Remove_Ten_Bit(num_list,sum_end):
    """
    #通过和尾去十位
    #规则:和尾*3，取尾去十位(去除同尾的数)
    :param num_list:
    :param sum_end:
    :return:
    """
    sum_key=str((sum_end*3)%10)
    # print('num_list_re_ten:', num_list)
    # print('sum_end:', sum_end, 'sum_key:', sum_key)
    result_re_ten = []
    for i in range(len(num_list)):
        if i == len(num_list) - 1:
            break
            pass
        if num_list[i][1] != sum_key:
            # print(num_list[i])
            result_re_ten.append(num_list[i])
            pass
        pass
    return result_re_ten
    pass
def BySum_Remove_One_Bit(num_list,sum_end):
    """
    #通过和尾去个位
    #规则:和尾*3+3，取尾去个位
    :param num_list:
    :param sum_end:
    :return:
    """
    sum_key = str((sum_end * 3+3) % 10)
    # print('num_list_re_one:', num_list)
    # print('sum_end:', sum_end, 'sum_key:', sum_key)
    result_re_one = []
    for i in range(len(num_list)):
        if i == len(num_list) - 1:
            break
            pass
        if num_list[i][2] != sum_key:
            # print(num_list[i])
            result_re_one.append(num_list[i])
            pass
        pass
    return result_re_one
    pass
####################################################和值尾数去个十百方法模块#################################################

#####################################################公共类方法模块########################################################
def Get_Odd_Even(index_num):
    """
    #判断index_num是否奇偶数并返回:奇-0，偶-1
    :param index_num:
    :return:
    """
    result_key=0
    if index_num%2==0:
        result_key=1
        pass
    return result_key
    pass
#####################################################公共类方法模块########################################################

###################################################直接去个十百方法模块#####################################################
def Remove_Hundred_Ten_One(num_list,hundred,ten,one):
    hundred_key=str(hundred)
    ten_key=str(ten)
    one_key=str(one)
    result_re_hundred = []
    for i in range(len(num_list)):
        if i == len(num_list) - 1:
            break
            pass
        if num_list[i][0] != hundred_key and num_list[i][1] !=ten_key and num_list[i][2] !=one_key:
            # print(num_list[i])
            result_re_hundred.append(num_list[i])
            pass
        pass

    return result_re_hundred
    pass
###################################################直接去个十百方法模块#####################################################