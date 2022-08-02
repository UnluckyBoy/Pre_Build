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

def Get_Read_File_Index(file_path):
    # 通过读取文件调用检测正确率
    file = pd.read_csv(file_path, header=None, encoding='utf-8')
    index_len = len(file)
    result_file_list = []
    for i in range(index_len):
        str = []
        for j in range(3):
            str.append(file[j][i])
            pass
        result_file_list.append(str)
        if i == index_len - 1:  # 检测是否最后一个，是则跳过。
            break
            pass
        pass

    return result_file_list
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

def GetResult_Funcation_01(list_01,list_02,list_03):
    """
    #将list_01,list_02,list_03中的单元素组合成一个list元素
    :param list_01:
    :param list_02:
    :param list_03:
    :return: 返回组合完成后且去重的list
    """
    index = GetMin(len(list_01), len(list_02), len(list_03))

    result=[]
    result_Remove_duplicate=[]
    for i in range(index):
        result.append(str(list_01[i])+ str(list_02[i]) + str(list_03[i]))
        pass

    """
    #去重list中重复项
    """
    for x in result:
        if x not in result_Remove_duplicate:
            result_Remove_duplicate.append(x)
        pass

    #print("下一次可能出现的结果:\n" + str(result))
    #print("下一次可能出现的结果(去重后):\n" + str(result_Remove_duplicate))
    #print("总可能数:" + str(len(result))+"\n去重后总可能数:"+str(len(result_Remove_duplicate)))
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
    print("下一次可能出现的结果:")
    for i in range(len(result_list)):
        print(result_list[i])
        pass
    print("总可能数量:" + str(len(result_list)))
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

def main(args):
    indexList = [1,5,1]  # 上一期数字
    """定义储存csv获取到三列数的数组"""
    result_num_01 =DoForecast(args.file_path,0)
    result_num_02 =DoForecast(args.file_path,1)
    result_num_03 =DoForecast(args.file_path,2)
    #print("获取结果:"+"\nresult_num_01:" + str(result_num_01)+"\nresult_num_02:"+str(result_num_02)+"\nresult_num_03:"+str(result_num_03))

    """
    ###此处为方法一使用数据###
    """
    result_index_01=GetNext_Index(indexList[0],result_num_01)
    result_index_02=GetNext_Index(indexList[1],result_num_02)
    result_index_03=GetNext_Index(indexList[2],result_num_03)
    #使用方法一预测
    result_Funcation_01=GetResult_Funcation_01(result_index_01,result_index_02,result_index_03)
    ###调用封装的显示方法显示结果###
    Show_Result(indexList,result_Funcation_01)

    ###使用方法二###
    #GetResult_Funcation_02(args.file_path, 3)

    pass

if __name__=='__main__':
    #file_dir = r"./work.csv"
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str,default='./data/3_min_3d_data.csv',help='csv文件地址')
    args = parser.parse_args()
    main(args)