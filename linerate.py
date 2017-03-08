#
# CONST
ETHERNET_CTRL = 20 # bytes: preamble(7) + SFD(1) + IFG (12)
#
'''
The catalogue of ASICs, currently represents a few basic Broadcom chips.
Every item contains two numbers: switching capacity in Mbps and forwarding capacity in Mpps.
'asicName': ( sw-capacity Mbps, fw-capacity Mpps )
Add your own to figure out above which packet size linerate is possible.
'''
asics = {
    #'custom': ( 0, 0 ),
    'Helix4 BCM56340': ( 128, 191),
    'Helix4 BCM56342': ( 104, 156 ),
    'Trident+ BCM56846': ( 640, 960 ),
    'Trident II BCM56850': ( 1280, 1440 ),
    'Trident II BCM56854': ( 720, 1000 ),
    'Trident II+ BCM56864': ( 1280, 1000 ),
    'Tomahawk BCM56960': ( 3200, 4700 )
}
#
def calc(asicName):
    '''
    The function to iterate thru packet sizes and check if the amount of packets
    with size in bytes fits in available switching capacity.
    :param asicName: a name of a list with capacity values
    :return: string with an edge value for packet size
    '''
    sw_capacity_bytes = (asics.get(asicName)[0] * 1024 * 1024 * 1024) / 8
    fw_capacity_flat = (asics.get(asicName)[1] * 1024 * 1024)
    for size in reversed(range(64,257)):
        #print('Current packet size is {}'.format(size))
        if sw_capacity_bytes / size >= fw_capacity_flat:
            a = asicName.center(22, ' ')
            b = str(asics.get(asicName)[0]).center(4, ' ')
            c = str(asics.get(asicName)[1]).center(4, ' ')
            return '[{}] {} Mbps / {} Mpps | Linerate if packet size is higher than {}'.format(a, b, c, size)
    return 'Something went wrong'
#
if __name__ == "__main__":
    for asic in asics:
            print(calc(asic))
    #print(calc('custom'))
#
#  EOF