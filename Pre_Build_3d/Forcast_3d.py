# ---************************************************---
# @coding: utf-8
# @Time : 2022/8/2 0002 9:11
# @Author : Matrix
# @File : Forcast_3d.py
# @Software: PyCharm
# ---************************************************---
import argparse
from collections import Counter
import pandas as pd

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
        result.append(num)
        pass
    return result
    pass

def Get_Read_file(path):
    file=pd.read_csv(path, header=None, encoding='utf-8')
    # print(file)
    # file_num = file.iloc[0]
    # file_num_str=Get_List_2_str(file_num.tolist())
    # print(file_num_str)
    result_list=[]
    for i in range(len(file)):
        file_num = file.iloc[i]
        file_num_str = Get_List_2_str(file_num.tolist())
        # print(file_num_str)
        result_list.append(file_num_str)
        pass
    return result_list
    pass

def Get_Index_List_File(file_path):
    """
    #读取txt文件获取上一期号码
    :param file_path:
    :return:
    """
    str_contents=""
    with open(file_path, 'r',encoding="utf-8") as f:
        str_contents = f.read()
        # print(str_contents.split()[-1])
        pass
    index_list = []
    str_contents_end=(str_contents.split()[-1]).split(",")#将读取的字符串截取分片成list
    for i in range(len(str_contents_end)):
        index_list.append(int(str_contents_end[i]))#将截取分片后的元素转化成整数类型放入list
        pass
    return index_list
    pass

def Get_Next_List_File(file_path):
    next_list = []
    file_str = ""
    with open(args.file_next_result_path, 'r', encoding='utf-8') as f:
        file_str = f.read()
        pass
    temp=file_str.split("\n")
    for i in range(len(temp)):
        temp_01 = temp[i]
        # temp_01_int_01=int(temp_01[0])
        temp_02 = temp_01[0] + temp_01[-3] + temp_01[-1]
        temp_02=temp_02.replace(',','')#去掉","，防止报错
        nums=[int(x) for x in temp_02]
        # print(nums)
        next_list.append(nums)
        pass

    return next_list
    pass

def DoForecast(file_path,column):
    """获取csv文件内容并返回
    :param file_path: 文件地址,类型为str
    :param column: 要查询的列数,类型为int
    :return: 返回的list值,result为返回结果list
    """
    file = pd.read_csv(file_path, header=None, encoding='utf-8')
    index_len = len(file)
    num=file.iloc[:,column]
    result=[]
    for i in range(index_len):
        result.append(num[i])
        if i == index_len - 1:  #检测是否最后一个，是则跳过。
            break
            pass
        pass
    return result
    pass

def Get_Next_Index(mIndex,mListIndex):
    """预测下一次的值
    :param mIndex:数字下标
    :param mListIndex:数字列表
    :return:返回可能出现的list值
    """
    result=[]
    for i in range(len(mListIndex)):
        if i == len(mListIndex) - 1:  #检测是否最后一个，是则跳过。
            break
            pass

        if mListIndex[i]==mIndex:
            #print("下一次可能出现的值:"+str(mListIndex[i+1]))
            result.append(mListIndex[i+1])
            pass
        pass

    return result
    pass

def Get_List_Difference_set(index_list,remove_list):
    """
    #获取两个list的差集
    :param index_list:原list
    :param remove_list:被删除list
    :return:
    """
    result = [i for i in index_list if i not in remove_list]
    return result
    pass

def GetMin(num_01,num_02,num_03):
    """三元运算获得最小数
    :param num_01:
    :param num_02:
    :param num_03:
    :return:
    """
    return num_01 if num_01 < num_02 and num_01 < num_03 else num_02 if num_02 < num_03 else num_03
    #return num_01 if num_01 > num_02 and num_01 > num_03 else num_02 if num_02 > num_03 else num_03#最大数
    pass

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

def Get_Max_Min(index_num):
    """
    #判断index_num的大小,大-1，小-0
    :param index_num:
    :return:
    """
    result_key=0
    if index_num <5:
        result_key=1
        pass

    return result_key
    pass

def Get_Sum_End(index):
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

