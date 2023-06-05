import sys
import psutil
from scapy.all import *
from scapy.layers.inet import TCP,IP
import os

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
        self.protocols = ["tcp","ip","tcp port 80"]
        
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
    

    def tcp_packets(self,packet):
            """Processes and prints information about TCP packets.

            Args:
                packet: The packet to analyze.

            Returns:
                None
            """
            try:
                if TCP in packet:
                    src_ip = packet[IP].src
                    dst_ip = packet[IP].dst
                    sport = packet[TCP].sport
                    dport = packet[TCP].dport
                    packet_length = len(packet)
                    ttl = packet[IP].ttl
                    protocol = packet[IP].proto
                print(f"packet length: {packet_length} /|\ source: {src_ip} /|\ destination: {dst_ip} /|\ source port:{sport} /|\ destination port:{dport} /|\ time to live :{ttl} /|\ protocol :{protocol}")
            except KeyboardInterrupt:
                os.system("cls")

        
    def ip_packets(self,packet):
            """Processes and prints information about IP packets.

            Args:
                packet: The packet to analyze.

            Returns:
                None
            """
            try:
                if IP in packet:
                    src_ip = packet[IP].src
                    dst_ip = packet[IP].dst
                    sport = packet[IP].sport
                    dport = packet[IP].dport
                    packet_length = len(packet)
                    ttl = packet[IP].ttl
                    protocol = packet[IP].proto
                print(f"packet length: {packet_length} /|\ source: {src_ip} /|\ destination: {dst_ip} /|\ source port:{sport} /|\ destination port:{dport} /|\ time to live :{ttl} /|\ protocol :{protocol}")
            except KeyboardInterrupt:
                os.system("cls")
                

    def http_packets(self,packet):
            """Processes and prints information about HTTP packets.

            Args:
                packet: The packet to analyze.

            Returns:
                None
            """
            try:
                if TCP in packet and (packet[TCP].dport == 80 or packet[TCP].dport == 8080):
                    src_ip = packet[IP].src
                    dst_ip = packet[IP].dst
                    sport = packet[TCP].sport
                    dport = packet[TCP].dport
                    packet_length = len(packet)
                    ttl = packet[IP].ttl
                    protocol = packet[IP].proto
                print(f"packet length: {packet_length} /|\ source: {src_ip} /|\ destination: {dst_ip} /|\ source port:{sport} /|\ destination port:{dport} /|\ time to live :{ttl} /|\ protocol :{protocol}")
            except KeyboardInterrupt:
                os.system("cls")
                



    def capture_packets(self,packet_type="tcp"):
            """Captures packets based on the specified packet type.

            Args:
                packet_type: The type of packets to capture (default is "tcp").

            Returns:
                None
            """
            try:
                if(packet_type == "tcp"):
                    sniff(filter=packet_type, prn=self.tcp_packets, count=sys.maxsize)
                if(packet_type == "ip"):
                    sniff(filter=packet_type, prn=self.ip_packets, count=sys.maxsize)
                if(packet_type == "tcp port 80"):
                    sniff(filter=packet_type, prn=self.http_packets,count=sys.maxsize)
            except KeyboardInterrupt:
                 os.system("cls")