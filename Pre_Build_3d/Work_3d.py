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
from Pre_Remove_Hundred_Ten_One_Bit import BySum_Remove_Hundred_Bit, BySum_Remove_Ten_Bit, BySum_Remove_One_Bit, \
    Remove_Hundred_Ten_One


#################################################读取文件取数模块##########################################################
def Get_Index_By_Index_File(file_path):
    """
    #读取file_path文件获取上一期号码
    :param file_path:
    :return:返回数据类型[int,int,int]---[2,8,2]
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
def Get_Base_File(file_path):
    """
    #读取文件file_path获取大底
    :param file_path:
    :return:返回数据类型list为:['str','str']---['282','584']
    """
    with open(file_path,'r',encoding='utf-8') as base_read:
        read_file=base_read.read().split('\n')
        pass
    # print(read_file, "\n", type(read_file))#list
    str_read_file=''
    for i in range(len(read_file)):
        str_read_file+=read_file[i]+" "#str
        pass
    # print(str_read_file,"\n",type(str_read_file))
    str_read_file_list=str_read_file.split(' ')#list
    # print(str_read_file_list,"\n",type(str_read_file_list))

    return str_read_file_list
    pass
#################################################读取文件取数模块##########################################################

#################################################数据操作方法模块##########################################################
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
def Get_Index_Sum(index_list):
    """
    #求list元素和
    :param index_list:
    :return:
    """
    return index_list[0]+index_list[1]+index_list[2]
    pass
def Get_Index_Sum_End(index_list):
    """
    #和值尾数取10的余数计算
    :param index:
    :return:
    """
    sum = (int(index_list[0]) + int(index_list[1]) + int(index_list[2]))% 10
    return sum
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
def Get_Result_Exclude(num_list,exclude):
    """
    #定胆方法函数
    :param num_list:
    :return:
    """
    exclude_key=str(exclude)
    result_Remove_exclude = []
    for i in range(len(num_list)):
        # print(result_Remove_duplicate[j])#类型为str
        #########################定胆(单胆)##########################
        if num_list[i][0] == exclude_key or num_list[i][1] == exclude_key or num_list[i][2] == exclude_key:
            # print(result_Remove_duplicate[j])
            result_Remove_exclude.append(num_list[i])
            pass
        pass
    return result_Remove_exclude
    pass
#################################################数据操作方法模块##########################################################

#################################################保存数据方法模块##########################################################
def Show_Result_Save(str_title,index_list,result_list,save_path):
    """
    #保存结果文件
    :param index_list:
    :param result_list:
    :param save_path:
    :return:
    """
    str_show = ''
    for i in range(len(result_list)):
        str_show += str(result_list[i]) + " "
        pass
    # print(str_show)
    # print("数量:", len(result_list))
    # print("上一期:" + str(index_list))
    count_str="\n数量:"+str(len(result_list))
    index_list_str="\n上一期:" + str(index_list)
    result_save_str=str_title+"\n"+str_show+count_str+index_list_str

    with open(save_path,'w+',encoding='utf-8') as write_file:
        write_file.write(result_save_str)
        pass
    print("保存完毕！***"+format(save_path))
    pass
def Save_CSV_File(file_path,index_list):
    """
    #保存CSV文件
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
#################################################保存数据方法模块##########################################################

#################################################显示数据方法模块##########################################################
def Show_Result(index_list,result_list):
    """
    #保存结果文件
    :param index_list:
    :param result_list:
    :param save_path:
    :return:
    """
    str_show = ''
    for i in range(len(result_list)):
        str_show += str(result_list[i]) + " "
        pass
    print(str_show)
    print("数量:", len(result_list))
    print("上一期:" + str(index_list))
    pass
#################################################显示数据方法模块##########################################################

#################################################调用预测方法模块##########################################################
def Get_Result_Funcation_01(args,index_list,exclude):
    """定义储存csv获取到三列数的数组"""
    result_num_01 = DoForecast_CSV_File(args.csv_path, 0)
    result_num_02 = DoForecast_CSV_File(args.csv_path, 1)
    result_num_03 = DoForecast_CSV_File(args.csv_path, 2)

    ###此处为方法一使用数据###
    # index_list = [7, 5, 3]  # 手动输入上一期数字
    result_index_01 = Get_Next_Index(index_list[0], result_num_01)
    result_index_02 = Get_Next_Index(index_list[1], result_num_02)
    result_index_03 = Get_Next_Index(index_list[2], result_num_03)

    index = GetMin(len(result_index_01), len(result_index_02), len(result_index_03))

    result=[]
    for i in range(index):
        result.append(str(result_index_01[i])+ str(result_index_02[i]) + str(result_index_03[i]))
        pass

    result_remove_duplicate = Get_Remove_duplicate(result)#去重

    result_remove_duplicate_exclude=Get_Result_Exclude(result_remove_duplicate,exclude)#调用定胆函数计算，4为胆

    ###################筛选特殊数字的结果(即定胆)并保存#####################
    str_funcation_01_exclude="*******************历史池走势定胆方法*******************"
    Show_Result_Save(str_funcation_01_exclude,index_list, result_remove_duplicate_exclude, args.result_exclude_path)

    #######################调用封装的显示方法显示结果并保存######################
    str_funcation_01 = "*******************历史池走势不定胆方法*******************"
    Show_Result_Save(str_funcation_01,index_list, result_remove_duplicate,args.result_path)
    pass