def Get_Remove_duplicate(list):
    """
    #去重list中重复项
    :param list:
    :return:
    """
    result_Remove_duplicate=[]
    for x in list:
        if x not in result_Remove_duplicate:
            result_Remove_duplicate.append(x)
        pass

    return result_Remove_duplicate
    pass

def Get_Result_Funcation_01(list_01,list_02,list_03):
    """
    #将list_01,list_02,list_03中的单元素组合成一个list元素
    :param list_01:
    :param list_02:
    :param list_03:
    :return: 返回组合完成后且去重的list
    """
    index = GetMin(len(list_01), len(list_02), len(list_03))

    result=[]
    for i in range(index):
        result.append(str(list_01[i])+ str(list_02[i]) + str(list_03[i]))
        pass

    # """
    # #去重list中重复项
    # """
    # result_Remove_duplicate = []
    # for x in result:
    #     if x not in result_Remove_duplicate:
    #         result_Remove_duplicate.append(x)
    #     pass
    result_Remove_duplicate=Get_Remove_duplicate(result)#去重方法函数

    return result_Remove_duplicate
    pass

def Show_Result(indexList,result_list):
    str_show = ''
    for i in range(len(result_list)):
        # print(mList[i])
        str_show += str(result_list[i]) + " "
        pass
    print(str_show)
    print("预测结果数量:", len(result_list),"\t上一期:" + str(indexList))
    pass

def Get_List_2_str(index_list):
    """
        #将list元素转为str
        :param index_list:
        :return:
        """
    str_list = ''
    for i in range(len(index_list)):
        # print(mList[i])
        str_list += str(index_list[i])
        pass
    return str_list
    pass

def Get_Remove_Way(index_list,file_path):
    """
    #通过跨度获取下一期预测
    :param index_list:
    :param file_path:
    :return:
    """
    way_key=max(index_list)-min(index_list)
    get_file_list=Get_Read_file(file_path)

    result_way_list=[]
    for i in range(len(get_file_list)):
        if i==len(get_file_list)-1:
            break
            pass
        # print("get_file_list:", get_file_list[i])
        # print("test_0:",get_file_list[i][0])
        # print("test_1:", get_file_list[i][1])
        # print("test_2:", get_file_list[i][2])
        remove_key=int(get_file_list[i][-1])
        if way_key==remove_key:
            #print("get_file_list:", get_file_list[i])
            # print("test_0:", get_file_list[i+1][0])
            # print("test_1:", get_file_list[i+1][1])
            # print("test_2:", get_file_list[i+1][2])
            test_0=get_file_list[i+1][0]
            test_1=get_file_list[i+1][1]
            test_2=get_file_list[i+1][2]
            #print(test_0+test_1+test_2)
            result_way_list.append(test_0+test_1+test_2)
            pass
        pass

    result_Remove_duplicate = Get_Remove_duplicate(result_way_list)
    return result_Remove_duplicate
    pass

def Get_Remove_Sum(index_list,num_list_01,num_list_02,num_list_03):
    sum_key=index_list[0]+index_list[1]+index_list[2]
    # print("len(num_list_01):",len(num_list_01),"len(num_list_02):",len(num_list_02),"len(num_list_03):",len(num_list_03))
    result_sum_list=[]
    for i in range(len(num_list_01)):
        if i==len(num_list_01)-1:
            break
            pass

        remove_sum_key=num_list_01[i]+num_list_02[i]+num_list_03[i]
        if sum_key==remove_sum_key:
            result_sum_list.append(str(num_list_01[i+1])+ str(num_list_02[i+1]) + str(num_list_03[i+1]))
            pass
        pass

    result_Remove_duplicate = Get_Remove_duplicate(result_sum_list)
    # print("result_sum_list:",result_Remove_duplicate)
    return result_Remove_duplicate
    pass

