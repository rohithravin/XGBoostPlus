import numpy as np

def metrics(y_valid, y_predict):

    # compute number of true positives

    tp = np.sum((y_valid == +1) * (y_predict == +1))
    fp = np.sum((y_valid == 0) * (y_predict == +1))
    fn = np.sum((y_valid == +1) * (y_predict == 0))
    tn = np.sum((y_valid == 0) * (y_predict == 0))
    # compute recall
    recall = tp / (tp + fn)

    if tp == 0 and fp == 0 and fn == 0:
        precision = 1
        recall = 1
        f1 = 1
    elif tp == 0:
        precision = 0
        recall = 0
        f1 = 0
    else :
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        # compute f1 score
        f1 = 2 / (recall ** -1 + precision ** -1)

    # compute specificity
    specificity = tn / (tn + fp)

    # compute g mean
    g_mean = np.sqrt(specificity * recall)

    acc = (tp+ tn) / len(y_valid)

    return recall, precision, specificity, f1, g_mean, acc
