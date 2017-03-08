#
# CONST
# ETHERNET_CTRL = 20 # bytes: preamble(7) + SFD(1) + IFG (12)
#
'''
The catalogue of ASICs, currently represents a few basic Broadcom chips.
Every item contains two numbers: switching capacity in Mbps and forwarding capacity in Mpps.
'asicName': ( full duplex sys-throughtput Mbps, fw-capacity Mpps )
Add your own to figure out above which packet size linerate is possible.
'''
asics = {
    #'custom': ( 0, 0 ),
    #'Mellanox Spectrum': ( 6400, 4770 ),
    'Helix4 BCM56340': ( 256, 191),
    'Helix4 BCM56342': ( 208, 156 ),
    'Trident+ BCM56846': ( 1280, 960 ),
    'Trident II BCM56850': ( 2560, 1440 ),
    'Trident II BCM56854': ( 1440, 1000 ),
    'Trident II+ BCM56864': ( 2560, 1000 ),
    'Tomahawk BCM56960': ( 6400, 4400 )
}
#
def linerateEdge(asicName):
    '''
    The function to iterate thru packet sizes and check if the amount of packets
    with size in bytes fits in available switching capacity.
    :param asicName: a name of a list with capacity values
    :return: string with an edge value for packet size
    '''
    throughtput_bytes = (asics.get(asicName)[0] * 1024 * 1024 * 1024) / 8
    fw_capacity_flat = (asics.get(asicName)[1] * 1024 * 1024)
    for size in reversed(range(64,512)):
        #print('Current packet size is {}'.format(size))
        if throughtput_bytes / size >= fw_capacity_flat:
        #if size * fw_capacity_flat <= throughtput_bytes:
            a = asicName.center(22, ' ')
            b = str(asics.get(asicName)[0]).center(4, ' ')
            c = str(asics.get(asicName)[1]).center(4, ' ')
            return '[{}] {} Mbps / {} Mpps | Linerate if packet size is higher than {}'.format(a, b, c, size)
    return 'Linerate even at 64 bytes packet size'
#
if __name__ == "__main__":
    for asic in asics:
            print(linerateEdge(asic))
    #print(calc('custom'))
#
#  EOF