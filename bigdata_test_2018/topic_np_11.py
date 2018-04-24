
from sklearn.metrics import precision_recall_curve
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
import numpy as np
import csv
import pandas as pd

#########################################################
#  其中[1]表示使用卡方检验是相关的
#  1、选取变量——gender(2)[1]、AGE(3)[1](等宽分箱法)、edu_class(4)[1]、
#   incomeCode(5)[1](采用了等宽，K=4)、duration(6)[1](采用了等宽，K=4)、feton(7)[1]、
#    peakMinAv(8)[1](采用了等宽，K=4)、
#    peakMinDiff(9)[1](采用了等宽，K=4)、
# 	posTrend(10)[1]、negTrend(11)[1]、	nrProm(12)[1]、prom(13)[0]、curPlan(14)[1]、
# 	avgplan(15)[1]、planChange(16)[1]、posPlanChange(17)[0]、negPlanChange(18)[0]、call_10086(19)[1]
#  2、使用朴素贝叶斯分类器
#
#
#
###############################################################
def read_train():
    #####################前面处理需要等宽分箱的数据，共5个######################
    #AGE
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        AGE_data = count_box_width_variable(reader, 3)

    #incomeCode
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        incomeCode_data = count_box_width_variable(reader, 5)

    # duration
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        duration_data = count_box_width_variable(reader, 6)

    # peakMinDiff
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        peakMinDiff_data = count_box_width_variable(reader, 8)

    # peakMinAv
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        peakMinAv_data = count_box_width_variable(reader, 9)

    ####################结束###########################################

    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        chrun_y = []
        X = []
        temp_x = []
        for item in reader:
            if item[1] != 'churn':
                temp_x = []
                chrun_y.append(int(float(item[1])))
                temp_x.append(int(float(item[2])))
                temp_x.append(int(float(item[4])))
                temp_x.append(int(float(item[7])))
                temp_x.append(int(float(item[10])))
                temp_x.append(int(float(item[11])))
                temp_x.append(int(float(item[12])))
                temp_x.append(int(float(item[14])))
                temp_x.append(int(float(item[15])))
                temp_x.append(int(float(item[16])) + 3)
                temp_x.append(int(float(item[19])))
                X.append(temp_x)

        #补充加载
        for i in range(len(X)):
            X[i].append(AGE_data[i])
            X[i].append(incomeCode_data[i])
            X[i].append(duration_data[i])
            X[i].append(peakMinDiff_data[i])
            X[i].append(peakMinAv_data[i])

        print(X)
        print(chrun_y)
        return X, chrun_y


def read_test():
    #####################前面处理需要等宽分箱的数据，共5个######################
    # AGE
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        AGE_data = count_box_width_variable(reader, 2)

    # incomeCode
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        incomeCode_data = count_box_width_variable(reader, 4)

    # duration
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        duration_data = count_box_width_variable(reader, 5)

    # peakMinDiff
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        peakMinDiff_data = count_box_width_variable(reader, 7)

    # peakMinAv
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        peakMinAv_data = count_box_width_variable(reader, 8)

    ####################结束###########################################
    with open("telecom_test.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        chrun_y = []
        X = []
        temp_x = []
        id_list = []
        for item in reader:
            if item[1] != 'gender':
                temp_x = []
                id_list.append(int(float(item[0])))
                # chrun_y.append(int(float(item[1])))
                temp_x.append(int(float(item[1])))
                temp_x.append(int(float(item[3])))
                temp_x.append(int(float(item[6])))
                temp_x.append(int(float(item[9])))
                temp_x.append(int(float(item[10])))
                temp_x.append(int(float(item[11])))
                temp_x.append(int(float(item[13])))
                temp_x.append(int(float(item[14])))
                temp_x.append(int(float(item[15])) + 3)
                temp_x.append(int(float(item[18])))
                X.append(temp_x)

        for i in range(len(X)):
            X[i].append(AGE_data[i])
            X[i].append(incomeCode_data[i])
            X[i].append(duration_data[i])
            X[i].append(peakMinDiff_data[i])
            X[i].append(peakMinAv_data[i])
        print(X)
        print(chrun_y)

    return X, chrun_y, id_list

def count_box_width_variable(reader, location):
    k = 4
    chrun_variable_0 = [0 for i in range(k)]
    chrun_variable_1 = [0 for i in range(k)]

    data_churn = []
    data_box_width = []

    for item in reader:
        if item[1] != 'churn':
            data_box_width.append(float(item[location]))
            data_churn.append(int(float(item[1])))
    data_box_width = pd.cut(data_box_width, k, labels=range(k))
    return data_box_width

def naive_bayes(test_x, train_x, test_y, train_y):
    clf = MultinomialNB()
    clf.fit(train_x, train_y)
    doc_class_predicted = clf.predict(test_x)
    print(doc_class_predicted)
    precision, recall, thresholds = precision_recall_curve(test_y, clf.predict(test_x))
    print(f1_score(test_y, clf.predict(test_x)))
    print(precision, recall)
    return doc_class_predicted

def output(predicted, id_list):
    """
    数据写入csv文件
    :param predicted:
    :param id_list:
    :return:
    """
    # with open("predicted.csv", "w") as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer = csv.writer(csvfile)
    #     writer.writerow(['subscriberID', 'prediction'])
    #
    #     data = []
    #     for i in range(len(predicted)):
    #         data.append([id_list[i], predicted[i]])
    #
    #     # data = [
    #     #     ('小河', '25', '1234567'),
    #     #     ('小芳', '18', '789456')
    #     # ]
    #     print(data)
    #
    #     writer.writerows(data)
    #
    # csvfile.close()


    # 字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'subscriberID': id_list, 'prediction': predicted})

    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv("predicted.csv", index=False, sep=',', columns=['subscriberID', 'prediction'])

def main():
    train_x, train_y = read_train()
    test_x, test_y, id_list = read_test()
    # predicted = naive_bayes(test_x, train_x, test_y, train_y)
    predicted = naive_bayes(train_x, train_x, train_y, train_y)
    print(predicted)
    # output(predicted, id_list)

if __name__ == '__main__':
    main()

    # X = [[1, 1, 1, 0], [1, 1, 1, 1], [2, 1, 1, 0], [3, 2, 1, 0], [3, 3, 2, 0]]
    # y = np.array([0, 0, 1, 1, 1])
    # clf = MultinomialNB()
    # clf.fit(X, y)
    # test_x = [[1, 3, 2, 0], [1, 1, 2, 0], [2, 1, 1, 0]]
    # doc_class_predicted = clf.predict(test_x)
    # print(doc_class_predicted)
    # precision, recall, thresholds = precision_recall_curve([1, 0, 1], clf.predict(test_x))
    # print(f1_score([1, 0, 1], clf.predict(test_x)))
    # print(precision, recall)