def Get_Result_Funcation_02(args,index_list,exclude):
    """
    #大底定胆,去除个十百位
    #和尾加减2(偶数+2，奇数-2)去百位
    #和尾*3，取尾去十位
    #和尾*3+3，取尾去个位
    :param num_list_re_one:
    :return:
    """
    num_list = Get_Base_File(args.base_path)#获取大底
    sum_end = Get_Index_Sum_End(index_list)#获取和尾

    num_list_re_hundred = BySum_Remove_Hundred_Bit(num_list, sum_end)  # 去除百位
    # print('num_list_re_hundred:\n', num_list_re_hundred)
    num_list_re_ten = BySum_Remove_Ten_Bit(num_list_re_hundred, sum_end)  # 去除十位
    # print('num_list_re_ten:\n', num_list_re_ten)
    num_list_re_one = BySum_Remove_One_Bit(num_list_re_ten, sum_end)  # 去除个位
    # print('num_list_re_one:\n', num_list_re_one, '\n数量:', len(num_list_re_one))

    result_list_exclude=Get_Result_Exclude(num_list_re_one,exclude)
    # print("********************大底定胆方法********************")
    # Show_Result(index_list,result_list_exclude)
    str_funcation_02_exclude = "***大底去个(和尾*3+3，取尾去个位)十(和尾*3，取尾去十位)百(和尾加减2(偶数+2，奇数-2)去百位)位定胆方法***"
    Show_Result_Save(str_funcation_02_exclude,index_list,result_list_exclude,args.base_result_exclude_path)
    pass
def Get_Result_Funcation_03(args,index_list,hundred,ten,one,exclude):
    # print("********************大底定胆方法********************")
    num_list = Get_Base_File(args.base_path)  # 获取大底
    num_list_remove=Remove_Hundred_Ten_One(num_list,hundred,ten,one)
    result_list_exclude=Get_Result_Exclude(num_list_remove,exclude)
    Show_Result(index_list, result_list_exclude)

    result_list_exclude_remevo=Remove_Hundred_Ten_One(result_list_exclude,1,5,6)#重新调用一次筛选个十百位数
    # Show_Result(index_list, result_list_exclude_remevo)
    str_funcation_03_exclude = "*******************大底直接去个十百位定胆方法*******************"
    Show_Result_Save(str_funcation_03_exclude,index_list, result_list_exclude_remevo,args.base_result_exclude_remove)
    pass
#################################################调用预测方法模块##########################################################

#################################################测试正确率模块###########################################################

#################################################测试正确率模块###########################################################

def main(args):
    # ##预测结果
    index_list=Get_Index_By_Index_File(args.index_path)
    # print("上一期:",index_list)
    exclude_key=7#定胆数
    hundred_key=4#百位筛选键值
    ten_key=1#十位筛选键值
    one_key=4#个位筛选键值

    Get_Result_Funcation_02(args,index_list,exclude_key)#调用大底定胆方法
    Get_Result_Funcation_03(args, index_list, hundred_key, ten_key, one_key, exclude_key)

    Get_Result_Funcation_01(args,index_list,exclude_key)#预测下一期结果,在data/work_3d_result.txt处查看
    #Save_CSV_File(args.csv_path,index_list)#保存(即更新csv结果池),该方法只运行一次

    pass

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_path', type=str,default='./data/work_3d.csv',help='csv文件地址')
    parser.add_argument('--next_path', type=str, default='./data/work_3d_GetNext.txt', help='work_3d_GetNext.txt文件地址')
    parser.add_argument('--index_path', type=str, default='./data/work_3d_Index.txt', help='work_3d_Index.txt文件地址')
    parser.add_argument('--result_path', type=str, default='./data/work_3d_result.txt', help='结果work_3d_result.txt文件保存地址')
    parser.add_argument('--result_exclude_path', type=str, default='./data/work_3d_result_exclude.txt',
                        help='定胆结果work_3d_result_exclude.txt文件保存地址')
    parser.add_argument('--base_result_exclude_path', type=str, default='./data/work_3d_base_result_exclude.txt',
                        help='大底定胆结果work_3d_base_result_exclude.txt文件地址')
    parser.add_argument('--base_result_exclude_remove', type=str, default='./data/work_3d_base_result_exclude_remove.txt',
                        help='大底定胆结果work_3d_base_result_exclude_remove.txt文件地址')
    parser.add_argument('--base_path', type=str, default='./data/base_Index.txt', help='测试文件地址')
    args = parser.parse_args()
    main(args)