
def recall(model):
    return model[1][1] / (model[1][0] + model[1][1])
def precision(model):
    return model[1][1] / (model[1][1] + model[0][1])

def f_measure(model):
    recall_v = recall(model)
    precision_v = precision(model)
    return 2 * recall_v * precision_v / (recall_v + precision_v)
def main():
    model1 = [[1286, 60],[432,646]]
    model2 = [[1264, 82],[294,784]]
    print('model1 recall:{:6.3f} model2 recall:{:6.3f}'.format(recall(model1), recall(model2)))
    print('model1 precision:{:6.3f} model2 precision:{:6.3f}'.format(precision(model1), precision(model2)))
    print('model1 f_measure:{:6.3f} model2 f_measure:{:6.3f}'.format(f_measure(model1), f_measure(model2)))


if __name__ == '__main__':
    main()