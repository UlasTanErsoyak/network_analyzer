import os
import psutil

class NetworkAnalyzer():
    def __init__(self) -> None:
        """Initializes the NetworkAnalyzer class."""
        self.current_device = None
        self.previous_stats = {}
        self.bandwidth_usage ={
            'bytes_sent': 0,
            'bytes_recv': 0,
            'packets_sent': 0,
            'packets_recv': 0,
            'errin': 0,
            'errout': 0}
        
    def monitor_bandwidth_usage(self) -> dict[str, int]:
        """Monitors the bandwidth usage of the current device.

        Returns:
            A dictionary containing the bandwidth usage of the current device.
        """
        net_io_counters = psutil.net_io_counters(pernic=True)[self.current_device]
        current_stats = {
            'bytes_sent': net_io_counters.bytes_sent,
            'bytes_recv': net_io_counters.bytes_recv,
            'packets_sent': net_io_counters.packets_sent,
            'packets_recv': net_io_counters.packets_recv,
            'errin': net_io_counters.errin,
            'errout': net_io_counters.errout
        }
        
        if self.previous_stats:
            bandwidth_usage = {
                'bytes_sent': current_stats['bytes_sent'] - self.previous_stats['bytes_sent'],
                'bytes_recv': current_stats['bytes_recv'] - self.previous_stats['bytes_recv'],
                'packets_sent': current_stats['packets_sent'] - self.previous_stats['packets_sent'],
                'packets_recv': current_stats['packets_recv'] - self.previous_stats['packets_recv'],
                'errin': current_stats['errin'] - self.previous_stats['errin'],
                'errout': current_stats['errout'] - self.previous_stats['errout']
            }
        else:
            bandwidth_usage = {
                'bytes_sent': 0,
                'bytes_recv': 0,
                'packets_sent': 0,
                'packets_recv': 0,
                'errin': 0,
                'errout': 0
            }
        
        self.previous_stats = current_stats
        return bandwidth_usage


    def choose_device(self) -> None:
        """Prints a list of available network devices and allows the user to choose one."""
        devices = self.get_devices()
        for i,device in enumerate(devices):
            print(f"{i+1}. {device}")
        index = input()
        self.current_device = devices[int(index)-1]

    def get_devices(self) -> list[str]:
        """Gets a list of available network devices.

        Returns:
            A list of network device names.
        """
        net_io_counters = psutil.net_io_counters(pernic=True)
        devices = []
        for device in net_io_counters:
            devices.append(device)
        return list(devices)
    
    def capture_packets(self):
        pass