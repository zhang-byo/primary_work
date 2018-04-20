
import csv
from bigdata_test_2018 import topic_4
def read_excel():
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        chrun_PlanChange_0 = [0, 1, 6, 1325, 13, 0, 1]
        chrun_PlanChange_1 = [1, 3, 1, 1060, 8, 3, 2]
        chrun_PlanChange_exp_0, chrun_PlanChange_exp_1 = topic_4.expection_value(chrun_PlanChange_0, chrun_PlanChange_1)
        X = topic_4.compute_X(chrun_PlanChange_0, chrun_PlanChange_1, chrun_PlanChange_exp_0,
                              chrun_PlanChange_exp_1)
        print(X)


if __name__ =='__main__':
    read_excel()