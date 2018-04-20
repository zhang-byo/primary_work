import csv

def read_excel():
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        duraion = []
        sum = 0
        chrun_num = 0
        for row in reader:
            if row[6] != 'duration':
                value = int(float(row[6]))
                duraion.append(value)
                if (value > 4 and value <= 10):
                    sum += 1
                    if (row[1] == '1.0'):
                        chrun_num += 1
        print(chrun_num / sum)

        # duraion = sorted(duraion)
        # eq_width(duraion)
def eq_width(duraion):
    print((duraion[len(duraion) - 1] - duraion[0]) / 3)


if __name__ =='__main__':
    read_excel()