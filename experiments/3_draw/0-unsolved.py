import os
import numpy as np
import matplotlib.pyplot as plt
from palettable.colorbrewer.qualitative import Dark2_8

color = Dark2_8.mpl_colors

if __name__ == '__main__':
    result_path = 'results/figs'
    os.makedirs(result_path, exist_ok=True)

    fig, axs = plt.subplots(1, 1, figsize=(16.8, 6.0))
    
    axs.bar(np.arange(6) - 0.22, [0,9,10,2,28,2], width=0.22, hatch='\\', color='none', edgecolor=color[0], label='GSI')
    axs.bar(np.arange(6) - 0.00, [21,42,33,35,62,29], width=0.22, hatch='-', color='none', edgecolor=color[3], label='CuTS')
    axs.bar(np.arange(6) + 0.22, [100,100,95,98,100,100], width=0.22, hatch='/', color='none', edgecolor=color[6], label='EGSM')
    #axs.set_yscale('log')

    #axs.set_title(xlabels[i], fontsize=25)
    axs.set_ylabel(f'# solved queries', fontsize=27)
    axs.set_xticks(np.arange(6))
    axs.set_xticklabels(['DBLP', 'Enron', 'Github', 'Gowalla', 'Patents', 'Wikitalk'])
    axs.tick_params(labelsize=27)
    axs.set_ylim(0, 100)

    handles, labels = axs.get_legend_handles_labels()
    fig.legend(handles, labels, facecolor='white', framealpha=0, ncol=10, bbox_to_anchor=(0.5, 1), loc=9, fontsize=27)
    fig.tight_layout(rect=(0,0,1,0.9))
    #fig.legend(framealpha=0, ncol=10, bbox_to_anchor=(0.5, 1), loc=9, fontsize=27)

    fig.savefig(f'{result_path}/0-solved.pdf')
    plt.close()
