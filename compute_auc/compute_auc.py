#!/usr/bin/env python
# -*- coding=utf-8 -*-

import random
import numpy as np
import time
from sklearn import metrics


def compute_auc(label_list, prediction_list):

  # Get number of positive and negative instances
  instance_number = len(label_list)
  positive_label_number = sum(label_list)
  negative_label_number = instance_number - positive_label_number

  # Generate rank list for positive instances
  label_prediction_pair_list = zip(label_list, prediction_list)
  label_prediction_pair_list = sorted(
      label_prediction_pair_list, key=lambda x: x[1])
  positive_rank_list = [
      i + 1 for i in range(instance_number)
      if label_prediction_pair_list[i][0] == 1
  ]

  # Refer to https://zhuanlan.zhihu.com/p/33407505
  # auc = (accumulated(positive_rank_list) - M * (M+1)) / 2 / (M * N)
  auc = (sum(positive_rank_list) -
         (positive_label_number * (positive_label_number + 1)) / 2.0) / (
             positive_label_number * negative_label_number)

  return auc


def verfiy_auc(label_list, prediction_list):

  label_list = np.array(label_list)
  prediction_list = np.array(prediction_list)

  fpr, tpr, thresholds = metrics.roc_curve(
      label_list, prediction_list, pos_label=1)
  auc = metrics.auc(fpr, tpr)
  return auc


if __name__ == "__main__":
  instance_number = 10000
  label_list = [random.randint(0, 1) for i in range(instance_number)]
  prediction_list = [random.random() for i in range(instance_number)]

  auc = compute_auc(label_list, prediction_list)
  print("Auc: {}".format(auc))

  auc = verfiy_auc(label_list, prediction_list)
  print("Auc from scikit-learn: {}".format(auc))
