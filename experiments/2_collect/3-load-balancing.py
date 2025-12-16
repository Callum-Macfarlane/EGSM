import os, re
import numpy as np

if __name__ == '__main__':
    out_path = 'results/csv/ablation'
    os.makedirs(out_path, exist_ok=True)

    for dataset, label in [
        ['gowalla', '16'], ['enron', '16'], ['dblp', '16'],
        ['github', '16'], ['patents', '16'], ['wikitalk', '64']
    ]:
        algorithms = ['ours-nolb', 'ours']

        time_array = np.zeros((100, len(algorithms)), dtype=float)

        for i, algorithm in enumerate(algorithms):
            for j in range(100):
                log_file = f'datasets/{dataset}/label_{label}/results/12/{j}_{algorithm}.txt'

                if not os.path.exists(log_file):
                    time_array[j, i] = 3600000
                else:
                    with open(log_file) as f:
                        full_txt = ''.join(f.readlines())
                    match = re.search('\(host\) (\d*)\(kernel\)', full_txt)
                    if match:
                        time_array[j, i] = float(match.group(1))

        np.savetxt(f'{out_path}/{dataset}_{label}_lb.csv', time_array, fmt='%12.1f', delimiter=',')
