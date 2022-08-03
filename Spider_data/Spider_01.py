# ---************************************************---
# @coding: utf-8
# @Time : 2022/8/2 0002 22:26
# @Author : Matrix
# @File : Spider_01.py
# @Software: PyCharm
# ---************************************************---
import requests

def GetHtml(htmlUrl,htmlfile):
    # response = requests.get( "http://www.zhihu.com")
    # 设置头部信息,伪装浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    response = requests.get(htmlUrl, headers=headers)  # get方法访问,传入headers参数，
    response.encoding = "utf-8" #设置接收编码格式
    print(response.text)
    with open(htmlfile, 'w',encoding='utf-8') as fp:#若文件为空，则创建，否则直接打开
        fp.write(response.text)
        pass


    pass

def main():
    # keyWord='秒针'
    htmlUrl='https://datachart.500.com/ssq/history/history_same.shtml'
    filePath='./data/html.txt'
    GetHtml(htmlUrl,filePath)
    pass

if __name__=='__main__':
    main()
    pass