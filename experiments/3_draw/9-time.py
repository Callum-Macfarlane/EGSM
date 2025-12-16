import os
import numpy as np
import matplotlib.pyplot as plt
from palettable.colorbrewer.qualitative import Dark2_8

color = Dark2_8.mpl_colors

if __name__ == '__main__':
    input_path = 'results/csv/scalability/shape'

    result_path = 'results/figs'
    os.makedirs(result_path, exist_ok=True)

    time_1 = np.loadtxt(f'{input_path}/enron_8-path_overall.csv', delimiter=',')
    time_4 = np.loadtxt(f'{input_path}/enron_8-tree_overall.csv', delimiter=',')
    time_8 = np.loadtxt(f'{input_path}/enron_12_overall.csv', delimiter=',')
    time_16 = np.loadtxt(f'{input_path}/enron_8-cycle_overall.csv', delimiter=',')
    time_32 = np.loadtxt(f'{input_path}/enron_8-dense_overall.csv', delimiter=',')

    time_1 = time_1[np.max(time_1, axis=1) < 3599999]
    time_4 = time_4[np.max(time_4, axis=1) < 3599999]
    time_8 = time_8[np.max(time_8, axis=1) < 3599999]
    time_16 = time_16[np.max(time_16, axis=1) < 3599999]
    time_32 = time_32[np.max(time_32, axis=1) < 3599999]

    cuts_time = [
        np.average(time_1, axis=0)[0],
        np.average(time_4, axis=0)[0],
        np.average(time_8, axis=0)[0],
        np.average(time_16, axis=0)[0],
        np.average(time_32, axis=0)[0]
    ]

    ours_time = [
        np.average(time_1, axis=0)[1],
        np.average(time_4, axis=0)[1],
        np.average(time_8, axis=0)[1],
        np.average(time_16, axis=0)[1],
        np.average(time_32, axis=0)[1]
    ]
    fig, axs = plt.subplots(1, 1, figsize=(8.4, 6.0))
    
    axs.bar(np.arange(5) - 0.16, cuts_time, width=0.32, hatch='-', color='none', edgecolor=color[3], label='CuTS')
    axs.bar(np.arange(5) + 0.16, ours_time, width=0.32, hatch='/', color='none', edgecolor=color[6], label='EGSM')
    axs.set_yscale('log')

    #axs.set_title(xlabels[i], fontsize=25)
    axs.set_ylabel(f'Query time (ms)', fontsize=27)
    #axs.set_xlabel(f'Shapes', fontsize=27)
    axs.set_xticks(np.arange(5))
    axs.set_xticklabels(['Path', 'Tree', 'Sparse', 'Cycle', 'Dense'])
    axs.set_yticks([1,10,100,1000,10000,100000])
    axs.set_yticklabels(['$10^0$','$10^1$','$10^2$','$10^3$','$10^4$','$10^5$'])
    axs.tick_params(labelsize=27)
    axs.set_ylim(1, 100000)

    handles, labels = axs.get_legend_handles_labels()
    fig.legend(handles, labels, facecolor='white', framealpha=0, ncol=10, bbox_to_anchor=(0.5, 1), loc=9, fontsize=27)
    fig.tight_layout(rect=(0,0,1,0.9))

    fig.savefig(f'{result_path}/9-time.pdf')
    plt.close()
    print(cuts_time)
    print(ours_time)
