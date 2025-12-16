import os
import numpy as np
import matplotlib.pyplot as plt
from palettable.colorbrewer.qualitative import Dark2_8

color = Dark2_8.mpl_colors

if __name__ == '__main__':
    result_path = 'results/figs'
    os.makedirs(result_path, exist_ok=True)

    fig, axs = plt.subplots(1, 1, figsize=(8.4, 6.0))
    
    axs.bar(np.arange(5) - 0.16, [9,32,1,42,95], width=0.32, hatch='-', color='none', edgecolor=color[3], label='CuTS')
    axs.bar(np.arange(5) + 0.16, [41,75,69,100,100], width=0.32, hatch='/', color='none', edgecolor=color[6], label='EGSM')
    #axs.set_yscale('log')

    #axs.set_title(xlabels[i], fontsize=25)
    axs.set_ylabel(f'# solved queries', fontsize=27)
    axs.set_xlabel(f'$|\Sigma|$', fontsize=27)
    axs.set_xticks(np.arange(5))
    axs.set_xticklabels(['1', '4', '8', '16', '32'])
    axs.tick_params(labelsize=27)
    axs.set_ylim(0, 100)

    handles, labels = axs.get_legend_handles_labels()
    fig.legend(handles, labels, facecolor='white', framealpha=0, ncol=10, bbox_to_anchor=(0.5, 1), loc=9, fontsize=27)
    fig.tight_layout(rect=(0,0,1,0.9))
    #fig.legend(framealpha=0, ncol=10, bbox_to_anchor=(0.5, 1), loc=9, fontsize=27)

    fig.savefig(f'{result_path}/7-solved.pdf')
    plt.close()
