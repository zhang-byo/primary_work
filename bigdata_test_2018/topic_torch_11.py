import csv

import torch
from sklearn.metrics import f1_score
from torch.autograd import Variable
import torch.nn.functional as F

class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)   # hidden layer
        self.hidden2 = torch.nn.Linear(n_hidden, n_hidden * 2)  # hidden layer
        self.out = torch.nn.Linear(n_hidden * 2, n_output)   # output layer

    def forward(self, x):
        x = F.relu(self.hidden(x))      # activation function for hidden layer
        x = F.relu(self.hidden2(x))  # activation function for hidden layer
        x = self.out(x)
        return x

def get_data():
    x_data = []
    y_data = []
    with open("telecom_train.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # 读取csv文件，返回的是迭代类型
        for item in reader:
            if item[0] != 'subscriberID':
                temp_data = []
                for i in range(2, 20):
                    temp_data.append(float(item[i]))
                y_data.append(int(float(item[1])))
                x_data.append(temp_data)
    return x_data, y_data

def main():
    x, y = get_data()
    x = torch.FloatTensor(x)
    y = torch.LongTensor(y)

    x, y = Variable(x), Variable(y)
    net = Net(n_feature=18, n_hidden=10, n_output=2)  # define the network
    print(net)  # net architecture

    optimizer = torch.optim.SGD(net.parameters(), lr=0.02)
    loss_func = torch.nn.CrossEntropyLoss()  # the target label is NOT an one-hotted

    for t in range(2000):
        out = net(x)  # input x and predict based on x
        loss = loss_func(out, y)  # must be (1. nn output, 2. target), the target label is NOT one-hotted

        optimizer.zero_grad()  # clear gradients for next train
        loss.backward()  # backpropagation, compute gradients
        optimizer.step()  # apply gradients

    prediction = torch.max(F.softmax(out), 1)[1]
    pred_y = prediction.data.numpy().squeeze()
    target_y = y.data.numpy()
    print(target_y)
    print(pred_y)
    sum = 0

    for i in range(len(target_y)):
        if target_y[i] == pred_y[i]:
            sum += 1
    print(sum, len(target_y))
    print(f1_score(target_y, pred_y))

if __name__ =='__main__':
    main()