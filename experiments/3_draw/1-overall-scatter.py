import os
import numpy as np
import matplotlib.pyplot as plt
from palettable.colorbrewer.qualitative import Dark2_8

color = Dark2_8.mpl_colors

if __name__ == '__main__':
    input_path = 'results/csv'

    result_path = 'results/figs'
    os.makedirs(result_path, exist_ok=True)

    fig, axs = plt.subplots(1, 3, figsize=(16.8, 6.0), sharey=True)
    
    for i, (dataset, label) in enumerate([['enron', '16'], ['github', '16'], ['patents', '16']]):
        time = np.loadtxt(f'{input_path}/overall/{dataset}_{label}_overall_scatter.csv', delimiter=',')
        gsi = time[:,[0,2]]
        cuts = time[:,[1,2]]
        gsi = gsi[np.max(gsi, axis=1) < 3599999]
        cuts = cuts[np.max(cuts, axis=1) < 3599999]

        axs[i].plot([1,1000000], [1, 1000000], color='grey', alpha=0.5)
        axs[i].scatter(cuts[:,0], cuts[:,1], color=color[1], facecolor='none', marker='o', s=180, label='vs CuTS')
        axs[i].scatter(gsi[:,0], gsi[:,1], color=color[0], facecolor='none', marker='^', s=240, label='vs GSI')
        axs[i].set_yscale('log')
        axs[i].set_xscale('log')
        axs[i].set_ylim(1, 1000000)
        axs[i].set_xlim(1, 1000000)
        axs[i].set_title(dataset.title(), fontsize=30)
        axs[i].grid()
        if i == 1: axs[i].set_xlabel(f'Query time of GSI/CuTS (ms)', fontsize=27)
        if i == 0: 
            axs[i].set_ylabel(f'Query time of EGSM (ms)', fontsize=27)
            axs[i].legend(facecolor='white', framealpha=0, ncol=1, loc=2, fontsize=27)
        axs[i].set_yticks([1,10,100,1000,10000,100000])
        axs[i].set_yticklabels(['$10^0$','$10^1$','$10^2$','$10^3$','$10^4$','$10^5$'])
        axs[i].set_xticks([1,10,100,1000,10000,100000])
        axs[i].set_xticklabels(['$10^0$','$10^1$','$10^2$','$10^3$','$10^4$','$10^5$'])
        axs[i].tick_params(labelsize=27)
        print(np.average(cuts[:,0]/cuts[:,1]))
        print(np.average(gsi[:,0]/gsi[:,1]))
        print(np.average(np.sum(cuts[:,0])/np.sum(cuts[:,1])))
        print(np.average(np.sum(gsi[:,0])/np.sum(gsi[:,1])))
    fig.tight_layout()


    #handles, labels = axs.get_legend_handles_labels()
    #fig.legend(handles, labels, facecolor='white', framealpha=0, ncol=10, bbox_to_anchor=(0.5, 1), loc=9, fontsize=27)
    #fig.tight_layout(rect=(0,0,1,0.9))

    fig.savefig(f'{result_path}/1-overall-scatter-combine.pdf')
    plt.close()