def Get_Remove_Odd_Even(index_list,num_list_01,num_list_02,num_list_03):
    """
    #奇偶性走势预测
    :param index_list:
    :param num_list_01:
    :param num_list_02:
    :param num_list_03:
    :return:
    """
    # print("len(num_list_01):",len(num_list_01))
    # print("len(num_list_02):", len(num_list_02))
    # print("len(num_list_03):", len(num_list_03))
    index_list_key_01=Get_Odd_Even(index_list[0])#上一期的第一个数据，判断奇偶性
    index_list_key_02 = Get_Odd_Even(index_list[1])#上一期的第二个数据，判断奇偶性
    index_list_key_03 = Get_Odd_Even(index_list[2])#上一期的第三个数据，判断奇偶性
    result_odd_even_list = []
    for i in range(len(num_list_01)):
        if i==len(num_list_01)-1:
            break
            pass

        result_list_key_01 = Get_Odd_Even(num_list_01[i])  # 历史第一个数据，判断奇偶性
        result_list_key_02 = Get_Odd_Even(num_list_02[i])  # 历史第二个数据，判断奇偶性
        result_list_key_03 = Get_Odd_Even(num_list_03[i])  # 历史第三个数据，判断奇偶性
        if index_list_key_01 == result_list_key_01 and index_list_key_02 == result_list_key_02 \
                and index_list_key_03 == result_list_key_03:
            # print(str(num_list_01[i]) + str(num_list_02[i]) + str(num_list_03[i]))
            # print(str(num_list_01[i+1])+str(num_list_02[i+1])+str(num_list_03[i+1]))
            result_odd_even_list.append(str(num_list_01[i+1])+str(num_list_02[i+1])+str(num_list_03[i+1]))
            pass
        pass

    result_Remove_duplicate = Get_Remove_duplicate(result_odd_even_list)
    return result_Remove_duplicate
    pass

def Get_Remove_Max_Min(index_list,num_list_01,num_list_02,num_list_03):
    index_list_key_01 = Get_Max_Min(index_list[0])  # 上一期的第一个数据，判断大小
    index_list_key_02 = Get_Max_Min(index_list[1])  # 上一期的第二个数据，判断大小
    index_list_key_03 = Get_Max_Min(index_list[2])  # 上一期的第三个数据，判断大小

    result_max_min_list = []
    for i in range(len(num_list_01)):
        if i == len(num_list_01) - 1:
            break
            pass

        result_list_key_01 = Get_Max_Min(num_list_01[i])  # 历史第一个数据，判断大小
        result_list_key_02 = Get_Max_Min(num_list_02[i])  # 历史第二个数据，判断大小
        result_list_key_03 = Get_Max_Min(num_list_03[i])  # 历史第三个数据，判断大小
        if index_list_key_01 == result_list_key_01 and index_list_key_02 == result_list_key_02 \
                and index_list_key_03 == result_list_key_03:
            result_max_min_list.append(str(num_list_01[i + 1]) + str(num_list_02[i + 1]) + str(num_list_03[i + 1]))
            pass
        pass

    result_Remove_duplicate = Get_Remove_duplicate(result_max_min_list)
    return result_Remove_duplicate
    pass

def Get_Remove_Special_Way(index_list,num_list_01,num_list_02,num_list_03):
    index_list_key=Get_Way(index_list)
    result_max_min_list = []
    for i in range(len(num_list_01)):
        temp_list=[]
        if i == len(num_list_01) - 1:
            break
            pass

        # list((num_list_01[i],num_list_02[i],num_list_03[i])):将元组(x,y,z)转为列表[x,y,z]
        result_list_key=Get_Way(list((num_list_01[i],num_list_02[i],num_list_03[i])))
        if index_list_key == result_list_key:
            result_max_min_list.append(str(num_list_01[i + 1]) + str(num_list_02[i + 1]) + str(num_list_03[i + 1]))
            pass
        pass

    result_Remove_duplicate = Get_Remove_duplicate(result_max_min_list)
    return result_Remove_duplicate
    pass

