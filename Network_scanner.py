#!/usr/bin/env python

import scapy.all as scapy
import optparse

def get_arg():
    parser = optparse.OptionParser()
    parser.add_option("-t","--target",dest="target",help="This is for scanning the network for given target ip ")
    (options , arguments ) = parser.parse_args()
    return options.target

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

get_target = get_arg()
scan_result = scan(get_target)
print_result(scan_result)




# arp_req.pdst = ip  // We do not need right now because i already use in upper line of code
# broadcast.dst = "" // This code is optional because i already used in upper line
# scapy.ls(scapy.Ether())  // This line is for listing Ether option to use
# scapy.ls(scapy.ARP()) // This line is for listing what we need to scan , so we run this shit
