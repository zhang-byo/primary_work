import scipy
from scipy.stats import chisquare
import numpy as np
import csv

##############################################
#
#   计算卡方检验值，值越大相关性越好
#   注：compute_X函数与python自带的chisquare包，效果一样
#
################################################

def read_excel():

    chrun_prom_0 = [0, 0]
    chrun_prom_1 = [0, 0]
    chrun_posPlanChange_0 = [0, 0]
    chrun_posPlanChange_1 = [0, 0]
    chrun_curPlan_0 = [0, 0, 0, 0]
    chrun_curPlan_1 = [0, 0, 0, 0]
    chrun_call_10086_0 = [0, 0]
    chrun_call_10086_1 = [0, 0]

    chrun_prom_exp_0 = [0, 0]
    chrun_prom_exp_1 = [0, 0]
    chrun_posPlanChange_exp_0 = [0, 0]
    chrun_posPlanChange_exp_1 = [0, 0]
    chrun_curPlan_exp_0 = [0, 0, 0, 0]
    chrun_curPlan_exp_1 = [0, 0, 0, 0]
    chrun_call_10086_exp_0 = [0, 0]
    chrun_call_10086_exp_1 = [0, 0]

    # 分别读取4个变量
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        chrun_prom_0, chrun_prom_1 = count_variable(reader, 13, 2)
        print(chrun_prom_0, chrun_prom_1)
        chrun_prom_exp_0, chrun_prom_exp_1 = expection_value(chrun_prom_0, chrun_prom_1)
        print(chrun_prom_exp_0, chrun_prom_exp_1)
        X = compute_X(chrun_prom_0, chrun_prom_1, chrun_prom_exp_0, chrun_prom_exp_1)
        print(X)
        # print(chisquare([1139, 207, 885, 193], [1123.8877887788778, 222.11221122112212, 911.8019801980198, 180.1980198019802]))
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        chrun_posPlanChange_0, chrun_posPlanChange_1 = count_variable(reader, 17, 2)
        print(chrun_posPlanChange_0, chrun_posPlanChange_1)
        chrun_posPlanChange_exp_0, chrun_posPlanChange_exp_1 = expection_value(chrun_posPlanChange_0, chrun_posPlanChange_1)
        print(chrun_posPlanChange_exp_0, chrun_posPlanChange_exp_1)
        X = compute_X(chrun_posPlanChange_0, chrun_posPlanChange_1, chrun_posPlanChange_exp_0, chrun_posPlanChange_exp_1)
        print(X)

    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        chrun_curPlan_0, chrun_curPlan_1 = count_curPlan(reader, 14, 4)
        print(chrun_curPlan_0, chrun_curPlan_1)
        chrun_curPlan_exp_0, chrun_curPlan_exp_1 = expection_value(chrun_curPlan_0,
                                                                   chrun_curPlan_1)
        print(chrun_curPlan_exp_0, chrun_curPlan_exp_1)
        X = compute_X(chrun_curPlan_0, chrun_curPlan_1, chrun_curPlan_exp_0,
                      chrun_curPlan_exp_1)
        print(X)

    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        chrun_call_10086_0, chrun_call_10086_1 = count_variable(reader, 19, 2)
        print(chrun_call_10086_0, chrun_call_10086_1)
        chrun_call_10086_exp_0, chrun_call_10086_exp_1 = expection_value(chrun_call_10086_0,
                                                                         chrun_call_10086_1)
        print(chrun_call_10086_exp_0, chrun_call_10086_exp_1)
        X = compute_X(chrun_call_10086_0, chrun_call_10086_1, chrun_call_10086_exp_0,
                      chrun_call_10086_exp_1)
        print(X)

def count_variable(reader, location, length):
    """
    用于计算
    :param reader:
    :param location:
    :param length:
    :return:
    """
    chrun_variable_0 = [0 for i in range(length)]
    chrun_variable_1 = [0 for i in range(length)]
    for item in reader:
        if item[1] == '0.0' and item[location] == '0.0':
            chrun_variable_0[0] += 1
        if item[1] == '0.0' and item[location] == '1.0':
            chrun_variable_0[1] += 1
        if item[1] == '1.0' and item[location] == '0.0':
            chrun_variable_1[0] += 1
        if item[1] == '1.0' and item[location] == '1.0':
            chrun_variable_1[1] += 1
    return chrun_variable_0, chrun_variable_1

def count_curPlan(reader, location, length):
    chrun_variable_0 = [0 for i in range(length)]
    chrun_variable_1 = [0 for i in range(length)]
    for item in reader:
        if item[1] == '0.0' and item[location] == '1.0':
            chrun_variable_0[0] += 1
        if item[1] == '0.0' and item[location] == '2.0':
            chrun_variable_0[1] += 1
        if item[1] == '0.0' and item[location] == '3.0':
            chrun_variable_0[2] += 1
        if item[1] == '0.0' and item[location] == '4.0':
            chrun_variable_0[3] += 1
        if item[1] == '1.0' and item[location] == '1.0':
            chrun_variable_1[0] += 1
        if item[1] == '1.0' and item[location] == '2.0':
            chrun_variable_1[1] += 1
        if item[1] == '1.0' and item[location] == '3.0':
            chrun_variable_1[2] += 1
        if item[1] == '1.0' and item[location] == '4.0':
            chrun_variable_1[3] += 1
    return chrun_variable_0, chrun_variable_1

def expection_value(reality_value_0, reality_value_1):
    sum = 0
    ideal_value_0 = []
    ideal_value_1 = []

    for i in reality_value_0:
        sum += i
    for i in reality_value_1:
        sum += i
    chrun_list = []
    variable_list = []
    sum1 = 0
    sum2 = 0
    for i in range(len(reality_value_0)):
        sum1 += reality_value_0[i]
        sum2 += reality_value_1[i]
    chrun_list.append(sum1)
    chrun_list.append(sum2)

    for i in range(len(reality_value_0)):
        variable_list.append(reality_value_0[i] + reality_value_1[i])

    for i in range(len(reality_value_0)):
        ideal_value_0.append(sum1 * variable_list[i] / sum)
        ideal_value_1.append(sum2 * variable_list[i] / sum)

    return ideal_value_0, ideal_value_1

def compute_X(reality_value_0, reality_value_1, ideal_value_0, ideal_value_1):
    return_value = 0
    for i in range(len(reality_value_0)):
        return_value += np.square(reality_value_0[i] - ideal_value_0[i]) / ideal_value_0[i]
        return_value += np.square(reality_value_1[i] - ideal_value_1[i]) / ideal_value_1[i]
    return return_value

if __name__ =='__main__':
    read_excel()