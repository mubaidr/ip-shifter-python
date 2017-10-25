''' IP scheduler '''

import sys
import time

# Import utility functions
UTILITIES = __import__('util')


def start(nic_index):
    ''' Starting the IP shifting... '''

    counter = 0
    config = UTILITIES.get_config()
    ip_list = UTILITIES.prepare_ip_range(
        config['ip']['start'], config['ip']['end'])

    while True:
        ip_address = ip_list[counter]
        set_ip_address(nic_index, ip_address, config)
        print('IP Address: {}\n'.format(ip_address))
        time.sleep(config['timeout'])
        if UTILITIES.is_connected():
            print('Connection seems good, waiting... \n')
            time.sleep(config['delay'])

        counter += 1
        if counter == len(ip_list):
            counter = 0


def set_ip_address(nic_index, ip_address, cfg):
    ''' Initialize ip shifting mechanism on provided NIC '''

    nics = UTILITIES.get_nic_list()
    nic = nics[nic_index]

    try:
        nic.EnableStatic(IPAddress=[ip_address],
                         SubnetMask=[cfg['subnet']])
        nic.SetGateways(DefaultIPGateway=[cfg['gateway']])
    except:
        print('Doh... Some unexpected error occured!')
        sys.exit(0)
