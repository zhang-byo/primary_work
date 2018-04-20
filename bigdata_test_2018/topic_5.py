import csv

def read_excel():
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        sum = 0
        for item in reader:
            if item[7] == '1.0' and item[19] == '1.0':  #判断incomeCode是否有缺失
                sum += 1
        print(sum)

if __name__ =='__main__':
    read_excel()