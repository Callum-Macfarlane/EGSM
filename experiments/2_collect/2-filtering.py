import os, re
import numpy as np

if __name__ == '__main__':
    out_path = 'results/csv/filtering'
    os.makedirs(out_path, exist_ok=True)

    for dataset, label in [
        ['gowalla', '16'], ['enron', '16'], ['dblp', '16'],
        ['github', '16'], ['patents', '16'], ['wikitalk', '64']
    ]:
        algorithms = ['gsi', 'ours-nof3', 'ours']

        time_array = np.zeros((100, len(algorithms)), dtype=float)

        for i, algorithm in enumerate(algorithms):
            for j in range(100):
                err_file = f'datasets/{dataset}/label_{label}/results/12/{j}_{algorithm}.err'
                log_file = f'datasets/{dataset}/label_{label}/results/12/{j}_{algorithm}.txt'

                if not os.path.exists(log_file):
                    log_file = err_file

                with open(log_file) as f:
                    full_txt = ''.join(f.readlines())
                match = re.findall('\(\d+, \d+\)\: (\d+) ', full_txt)
                time_array[j, i] = np.average(list(map(int, match)))

        np.savetxt(f'{out_path}/{dataset}_{label}_filtering.csv', time_array, fmt='%12.1f', delimiter=',')
