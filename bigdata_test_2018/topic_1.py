import csv

def read_excel():
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        for item in reader:
            if item[5] == '':  #判断incomeCode是否有缺失
                print(item)
            if item[13] == '':  #判断prom是否有缺失
                print(item)

if __name__ =='__main__':
    read_excel()