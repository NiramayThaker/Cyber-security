import subprocess
import optparse
import re


def mac_changer(interface, addrs):
    print(f"[+] Changeing MAC Adress for {interface} to {addrs}")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", addrs])
    subprocess.call(["ifconfig", interface, "up"])


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC")
    parser.add_option("-a", "--addrs", dest="addrs", help="It's New MAC Address")

    # (options, args) = parser.parse_args()
    return parser.parse_args()


def show_mac(interface):
    ifconfig_res = subprocess.check_output(["ifconfig", options.interface]).decode("utf-8")
    
    mac_addrs_search_res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_res)

    if mac_addrs_search_res:
        return str(mac_addrs_search_res.group(0))
    else:
        print("[-] Some error occured")    


if __name__ == "__main__":
    (options, args) = get_args()

    mac_changer(options.interface, options.addrs)

    curr_mac = show_mac(options.interface)

    if options.addrs == curr_mac:
        print("[-] MAC Changed successfully")
    else:
        print("[-] MAC didn't changed")
