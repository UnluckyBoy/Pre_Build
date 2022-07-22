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

def GetSubtraction(index_01,index_02):
    """
    #取相减和值
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
    :param index:
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
    print("长度:",len(mList))
    pass

def main():
    num_list=Pre_Build_num()
    #上一期号数
    index=[1,4,1]

    ##方法:***根据合值去下期百位、十位、个位
    result_01=Pre_Funcation_01(index,num_list)
    result_01_str=List_2_Str(result_01)
    print("此方法规则:\n","****根据合值杀下期百位****\n","*当合值为0时，下期百位杀3*\n","*当合值为1时，下期百位杀9*\n",
          "*当合值为2时，下期百位杀2*\n","*当合值为3时，下期百位杀9*\n","*当合值为4时，下期百位杀6*\n",
          "*当合值为5时，下期百位杀4*\n","*当合值为6时，下期百位杀1*\n","*当合值为7时，下期百位杀7*\n",
          "*当合值为8时，下期百位杀0*\n","*当合值为9时，下期百位杀6*\n","****根据合值杀下期十位****\n",
          "*当合值为0时，下期十位杀5*\n","*当合值为1时，下期十位杀0*\n","*当合值为2时，下期十位杀0*\n",
          "*当合值为3时，下期十位杀2*\n","*当合值为4时，下期十位杀6*\n","*当合值为5时，下期十位杀7*\n",
          "*当合值为6时，下期十位杀9*\n","*当合值为7时，下期十位杀8*\n","*当合值为8时，下期十位杀5*\n",
          "*当合值为9时，下期十位杀4*\n","****根据合值杀下期个位****\n","当合值为0时，下期个位杀6*\n",
          "*当合值为1时，下期个位杀8*\n","*当合值为2时，下期个位杀3*\n","*当合值为3时，下期个位杀2*\n",
          "*当合值为4时，下期个位杀7*\n","*当合值为5时，下期个位杀2*\n","*当合值为6时，下期个位杀0*\n",
          "*当合值为7时，下期个位杀1*\n","*当合值为8时，下期个位杀4*\n","*当合值为9时，下期个位杀4*\n")
    print("___结果:")
    Show(result_01_str)#显示
    print("上一期:", index)

    ##方法:***和值尾数去重***
    sum_f2_01=GetSum(index)
    result_02=Pre_Funcation_02(sum_f2_01, num_list)
    result_02_str = List_2_Str(result_02)
    print("\n方法:***和值尾数去码***_尾数:", sum_f2_01,"\n___结果:")
    Show(result_02_str)  # 显示
    print("上一期:", index)

    ##方法:***和值尾*3尾数去码***
    sum_f2_02=(GetSum(index)*3)%10
    result_03=Pre_Funcation_02(sum_f2_02, num_list)
    result_03_str = List_2_Str(result_03)
    print("\n方法:***和值尾*3尾数去码***_尾数:", sum_f2_02,"\n___结果:")
    Show(result_03_str)  # 显示
    print("上一期:", index)

    ##方法:***和值尾*4尾数去码***
    sum_f2_03 = (GetSum(index) * 4) % 10
    result_04 = Pre_Funcation_02(sum_f2_03, num_list)
    result_04_str = List_2_Str(result_04)
    print("\n方法:***和值尾*4尾数去码***_尾数:", sum_f2_03,"\n___结果:")
    Show(result_04_str)  # 显示
    print("上一期:", index)

    ##方法:***和值*5尾数去码***
    sum_f2_04 = (GetSum(index) * 5) % 10
    result_05 = Pre_Funcation_02(sum_f2_04, num_list)
    result_05_str = List_2_Str(result_05)
    print("\n方法:***和值尾*5尾数去码***_尾数:", sum_f2_04,"\n___结果:")
    Show(result_05_str)  # 显示
    print("上一期:", index)

    ##百位减个位尾数去码
    sum_f3_01=GetSubtraction(index[0],index[2])
    result_06=Pre_Funcation_02(sum_f3_01, num_list)
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
    sum=(index[0]+index[1]+index[2])%8
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
    sum_f5_01=GetSquare(index[2])
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
    mFinish_Result=[]
    mFinish_Result=result_01_str+result_02_str+result_03_str+result_03_str+result_04_str+result_05_str\
                   +result_06_str+result_07_str+result_08_str+result_09_str+result_10_str+result_11_str\
                   +result_12_str+result_13_str+result_14_str+result_15_str
    mResult_Remove_duplicate=Remove_duplicate(mFinish_Result)
    print("去重前:")
    Show(mFinish_Result)
    print("去重后:")
    Show(mResult_Remove_duplicate)
    pass

if __name__=='__main__':
    main()