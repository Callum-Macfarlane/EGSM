import os, re
import numpy as np

if __name__ == '__main__':
    out_path = 'results/csv/scalability/nlabels'
    os.makedirs(out_path, exist_ok=True)

    dataset = 'enron'
    for label, size in [
        ['1', '6'], ['4', '8'], ['8', '12'], ['16', '12'], ['32', '12']
    ]:
        algorithms = ['cuts', 'ours']

        time_array = np.zeros((100, len(algorithms)), dtype=float)

        for i, algorithm in enumerate(algorithms):
            for j in range(100):
                err_file = f'datasets/{dataset}/label_{label}/results/12/{size}/{j}_{algorithm}.err'
                log_file = f'datasets/{dataset}/label_{label}/results/12/{size}/{j}_{algorithm}.txt'

                if not os.path.exists(log_file):
                    time_array[j, i] = 3600000
                else:
                    with open(log_file) as f:
                        full_txt = ''.join(f.readlines())
                    match = re.search(',((?:\d|\.)*)ms,|\(host\) (\d*)\(kernel\)', full_txt)
                    #match = re.search(',((?:\d|\.)*)ms,|\(host\) (\d*)\(kernel\)', full_txt)
                    if match:
                        time_array[j, i] = float(match.group(i + 1))

        np.savetxt(f'{out_path}/{dataset}_{label}_overall.csv', time_array, fmt='%12.1f', delimiter=',')
