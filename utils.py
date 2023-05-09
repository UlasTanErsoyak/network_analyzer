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
    while True:
        output = networkanalyzer.monitor_bandwidth_usage()
        update(output)
        print(output)
        time.sleep(1)

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
            pass

        elif(x == 3):
            break

        else:
            os.system("cls")
            print("invalid input")