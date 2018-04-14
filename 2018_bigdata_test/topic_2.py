import csv

def read_excel():
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        edu_class = [row[4] for row in reader]
        print(edu_class)

        # 统计每个key的数量并排序
        num_dic = {}
        for each in edu_class:
            if each in num_dic:
                num_dic[each] += 1
            else:
                num_dic[each] = 1
        num_dic = sorted(num_dic.items(), key=lambda x: x[1], reverse=True)
        print(num_dic)

        # 判断众数是什么
        if num_dic[0][1] == num_dic[len(num_dic) - 1][1]:
            print("没有众数")
        else:
            mode_num_list = []
            max_num = num_dic[0][1]
            for key, value in num_dic:
                if value == max_num:
                    mode_num_list.append(key)
            print(mode_num_list)

if __name__ =='__main__':
    read_excel()