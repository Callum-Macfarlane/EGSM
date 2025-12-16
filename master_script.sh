# remove previous experimental results

rm -rf results;
rm -rf datasets/dblp/label_16/results;
rm -rf datasets/enron/label_1/results;
rm -rf datasets/enron/label_4/results;
rm -rf datasets/enron/label_8/results;
rm -rf datasets/enron/label_16/results;
rm -rf datasets/enron/label_32/results;
rm -rf datasets/github/label_16/results;
rm -rf datasets/gowalla/label_16/results;
rm -rf datasets/patents/label_16/results;
rm -rf datasets/wikitalk/label_64/results;

# run experiments

## part 1
python3 experiments/1_run/run_gsi.py dblp 16 12;
python3 experiments/1_run/run_gsi.py enron 16 12;
python3 experiments/1_run/run_gsi.py github 16 12;
python3 experiments/1_run/run_gsi.py gowalla 16 12;
python3 experiments/1_run/run_gsi.py patents 16 12;
python3 experiments/1_run/run_gsi.py wikitalk 64 12;

python3 experiments/1_run/run_cuts.py dblp 16 12;
python3 experiments/1_run/run_cuts.py enron 16 12;
python3 experiments/1_run/run_cuts.py github 16 12;
python3 experiments/1_run/run_cuts.py gowalla 16 12;
python3 experiments/1_run/run_cuts.py patents 16 12;
python3 experiments/1_run/run_cuts.py wikitalk 64 12;

python3 experiments/1_run/run_ours.py dblp 16 12;
python3 experiments/1_run/run_ours.py enron 16 12;
python3 experiments/1_run/run_ours.py github 16 12;
python3 experiments/1_run/run_ours.py gowalla 16 12;
python3 experiments/1_run/run_ours.py patents 16 12;
python3 experiments/1_run/run_ours.py wikitalk 64 12;

## part 2
python3 experiments/1_run/run_ours_nof3.py dblp 16 12;
python3 experiments/1_run/run_ours_nof3.py enron 16 12;
python3 experiments/1_run/run_ours_nof3.py github 16 12;
python3 experiments/1_run/run_ours_nof3.py gowalla 16 12;
python3 experiments/1_run/run_ours_nof3.py patents 16 12;
python3 experiments/1_run/run_ours_nof3.py wikitalk 64 12;

## part 3
python3 experiments/1_run/run_ours_dfs.py dblp 16 12;
python3 experiments/1_run/run_ours_dfs.py enron 16 12;
python3 experiments/1_run/run_ours_dfs.py github 16 12;
python3 experiments/1_run/run_ours_dfs.py gowalla 16 12;
python3 experiments/1_run/run_ours_dfs.py patents 16 12;
python3 experiments/1_run/run_ours_dfs.py wikitalk 64 12;

python3 experiments/1_run/run_ours_bfs.py dblp 16 12;
python3 experiments/1_run/run_ours_bfs.py enron 16 12;
python3 experiments/1_run/run_ours_bfs.py github 16 12;
python3 experiments/1_run/run_ours_bfs.py gowalla 16 12;
python3 experiments/1_run/run_ours_bfs.py patents 16 12;
python3 experiments/1_run/run_ours_bfs.py wikitalk 64 12;

python3 experiments/1_run/run_ours_static.py dblp 16 12;
python3 experiments/1_run/run_ours_static.py enron 16 12;
python3 experiments/1_run/run_ours_static.py github 16 12;
python3 experiments/1_run/run_ours_static.py gowalla 16 12;
python3 experiments/1_run/run_ours_static.py patents 16 12;
python3 experiments/1_run/run_ours_static.py wikitalk 64 12;

python3 experiments/1_run/run_ours_nolb.py dblp 16 12;
python3 experiments/1_run/run_ours_nolb.py enron 16 12;
python3 experiments/1_run/run_ours_nolb.py github 16 12;
python3 experiments/1_run/run_ours_nolb.py gowalla 16 12;
python3 experiments/1_run/run_ours_nolb.py patents 16 12;
python3 experiments/1_run/run_ours_nolb.py wikitalk 64 12;

## part 4
python3 experiments/1_run/run_cuts.py enron 1 6;
python3 experiments/1_run/run_cuts.py enron 4 8;
python3 experiments/1_run/run_cuts.py enron 8 12;
python3 experiments/1_run/run_cuts.py enron 32 12;

python3 experiments/1_run/run_cuts.py enron 16 8;
python3 experiments/1_run/run_cuts.py enron 16 10;
python3 experiments/1_run/run_cuts.py enron 16 14;
python3 experiments/1_run/run_cuts.py enron 16 16;

python3 experiments/1_run/run_cuts.py enron 16 8-path;
python3 experiments/1_run/run_cuts.py enron 16 8-tree;
python3 experiments/1_run/run_cuts.py enron 16 8-cycle;
python3 experiments/1_run/run_cuts.py enron 16 8-dense;

# collect data

python3 experiments/2_collect/0-unsolved.py;
python3 experiments/2_collect/1-overall-scatter.py;
python3 experiments/2_collect/2-filtering-space.py;
python3 experiments/2_collect/2-filtering.py;
python3 experiments/2_collect/2-filtering-time.py;
python3 experiments/2_collect/3-filtering.py;
python3 experiments/2_collect/3-DFS.py;
python3 experiments/2_collect/3-BFS.py;
python3 experiments/2_collect/3-order.py;
python3 experiments/2_collect/3-load-balancing.py;
python3 experiments/2_collect/7-solved.py;
python3 experiments/2_collect/7-time.py;
python3 experiments/2_collect/8-solved.py;
python3 experiments/2_collect/8-time.py;
python3 experiments/2_collect/9-solved.py;
python3 experiments/2_collect/9-time.py;
python3 experiments/2_collect/10-num-results.py;

# draw figures

python3 experiments/3_draw/0-unsolved.py;
python3 experiments/3_draw/1-overall-scatter.py;
python3 experiments/3_draw/2-filtering-space.py;
python3 experiments/3_draw/2-filtering.py;
python3 experiments/3_draw/2-filtering-time.py;
python3 experiments/3_draw/3-filtering.py;
python3 experiments/3_draw/3-DFS.py;
python3 experiments/3_draw/3-BFS.py;
python3 experiments/3_draw/3-order.py;
python3 experiments/3_draw/3-load-balancing.py;
python3 experiments/3_draw/7-solved.py;
python3 experiments/3_draw/7-time.py;
python3 experiments/3_draw/8-solved.py;
python3 experiments/3_draw/8-time.py;
python3 experiments/3_draw/9-solved.py;
python3 experiments/3_draw/9-time.py;
python3 experiments/3_draw/10-num-results.py;
