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

def Get_Index_By_Index_File(file_path):
    """
    #读取file_path文件获取上一期号码
    :param file_path:
    :return:
    """
    with open(file_path,'r',encoding='utf-8') as read_file:
        str_split_2_list=(read_file.read()).split('\n')#str_split_2_list是llist数据类型
        # print(str_split_2_list)
        result = []

        #读取无符号“,”的文件操作,如:652
        for i in range(len(str_split_2_list)):
            str_temp=str_split_2_list[i]#str_temp类型为str
            pass
        # print(str_temp[0]+str_temp[1]+str_temp[2])#打印前三个字符
        for j in range(len(str_temp)):
            # print(str_temp[j])
            result.append(int(str_temp[j]))
            pass

        # 读取有符号“,”的文件操作,如:6,5,2
        # get_str_temp_element=str_temp.split()
        # for j in range(len(get_str_temp_element)):
        #     str_temp_int=int(get_str_temp_element[j])
        #     result.append(str_temp_int)
        #     pass
        # #print("最后一个:",result)

        return result
        pass
    pass

def Get_Next_By_Next_File(file_path):
    with open(file_path,'r',encoding='utf-8') as read_file:
        str_split_2_list = (read_file.read()).split('\n')  # str_split_2_list是llist数据类型
        # print(str_split_2_list)
        next_list=[]
        for i in range(len(str_split_2_list)):
            str_split_2_list_element_temp=[]
            for j in range(3):
                str_split_2_list_element_temp.append(int(str_split_2_list[i].split(',')[j]))#取前三个数
                pass
            # print(str_split_2_list_element_temp)#打印str_split_2_list_element_temp全部元素
            next_list.append(str_split_2_list_element_temp)
            pass
        # print(str_split_2_list_element_temp)#打印str_split_2_list_element_temp最后一个元素
        print(next_list)
        pass
    pass

def Get_Index_Sum(index_list):
    """
    #求list元素和
    :param index_list:
    :return:
    """
    return index_list[0]+index_list[1]+index_list[2]
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

def GetResult_Funcation_01(args,index_list):
    """定义储存csv获取到三列数的数组"""
    result_num_01 = DoForecast_CSV_File(args.csv_path, 0)
    result_num_02 = DoForecast_CSV_File(args.csv_path, 1)
    result_num_03 = DoForecast_CSV_File(args.csv_path, 2)

    ###此处为方法一使用数据###
    # index_list = [7, 5, 3]  # 手动输入上一期数字
    result_index_01 = GetNext_Index(index_list[0], result_num_01)
    result_index_02 = GetNext_Index(index_list[1], result_num_02)
    result_index_03 = GetNext_Index(index_list[2], result_num_03)

    index = GetMin(len(result_index_01), len(result_index_02), len(result_index_03))

    result=[]
    for i in range(index):
        result.append(str(result_index_01[i])+ str(result_index_02[i]) + str(result_index_03[i]))
        pass

    result_Remove_duplicate = Get_Remove_duplicate(result)#去重

    # print(result_Remove_duplicate[0][0]+result_Remove_duplicate[0][1]+result_Remove_duplicate[0][2])
    result_Remove_duplicate_exclude=[]
    for j in range(len(result_Remove_duplicate)):
        # print(result_Remove_duplicate[j])#类型为str
        if result_Remove_duplicate[j][0]=='4' or result_Remove_duplicate[j][0]=='3' or \
                result_Remove_duplicate[j][1]=='4'  or result_Remove_duplicate[j][1]=='3' or \
                result_Remove_duplicate[j][2]=='4'  or result_Remove_duplicate[j][2]=='3':
            # print(result_Remove_duplicate[j])
            result_Remove_duplicate_exclude.append(result_Remove_duplicate[j])
            pass
        pass
    # print(result_Remove_duplicate_exclude)
    #去除不含有特殊数字的结果
    Show_Result_Save(index_list, result_Remove_duplicate_exclude, args.result_exclude_path)

    ###调用封装的显示方法显示结果并保存###
    Show_Result_Save(index_list, result_Remove_duplicate,args.result_path)
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

def Show_Result_Save(index_list,result_list,save_path):
    str_show = ''
    for i in range(len(result_list)):
        str_show += str(result_list[i]) + " "
        pass
    # print(str_show)
    # print("数量:", len(result_list))
    # print("上一期:" + str(index_list))
    count_str="\n数量:"+str(len(result_list))
    index_list_str="\n上一期:" + str(index_list)
    result_save_str=str_show+count_str+index_list_str

    with open(save_path,'w+',encoding='utf-8') as write_file:
        write_file.write(result_save_str)
        pass
    print("保存完毕！***"+format(save_path))
    pass

def Save_CSV_File(file_path,index_list):
    """
    #保存文件
    :param file_path:
    :param index_list:
    :return:
    """
    sum_2_str=str(Get_Index_Sum(index_list))
    index_list_split_element_2_str=str(index_list[0])+","+str(index_list[1])+","+str(index_list[2])
    index_list_2_str=str(index_list[0])+str(index_list[1])+str(index_list[2])
    str_save=index_list_split_element_2_str+","+index_list_2_str+","+sum_2_str
    with open(file_path,'a+',encoding='utf-8') as write_file:
        write_file.write(str_save+"\n")
        pass
    print("保存完毕！"+format(file_path))
    pass


def main(args):
    ##预测专用
    index_list=Get_Index_By_Index_File(args.index_path)
    print("上一期:",index_list)
    GetResult_Funcation_01(args,index_list)#预测下一期结果,在data/work_3d_result.txt处查看
    Save_CSV_File(args.csv_path,index_list)#保存(即更新csv结果池)

    pass

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_path', type=str,default='./data/work_3d.csv',help='csv文件地址')
    parser.add_argument('--next_path', type=str, default='./data/work_3d_GetNext.txt', help='work_3d_GetNext.txt文件地址')
    parser.add_argument('--index_path', type=str, default='./data/work_3d_Index.txt', help='work_3d_Index.txt文件地址')
    parser.add_argument('--result_path', type=str, default='./data/work_3d_result.txt', help='结果work_3d_result.txt文件保存地址')
    parser.add_argument('--result_exclude_path', type=str, default='./data/work_3d_result_exclude.txt',help='结果work_3d_result_exclude.txt文件保存地址')
    parser.add_argument('--test_path', type=str, default='./data/test_index.txt', help='测试文件地址')
    args = parser.parse_args()
    main(args)