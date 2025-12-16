import os, re
import numpy as np

if __name__ == '__main__':
    out_path = 'results/csv/overall'
    os.makedirs(out_path, exist_ok=True)

    for dataset, size in [
        ['enron', '8'], ['enron', '10'], ['enron', '12'],
        ['enron', '14'], ['enron', '16']
    ]:
        algorithms = ['cuts', 'ours']

        time_array = np.zeros((100, 1 + len(algorithms)), dtype=float)

        for i, algorithm in enumerate(algorithms):
            for j in range(100):
                err_file = f'datasets/{dataset}/label_16/results/12/{size}/{j}_{algorithm}.err'
                log_file = f'datasets/{dataset}/label_16/results/12/{size}/{j}_{algorithm}.txt'

                if not os.path.exists(log_file):
                    time_array[j, i + 1] = 3600000
                else:
                    with open(log_file) as f:
                        full_txt = ''.join(f.readlines())
                    match = re.search('# Matches: (\d*)', full_txt)
                    if match:
                        time_array[j, 0] = float(match.group(1))
                    match = re.search(',((?:\d|\.)*)ms,|\(host\) (\d*)\(kernel\)', full_txt)
                    if match:
                        time_array[j, i + 1] = float(match.group(i + 1))

        np.savetxt(f'{out_path}/{dataset}_16_num_results_{size}.csv', time_array, fmt='%d', delimiter=',')
