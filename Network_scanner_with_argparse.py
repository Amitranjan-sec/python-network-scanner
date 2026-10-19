#!/usr/bin/env python

import scapy.all as scapy
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest="target",help = "we use this for target to scan inside a network")
    options = parser.parse_args()
    return options


def scan(ip):
    arp_req = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_req
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(client_result):
    print("IP\t\t\tMac address\t\n____________________________________")
    for client in client_result:
        print(client["ip"] + "\t\t" + client["mac"])
        
options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)




# arp_req.pdst = ip  // We do not need right now because i already use in upper line of code
# broadcast.dst = "" // This code is optional because i already used in upper line
# scapy.ls(scapy.Ether())  // This line is for listing Ether option to use
# scapy.ls(scapy.ARP()) // This line is for listing what we need to scan , so we run this shit
