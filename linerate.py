#
# IMPORT
from collections import namedtuple
#
# CONST
#ETHERNET_CTRL = 20 # bytes: preamble(7) + SFD(1) + IFG (12)
#
'''
The catalogue of ASICs, currently represents a few basic Broadcom chips.
Every item contains two numbers: switching capacity in Gbps and forwarding capacity in Mpps.
'asicName': ( full duplex sys-throughtput Gbps, fw-capacity Mpps )
Add your own to figure out above which packet size linerate is possible.
'''
values = namedtuple('Asic', 'sys_throughtput fw_capacity')
asics = {
    #'custom': value( 0, 0 ),
    #'Mellanox Spectrum': value( 6400, 4770 ),
    'Helix4 BCM56340': values( 256, 191),
    'Helix4 BCM56342': values( 208, 156 ),
    'Trident+ BCM56846': values( 1280, 960 ),
    'Trident II BCM56850': values( 2560, 1440 ),
    'Trident II BCM56854': values( 1440, 1000 ),
    'Trident II+ BCM56864': values( 2560, 1000 ),
    'Tomahawk BCM56960': values( 6400, 4400 )
}
#
def linerate_edge(asic_name):
    '''
    The function to iterate thru packet sizes and check if the amount of packets
    with size in bytes fits in available switching capacity.
    :param asic_name: a name of a list with capacity values
    :return: string with an edge value for packet size
    '''
    sys_throughtput_bytes = (asics[asic_name].sys_throughtput * (10 ** 9)) / 8
    fw_capacity_flat = (asics[asic_name].fw_capacity * (10 ** 6))
    for size in range(512, 64, -1):
        if sys_throughtput_bytes / size >= fw_capacity_flat:
        #if size * fw_capacity_flat <= sys_throughtput_bytes:
            return '[{:^25}] {:^4} Gbps / {:^5} Mpps | Linerate if packet size is higher than {}'\
                .format(asic_name, asics[asic_name].sys_throughtput, asics[asic_name].fw_capacity, size)
    return 'Linerate even at 64 bytes packet size'
#
if __name__ == "__main__":
    for asic in asics:
        print(linerate_edge(asic))
    #print(calc('custom'))
#
#  EOF