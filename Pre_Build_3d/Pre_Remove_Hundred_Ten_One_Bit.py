# ---************************************************---
# @coding: utf-8
# @Time : 2022/8/14 0014 11:21
# @Author : Matrix
# @File : Pre_Remove_Hundred_Ten_One_Bit.py
# @Software: PyCharm
# ---************************************************---

####################################################和值尾数去个十百方法模块#################################################
def BySum_Remove_Hundred_Bit(num_list, sum_end):
    """
    #通过和尾去百位
    #规则:和尾加减2(偶数+2，奇数-2),去百位同值
    :param num_list:
    :param sum_end:
    :return:
    """
    if Get_Odd_Even(sum_end) > 0:
        # 为偶数
        sum_key = str(sum_end + 2)
        pass
    else:
        sum_key = (abs(sum_end - 2))  # 取绝对值
        pass
    # print('num_list_re_hundred:',num_list)
    # print('sum_end:',sum_end,'sum_key:',sum_key)
    # print(num_list[0][0])#第一个元素第一个字符
    result_re_hundred = []
    for i in range(len(num_list)):
        if i == len(num_list) - 1:
            break
            pass
        if num_list[i][0] != sum_key:
            # print(num_list[i])
            result_re_hundred.append(num_list[i])
            pass
        pass

    return result_re_hundred
    pass
def BySum_Remove_Ten_Bit(num_list, sum_end):
    """
    #通过和尾去十位
    #规则:和尾*3，取尾去十位(去除同尾的数)
    :param num_list:
    :param sum_end:
    :return:
    """
    sum_key = str((sum_end * 3) % 10)
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
def BySum_Remove_One_Bit(num_list, sum_end):
    """
    #通过和尾去个位
    #规则:和尾*3+3，取尾去个位
    :param num_list:
    :param sum_end:
    :return:
    """
    sum_key = str((sum_end * 3 + 3) % 10)
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
    result_key = 0
    if index_num % 2 == 0:
        result_key = 1
        pass
    return result_key
    pass
def Get_Sum_End(index_num):
    sum = (int(index_num[0]) + int(index_num[1]) + int(index_num[2])) % 10
    return sum
    pass
def Get_Broken(num_str, broken_str, key):
    result_key = 0
    for i in range(len(broken_str)):
        if num_str == broken_str[i]:
            result_key = key
            pass
        pass
    return result_key
    pass
#####################################################公共类方法模块########################################################

#######################################################其他方法模块#######################################################
def Remove_Hundred_Ten_One(num_list, hundred, ten, one):
    """
    #直接筛选个十百位
    :param num_list:
    :param hundred:
    :param ten:
    :param one:
    :return:
    """
    hundred_key = str(hundred)
    ten_key = str(ten)
    one_key = str(one)
    result_reomve = []
    for i in range(len(num_list)):
        if i == len(num_list) - 1:
            break
            pass
        if num_list[i][0] != hundred_key and num_list[i][1] != ten_key and num_list[i][2] != one_key:
            # print(num_list[i])
            result_reomve.append(num_list[i])
            pass
        pass

    return result_reomve
    pass
def Remove_Span(num_list, span):
    """
    #跨度筛选
    #规则:下一期跨度不会出现span
    :param num_list:
    :param span:
    :return:
    """
    result_remove = []
    for i in range(len(num_list)):
        if i == len(num_list):
            break
            pass
        list_span = int(max(num_list[0])) - int(min(num_list[0]))
        if list_span != span:
            # print(num_list[i])
            result_remove.append(num_list[i])
            pass
        pass
    return result_remove
    pass
def Remove_Sum(num_list, sum_end):
    """
    #筛选和尾
    #和尾不能为sum_end
    :param num_list:
    :param sum_end:
    :return:
    """
    result_remove = []
    for i in range(len(num_list)):
        if i == len(num_list):
            break
            pass
        list_sum_end = Get_Sum_End(num_list[i])
        if list_sum_end != sum_end:
            # print(num_list[i])
            result_remove.append(num_list[i])
            pass
        pass
    return result_remove
    pass
def Remove_Special_Num(num_list, special_num):
    """
    #筛选特殊数字
    #个十百不能为special_num
    :param num_list:
    :param special_num:
    :return:
    """
    special_num_key = str(special_num)
    result_remove = []
    for i in range(len(num_list)):
        if i == len(num_list):
            break
            pass
        if num_list[i][0] != special_num_key and num_list[i][1] != special_num_key and num_list[i][
            2] != special_num_key:
            # print(num_list[i])
            result_remove.append(num_list[i])
            pass
        pass
    return result_remove
    pass
def Remove_Broken(num_list, broken_list):
    """
    #断组筛选
    #规则:num_list中的数不能同时为broken_list中的三个元素字符串
    :param num_list:
    :param broken_list:list类型['str','str','str']
    :return:
    """
    result_remove = []
    for i in range(len(num_list)):
        if i == len(num_list):
            break
            pass
        element_01 = num_list[i][0]
        element_02 = num_list[i][1]
        element_03 = num_list[i][2]
        #####################################3判断num_list的元素在组broken中的第几组##########################################
        test_01=Get_Broken('8', broken_list[0], 1) + Get_Broken('8', broken_list[1], 2) + Get_Broken('8', broken_list[2], 3)# 2
        test_02 = Get_Broken('5', broken_list[0], 1) + Get_Broken('5', broken_list[1], 2) + Get_Broken('5', broken_list[2],3)# 1
        test_03 = Get_Broken('3', broken_list[0], 1) + Get_Broken('3', broken_list[1], 2) + Get_Broken('3',broken_list[2],3)# 3
        temp_01 = Get_Broken(element_01, broken_list[0], 1) + Get_Broken(element_01, broken_list[1], 2) + Get_Broken(element_01, broken_list[2], 3)
        temp_02 = Get_Broken(element_02, broken_list[0], 1) + Get_Broken(element_02, broken_list[1], 2) + Get_Broken(element_02, broken_list[2], 3)
        temp_03 = Get_Broken(element_03, broken_list[0], 1) + Get_Broken(element_03, broken_list[1], 2) + Get_Broken(element_03, broken_list[2], 3)
        broken_key = str(temp_01) + str(temp_02) + str(temp_03)
        if broken_key != "123" and broken_key != "132" and broken_key != "213" and broken_key != "231" and broken_key != "312" and broken_key != "321":
            # print(num_list[i])
            result_remove.append(num_list[i])
            pass
        pass
    return result_remove
    pass
#######################################################其他方法模块#######################################################
