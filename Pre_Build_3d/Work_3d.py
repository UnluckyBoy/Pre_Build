# ---************************************************---
# @coding: utf-8
# @Time : 2022/8/12 0012 15:47
# @Author : Matrix
# @File : Work_3d.py
# @Software: PyCharm
# ---************************************************---
import argparse
import random
import pandas as pd

def Get_Index_By_GetIndex_File(file_path):
    with open(file_path,'r',encoding='utf-8') as read_file:
        str_split_2_list=(read_file.read()).split('\n')#str_split_2_list是llist数据类型
        # print(str_split_2_list)
        for i in range(len(str_split_2_list)):
            str_temp=str_split_2_list[i]
            pass
        print("最后一个:",str_temp)
        pass
    pass

def DoForecast_CSV_File(file_path,column):
    """获取csv文件内容并返回
    :param file_path: 文件地址,类型为str
    :param column: 要查询的列数,类型为int
    :return: 返回的list值,result为返回结果list
    """
    file = pd.read_csv(file_path, header=None, encoding='utf-8')
    index = len(file)
    #index=5266
    num=file.iloc[:,column]
    result=[]
    for i in range(index):
        result.append(num[i])
        if i == index - 1:  #检测是否最后一个，是则跳过。
            break
            pass
        pass

    return result
    pass

def GetNext_Index(mIndex,mListIndex):
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

def GetResult_Funcation_01(args):
    """定义储存csv获取到三列数的数组"""
    result_num_01 = DoForecast_CSV_File(args.csv_path, 0)
    result_num_02 = DoForecast_CSV_File(args.csv_path, 1)
    result_num_03 = DoForecast_CSV_File(args.csv_path, 2)
    # print("获取结果:"+"\nresult_num_01:" + str(result_num_01)+"\nresult_num_02:"+str(result_num_02)+"\nresult_num_03:"+str(result_num_03))
    ###此处为方法一使用数据###
    indexList = [7, 5, 3]  # 手动输入上一期数字
    result_index_01 = GetNext_Index(indexList[0], result_num_01)
    result_index_02 = GetNext_Index(indexList[1], result_num_02)
    result_index_03 = GetNext_Index(indexList[2], result_num_03)

    index = GetMin(len(result_index_01), len(result_index_02), len(result_index_03))

    result=[]
    for i in range(index):
        result.append(str(result_index_01[i])+ str(result_index_02[i]) + str(result_index_03[i]))
        pass

    result_Remove_duplicate = Get_Remove_duplicate(result)#去重

    ###调用封装的显示方法显示结果###
    Show_Result(indexList, result_Remove_duplicate)
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

def Show_Result(indexList,result_list):
    str_show = ''
    for i in range(len(result_list)):
        str_show += str(result_list[i]) + " "
        pass
    print(str_show)
    print("数量:", len(result_list))
    print("上一期:" + str(indexList))
    pass

def main(args):
    #GetResult_Funcation_01(args)
    Get_Index_By_GetIndex_File(args.next_path)
    pass

if __name__=='__main__':
    #file_dir = r"./work.csv"
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_path', type=str,default='./data/work_3d.csv',help='csv文件地址')
    parser.add_argument('--next_path', type=str, default='./data/work_3d_GetIndex.txt', help='csv文件地址')
    parser.add_argument('--index_path', type=str, default='./data/work_3d_Index.txt', help='csv文件地址')
    args = parser.parse_args()
    main(args)