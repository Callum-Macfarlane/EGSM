import os, re
import numpy as np

if __name__ == '__main__':
    out_path = 'results/csv/filtering'
    os.makedirs(out_path, exist_ok=True)

    for dataset, label in [
        ['gowalla', '16'], ['enron', '16'], ['dblp', '16'],
        ['github', '16'], ['patents', '16'], ['wikitalk', '64']
    ]:
        time_array = np.zeros((100, 2), dtype=float)

        i, algorithm = 0, 'gsi'
        for j in range(100):
            err_file = f'datasets/{dataset}/label_{label}/results/12/{j}_{algorithm}.err'
            log_file = f'datasets/{dataset}/label_{label}/results/12/{j}_{algorithm}.txt'

            if not os.path.exists(log_file):
                log_file = err_file

            with open(log_file) as f:
                full_txt = ''.join(f.readlines())
            match = re.findall('\(\d+, \d+\)\: \d+ (\d+)\: (\d+) (\d+)\: (\d+)', full_txt)
            can_num = {}
            for match_single in match:
                if int(match_single[0]) not in can_num:
                    can_num[int(match_single[0])] = int(match_single[1])
                else:
                    can_num[int(match_single[0])] = max(can_num[int(match_single[0])], int(match_single[1]))
                if int(match_single[2]) not in can_num:
                    can_num[int(match_single[2])] = int(match_single[3])
                else:
                    can_num[int(match_single[2])] = max(can_num[int(match_single[2])], int(match_single[3]))
            time_array[j, i] = sum(list(can_num.values())) * 4

        i, algorithm = 1, 'ours-nof3'
        for j in range(100):
            err_file = f'datasets/{dataset}/label_{label}/results/12/{j}_{algorithm}.err'
            log_file = f'datasets/{dataset}/label_{label}/results/12/{j}_{algorithm}.txt'

            if not os.path.exists(log_file):
                log_file = err_file

            with open(log_file) as f:
                full_txt = ''.join(f.readlines())
            match = re.findall('\(\d+, \d+\)\: (\d+) \d+\: (\d+) \d+\: (\d+)', full_txt)
            size = 0
            for match_single in match:
                size += int(match_single[0])
                size += int(match_single[1]) * 12
                size += int(match_single[2]) * 12
            time_array[j, i] = size * 4

        np.savetxt(f'{out_path}/{dataset}_{label}_filtering_space.csv', time_array, fmt='%12.1f', delimiter=',')
