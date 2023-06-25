from http import client
from pydoc import cli
import scapy.all as scapy


def scan(ip):
    # scapy obj has properties like: summary, show, scapy.ls(scapy.ARP())

    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast / arp_req
    
    ans = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]

    # Parsing getting ip and mac h/w 
    client_list = []
    # print("IP\t\t\t\tMAC Addrs\n------------------------------------------")
    for ele in ans:
        client_list.append({"ip": ele[1].psrc, "mac": ele[1].hwdst})
        # print(ele[1].psrc, end="\t\t")
        # print(ele[1].hwdst, "\n")
        # print('-------------------------------------------')
    print(client_list)

    # scapy.arping(ip)


scan("192.168.203.1/24")
