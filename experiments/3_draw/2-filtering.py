import os
import numpy as np
import matplotlib.pyplot as plt
from palettable.colorbrewer.qualitative import Dark2_8

color = Dark2_8.mpl_colors

if __name__ == '__main__':
    input_path = 'results/csv'

    result_path = 'results/figs'
    os.makedirs(result_path, exist_ok=True)

    time_dblp = np.loadtxt(f'{input_path}/filtering/dblp_16_filtering.csv', delimiter=',')
    time_enron = np.loadtxt(f'{input_path}/filtering/enron_16_filtering.csv', delimiter=',')
    time_github = np.loadtxt(f'{input_path}/filtering/github_16_filtering.csv', delimiter=',')
    time_gowalla = np.loadtxt(f'{input_path}/filtering/gowalla_16_filtering.csv', delimiter=',')
    time_patents = np.loadtxt(f'{input_path}/filtering/patents_16_filtering.csv', delimiter=',')
    time_wikitalk = np.loadtxt(f'{input_path}/filtering/wikitalk_64_filtering.csv', delimiter=',')

    gsi = [
        np.average(time_dblp, axis=0)[0],
        np.average(time_enron, axis=0)[0],
        np.average(time_github, axis=0)[0],
        np.average(time_gowalla, axis=0)[0],
        np.average(time_patents, axis=0)[0],
        np.average(time_wikitalk, axis=0)[0]
    ]

    ours_no3 = [
        np.average(time_dblp, axis=0)[1],
        np.average(time_enron, axis=0)[1],
        np.average(time_github, axis=0)[1],
        np.average(time_gowalla, axis=0)[1],
        np.average(time_patents, axis=0)[1],
        np.average(time_wikitalk, axis=0)[1]
    ]

    ours = [
        np.average(time_dblp, axis=0)[2],
        np.average(time_enron, axis=0)[2],
        np.average(time_github, axis=0)[2],
        np.average(time_gowalla, axis=0)[2],
        np.average(time_patents, axis=0)[2],
        np.average(time_wikitalk, axis=0)[2]
    ]

    individual_speedup = [
        np.average(time_dblp[:,0] / time_dblp[:,1]),
        np.average(time_enron[:,0] / time_enron[:,1]),
        np.average(time_github[:,0] / time_github[:,1]),
        np.average(time_gowalla[:,0] / time_gowalla[:,1]),
        np.average(time_patents[:,0] / time_patents[:,1]),
        np.average(time_wikitalk[:,0] / time_wikitalk[:,1])
    ]
    fig, axs = plt.subplots(1, 1, figsize=(8.4, 6.0))
    
    axs.bar(np.arange(6) - 0.24, gsi, width=0.24, hatch='\\', color='none', edgecolor=color[0], label='GSI')
    axs.bar(np.arange(6) - 0.00, ours_no3, width=0.24, hatch='.', color='none', edgecolor=color[3], label='NoF3')
    axs.bar(np.arange(6) + 0.24, ours, width=0.24, hatch='/', color='none', edgecolor=color[6], label='EGSM')
    axs.set_yscale('log')

    #axs.set_title(xlabels[i], fontsize=25)
    axs.set_ylabel(f'# Candidate edges', fontsize=27)
    axs.set_xticks(np.arange(6))
    axs.set_xticklabels(['DBLP', 'Enron', 'Github', 'Gowalla', 'Patents', 'Wikitalk'], rotation = 24)
    axs.tick_params(labelsize=27)
    axs.set_ylim(1, 800000)

    #handles, labels = axs.get_legend_handles_labels()
    #fig.legend(handles, labels, facecolor='white', framealpha=0, ncol=10, bbox_to_anchor=(0.5, 1), loc=9, fontsize=27)
    #fig.tight_layout(rect=(0,0,1,0.9))
    axs.legend(facecolor='white', framealpha=0, ncol=2, loc=2, fontsize=27)
    fig.tight_layout()

    fig.savefig(f'{result_path}/2-filtering.pdf')
    plt.close()
    print('individual_speedup', individual_speedup)
    print('average_speedup', [a / b for a, b in zip(gsi,ours)])
