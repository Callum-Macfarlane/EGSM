import os, sys
from subprocess import Popen, PIPE, TimeoutExpired, check_output
import multiprocessing

def get_total_num_gpus():
    try:
        n = len(
            check_output(['nvidia-smi', '-L']).decode('utf-8').strip().split('\n'))
    except OSError:
        print("no GPU detected by 'nvidia-smi -L'")
        exit(-1)
    return n

def run_execution_time(dataset, label, size, algo_name, i):
    base_path = f'datasets/{dataset}/label_{label}'
    
    data_path = f'{base_path}/data_graph/ours.graph'
    
    query_base_path = f'{base_path}/query_graph/{size}/ours'
    result_path_base = f'{base_path}/results/{size}'

    os.makedirs(result_path_base, exist_ok=True)
    
    if os.path.exists(f'{result_path_base}/{i}_{algo_name}.txt') or \
        os.path.exists(f'{result_path_base}/{i}_{algo_name}.err') or \
        not os.path.exists(f'{query_base_path}/Q_{i}'):
        return
    p = Popen(['./build/EGSM',
        '-q', f'{query_base_path}/Q_{i}',
        '-d', data_path,
        '-m', 'BFS',
        '--gpu', str(multiprocessing.current_process()._identity[0] - 1)], 
        stdout=PIPE, stderr=PIPE)
    try:
        output, err = p.communicate(timeout=3600)
    except TimeoutExpired:
        p.kill()
        output, err = p.communicate()

    if not err and p.returncode == 0:
        print(f'finish-{i}-{algo_name}')
        with open(f'{result_path_base}/{i}_{algo_name}.txt', 'w') as f:
            f.write(output.decode())
    else:
        with open(f'{result_path_base}/{i}_{algo_name}.err', 'w') as f:
            f.write(output.decode() + '\n')
            f.write(f'return code: {p.returncode}\n')
            f.write(err.decode())
        print(f'{i}-{algo_name} **ERROR**')

if __name__ == '__main__':
    pool = multiprocessing.Pool(get_total_num_gpus())
    for i in range(100):
        pool.apply_async(run_execution_time, (sys.argv[1], sys.argv[2], sys.argv[3], 'ours-bfs', i))
    pool.close()
    pool.join()