def Get_Remove_By_Hundred(index_list,num_list):
    hundred_key=index_list[0]
    remove_list = []
    for i in range(len(num_list)):
        hundred = int(num_list[i]) // 100
        ten = (int(num_list[i]) // 10) % 10
        one = int(num_list[i]) % 10
        if hundred_key == hundred or hundred_key == ten or hundred_key == one:
            # print(num_list[i])
            remove_list.append(num_list[i])
            pass
        pass

    result = Get_List_Difference_set(num_list, remove_list)
    return result
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
    # print("***和尾*3去十位***__和值尾为:",sum)
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
    # print("***和尾*3+3去个位***__和值尾为:", sum)
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
    # print("***和尾加减2(偶数+2，奇数-2)去百位***__和值尾为:", sum)
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

def Lists_2_List(requeList):
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

def Get_Result_Correct(index_list,result_num_lists,next_list,file_csv_path,file_txt_path,result_path):
    """
    #判断预测的结果是否正确并保存
    #保存next_list到txt文件
    #保存index_list,以及跨度和和值到csv文件
    :param index_list:
    :param result_num_lists:
    :param next_list:
    :param file_csv_path:
    :param file_txt_path:
    :return:
    """

    test_next_list = []
    test_next_str=Get_List_2_str(next_list)
    test_next_list.append(test_next_str)

    #将结果列表转为字符串以作保存
    result_num_lists_save =""
    for i in range(len(result_num_lists)):
        # print(mList[i])
        result_num_lists_save += str(result_num_lists[i])+" "
        pass

    result_key_save = ""
    if len([v for v in test_next_list if v in result_num_lists])>0:
        # print("正确")
        result_key_save="正确"
        pass
    else:
        # print("错误")
        result_key_save = "错误"
        pass

    int_sum = next_list[0] + next_list[1] + next_list[2]  # 和值
    int_span = max(next_list) - min(next_list)  # 跨度
    index_result_save =Get_List_2_str(index_list)  #上期号码转字符串存入结果txt文件
    next_result_save=Get_List_2_str(next_list)#预测号码转字符串存入结果txt文件
    next_list_csv_save = str(next_list[0]) + "," + str(next_list[1]) + "," + str(next_list[2])#预测号码转字符串存入csv
    key_csv_save = next_list_csv_save + "," + str(int_span) + "," + str(int_sum)  # 保存的csv最终字符串
    result_txt_save="预测可能结果:"+result_num_lists_save+"\n可能结果总数量:"+str(len(result_num_lists))+"\t上期号:"+index_result_save+"\t真实号码:"+next_result_save+"\t结果:"+result_key_save
    print(result_txt_save)

    #写入csv文件末尾
    with open(file_csv_path, 'a+',encoding="utf-8") as csv_write:
        csv_write.write(key_csv_save+"\n")
        pass

    #写入txt文件末尾
    with open(file_txt_path, 'a+',encoding="utf-8") as txt_write:
        txt_write.write(next_list_csv_save+"\n")
        pass

    # 写入结果txt文件
    with open(result_path, 'a+',encoding="utf-8") as result_write:
        result_write.write(result_txt_save + "\n")
        pass

    print("***保存数据成功***")
    pass

def Get_Correct_Show(result_path):
    """
    #计算平均数量、正确率等
    :param result_path:
    :return:
    """
    str_contents=""
    with open(result_path, 'r',encoding="utf-8") as f:
        str_contents = f.read()
        #str_contents_list.append(f.readline())
        pass
    # print(str_contents)
    # print(str_contents.split()[-4])
    correct_key="正确"
    mistake_key="错误"
    int_correct_key=str_contents.count(correct_key,0,len(str_contents))#正确的个数
    int_mistake_key=str_contents.count(mistake_key,0,len(str_contents))#错误的个数
    int_all_key=int_correct_key+int_mistake_key#总个数
    print("总数:"+str(int_all_key)+"\t正确:"+str(int_correct_key)+
          "\t错误:"+str(int_mistake_key)+"\t正确率:"+str(int_correct_key/int_all_key))

    str_split_list=str_contents.split("\n")
    str_split_list=str_split_list[0:-1]
    # print("str_split_list:",str_split_list)
    #int_line_key = sum(1 for _ in open(result_path, 'r', encoding="utf-8"))  # 获取行号
    # print(str_split_list[1])
    str_list=[]
    for i in range(len(str_split_list)):
        int_sub_num=2*i-1
        # print("i=",i,"2*i-1=",2*i-1,"len(str_split_list)=",len(str_split_list))
        # print(str_split_list[int_sub_num])
        str_list.append(str_split_list[int_sub_num])

        if i==len(str_split_list)/2:
            break
            pass
        pass
    # print("str_list:",str_list[0])
    # print("str_list_int:",str_list[0].split(":")[1].split("\t")[0])
    int_result_num =0
    for j in range(len(str_list)):
        int_result_num+=int(str_list[j].split(":")[1].split("\t")[0])
        pass

    print("平均总可能出现次数:",int_result_num/int_all_key)
    pass

def Run_Result():
    """
    #运行最终方法函数
    :return:
    """
    # 随机生成1000个数据
    pre_build_index_list = Pre_Build_num()

    # index_list = [1,7,0]  #上一期数字
    index_list = Get_Index_List_File(args.file_txt_path)  # 通过读取数据获得上一期数字
    next_list = [1, 5, 1]  # 目标预测号码

    """定义储存csv获取到三列数的数组"""
    result_num_01 = DoForecast(args.file_csv_path, 0)
    result_num_02 = DoForecast(args.file_csv_path, 1)
    result_num_03 = DoForecast(args.file_csv_path, 2)

    """
    ###此处为方法一使用数据###
    """
    result_index_01 = Get_Next_Index(index_list[0], result_num_01)
    result_index_02 = Get_Next_Index(index_list[1], result_num_02)
    result_index_03 = Get_Next_Index(index_list[2], result_num_03)
    # 方法一:走势预测
    result_Funcation_01 = Get_Result_Funcation_01(result_index_01, result_index_02, result_index_03)
    # 方法二:跨度走势预测
    result_Way = Get_Remove_Way(index_list, args.file_csv_path)
    # 方法三:和值走势预测
    result_sum_way = Get_Remove_Sum(index_list, result_num_01, result_num_02, result_num_03)
    # 方法四:奇偶性走势预测
    result_odd_even_way = Get_Remove_Odd_Even(index_list, result_num_01, result_num_02, result_num_03)
    # 方法五:大小走势预测
    result_max_min_way = Get_Remove_Max_Min(index_list, result_num_01, result_num_02, result_num_03)
    # 方法六:012路预测
    result_special_way = Get_Remove_Special_Way(index_list, result_num_01, result_num_02, result_num_03)
    # 方法七:通过百位去除特定数字预测
    result_hundred_way = Get_Remove_By_Hundred(index_list, pre_build_index_list)
    # 方法八:去除百、十、个位预测
    sum = Get_Sum_End(index_list)
    result_list_hundred = Pre_Funcation_03_Rem_hundred(sum, pre_build_index_list)  # 去除百位
    result_Rem_ten = Pre_Funcation_03_Rem_ten(sum, result_list_hundred)  # 去除十位
    result_one = Pre_Funcation_03_Rem_one(sum, result_Rem_ten)  # 去除个位
    result_list_2_str = Lists_2_List(result_one)

    ###调用封装的显示方法显示结果###
    # print("***方法一:走势预测***")
    # Show_Result(index_list, result_Funcation_01)
    # print("***方法二:跨度走势预测***")
    # Show_Result(index_list,result_Way)
    # # print("***方法三:和值走势预测***")
    # # Show_Result(index_list,result_sum_way)
    # # print("***方法四:奇偶性走势预测***")
    # # Show_Result(index_list,result_odd_even_way)
    # # print("***方法五:大小走势预测***")
    # # Show_Result(index_list, result_max_min_way)
    # print("***方法六:012路预测***")
    # Show_Result(index_list, result_special_way)
    # print("***方法七:通过百位去除特定数字预测***")
    # Show_Result(index_list, result_hundred_way)
    # print("***方法八:通过去除百、十、个位预测***")
    # Show_Result(index_list, result_list_2_str)

    # 所有结果2个交集:
    result_01 = [i for i in result_Funcation_01 if i in result_Way]
    result_02 = [i for i in result_Way if i in result_special_way]
    result_03 = [i for i in result_special_way if i in result_hundred_way]
    result_04 = [i for i in result_hundred_way if i in result_list_2_str]
    result_05 = [i for i in result_list_2_str if i in result_Funcation_01]
    result_str = result_01 + result_02 + result_03 + result_04 + result_05
    result_duplicate = Get_Remove_duplicate(result_str)
    # print("所有结果2个交集:")
    # Show_Result(index_list, result_duplicate)

    # Get_Result_Correct(index_list,result_duplicate,next_list,args.file_csv_path,args.file_txt_path,args.file_result_path)

    Get_Correct_Show(args.file_result_path)
    pass

def Run_Get_Resulr_test():
    """
        #运行最终方法函数
        :return:
        """
    # 随机生成1000个数据
    pre_build_index_list = Pre_Build_num()

    # index_list = [1,7,0]  #上一期数字
    index_list = Get_Index_List_File(args.file_txt_path)  # 通过读取数据获得上一期数字
    #next_list = [1, 5, 1]  # 目标预测号码
    next_lists=Get_Next_List_File(args.file_next_result_path)# 通过读取数据获得下一期数字
    # print("获取的next_lists_next_lists[0]:",next_lists[0])
    for i in range(len(next_lists)):
        """定义储存csv获取到三列数的数组"""
        result_num_01 = DoForecast(args.file_csv_path, 0)
        result_num_02 = DoForecast(args.file_csv_path, 1)
        result_num_03 = DoForecast(args.file_csv_path, 2)

        """
        ###此处为方法一使用数据###
        """
        result_index_01 = Get_Next_Index(index_list[0], result_num_01)
        result_index_02 = Get_Next_Index(index_list[1], result_num_02)
        result_index_03 = Get_Next_Index(index_list[2], result_num_03)
        # 方法一:走势预测
        result_Funcation_01 = Get_Result_Funcation_01(result_index_01, result_index_02, result_index_03)
        # 方法二:跨度走势预测
        result_Way = Get_Remove_Way(index_list, args.file_csv_path)
        # 方法三:和值走势预测
        result_sum_way = Get_Remove_Sum(index_list, result_num_01, result_num_02, result_num_03)
        # 方法四:奇偶性走势预测
        result_odd_even_way = Get_Remove_Odd_Even(index_list, result_num_01, result_num_02, result_num_03)
        # 方法五:大小走势预测
        result_max_min_way = Get_Remove_Max_Min(index_list, result_num_01, result_num_02, result_num_03)
        # 方法六:012路预测
        result_special_way = Get_Remove_Special_Way(index_list, result_num_01, result_num_02, result_num_03)
        # 方法七:通过百位去除特定数字预测
        result_hundred_way = Get_Remove_By_Hundred(index_list, pre_build_index_list)
        # 方法八:去除百、十、个位预测
        sum_num = Get_Sum_End(index_list)
        result_list_hundred = Pre_Funcation_03_Rem_hundred(sum_num, pre_build_index_list)  # 去除百位
        result_Rem_ten = Pre_Funcation_03_Rem_ten(sum_num, result_list_hundred)  # 去除十位
        result_one = Pre_Funcation_03_Rem_one(sum_num, result_Rem_ten)  # 去除个位
        result_list_2_str = Lists_2_List(result_one)

        # 所有结果2个交集:
        result_01 = [i for i in result_Funcation_01 if i in result_Way]
        result_02 = [i for i in result_Way if i in result_special_way]
        result_03 = [i for i in result_special_way if i in result_hundred_way]
        result_04 = [i for i in result_hundred_way if i in result_list_2_str]
        result_05 = [i for i in result_list_2_str if i in result_Funcation_01]
        result_str = result_01 + result_02 + result_03 + result_04 + result_05
        result_duplicate = Get_Remove_duplicate(result_str)
        # print("所有结果2个交集:")
        # Show_Result(index_list, result_duplicate)
        Get_Result_Correct(index_list,result_duplicate,next_lists[i],args.file_csv_path,args.file_txt_path,args.file_result_path)
        pass
    pass

def main(args):
    #Run_Result()

    #Run_Get_Resulr_test()

    Get_Correct_Show(args.file_result_path)
    pass

if __name__=='__main__':
    #file_dir = r"./work.csv"
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_csv_path', type=str,default='./data/3_min_3d_data.csv',help='csv文件地址')
    parser.add_argument('--file_txt_path', type=str, default='./data/3_min_3d_data.txt', help='txt文件地址')
    parser.add_argument('--file_result_path', type=str, default='./data/result.txt', help='结果txt文件地址')
    parser.add_argument('--file_next_result_path', type=str, default='./data/next.txt', help='结果txt文件地址')
    args = parser.parse_args()
    main(args)