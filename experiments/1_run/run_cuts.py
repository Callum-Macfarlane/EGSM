import os, sys
from subprocess import Popen, PIPE, STDOUT

def run_execution_time(dataset, label, size, algo_name, i):
    base_path = f'datasets/{dataset}/label_{label}'
    
    data_path = f'{base_path}/data_graph/cuts.graph'
    
    query_base_path = f'{base_path}/query_graph/{size}/cuts'
    result_path_base = f'{base_path}/results/{size}'

    os.makedirs(result_path_base, exist_ok=True)
    
    if os.path.exists(f'{result_path_base}/{i}_{algo_name}.txt') or \
        os.path.exists(f'{result_path_base}/{i}_{algo_name}.err') or \
        not os.path.exists(f'{query_base_path}/Q_{i}'):
        return
    p = Popen(['../CuTS/build/cuts',
        data_path, f'{query_base_path}/Q_{i}'], 
        stdout=PIPE, stderr=STDOUT)
    output, err = p.communicate()

    if p.returncode == 0:
        print(f'finish-{i}-{algo_name}')
        with open(f'{result_path_base}/{i}_{algo_name}.txt', 'w') as f:
            f.write(output.decode())
    else:
        with open(f'{result_path_base}/{i}_{algo_name}.err', 'w') as f:
            f.write(output.decode() + '\n')
            f.write(f'return code: {p.returncode}\n')
            #f.write(err.decode())
        print(f'{i}-{algo_name} **ERROR**')

if __name__ == '__main__':
    for i in range(100):
        run_execution_time(sys.argv[1], sys.argv[2], sys.argv[3], 'cuts', i)
