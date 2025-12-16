import os
import numpy as np
import matplotlib.pyplot as plt
from palettable.colorbrewer.qualitative import Dark2_8

color = Dark2_8.mpl_colors

if __name__ == '__main__':
    input_path = 'results/csv/ablation'

    result_path = 'results/figs'
    os.makedirs(result_path, exist_ok=True)

    time_dblp = np.loadtxt(f'{input_path}/dblp_16_dfs.csv', delimiter=',')
    time_enron = np.loadtxt(f'{input_path}/enron_16_dfs.csv', delimiter=',')
    time_github = np.loadtxt(f'{input_path}/github_16_dfs.csv', delimiter=',')
    time_gowalla = np.loadtxt(f'{input_path}/gowalla_16_dfs.csv', delimiter=',')
    time_patents = np.loadtxt(f'{input_path}/patents_16_dfs.csv', delimiter=',')
    time_wikitalk = np.loadtxt(f'{input_path}/wikitalk_64_dfs.csv', delimiter=',')

    time_dblp = time_dblp[np.max(time_dblp, axis=1) < 3599999]
    time_enron = time_enron[np.max(time_enron, axis=1) < 3599999]
    time_github = time_github[np.max(time_github, axis=1) < 3599999]
    time_gowalla = time_gowalla[np.max(time_gowalla, axis=1) < 3599999]
    time_patents = time_patents[np.max(time_patents, axis=1) < 3599999]
    time_wikitalk = time_wikitalk[np.max(time_wikitalk, axis=1) < 3599999]

    time_dblp = time_dblp[np.min(time_dblp, axis=1) > 0]
    time_enron = time_enron[np.min(time_enron, axis=1) > 0]
    time_github = time_github[np.min(time_github, axis=1) > 0]
    time_gowalla = time_gowalla[np.min(time_gowalla, axis=1) > 0]
    time_patents = time_patents[np.min(time_patents, axis=1) > 0]
    time_wikitalk = time_wikitalk[np.min(time_wikitalk, axis=1) > 0]

    dfs_lb_time = [
        np.average(time_dblp, axis=0)[0],
        np.average(time_enron, axis=0)[0],
        np.average(time_github, axis=0)[0],
        np.average(time_gowalla, axis=0)[0],
        np.average(time_patents, axis=0)[0],
        np.average(time_wikitalk, axis=0)[0]
    ]

    bfs_dfs_time = [
        np.average(time_dblp, axis=0)[1],
        np.average(time_enron, axis=0)[1],
        np.average(time_github, axis=0)[1],
        np.average(time_gowalla, axis=0)[1],
        np.average(time_patents, axis=0)[1],
        np.average(time_wikitalk, axis=0)[1]
    ]

    speedup = [
        np.average(time_dblp[:,0] / time_dblp[:,1]),
        np.average(time_enron[:,0] / time_enron[:,1]),
        np.average(time_github[:,0] / time_github[:,1]),
        np.average(time_gowalla[:,0] / time_gowalla[:,1]),
        np.average(time_patents[:,0] / time_patents[:,1]),
        np.average(time_wikitalk[:,0] / time_wikitalk[:,1])
    ]

    print(speedup)
