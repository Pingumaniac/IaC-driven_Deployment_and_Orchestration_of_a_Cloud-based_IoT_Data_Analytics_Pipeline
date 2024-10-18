import numpy as np
import matplotlib.pyplot as plt

def read_latencies(file_path):
    with open(file_path, 'r') as f:
        latencies = [float(line.strip()) for line in f]
    return np.array(latencies)

log_files = {
    1: 'latency_vm1.log',
    2: 'latency_vm2.log',
    3: 'latency_vm3.log',
    4: 'latency_vm4.log'
}

latencies = {}

for num_producers, file_path in log_files.items():
    latencies[num_producers] = read_latencies(file_path)

def plot_cdf(latencies, num_producers):
    sorted_latencies = np.sort(latencies)
    cdf = np.arange(1, len(sorted_latencies) + 1) / len(sorted_latencies)
    
    plt.plot(sorted_latencies, cdf, label=f'{num_producers} Producers')
    plt.xlabel('Latency (seconds)')
    plt.ylabel('CDF')
    plt.title('CDF of Latency')
    plt.legend()

plt.figure()
for num_producers, latency_data in latencies.items():
    plot_cdf(latency_data, num_producers)
plt.grid(True)
plt.savefig('latency_cdf.png')

percentiles = {}
for num_producers, latency_data in latencies.items():
    percentiles[num_producers] = {
        '90th': np.percentile(latency_data, 90),
        '95th': np.percentile(latency_data, 95)
    }

for num_producers, values in percentiles.items():
    print(f'{num_producers} Producers: 90th Percentile = {values["90th"]}s, 95th Percentile = {values["95th"]}s')
