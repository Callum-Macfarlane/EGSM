import os
import numpy as np
import matplotlib.pyplot as plt
from palettable.colorbrewer.qualitative import Dark2_8

color = Dark2_8.mpl_colors

if __name__ == '__main__':
    input_path = 'results/csv/overall'

    result_path = 'results/figs'
    os.makedirs(result_path, exist_ok=True)

    time_8 = np.loadtxt(f'{input_path}/enron_16_num_results_8.csv', delimiter=',')
    time_10 = np.loadtxt(f'{input_path}/enron_16_num_results_10.csv', delimiter=',')
    time_12 = np.loadtxt(f'{input_path}/enron_16_num_results_12.csv', delimiter=',')
    time_14 = np.loadtxt(f'{input_path}/enron_16_num_results_14.csv', delimiter=',')
    time_16 = np.loadtxt(f'{input_path}/enron_16_num_results_16.csv', delimiter=',')

    time_8 = time_8[time_8[:,0] > 0]
    time_10 = time_10[time_10[:,0] > 0]
    time_12 = time_12[time_12[:,0] > 0]
    time_14 = time_14[time_14[:,0] > 0]
    time_16 = time_16[time_16[:,0] > 0]

    time_8[time_8[:,2] == 0, 2] = 1
    time_10[time_10[:,2] == 0, 2] = 1
    time_12[time_12[:,2] == 0, 2] = 1
    time_14[time_14[:,2] == 0, 2] = 1
    time_16[time_16[:,2] == 0, 2] = 1

    time_8 = time_8[time_8[:,2] < 3599999]
    time_10 = time_10[time_10[:,2] < 3599999]
    time_12 = time_12[time_12[:,2] < 3599999]
    time_14 = time_14[time_14[:,2] < 3599999]
    time_16 = time_16[time_16[:,2] < 3599999]

    time_all = np.vstack((time_8, time_10, time_12, time_14, time_16))

    time_all = np.array(sorted(time_all, key=lambda x:x[0]))[40:]
    time_all = np.hstack((np.arange(time_all.shape[0]).reshape((-1,1)), time_all))
    cuts_solved = time_all[time_all[:,2] < 3599999]
    cuts_unsolved = time_all[time_all[:,2] > 3599999]
    cuts_unsolved[:,2] = 6000000
    fig, axs = plt.subplots(1, 1, figsize=(16.8, 6.0))
    
    axs.scatter(cuts_solved[:,0], cuts_solved[:,2], color=color[1], facecolor='none', marker='v', s=120, label='CuTS')
    axs.scatter(cuts_unsolved[:,0], cuts_unsolved[:,2], color='none', facecolor=color[3], marker='x', s=150)
    axs.plot(time_all[:,0], time_all[:,3], color=color[2], label='EGSM')
    #axs.axhline(y=3600000, color='k', linestyle='--', alpha=0.5)
    axs.set_yscale('log')

    #axs.set_title(xlabels[i], fontsize=25)
    axs.set_ylabel(f'Query time (ms)', fontsize=27)
    axs.set_yticks([10**0, 10**2, 10**4, 10**6])
    axs.set_yticklabels(['$10^0$', '$10^2$', '$10^4$', '$10^6$'])
    #axs.set_xticklabels(['DBLP', 'Enron', 'Github', 'Gowalla', 'Patents', 'Wikitalk'])
    axs.tick_params(labelsize=27)
    axs.set_xlabel('Query ID', fontsize=27)
    axs.set_ylim(1, 10000000)
    axs.set_xlim(0, 408)
    axs.grid()

    handles, labels = axs.get_legend_handles_labels()
    plt.legend(handles, labels, facecolor='white', framealpha=0, ncol=10, loc='lower right', fontsize=27)
    fig.tight_layout()

    fig.savefig(f'{result_path}/10-overall-num-results.pdf')
    plt.close()
