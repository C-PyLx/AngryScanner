#__Author__: Learning :~#
#Fast & powerful python port scanner

import os
import sys
import time
import socket
import datetime
import argparse

class color:
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Bold = '\033[1m'
    End = '\033[0m'

def portScanner(server, minPort, maxPort):
    os.system('clear')
    if minPort > maxPort:
        print (color.Red + '[!] Minimum port must be smaller than maximum port !', color.End)
        sys.exit()

    print (color.Blue + color.Bold + '[~] Program started at: ~> %s <~\n' %time.strftime('%H:%M:%S'), color.End )
    print (color.Blue + color.Bold + '[~] Host entry ip address: ~> %s <~' %socket.gethostbyname(server))
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = socket.gethostbyname(server)
    time_1 = datetime.datetime.now()
    sys.stdout.write(color.Green + '\r[+] Scanning on ports: ~> %d : %d <~\n' %(minPort, maxPort)+color.End)

    for currentPort in range(minPort, maxPort+1):
        result = connection.connect_ex((server, currentPort))
        if result == 0:
            sys.stdout.write(color.Green + '\r\n[~] Port: ~> %d <~ on server ~> %s <~ [Open].' %(currentPort, server)+color.End )
        else:
            sys.stdout.write(color.Red + '\r\n[!] Port: ~> %d <~ on server ~> %s <~ [Close].\n' %(currentPort, server)+color.End )

    time_2 = datetime.datetime.now()
    time_3 = time_2 - time_1
    print (color.Blue + color.Bold + '\n[+] Scan completed successfully.\n', color.End)
    print (color.Blue + color.Bold + '[>] Time elapsed ~> %s <~' %time_3, color.End)
    print (color.Blue + color.Bold + '[>] Now time ~> %s <~\n' %time.strftime('%H:%M:%S'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    formatter_class=argparse.RawTextHelpFormatter,
    description='--> Python Port Scanner Fasten & Powerfull. <--',
    usage='\033[91mpython AngryScanner.py -host [IP] -min [min port] -max [max port]\033[0m')

    parser.add_argument('-host', '--host_ip',
    default=None, help='Server ip or web address')

    parser.add_argument('-min', '--min_port',
    type=int, default=21, help='Minimum port number for scan')

    parser.add_argument('-max', '--max_port', 
    type=int, default=23, help='Maximum port number for scan')

    args = parser.parse_args()
    if args.host_ip == None:
        args.host_ip = 'localhost'

    try:
        portScanner(args.host_ip, args.min_port, args.max_port)
    except socket.error:
        print (color.Red + '[!] Check your internet connection !', color.End)
    except socket.gaierror:
        print (color.Red + '[!] Can not find host or service !', color.End)
    #except TypeError:
        #print (color.Red + '[!] This type not recommended !', color.End)
    except NameError:
        print (color.Red + '[!] This name was not defined !', color.End)
    except KeyboardInterrupt:
        print (color.Red + color.Bold + '\n[!] Shutting down service...', color.End)
        time.sleep(2)
        sys.exit(1)