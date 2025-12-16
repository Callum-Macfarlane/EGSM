import os
import numpy as np

if __name__ == '__main__':
    out_path = 'results/csv/scalability/qsize'
    os.makedirs(out_path, exist_ok=True)

    dataset, label = 'enron', 16
    for size in [8, 10, 12, 14, 16]:
        algorithms = ['cuts', 'ours']

        unsolved = np.zeros((len(algorithms)), dtype=int)

        for i, algorithm in enumerate(algorithms):
            for j in range(100):
                err_file = f'datasets/{dataset}/label_{label}/results/12/{size}/{j}_{algorithm}.err'
                log_file = f'datasets/{dataset}/label_{label}/results/12/{size}/{j}_{algorithm}.txt'

                if os.path.exists(log_file):
                    unsolved[i] += 1

        print(dataset, unsolved)