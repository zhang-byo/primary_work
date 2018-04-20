import csv

def read_excel():
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型

        man_num = 0
        woman_num = 0
        man_lose_num = 0
        woman_lose_num = 0

        for item in reader:
            if item[2] == '0.0':
                woman_num += 1
                if item[1] == '1.0':
                    woman_lose_num += 1
            else:
                man_num += 1
                if item[1] == '1.0':
                    man_lose_num += 1

        print('男性离网率：', man_lose_num / man_num, '\n女性离网率：', woman_lose_num / woman_num)

if __name__ =='__main__':
    read_excel()