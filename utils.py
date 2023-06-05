import os
import time
from network_analyzer import NetworkAnalyzer
from graph import update

def bandwidth_monitoring() -> None:
    """Continuously monitors the bandwidth usage of the selected device and updates the graph.

    Returns:
        None
    """
    networkanalyzer = NetworkAnalyzer()
    networkanalyzer.choose_device()
    os.system("cls")
    print(f"current device: {networkanalyzer.current_device}")
    while(True):
        try:
            output = networkanalyzer.monitor_bandwidth_usage()
            update(output)
            print(output)
            time.sleep(0.5)
        except KeyboardInterrupt:
            os.system("cls")
            break

def sniff_packets()-> None:
    """Prompts the user to choose a protocol and captures packets based on the selected protocol.

    Returns:
        None
    """
    networkanalyzer = NetworkAnalyzer()
    os.system("cls")
    print("choose a protocol to capture packets from")
    for i,protocol in enumerate(networkanalyzer.protocols):
        print(f"{i+1}. {protocol}")
    index = int(input()) - 1
    choosen_protocol = networkanalyzer.protocols[index]
    networkanalyzer.capture_packets(choosen_protocol)


def menu() -> None:
    """Displays a menu with options to perform network analysis tasks.

    Returns:
        None
    """
    while True:
        print("------------------------------------------------------------------------------------------------------")
        print("|                                                                                                    |")
        print("| 1)Bandwidth Monitoring                                                                             |")
        print("| 2)Packet Sniffing                                                                                  |")
        print("| 3)Quit                                                                                             |")
        print("|                                                                                                    |")
        print("------------------------------------------------------------------------------------------------------")
        x = input()
        x = int(x)
        if(x == 1):
            os.system("cls")
            print("these are the devices that can potentially use band. choose one to monitor")
            bandwidth_monitoring()

        elif(x == 2):
            os.system("cls")
            sniff_packets()

        elif(x == 3):
            os.system("cls")
            break

        else:
            os.system("cls")
            print("invalid input")