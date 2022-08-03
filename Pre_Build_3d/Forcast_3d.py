# ---************************************************---
# @coding: utf-8
# @Time : 2022/8/2 0002 9:11
# @Author : Matrix
# @File : Forcast_3d.py
# @Software: PyCharm
# ---************************************************---
import argparse
import random
import pandas as pd

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

def GetResult_Funcation_02(path,column):
    sum_list=DoForecast(path,column)
    print(sum_list)
    for i in range(len(sum_list)):
        #num=sum_list[i]
        if sum_list[i]%2==0:
            print(str(sum_list[i])+":偶")
            pass
        else:
            print(str(sum_list[i]) + ":奇")
            pass
        pass
    pass

def Show_Result(indexList,result_list):
    str_show = ''
    for i in range(len(result_list)):
        # print(mList[i])
        str_show += str(result_list[i]) + " "
        pass
    print(str_show)
    print("数量:", len(result_list))
    print("上一期:" + str(indexList))
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

def main(args):
    indexList = [3,6,1]  # 上一期数字
    """定义储存csv获取到三列数的数组"""
    result_num_01 =DoForecast(args.file_path,0)
    result_num_02 =DoForecast(args.file_path,1)
    result_num_03 =DoForecast(args.file_path,2)

    """
    ###此处为方法一使用数据###
    """
    result_index_01=Get_Next_Index(indexList[0],result_num_01)
    result_index_02=Get_Next_Index(indexList[1],result_num_02)
    result_index_03=Get_Next_Index(indexList[2],result_num_03)

    #使用方法一:走势预测
    result_Funcation_01=Get_Result_Funcation_01(result_index_01,result_index_02,result_index_03)
    #方法二:跨度走势预测
    result_Way=Get_Remove_Way(indexList,args.file_path)
    #方法三:和值走势预测
    result_sum_way=Get_Remove_Sum(indexList,result_num_01,result_num_02,result_num_03)


    ###调用封装的显示方法显示结果###
    Show_Result(indexList, result_Funcation_01)
    Show_Result(indexList,result_Way)
    Show_Result(indexList,result_sum_way)

    pass

if __name__=='__main__':
    #file_dir = r"./work.csv"
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str,default='./data/work_3d.csv',help='csv文件地址')
    args = parser.parse_args()
    main(args)