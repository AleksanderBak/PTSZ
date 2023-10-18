import os
import random
import numpy as np

INDEX_NUM = 148208

if __name__ == '__main__':
    instances = [i for i in range(50, 501, 50)]
    #instances = [10, 20, 30]
    lower_bound = 10
    upper_bound = 1000

    if not os.path.isdir("instances"):
        os.mkdir("instances")

    for num in instances:
        jobs = np.round(np.random.beta(0.5, 0.5, num) * (upper_bound - lower_bound) + lower_bound)
        ready_times = [random.randint(lower_bound, upper_bound) for _ in range(num)]

        f = open(f"instances/in_{INDEX_NUM}_{num}.txt", "w")
        f.write(f"{num}\n")
        for p in range(num):
            f.write(f"{int(jobs[p])} {ready_times[p]}\n")

        between_times = [[0 for _ in range(num)] for _ in range(num)]

        for i in range(num):
            for j in range(num):
                a = random.randint(lower_bound, upper_bound)
                b = random.randint(lower_bound, upper_bound)
                if i is not j:
                    if jobs[i] >= jobs[j]:
                        between_times[i][j] = min(a, b)
                        between_times[j][i] = max(a, b)
                    else:
                        between_times[i][j] = max(a, b)
                        between_times[j][i] = min(a, b)

        for i in range(num):
            for j in range(num):
                f.write(f"{between_times[i][j]} ")
            f.write("\n")
        f.close()