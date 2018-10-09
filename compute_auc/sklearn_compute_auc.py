#!/usr/bin/env python

import numpy as np
from sklearn import metrics


def main():

  label_list = np.array([0, 0, 1, 1])
  prediction_list = np.array([0.1, 0.4, 0.35, 0.8])

  fpr, tpr, thresholds = metrics.roc_curve(
      label_list, prediction_list, pos_label=1)

  auc = metrics.auc(fpr, tpr)
  print("Auc: {}".format(auc))


if __name__ == "__main__":
  main()
