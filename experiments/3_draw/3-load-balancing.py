import os
import numpy as np
import matplotlib.pyplot as plt
from palettable.colorbrewer.qualitative import Dark2_8

color = Dark2_8.mpl_colors

if __name__ == '__main__':
    input_path = 'results/csv/ablation'

    result_path = 'results/figs'
    os.makedirs(result_path, exist_ok=True)

    time_dblp = np.loadtxt(f'{input_path}/dblp_16_lb.csv', delimiter=',')
    time_enron = np.loadtxt(f'{input_path}/enron_16_lb.csv', delimiter=',')
    time_github = np.loadtxt(f'{input_path}/github_16_lb.csv', delimiter=',')
    time_gowalla = np.loadtxt(f'{input_path}/gowalla_16_lb.csv', delimiter=',')
    time_patents = np.loadtxt(f'{input_path}/patents_16_lb.csv', delimiter=',')
    time_wikitalk = np.loadtxt(f'{input_path}/wikitalk_64_lb.csv', delimiter=',')

    time_dblp = time_dblp[[36, 71, 93]]
    time_enron = time_enron[[13, 18]]
    time_github = time_github[[77]]
    time_gowalla = time_gowalla[[12, 28, 52, 56, 61, 77, 79]]
    time_patents = time_patents[[33]]

    nolb_time = [
        np.average(time_dblp, axis=0)[0],
        np.average(time_enron, axis=0)[0],
        np.average(time_github, axis=0)[0],
        np.average(time_gowalla, axis=0)[0],
        np.average(time_patents, axis=0)[0],
        np.average(time_wikitalk, axis=0)[0]
    ]

    lb_time = [
        np.average(time_dblp, axis=0)[1],
        np.average(time_enron, axis=0)[1],
        np.average(time_github, axis=0)[1],
        np.average(time_gowalla, axis=0)[1],
        np.average(time_patents, axis=0)[1],
        np.average(time_wikitalk, axis=0)[1]
    ]

    speedup = [
        np.average(np.sum(time_dblp[:,0]) / np.sum(time_dblp[:,1])),
        np.average(np.sum(time_enron[:,0]) / np.sum(time_enron[:,1])),
        np.average(np.sum(time_github[:,0]) / np.sum(time_github[:,1])),
        np.average(np.sum(time_gowalla[:,0]) / np.sum(time_gowalla[:,1])),
        np.average(np.sum(time_patents[:,0]) / np.sum(time_patents[:,1])),
        np.average(np.sum(time_wikitalk[:,0]) / np.sum(time_wikitalk[:,1]))
    ]

    print(speedup)
