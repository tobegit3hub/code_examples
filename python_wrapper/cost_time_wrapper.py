#!/usr/bin/env python

import time


def cost_time(func):
  def wrapper(*args, **kwargs):

    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print("Cost time: {}".format(end_time - start_time))
    return result

  return wrapper


@cost_time
def main():
  for i in range(1000000):
    temp = 100 * 100
  return


if __name__ == "__main__":
  main()
