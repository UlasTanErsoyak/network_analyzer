import matplotlib.pyplot as plt

fig, axs = plt.subplots(3, 2, figsize=(10, 10))

axs[0, 0].set_ylim(0, 50_000)
axs[0, 1].set_ylim(0, 50_000)
axs[1, 0].set_ylim(0, 100)
axs[1, 1].set_ylim(0, 100)
axs[2, 0].set_ylim(0, 10)
axs[2, 1].set_ylim(0, 10)

bytes_sent = []
bytes_recv = []
packets_sent = []
packets_recv = []
errin = []
errout = []

def update(bandwidth_usage) -> None :
    """Update the plot with the new bandwidth usage data.

    Args:
        bandwidth_usage (dict): A dictionary containing the new bandwidth usage data, with the following keys:
            - 'bytes_sent': int
            - 'bytes_recv': int
            - 'packets_sent': int
            - 'packets_recv': int
            - 'errin': int
            - 'errout': int

    Returns:
        None
    """
    bw = bandwidth_usage
    
    bytes_sent.append(bw['bytes_sent'])
    bytes_recv.append(bw['bytes_recv'])
    packets_sent.append(bw['packets_sent'])
    packets_recv.append(bw['packets_recv'])
    errin.append(bw['errin'])
    errout.append(bw['errout'])
    
    axs[0, 0].plot(bytes_sent[-100:], color='red')
    axs[0, 0].set_title('Bytes sent')
    axs[0, 1].plot(bytes_recv[-100:], color='blue')
    axs[0, 1].set_title('Bytes received')
    axs[1, 0].plot(packets_sent[-100:], color='green')
    axs[1, 0].set_title('Packets sent')
    axs[1, 1].plot(packets_recv[-100:], color='purple')
    axs[1, 1].set_title('Packets received')
    axs[2, 0].plot(errin[-100:], color='orange')
    axs[2, 0].set_title('Errors in')
    axs[2, 1].plot(errout[-100:], color='magenta')
    axs[2, 1].set_title('Errors out')
    
    plt.draw()
    plt.pause(0.1)

