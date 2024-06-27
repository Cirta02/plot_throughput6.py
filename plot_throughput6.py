import matplotlib.pyplot as plt

def read_results(file_path):
    nodes = [5,10,20,25,30]
    throughputs = [0.16,0.08,0.04,0.032,0.026]

    with open(file_path, 'r') as file:
        next(file)  # Skip header line
        for line in file:
            parts = line.split()
            # Ignore lines that do not contain exactly two elements (number of nodes and throughput)
            if len(parts) != 2:
                continue
            try:
                nodes.append(int(parts[0]))
                throughputs.append(float(parts[1]))
            except ValueError:
                continue

    return nodes, throughputs

def plot_throughput(nodes, throughputs):
    plt.figure(figsize=(10, 6))
    plt.plot(nodes, throughputs, marker='o', linestyle='-', color='b', label='Débit moyen par nœud')

    plt.xlabel('Nombre de nœuds')
    plt.ylabel('Débit moyen par nœud (Mbps)')
    plt.title('Débit moyen par nœud en fonction du nombre de nœuds avec mobilité')
    plt.legend()
    plt.grid(True)
    plt.savefig('throughput_plot_with_mobility.png')  # Save the plot as a PNG file
    plt.show()

if __name__ == '__main__':
    file_path = 'throughput_results6.txt'  # Adjust this to match your NS-3 output file path
    nodes, throughputs = read_results(file_path)
    plot_throughput(nodes, throughputs)

