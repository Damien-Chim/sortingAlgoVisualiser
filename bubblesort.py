import matplotlib.pyplot as plt
import numpy as np
import random

lst = list(range(1,11))
random.shuffle(lst)
x = np.arange(1, len(lst) + 1, 1)
n = len(lst)
for i in range(n):
    for j in range(n - i -1):
        bars = plt.bar(x, lst)
        bars[j].set_color('red')
        plt.pause(0.0001)
        plt.clf()
        # compare current bar with next bar
        if lst[j] > lst[j + 1]:
            # if current bar is larger than the next bar, swap
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
for i in range(n):
    bars = plt.bar(x ,lst)
    bars[i].set_color('green')
    plt.pause(0.001)
    plt.clf()
plt.bar(x,lst,color="green")
plt.show()







# print(lst)