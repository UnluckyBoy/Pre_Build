# ---************************************************---
# @coding: utf-8
# @Time : 2022/7/22 0022 10:54
# @Author : Matrix
# @File : Pre_Build_3d.py
# @Software: PyCharm
# ---************************************************---
import math
import random


def Pre_Build_num():
    """
    #生成1000个数列
    :return:
    """
    result=[]
    for i in range(1000):
        if i < 10:
            i = '00' + str(i)
            num=i
        elif 10 <= i and i < 100:
            i = '0' + str(i)
            num = i
        else:
            i = str(i)
            num = i
            pass
        #print(num)
        result.append(num)
        pass
    #print(result)
    return result
    pass

def Spilt_list(index_List):
    """
    #将生成的000-999的元素拆分为0,0,0-9,9,9存至result_str
    :param index_List:
    :return:
    """
    result_str = []
    for i in range(len(index_List)):
        """##将生成的000-999的元素拆分为0,0,0-9,9,9存至num_spilt_str"""
        result_str.append(list(index_List[i]))
        pass
    return result_str
    pass

def GetSum(index):
    """
    #和值尾数取10的余数计算
    :param index:
    :return:
    """
    sum = (int(index[0]) + int(index[1]) + int(index[2]))% 10
    return sum
    pass

def Get_Way(index):
    """
    #将上一期号码转为012路
    :param index:
    :return:
    """
    index_way = ""
    for i in range(len(index)):
        if index[i] == 0 or index[i] == 3 or index[i] == 6 or index[i] == 9:
            index_way += "0"
            pass
        if index[i] == 1 or index[i] == 4 or index[i] == 7:
            index_way += "1"
            pass
        if index[i] == 2 or index[i] == 5 or index[i] == 8:
            index_way += "2"
        pass
    return index_way
    pass

