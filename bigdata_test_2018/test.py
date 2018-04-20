import csv
import pandas as pd
def read_excel():
    reader = csv.reader(open("telecom_train.csv", "r"))  # 读取csv文件，返回的是迭代类型
    for item in reader:
        if item[1] != 'churn':
            print(22222)
    reader1 = csv.reader(open("telecom_train.csv", "r"))  # 读取csv文件，返回的是迭代类型
    for item in reader1:
        if item[1] != 'churn':
            print(111111)

if __name__ =='__main__':
    read_excel()