import os
import numpy as np

if __name__ == '__main__':
    out_path = 'results/csv'
    os.makedirs(out_path, exist_ok=True)

    for dataset, label in [
        ['dblp', '16'], ['enron', '16'], ['github', '16'],
        ['gowalla', '16'], ['patents', '16'], ['wikitalk', '64']
    ]:
        #algorithms = ['rapidmatch', 'gsi', 'cuts', 'ours']
        algorithms = ['gsi', 'cuts', 'ours']

        unsolved = np.zeros((len(algorithms)), dtype=int)

        for i, algorithm in enumerate(algorithms):
            for j in range(100):
                log_file = f'datasets/{dataset}/label_{label}/results/12/{j}_{algorithm}.txt'

                if os.path.exists(log_file):
                    unsolved[i] += 1

        print(dataset, unsolved)