def Get_Way_Remove_combination(num_list,way_index):
    """
    #根据和尾杀下期012路特征,只杀221,201,210,001,202,121,021,112,010路
    :param num_list:
    :param way_index:
    :return:
    """
    key_list = []
    match way_index:
        case "010":
            for i in range(len(num_list)):
                hundred = int(num_list[i]) // 100
                ten = (int(num_list[i]) // 10) % 10
                one = int(num_list[i]) % 10
                if hundred == 0 or hundred == 3 or hundred == 6 or hundred==9:
                    if ten == 1 or ten == 4 or ten == 7:
                        if one == 0 or one == 3 or one == 6 or one==9:
                            # print(indexList[i])
                            key_list.append(num_list[i])
            pass
        case "001":
            for i in range(len(num_list)):
                hundred = int(num_list[i]) // 100
                ten = (int(num_list[i]) // 10) % 10
                one = int(num_list[i]) % 10
                if hundred == 0 or hundred == 3 or hundred == 6 or hundred == 9:
                    if ten == 0 or ten == 3 or ten == 6 or ten == 9:
                        if one == 1 or one == 4 or one == 7:
                            # print(indexList[i])
                            key_list.append(num_list[i])
            pass
        case "021":
            for i in range(len(num_list)):
                hundred = int(num_list[i]) // 100
                ten = (int(num_list[i]) // 10) % 10
                one = int(num_list[i]) % 10
                if hundred == 0 or hundred == 3 or hundred == 6 or hundred == 9:
                    if ten == 2 or ten == 5 or ten == 8:
                        if one == 1 or one == 4 or one == 7:
                            # print(indexList[i])
                            key_list.append(num_list[i])
            pass
        case "112":
            for i in range(len(num_list)):
                hundred = int(num_list[i]) // 100
                ten = (int(num_list[i]) // 10) % 10
                one = int(num_list[i]) % 10
                if hundred == 1 or hundred == 4 or hundred == 7:
                    if ten == 1 or ten == 4 or ten == 7:
                        if one == 2 or one == 5 or one == 8:
                            # print(indexList[i])
                            key_list.append(num_list[i])
            pass
        case "121":
            for i in range(len(num_list)):
                hundred = int(num_list[i]) // 100
                ten = (int(num_list[i]) // 10) % 10
                one = int(num_list[i]) % 10
                if hundred == 1 or hundred == 4 or hundred == 7:
                    if ten == 2 or ten == 5 or ten == 8:
                        if one == 1 or one == 4 or one == 7:
                            # print(indexList[i])
                            key_list.append(num_list[i])
            pass
        case "201":
            for i in range(len(num_list)):
                hundred = int(num_list[i]) // 100
                ten = (int(num_list[i]) // 10) % 10
                one = int(num_list[i]) % 10
                if hundred == 2 or hundred == 5 or hundred == 8:
                    if ten == 0 or ten == 3 or ten == 6 or ten==9:
                        if one == 1 or one == 4 or one == 7:
                            # print(indexList[i])
                            key_list.append(num_list[i])
            pass
        case "202":
            for i in range(len(num_list)):
                hundred = int(num_list[i]) // 100
                ten = (int(num_list[i]) // 10) % 10
                one = int(num_list[i]) % 10
                if hundred == 2 or hundred == 5 or hundred == 8:
                    if ten == 0 or ten == 3 or ten == 6 or ten == 9:
                        if one == 2 or one == 5 or one == 8:
                            # print(indexList[i])
                            key_list.append(num_list[i])
            pass
        case "210":
            for i in range(len(num_list)):
                hundred = int(num_list[i]) // 100
                ten = (int(num_list[i]) // 10) % 10
                one = int(num_list[i]) % 10
                if hundred == 2 or hundred == 5 or hundred == 8:
                    if ten == 1 or ten == 4 or ten == 7:
                        if one == 0 or one == 3 or one == 6 or one == 9:
                            # print(indexList[i])
                            key_list.append(num_list[i])
            pass
        case "221":
            for i in range(len(num_list)):
                hundred = int(num_list[i]) // 100
                ten = (int(num_list[i]) // 10) % 10
                one = int(num_list[i]) % 10
                if hundred == 2 or hundred == 5 or hundred == 8:
                    if ten == 2 or ten == 5 or ten == 8:
                        if one == 1 or one == 4 or one == 7:
                            # print(indexList[i])
                            key_list.append(num_list[i])
            pass
    return key_list
    pass

def GetSubtraction(index_01,index_02):
    """
    #取相减和值(绝对值)
    :param index_01:
    :param index_02:
    :return:
    """
    sum=(abs(index_01-index_02))%10
    return sum
    pass

def GetAdd(index_01,index_02):
    """
    #取相加和值
    :param index_01:
    :param index_02:
    :return:
    """
    sum = (index_01 + index_02) % 10
    return sum
    pass

def GetSquare(index):
    """
    #乘法取余(模10)
    :param index_01:
    :param index_02:
    :return:
    """
    sum = (index*index) % 10
    return sum
    pass

def Remove_Bit_list(spilt_str_list,start,end):
    """
    #和值为指定的数时去除百位数为指定数的元素
    :param spilt_str_list:被去除list
    :param start:开始元素
    :param end:结束元素
    :return:
    """
    reList = []
    for mlist in spilt_str_list[start:end]:  # 从list列表的第start个元素开始遍历到end
        reList.append(mlist)
        pass
    for m in range(len(reList)):
        spilt_str_list.remove(reList[m])  ##去除元素
        pass
    #print(spilt_str_list, "长度:", len(spilt_str_list))
    return spilt_str_list
    pass

def Remove_ten_bit_cycle(index_list,index):
    """
    #循环杀十位数码
    #取数长度公共公式:start=index*10+90*i;end=(index+1)*10+90*i
    :param index_list:
    :param index:去除的目标数
    :return:
    """
    result_list=[]
    for i in range(len(index_list)):
        start=index*10+90*i
        end=(index+1)*10+90*i
        result_list = Remove_Bit_list(index_list, start, end)
        pass
    # result_list = Remove_Bit_list(index_list, start, end)
    # print(result_list)
    return result_list
    pass

def Remove_one_bit_cycle(index_list,index):
    """
    #循环杀个位数码
    #取数长度公共公式:start=index+9*i;end=(index+1)+9*i
    :param index_list:
    :param index:去除的目标数
    :return:
    """
    result_list = []
    for i in range(len(index_list)):
        start = index + 9*i
        end = (index + 1)+ 9*i
        result_list = Remove_Bit_list(index_list, start, end)
        pass
    return result_list
    pass

def Funcation01_Remove_hundred_Bit_list(spilt_list_hundred,sum):
    """
    # 根据合值杀下期百位
    # 当合值为0时，下期百位杀3
    # 当合值为1时，下期百位杀9
    # 当合值为2时，下期百位杀2
    # 当合值为3时，下期百位杀9
    # 当合值为4时，下期百位杀6
    # 当合值为5时，下期百位杀4
    # 当合值为6时，下期百位杀1
    # 当合值为7时，下期百位杀7
    # 当合值为8时，下期百位杀0
    # 当合值为9时，下期百位杀6
    :param list_spilt_str:
    :param sum:和值
    :return:
    """
    # print("sum:", sum, "___杀百位")
    result_hundred_list=[]
    match sum:
        case 0:
            remove_hundred_list = Remove_Bit_list(spilt_list_hundred, 300, 400)
            # print("杀百位结果:\n", remove_hundred_list,"\n长度:", len(remove_hundred_list))
            result_hundred_list=Funcation01_Remove_ten_Bit_list(remove_hundred_list, sum)##调用杀十位数码方法
            pass
        case 1:
            remove_hundred_list = Remove_Bit_list(spilt_list_hundred, 900, 1000)
            # print("杀百位结果:\n", remove_hundred_list, "\n长度:", len(remove_hundred_list))
            result_hundred_list=Funcation01_Remove_ten_Bit_list(remove_hundred_list, sum)  ##调用杀十位数码方法
            pass
        case 2:
            remove_hundred_list = Remove_Bit_list(spilt_list_hundred, 200, 300)
            # print("杀百位结果:\n", remove_hundred_list, "\n长度:", len(remove_hundred_list))
            result_hundred_list=Funcation01_Remove_ten_Bit_list(remove_hundred_list, sum)  ##调用杀十位数码方法
            pass
        case 3:
            remove_hundred_list = Remove_Bit_list(spilt_list_hundred, 900, 1000)
            # print("杀百位结果:\n", remove_hundred_list, "\n长度:", len(remove_hundred_list))
            result_hundred_list=Funcation01_Remove_ten_Bit_list(remove_hundred_list, sum)  ##调用杀十位数码方法
            pass
        case 4:
            remove_hundred_list = Remove_Bit_list(spilt_list_hundred, 600, 700)
            # print("杀百位结果:\n", remove_hundred_list, "\n长度:", len(remove_hundred_list))
            result_hundred_list=Funcation01_Remove_ten_Bit_list(remove_hundred_list, sum)  ##调用杀十位数码方法
            pass
        case 5:
            remove_hundred_list = Remove_Bit_list(spilt_list_hundred, 400, 500)
            # print("杀百位结果:\n", remove_hundred_list, "\n长度:", len(remove_hundred_list))
            result_hundred_list=Funcation01_Remove_ten_Bit_list(remove_hundred_list, sum)  ##调用杀十位数码方法
            pass
        case 6:
            remove_hundred_list = Remove_Bit_list(spilt_list_hundred, 100, 200)
            # print("杀百位结果:\n", remove_hundred_list, "\n长度:", len(remove_hundred_list))
            result_hundred_list=Funcation01_Remove_ten_Bit_list(remove_hundred_list, sum)  ##调用杀十位数码方法
            pass
        case 7:
            remove_hundred_list = Remove_Bit_list(spilt_list_hundred, 700, 800)
            # print("杀百位结果:\n", remove_hundred_list, "\n长度:", len(remove_hundred_list))
            result_hundred_list=Funcation01_Remove_ten_Bit_list(remove_hundred_list, sum)  ##调用杀十位数码方法
            pass
        case 8:
            remove_hundred_list = Remove_Bit_list(spilt_list_hundred, 0, 100)
            # print("杀百位结果:\n", remove_hundred_list, "\n长度:", len(remove_hundred_list))
            result_hundred_list=Funcation01_Remove_ten_Bit_list(remove_hundred_list, sum)  ##调用杀十位数码方法
            pass
        case 9:
            remove_hundred_list = Remove_Bit_list(spilt_list_hundred, 600, 700)
            # print("杀百位结果:\n", remove_hundred_list, "\n长度:", len(remove_hundred_list))
            result_hundred_list=Funcation01_Remove_ten_Bit_list(remove_hundred_list, sum)  ##调用杀十位数码方法
            pass
    # print("result_hundred_list_结果:\n", result_hundred_list, "\n长度:", len(result_hundred_list))
    return result_hundred_list
    pass

def Funcation01_Remove_ten_Bit_list(spilt_list_ten,sum):
    """
    # 根据合值杀下期十位
    # 当合值为0时，下期十位杀5
    # 当合值为1时，下期十位杀0
    # 当合值为2时，下期十位杀0
    # 当合值为3时，下期十位杀2
    # 当合值为4时，下期十位杀6
    # 当合值为5时，下期十位杀7
    # 当合值为6时，下期十位杀9
    # 当合值为7时，下期十位杀8
    # 当合值为8时，下期十位杀5
    # 当合值为9时，下期十位杀4
    :param spilt_list:
    :param sum:
    :return:
    """
    # print("sum:", sum, "___杀十位")
    result_ten_list=[]
    match sum:
        case 0:
            remove_ten_list = Remove_ten_bit_cycle(spilt_list_ten,5)
            # print("结果:\n",remove_ten_list,"\n长度:",len(remove_ten_list))
            result_ten_list=Funcation01_Remove_bit_list(remove_ten_list, sum)  ##调用杀个位数方法
            pass
        case 1:
            remove_ten_list = Remove_ten_bit_cycle(spilt_list_ten,0)
            # print("结果:\n",remove_ten_list,"\n长度:",len(remove_ten_list))
            result_ten_list=Funcation01_Remove_bit_list(remove_ten_list, sum)  ##调用杀个位数方法
            pass
        case 2:
            remove_ten_list = Remove_ten_bit_cycle(spilt_list_ten,0)
            # print("结果:\n",remove_ten_list,"\n长度:",len(remove_ten_list))
            result_ten_list=Funcation01_Remove_bit_list(remove_ten_list, sum)  ##调用杀个位数方法
            pass
        case 3:
            remove_ten_list = Remove_ten_bit_cycle(spilt_list_ten,2)
            # print("结果:\n",remove_ten_list,"\n长度:",len(remove_ten_list))
            result_ten_list=Funcation01_Remove_bit_list(remove_ten_list, sum)  ##调用杀个位数方法
            pass
        case 4:
            remove_ten_list = Remove_ten_bit_cycle(spilt_list_ten,6)
            # print("结果:\n",remove_ten_list,"\n长度:",len(remove_ten_list))
            result_ten_list=Funcation01_Remove_bit_list(remove_ten_list, sum)  ##调用杀个位数方法
            pass
        case 5:
            remove_ten_list = Remove_ten_bit_cycle(spilt_list_ten,7)
            # print("结果:\n",remove_ten_list,"\n长度:",len(remove_ten_list))
            result_ten_list=Funcation01_Remove_bit_list(remove_ten_list, sum)  ##调用杀个位数方法
            pass
        case 6:
            remove_ten_list = Remove_ten_bit_cycle(spilt_list_ten,9)
            # print("结果:\n",remove_ten_list,"\n长度:",len(remove_ten_list))
            result_ten_list=Funcation01_Remove_bit_list(remove_ten_list, sum)  ##调用杀个位数方法
            pass
        case 7:
            remove_ten_list = Remove_ten_bit_cycle(spilt_list_ten,8)
            # print("结果:\n",remove_ten_list,"\n长度:",len(remove_ten_list))
            result_ten_list=Funcation01_Remove_bit_list(remove_ten_list, sum)  ##调用杀个位数方法
            pass
        case 8:
            remove_ten_list = Remove_ten_bit_cycle(spilt_list_ten,5)
            # print("结果:\n",remove_ten_list,"\n长度:",len(remove_ten_list))
            result_ten_list=Funcation01_Remove_bit_list(remove_ten_list,sum)##调用杀个位数方法
            pass
        case 9:
            remove_ten_list = Remove_ten_bit_cycle(spilt_list_ten,4)
            # print("结果:\n",remove_ten_list,"\n长度:",len(remove_ten_list))
            result_ten_list=Funcation01_Remove_bit_list(remove_ten_list, sum)  ##调用杀个位数方法
            pass
    # print("result_ten_list_结果:\n", result_ten_list, "\n长度:", len(result_ten_list))
    return result_ten_list
    pass

def Funcation01_Remove_bit_list(spilt_list_one,sum):
    """
    # 根据合值杀下期个位
    # 当合值为0时，下期个位杀6
    # 当合值为1时，下期个位杀8
    # 当合值为2时，下期个位杀3
    # 当合值为3时，下期个位杀2
    # 当合值为4时，下期个位杀7
    # 当合值为5时，下期个位杀2
    # 当合值为6时，下期个位杀0
    # 当合值为7时，下期个位杀1
    # 当合值为8时，下期个位杀4
    # 当合值为9时，下期个位杀4
    :param spilt_list:
    :param sum:
    :return:
    """
    # print("sum:", sum, "___杀个位")
    remvoe_Cache_list=[]
    match sum:
        case 0:
            remvoe_Cache_list = Remove_one_bit_cycle(spilt_list_one, 6)
            # print("结果:\n", remvoe_Cache_list, "\n长度:", len(remvoe_Cache_list))
            pass
        case 1:
            remvoe_Cache_list = Remove_one_bit_cycle(spilt_list_one, 8)
            # print("结果:\n", remvoe_Cache_list, "\n长度:", len(remvoe_Cache_list))
            pass
        case 2:
            remvoe_Cache_list = Remove_one_bit_cycle(spilt_list_one, 3)
            # print("结果:\n", remvoe_Cache_list, "\n长度:", len(remvoe_Cache_list))
            pass
        case 3:
            remvoe_Cache_list = Remove_one_bit_cycle(spilt_list_one, 2)
            # print("结果:\n", remvoe_Cache_list, "\n长度:", len(remvoe_Cache_list))
            pass
        case 4:
            remvoe_Cache_list = Remove_one_bit_cycle(spilt_list_one, 7)
            # print("结果:\n", remvoe_Cache_list, "\n长度:", len(remvoe_Cache_list))
            pass
        case 5:
            remvoe_Cache_list = Remove_one_bit_cycle(spilt_list_one, 2)
            # print("结果:\n", remvoe_Cache_list, "\n长度:", len(remvoe_Cache_list))
            pass
        case 6:
            remvoe_Cache_list = Remove_one_bit_cycle(spilt_list_one, 0)
            # print("结果:\n", remvoe_Cache_list, "\n长度:", len(remvoe_Cache_list))
            pass
        case 7:
            remvoe_Cache_list = Remove_one_bit_cycle(spilt_list_one, 1)
            # print("结果:\n", remvoe_Cache_list, "\n长度:", len(remvoe_Cache_list))
            pass
        case 8:
            remvoe_Cache_list=Remove_one_bit_cycle(spilt_list_one,4)
            # print("结果:\n", remvoe_Cache_list, "\n长度:", len(remvoe_Cache_list))
            pass
        case 9:
            remvoe_Cache_list = Remove_one_bit_cycle(spilt_list_one, 4)
            # print("结果:\n", remvoe_Cache_list, "\n长度:", len(remvoe_Cache_list))
            pass
    # print("remvoe_Cache_list_结果:\n", remvoe_Cache_list, "\n长度:", len(remvoe_Cache_list))
    return remvoe_Cache_list
    pass

def List_2_Str(requeList):
    """
    ##将requeList中的单个list元素转为str，存入result_str
    :param requeList:
    :return:
    """
    result_str=[]
    for i in range(len(requeList)):
        result_str.append(''.join(requeList[i]))##将requeList中的list元素转为str，存入result_str
        pass

    return result_str
    pass

def Pre_Funcation_01(index,num_List):
    """
    #方法一
    :param index:上一期的号码
    :param num_List:
    :return:
    """
    list_spilt_str=Spilt_list(num_List)##调用拆分list公共方法
    sum=GetSum(index)
    print("方法:***根据合值去下期百位、十位、个位***_尾数:", sum)
    result_list=Funcation01_Remove_hundred_Bit_list(list_spilt_str,sum)
    return result_list
    pass

def Pre_Funcation_02(sum,num_List):
    """
    #方法二
    :param index:
    :param num_List:
    :return:
    """
    list_spilt_str = Spilt_list(num_List)  ##调用拆分list公共方法
    # sum = GetSum(index)
    # print("方法二和值:",sum)
    result_f2_list=[]
    match sum:
        case 0:
            remove_hundred_list_f2 = Remove_Bit_list(list_spilt_str, 0,100)
            remove_ten_list_f2 = Remove_ten_bit_cycle(remove_hundred_list_f2, 0)
            result_f2_list = Remove_one_bit_cycle(remove_ten_list_f2, 0)
            pass
        case 1:
            remove_hundred_list_f2=Remove_Bit_list(list_spilt_str,100,200)
            # print("remove_hundred_list_f2:\n",remove_hundred_list_f2,"\n长度:",len(remove_hundred_list_f2))
            remove_ten_list_f2=Remove_ten_bit_cycle(remove_hundred_list_f2,1)
            # print("remove_ten_list_f2:\n", remove_ten_list_f2, "\n长度:", len(remove_ten_list_f2))
            result_f2_list=Remove_one_bit_cycle(remove_ten_list_f2,1)
            # print("result_02:\n", result_02, "\n长度:", len(result_02))
            pass
        case 2:
            remove_hundred_list_f2 = Remove_Bit_list(list_spilt_str, 200, 300)
            remove_ten_list_f2 = Remove_ten_bit_cycle(remove_hundred_list_f2, 2)
            result_f2_list = Remove_one_bit_cycle(remove_ten_list_f2, 2)
            pass
        case 3:
            remove_hundred_list_f2 = Remove_Bit_list(list_spilt_str, 300, 400)
            remove_ten_list_f2 = Remove_ten_bit_cycle(remove_hundred_list_f2, 3)
            result_f2_list = Remove_one_bit_cycle(remove_ten_list_f2, 3)
            pass
        case 4:
            remove_hundred_list_f2 = Remove_Bit_list(list_spilt_str, 400, 500)
            remove_ten_list_f2 = Remove_ten_bit_cycle(remove_hundred_list_f2, 4)
            result_f2_list = Remove_one_bit_cycle(remove_ten_list_f2, 4)
            pass
        case 5:
            remove_hundred_list_f2 = Remove_Bit_list(list_spilt_str, 500, 600)
            remove_ten_list_f2 = Remove_ten_bit_cycle(remove_hundred_list_f2, 5)
            result_f2_list = Remove_one_bit_cycle(remove_ten_list_f2, 5)
            pass
        case 6:
            remove_hundred_list_f2 = Remove_Bit_list(list_spilt_str, 600, 700)
            remove_ten_list_f2 = Remove_ten_bit_cycle(remove_hundred_list_f2, 6)
            result_f2_list = Remove_one_bit_cycle(remove_ten_list_f2, 6)
            pass
        case 7:
            remove_hundred_list_f2 = Remove_Bit_list(list_spilt_str, 700, 800)
            remove_ten_list_f2 = Remove_ten_bit_cycle(remove_hundred_list_f2, 7)
            result_f2_list = Remove_one_bit_cycle(remove_ten_list_f2, 7)
            pass
        case 8:
            remove_hundred_list_f2 = Remove_Bit_list(list_spilt_str, 800, 900)
            remove_ten_list_f2 = Remove_ten_bit_cycle(remove_hundred_list_f2, 8)
            result_f2_list = Remove_one_bit_cycle(remove_ten_list_f2, 8)
            pass
        case 9:
            remove_hundred_list_f2 = Remove_Bit_list(list_spilt_str, 900, 1000)
            remove_ten_list_f2 = Remove_ten_bit_cycle(remove_hundred_list_f2, 9)
            result_f2_list = Remove_one_bit_cycle(remove_ten_list_f2, 9)
            pass
    return result_f2_list
    pass

def Pre_Funcation_03_Rem_ten(sum_index,num_List):
    """
    #方法三:和尾*3，取尾去十位(去除同尾的数)
    :param sum:
    :param num_List:
    :return:
    """
    list_spilt_str = Spilt_list(num_List)  ##调用拆分list公共方法
    sum=(sum_index*3)%10
    print("***和尾*3去十位***__和值尾为:",sum)
    result_f3_list = []
    match sum:
        case 0:
            result_f3_list = Remove_ten_bit_cycle(list_spilt_str, 0)
            pass
        case 1:
            result_f3_list = Remove_ten_bit_cycle(list_spilt_str, 1)
            pass
        case 2:
            result_f3_list=Remove_ten_bit_cycle(list_spilt_str,2)
            # print(result_f3_list)
            pass
        case 3:
            result_f3_list = Remove_ten_bit_cycle(list_spilt_str, 3)
            pass
        case 4:
            result_f3_list = Remove_ten_bit_cycle(list_spilt_str, 4)
            pass
        case 5:
            result_f3_list = Remove_ten_bit_cycle(list_spilt_str, 5)
            pass
        case 6:
            result_f3_list = Remove_ten_bit_cycle(list_spilt_str,6)
            pass
        case 7:
            result_f3_list = Remove_ten_bit_cycle(list_spilt_str, 7)
            pass
        case 8:
            result_f3_list = Remove_ten_bit_cycle(list_spilt_str, 8)
            pass
        case 9:
            result_f3_list = Remove_ten_bit_cycle(list_spilt_str, 9)
            pass
    return result_f3_list
    pass

def Pre_Funcation_03_Rem_one(sum_index,num_List):
    """
    #方法三:和尾*3+3，取尾去个位
    :param sum:
    :param num_List:
    :return:
    """
    list_2_str = Spilt_list(num_List)  ##调用拆分list公共方法
    sum = (sum_index * 3+3) % 10
    print("***和尾*3+3去个位***__和值尾为:", sum)
    result_f3 = []
    match sum:
        case 0:
            result_f3 = Remove_one_bit_cycle(list_2_str, 0)
            pass
        case 1:
            result_f3 = Remove_one_bit_cycle(list_2_str, 1)
            pass
        case 2:
            result_f3 = Remove_one_bit_cycle(list_2_str, 2)
            # print(result_f3_list)
            pass
        case 3:
            result_f3 = Remove_one_bit_cycle(list_2_str, 3)
            pass
        case 4:
            result_f3 = Remove_one_bit_cycle(list_2_str, 4)
            pass
        case 5:
            result_f3 = Remove_one_bit_cycle(list_2_str, 5)
            pass
        case 6:
            result_f3 = Remove_one_bit_cycle(list_2_str, 6)
            pass
        case 7:
            result_f3 = Remove_one_bit_cycle(list_2_str, 7)
            pass
        case 8:
            result_f3 = Remove_one_bit_cycle(list_2_str, 8)
            pass
        case 9:
            result_f3 = Remove_one_bit_cycle(list_2_str, 9)
            pass
    return result_f3
    pass

def Pre_Funcation_03_Rem_hundred(sum_index,num_List):
    """
    #方法三:和尾加减2(偶数+2，奇数-2)
    :param sum:
    :param num_List:
    :return:
    """
    result_List = Spilt_list(num_List)  ##调用拆分list公共方法
    sumKey=sum_index%2
    if sumKey==0:
        sum = (sum_index+2) % 10
        pass
    else:
        sum = GetSubtraction(sum_index, 2)
        pass
    print("***和尾加减2(偶数+2，奇数-2)去百位***__和值尾为:", sum)
    result = []
    match sum:
        case 0:
            result = Remove_Bit_list(result_List, 0,100)
            pass
        case 1:
            result = Remove_Bit_list(result_List, 100,200)
            pass
        case 2:
            result = Remove_Bit_list(result_List, 200,300)
            # print(result_f3_list)
            pass
        case 3:
            result = Remove_Bit_list(result_List, 300,400)
            pass
        case 4:
            result = Remove_Bit_list(result_List, 400,500)
            pass
        case 5:
            result = Remove_Bit_list(result_List, 500,600)
            pass
        case 6:
            result = Remove_Bit_list(result_List, 600,700)
            pass
        case 7:
            result = Remove_Bit_list(result_List, 700,800)
            pass
        case 8:
            result = Remove_Bit_list(result_List, 800,900)
            pass
        case 9:
            result = Remove_Bit_list(result_List, 900,1000)
            pass
    return result
    pass

def Remove_duplicate(mList):
    """
    #去除list中重复项
    :param mList:
    :return:
    """
    result_Remove_duplicate = []
    """#去重"""
    for i in mList:
        if i not in result_Remove_duplicate:
            result_Remove_duplicate.append(i)
        pass
    return result_Remove_duplicate
    pass

def Show(mList):
    """
    #显示方法
    :param mList:
    :return:
    """
    # print("转换后的结果:")
    str_show=''
    for i in range(len(mList)):
        # print(mList[i])
        str_show+=str(mList[i])+" "
        pass
    print(str_show)
    print("数量:",len(mList))
    pass

def GetFuncation_Result(num_list,index):

    ##方法:***根据合值去下期百位、十位、个位
    result_01 = Pre_Funcation_01(index, num_list)
    result_01_str = List_2_Str(result_01)
    print("此方法规则:\n", "****根据合值杀下期百位****\n", "*当合值为0时，下期百位杀3*\n", "*当合值为1时，下期百位杀9*\n",
          "*当合值为2时，下期百位杀2*\n", "*当合值为3时，下期百位杀9*\n", "*当合值为4时，下期百位杀6*\n",
          "*当合值为5时，下期百位杀4*\n", "*当合值为6时，下期百位杀1*\n", "*当合值为7时，下期百位杀7*\n",
          "*当合值为8时，下期百位杀0*\n", "*当合值为9时，下期百位杀6*\n", "****根据合值杀下期十位****\n",
          "*当合值为0时，下期十位杀5*\n", "*当合值为1时，下期十位杀0*\n", "*当合值为2时，下期十位杀0*\n",
          "*当合值为3时，下期十位杀2*\n", "*当合值为4时，下期十位杀6*\n", "*当合值为5时，下期十位杀7*\n",
          "*当合值为6时，下期十位杀9*\n", "*当合值为7时，下期十位杀8*\n", "*当合值为8时，下期十位杀5*\n",
          "*当合值为9时，下期十位杀4*\n", "****根据合值杀下期个位****\n", "当合值为0时，下期个位杀6*\n",
          "*当合值为1时，下期个位杀8*\n", "*当合值为2时，下期个位杀3*\n", "*当合值为3时，下期个位杀2*\n",
          "*当合值为4时，下期个位杀7*\n", "*当合值为5时，下期个位杀2*\n", "*当合值为6时，下期个位杀0*\n",
          "*当合值为7时，下期个位杀1*\n", "*当合值为8时，下期个位杀4*\n", "*当合值为9时，下期个位杀4*\n")

    print("___结果:")
    Show(result_01_str)  # 显示
    print("上一期:", index)

    ##方法:***和值尾数去重***
    sum_f2_01 = GetSum(index)
    result_02 = Pre_Funcation_02(sum_f2_01, num_list)
    result_02_str = List_2_Str(result_02)
    print("\n方法:***和值尾数去码***_尾数:", sum_f2_01, "\n___结果:")
    Show(result_02_str)  # 显示
    print("上一期:", index)

    ##方法:***和值尾*3尾数去码***
    sum_f2_02 = (GetSum(index) * 3) % 10
    result_03 = Pre_Funcation_02(sum_f2_02, num_list)
    result_03_str = List_2_Str(result_03)
    print("\n方法:***和值尾*3尾数去码***_尾数:", sum_f2_02, "\n___结果:")
    Show(result_03_str)  # 显示
    print("上一期:", index)

    ##方法:***和值尾*4尾数去码***
    sum_f2_03 = (GetSum(index) * 4) % 10
    result_04 = Pre_Funcation_02(sum_f2_03, num_list)
    result_04_str = List_2_Str(result_04)
    print("\n方法:***和值尾*4尾数去码***_尾数:", sum_f2_03, "\n___结果:")
    Show(result_04_str)  # 显示
    print("上一期:", index)

    ##方法:***和值*5尾数去码***
    sum_f2_04 = (GetSum(index) * 5) % 10
    result_05 = Pre_Funcation_02(sum_f2_04, num_list)
    result_05_str = List_2_Str(result_05)
    print("\n方法:***和值尾*5尾数去码***_尾数:", sum_f2_04, "\n___结果:")
    Show(result_05_str)  # 显示
    print("上一期:", index)

    ##百位减个位尾数去码
    sum_f3_01 = GetSubtraction(index[0], index[2])
    result_06 = Pre_Funcation_02(sum_f3_01, num_list)
    result_06_str = List_2_Str(result_06)
    print("\n方法:***百位减个位尾数去码***_尾数:", sum_f3_01, "\n___结果:")
    Show(result_06_str)  # 显示
    print("上一期:", index)

    ##百位减十位尾数去码
    sum_f3_02 = GetSubtraction(index[0], index[1])
    result_07 = Pre_Funcation_02(sum_f3_02, num_list)
    result_07_str = List_2_Str(result_07)
    print("\n方法:***百位减十位尾数去码***_尾数:", sum_f3_02, "\n___结果:")
    Show(result_07_str)  # 显示
    print("上一期:", index)

    ##个位减十位尾数去码
    sum_f3_03 = GetSubtraction(index[2], index[1])
    result_08 = Pre_Funcation_02(sum_f3_03, num_list)
    result_08_str = List_2_Str(result_08)
    print("\n方法:***个位减十位尾数去码***_尾数:", sum_f3_03, "\n___结果:")
    Show(result_08_str)  # 显示
    print("上一期:", index)

    ##个位减百位尾数去码
    sum_f3_04 = GetSubtraction(index[2], index[0])
    result_09 = Pre_Funcation_02(sum_f3_04, num_list)
    result_09_str = List_2_Str(result_09)
    print("\n方法:***个位减百位尾数去码***_尾数:", sum_f3_04, "\n___结果:")
    Show(result_09_str)  # 显示
    print("上一期:", index)

    ##百位加十位尾数去码
    sum_f3_05 = GetAdd(index[0], index[1])
    result_10 = Pre_Funcation_02(sum_f3_05, num_list)
    result_10_str = List_2_Str(result_10)
    print("\n方法:***百位加十位尾数去码***_尾数:", sum_f3_05, "\n___结果:")
    Show(result_10_str)  # 显示
    print("上一期:", index)

    ##和数除8的余数去码
    sum = (index[0] + index[1] + index[2]) % 8
    result_11 = Pre_Funcation_02(sum, num_list)
    result_11_str = List_2_Str(result_11)
    print("\n方法:***和数除8的余数去码***_尾数:", sum, "\n___结果:")
    Show(result_11_str)  # 显示
    print("上一期:", index)

    ##方法:***和值尾*2尾数去码***
    sum_f4 = (GetSum(index) * 2) % 10
    result_12 = Pre_Funcation_02(sum_f4, num_list)
    result_12_str = List_2_Str(result_12)
    print("\n方法:***和值尾*2尾数去码***_尾数:", sum_f4, "\n___结果:")
    Show(result_12_str)  # 显示
    print("上一期:", index)

    ##个位*个位尾数去码
    sum_f5_01 = GetSquare(index[2])
    result_13 = Pre_Funcation_02(sum_f5_01, num_list)
    result_13_str = List_2_Str(result_13)
    print("\n方法:***个位*个位尾数去码***_尾数:", sum_f5_01, "\n___结果:")
    Show(result_13_str)  # 显示
    print("上一期:", index)

    ##十位*十位尾数去码
    sum_f5_02 = GetSquare(index[1])
    result_14 = Pre_Funcation_02(sum_f5_02, num_list)
    result_14_str = List_2_Str(result_14)
    print("\n方法:***十位*十位尾数去码***_尾数:", sum_f5_02, "\n___结果:")
    Show(result_14_str)  # 显示
    print("上一期:", index)

    ##百位*百位尾数去码
    sum_f5_03 = GetSquare(index[0])
    result_15 = Pre_Funcation_02(sum_f5_03, num_list)
    result_15_str = List_2_Str(result_15)
    print("\n方法:***百位*百位尾数去码***_尾数:", sum_f5_03, "\n___结果:")
    Show(result_15_str)  # 显示
    print("上一期:", index)

    ###整理所有结果，去重###
    mFinish_Result = []
    mFinish_Result = result_01_str + result_02_str + result_03_str + result_03_str + result_04_str + result_05_str \
                     + result_06_str + result_07_str + result_08_str + result_09_str + result_10_str + result_11_str \
                     + result_12_str + result_13_str + result_14_str + result_15_str
    mResult_Remove_duplicate = Remove_duplicate(mFinish_Result)
    print("去重前:")
    Show(mFinish_Result)
    print("去重后:")
    Show(mResult_Remove_duplicate)
    pass

def GetResult_02(num_list,index,mIndex):
    sum=GetSum(index)
    result_list = Pre_Funcation_03_Rem_hundred(sum, num_list)#去除百位
    result_Rem_ten = Pre_Funcation_03_Rem_ten(sum, result_list)#去除十位
    result = Pre_Funcation_03_Rem_one(sum, result_Rem_ten)#去除个位
    result_test_str_02 = List_2_Str(result)
    result_Remove_tenBit=Get_Remove_tenBit_combination(result_test_str_02,mIndex[1],index[1])#前两期去除组合
    Show(result_Remove_tenBit)

    result_Remove_Way=GetResult_Rem_Way(result_Remove_tenBit,index)#路数去除组合
    Show(result_Remove_Way)

    result_Remove_Sum_Way=GetResult_Sum_Way(result_Remove_Way,sum)#和尾去下一期两码组合
    Show(result_Remove_Sum_Way)

    result_Remove_Sum_Befoe=GetResult_Sum_Way_Before(result_Remove_Sum_Way,sum)#和尾去前2组合
    Show(result_Remove_Sum_Befoe)

    result_Remove_Sum_After=GetResult_Sum_Way_After(result_Remove_Sum_Befoe,sum)#和尾去后2组合
    Show(result_Remove_Sum_After)

    result_Remove_Way_Sum=GetResult_Sum_Way_Remove(result_Remove_Sum_After,sum)#和尾去012
    Show(result_Remove_Way_Sum)

    print("上上一期:", mIndex)
    print("上一期:", index)
    pass


def Get_Remove_tenBit_combination(indexList,x,y):
    """
    #去除上两期十位的组合,x和y为键值
    :param indexList:
    :return:
    """
    key = []
    for i in range(len(indexList)):
        hundred = int(indexList[i]) // 100
        ten=(int(indexList[i]) // 10)%10
        one=int(indexList[i])%10
        if hundred==x and ten==y or ten==x and one==y:
            # print(indexList[i])
            key.append(indexList[i])
        pass
    """
    #获取两个list的差集:
    #result=[i for i in A if i not in B]#元素在A里，但不在B里
    """
    result=[i for i in indexList if i not in key]
    return result
    pass

def Get_Remove_Sum_2bit_Before_combination(indexList,x,y):
    """
    #去除前两位组合(即百位和十位)
    :param indexList:
    :param x:百位
    :param y:十位
    :return:
    """
    key = []
    for i in range(len(indexList)):
        hundred = int(indexList[i]) // 100
        ten = (int(indexList[i]) // 10) % 10
        if hundred == x and ten == y:
            # print(indexList[i])
            key.append(indexList[i])
        pass
    result = [i for i in indexList if i not in key]#获取两个list的差集:
    return result
    pass

def Get_Remove_Sum_2bit_After_combination(indexList,x,y):
    """
    #去除后两位组合(即十位和个位)
    :param indexList:
    :param x:是位
    :param y:个位
    :return:
    """
    key = []
    for i in range(len(indexList)):
        ten = (int(indexList[i]) // 10) % 10
        one = int(indexList[i]) % 10
        if ten == x and one == y:
            # print(indexList[i])
            key.append(indexList[i])
        pass
    result = [i for i in indexList if i not in key]#获取两个list的差集:
    return result
    pass

def GetResult_Rem_Way(num_list,index):
    """
    #路数去除下一期
    #0路:0,3,6,9
    #1路:1,4,7
    #2路:2,5,8
    :param num_list:
    :param index:上一期号码
    :return:
    """
    index_way=Get_Way(index)
    # print("路数:",index_way)
    mReturnList=[]
    match index_way:
        case "000":
            """
            #000:去掉?13,13?,?19,19?
            """
            mRList = Get_Remove_tenBit_combination(num_list, 1, 3)
            mReturnList = Get_Remove_tenBit_combination(mRList, 1, 9)
            pass
        case "001":
            mRList = Get_Remove_tenBit_combination(num_list, 0, 6)
            mReturnList = Get_Remove_tenBit_combination(mRList, 0, 7)
            pass
        case "002":
            mRList = Get_Remove_tenBit_combination(num_list, 2, 7)
            mReturnList = Get_Remove_tenBit_combination(mRList, 3, 8)
            pass
        case "010":
            mRList = Get_Remove_tenBit_combination(num_list, 0, 7)
            mReturnList = Get_Remove_tenBit_combination(mRList, 3, 0)
            pass
        case "011":
            mRList = Get_Remove_tenBit_combination(num_list, 2, 4)
            mReturnList = Get_Remove_tenBit_combination(mRList, 2, 6)
            pass
        case "012":
            mRList = Get_Remove_tenBit_combination(num_list, 3, 8)
            mReturnList = Get_Remove_tenBit_combination(mRList, 6, 0)
            pass
        case "020":
            mRList = Get_Remove_tenBit_combination(num_list, 2, 2)
            mReturnList = Get_Remove_tenBit_combination(mRList, 4, 8)
            pass
        case "021":
            mRList = Get_Remove_tenBit_combination(num_list, 0, 6)
            mReturnList = Get_Remove_tenBit_combination(mRList, 4, 1)
            pass
        case "022":
            mRList = Get_Remove_tenBit_combination(num_list, 0, 3)
            mReturnList = Get_Remove_tenBit_combination(mRList, 2, 2)
            pass
        case "100":
            mRList = Get_Remove_tenBit_combination(num_list, 1, 6)
            mReturnList = Get_Remove_tenBit_combination(mRList, 2, 3)
            pass
        case "101":
            mRList = Get_Remove_tenBit_combination(num_list, 1, 3)
            mReturnList = Get_Remove_tenBit_combination(mRList, 2, 3)
            pass
        case "102":
            mRList = Get_Remove_tenBit_combination(num_list, 1, 6)
            mReturnList = Get_Remove_tenBit_combination(mRList, 3, 3)
            pass
        case "110":
            mRList = Get_Remove_tenBit_combination(num_list, 0, 9)
            mReturnList = Get_Remove_tenBit_combination(mRList, 4, 1)
            pass
        case "111":
            mRList = Get_Remove_tenBit_combination(num_list, 1, 8)
            mReturnList = Get_Remove_tenBit_combination(mRList, 2, 8)
            pass
        case "112":
            mRList = Get_Remove_tenBit_combination(num_list, 4, 3)
            mReturnList = Get_Remove_tenBit_combination(mRList, 4, 5)
            pass
        case "120":
            mRList = Get_Remove_tenBit_combination(num_list, 0, 1)
            mReturnList = Get_Remove_tenBit_combination(mRList, 0, 2)
            pass
        case "121":
            """
            #121路数:去掉?17,17?,?23,23?
            """
            # print("路数:", index_way)
            mRList=Get_Remove_tenBit_combination(num_list,1,7)
            mReturnList=Get_Remove_tenBit_combination(mRList,2,3)
            pass
        case "122":
            mRList = Get_Remove_tenBit_combination(num_list, 1, 2)
            mReturnList = Get_Remove_tenBit_combination(mRList, 2, 5)
            pass
        case "200":
            mRList = Get_Remove_tenBit_combination(num_list, 1, 7)
            mReturnList = Get_Remove_tenBit_combination(mRList, 2, 5)
            pass
        case "201":
            mRList = Get_Remove_tenBit_combination(num_list, 3, 0)
            mReturnList = Get_Remove_tenBit_combination(mRList, 4, 1)
            pass
        case "202":
            mRList = Get_Remove_tenBit_combination(num_list, 4, 3)
            mReturnList = Get_Remove_tenBit_combination(mRList, 6, 0)
            pass
        case "210":
            mRList = Get_Remove_tenBit_combination(num_list, 1, 7)
            mReturnList = Get_Remove_tenBit_combination(mRList, 2, 9)
            pass
        case "211":
            mRList = Get_Remove_tenBit_combination(num_list, 1, 5)
            mReturnList = Get_Remove_tenBit_combination(mRList, 5, 4)
            pass
        case "212":
            mRList = Get_Remove_tenBit_combination(num_list, 1, 0)
            mReturnList = Get_Remove_tenBit_combination(mRList, 4, 6)
            pass
        case "220":
            mRList = Get_Remove_tenBit_combination(num_list, 1, 8)
            mReturnList = Get_Remove_tenBit_combination(mRList, 5, 1)
            pass
        case "221":
            mRList = Get_Remove_tenBit_combination(num_list, 3, 2)
            mReturnList = Get_Remove_tenBit_combination(mRList, 3, 3)
            pass
        case "222":
            mRList = Get_Remove_tenBit_combination(num_list, 1, 7)
            mReturnList = Get_Remove_tenBit_combination(mRList, 1, 8)
            pass

    return mReturnList
    pass

def GetResult_Sum_Way(num_list,sum):
    """
    #和值去下一期两码组合
    :param num_list:
    :param sum:
    :return:
    """
    mReturnList_Sum = []
    match sum:
        case 0:
            """
            #上一期和尾:0,去除?22,22?,?56,56?
            """
            sum_mRList = Get_Remove_tenBit_combination(num_list, 2, 2)
            mReturnList_Sum = Get_Remove_tenBit_combination(sum_mRList, 5, 6)
            pass
        case 1:
            sum_mRList = Get_Remove_tenBit_combination(num_list, 3, 3)
            mReturnList_Sum = Get_Remove_tenBit_combination(sum_mRList, 6, 9)
            pass
        case 2:
            sum_mRList = Get_Remove_tenBit_combination(num_list, 2, 7)
            mReturnList_Sum = Get_Remove_tenBit_combination(sum_mRList, 3, 6)
            pass
        case 3:
            sum_mRList = Get_Remove_tenBit_combination(num_list, 2, 6)
            mReturnList_Sum = Get_Remove_tenBit_combination(sum_mRList, 9, 9)
            pass
        case 4:
            sum_mRList = Get_Remove_tenBit_combination(num_list, 2, 5)
            mReturnList_Sum = Get_Remove_tenBit_combination(sum_mRList, 4, 6)
            pass
        case 5:
            sum_mRList = Get_Remove_tenBit_combination(num_list, 3, 9)
            mReturnList_Sum = Get_Remove_tenBit_combination(sum_mRList, 7, 9)
            pass
        case 6:
            sum_mRList = Get_Remove_tenBit_combination(num_list, 1, 7)
            mReturnList_Sum = Get_Remove_tenBit_combination(sum_mRList, 2, 4)
            pass
        case 7:
            sum_mRList = Get_Remove_tenBit_combination(num_list, 0, 4)
            mReturnList_Sum = Get_Remove_tenBit_combination(sum_mRList, 3, 8)
            pass
        case 8:
            sum_mRList = Get_Remove_tenBit_combination(num_list, 2, 5)
            mReturnList_Sum = Get_Remove_tenBit_combination(sum_mRList, 4, 4)
            pass
        case 9:
            sum_mRList = Get_Remove_tenBit_combination(num_list, 4, 6)
            mReturnList_Sum = Get_Remove_tenBit_combination(sum_mRList, 6, 7)
            pass
    return mReturnList_Sum
    pass

def GetResult_Sum_Way_Before(num_list,sum):
    """
    #根据和值去除前两位组合
    :param num_list:
    :param sum:
    :return:
    """
    mReturnList_Sum = []
    match sum:
        case 0:
            #和尾为0,去掉34?,65?
            sum_list_before=Get_Remove_Sum_2bit_Before_combination(num_list,3,4)
            mReturnList_Sum = Get_Remove_Sum_2bit_Before_combination(sum_list_before, 6, 5)
            pass
        case 1:
            sum_list_before = Get_Remove_Sum_2bit_Before_combination(num_list, 1, 2)
            mReturnList_Sum = Get_Remove_Sum_2bit_Before_combination(sum_list_before, 4, 8)
            pass
        case 2:
            sum_list_before = Get_Remove_Sum_2bit_Before_combination(num_list, 2, 0)
            mReturnList_Sum = Get_Remove_Sum_2bit_Before_combination(sum_list_before, 2, 9)
            pass
        case 3:
            sum_list_before = Get_Remove_Sum_2bit_Before_combination(num_list, 3, 7)
            mReturnList_Sum = Get_Remove_Sum_2bit_Before_combination(sum_list_before, 4, 2)
            pass
        case 4:
            sum_list_before = Get_Remove_Sum_2bit_Before_combination(num_list, 2, 6)
            mReturnList_Sum = Get_Remove_Sum_2bit_Before_combination(sum_list_before, 9, 6)
            pass
        case 5:
            sum_list_before = Get_Remove_Sum_2bit_Before_combination(num_list, 3, 9)
            mReturnList_Sum = Get_Remove_Sum_2bit_Before_combination(sum_list_before, 4, 7)
            pass
        case 6:
            sum_list_before = Get_Remove_Sum_2bit_Before_combination(num_list, 1, 9)
            mReturnList_Sum = Get_Remove_Sum_2bit_Before_combination(sum_list_before, 7, 6)
            pass
        case 7:
            sum_list_before = Get_Remove_Sum_2bit_Before_combination(num_list, 5, 8)
            mReturnList_Sum = Get_Remove_Sum_2bit_Before_combination(sum_list_before, 6, 1)
            pass
        case 8:
            sum_list_before = Get_Remove_Sum_2bit_Before_combination(num_list, 0, 9)
            mReturnList_Sum = Get_Remove_Sum_2bit_Before_combination(sum_list_before, 2, 3)
            pass
        case 9:
            sum_list_before = Get_Remove_Sum_2bit_Before_combination(num_list, 1, 8)
            mReturnList_Sum = Get_Remove_Sum_2bit_Before_combination(sum_list_before, 4, 6)
            pass
    return mReturnList_Sum
    pass

def GetResult_Sum_Way_After(num_list,sum):
    """
    #根据和值去除后两位组合
    :param num_list:
    :param sum:
    :return:
    """
    mReturnList_Sum = []
    match sum:
        case 0:
            #和尾为0,去掉?21,?63
            sum_list_before=Get_Remove_Sum_2bit_After_combination(num_list,2,1)
            mReturnList_Sum = Get_Remove_Sum_2bit_After_combination(sum_list_before, 6, 3)
            pass
        case 1:
            sum_list_before = Get_Remove_Sum_2bit_After_combination(num_list, 1, 6)
            mReturnList_Sum = Get_Remove_Sum_2bit_After_combination(sum_list_before, 7, 9)
            pass
        case 2:
            sum_list_before = Get_Remove_Sum_2bit_After_combination(num_list, 2, 8)
            mReturnList_Sum = Get_Remove_Sum_2bit_After_combination(sum_list_before, 5, 6)
            pass
        case 3:
            sum_list_before = Get_Remove_Sum_2bit_After_combination(num_list, 0, 9)
            mReturnList_Sum = Get_Remove_Sum_2bit_After_combination(sum_list_before, 4, 7)
            pass
        case 4:
            sum_list_before = Get_Remove_Sum_2bit_After_combination(num_list, 5, 2)
            mReturnList_Sum = Get_Remove_Sum_2bit_After_combination(sum_list_before, 9, 4)
            pass
        case 5:
            sum_list_before = Get_Remove_Sum_2bit_After_combination(num_list, 3, 2)
            mReturnList_Sum = Get_Remove_Sum_2bit_After_combination(sum_list_before, 7, 3)
            pass
        case 6:
            sum_list_before = Get_Remove_Sum_2bit_After_combination(num_list, 3, 9)
            mReturnList_Sum = Get_Remove_Sum_2bit_After_combination(sum_list_before, 7, 0)
            pass
        case 7:
            sum_list_before = Get_Remove_Sum_2bit_After_combination(num_list, 4, 5)
            mReturnList_Sum = Get_Remove_Sum_2bit_After_combination(sum_list_before, 8, 2)
            pass
        case 8:
            sum_list_before = Get_Remove_Sum_2bit_After_combination(num_list, 2, 6)
            mReturnList_Sum = Get_Remove_Sum_2bit_After_combination(sum_list_before, 5, 2)
            pass
        case 9:
            sum_list_before = Get_Remove_Sum_2bit_After_combination(num_list, 4, 8)
            mReturnList_Sum = Get_Remove_Sum_2bit_After_combination(sum_list_before, 7, 6)
            pass
    return mReturnList_Sum
    pass

def GetResult_Sum_Way_Remove(num_list,sum):
    """
    #根据和尾去012路特征
    :param num_list:
    :param sum:
    :return:
    """
    result_Remove_combination=[]
    match sum:
        case 0:
            """
            #当和尾为0,下期去221类型
            """
            result_Remove_combination=Get_Way_Remove_combination(num_list,"221")
            pass
        case 1:
            result_Remove_combination = Get_Way_Remove_combination(num_list, "201")
            pass
        case 2:
            result_Remove_combination = Get_Way_Remove_combination(num_list, "210")
            pass
        case 3:
            result_Remove_combination = Get_Way_Remove_combination(num_list, "001")
            pass
        case 4:
            result_Remove_combination = Get_Way_Remove_combination(num_list, "221")
            pass
        case 5:
            result_Remove_combination = Get_Way_Remove_combination(num_list, "202")
            pass
        case 6:
            result_Remove_combination = Get_Way_Remove_combination(num_list, "121")
            pass
        case 7:
            result_Remove_combination = Get_Way_Remove_combination(num_list, "021")
            pass
        case 8:
            result_Remove_combination = Get_Way_Remove_combination(num_list, "112")
            pass
        case 9:
            result_Remove_combination = Get_Way_Remove_combination(num_list, "010")
            pass

    result_re = [i for i in num_list if i not in result_Remove_combination]
    return result_re
    pass

def main():
    num_list=Pre_Build_num()
    #上一期号数
    index=[0,3,9]
    #上上期
    mIndex=[6,0,0]

    #GetFuncation_Result(num_list,index)#调用结果方法函数

    GetResult_02(num_list, index,mIndex)

    pass

if __name__=='__main__':
    main()