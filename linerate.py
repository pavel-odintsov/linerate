#
'''
The catalogue of ASICs, currently represents a few basic Broadcom chips.
Every item contains two numbers: switching capacity in Mbps and forwarding capacity in Mpps.
'asicName': ( sw-capacity Mbps, fw-capacity Mpps )
Add your own to figure out above which packet size linerate is possible.
'''
asics = {
    'helix4_40': ( 128, 191), # BCM56340
    'helix4_42': ( 104, 156 ), # BCM56342
    'trident_plus': ( 640, 960 ), # BCM56846
    'trident2_50': ( 1280, 1440 ), # BCM56850
    'trident2_54': ( 720, 1000 ), # BCM56854
    'trident2_plus': ( 1280, 1000 ), # BCM56864
    'tomahawk': ( 3200, 4700 ) # BCM56960
}
#
def calc(asicName):
    '''
    The function to iterate thru packet size and calculate if the amount of packets
    with size in bytes fits in available switching capacity, represented in bytes either.
    :param asicName: a name of a list with capacity values
    :return: string with an edge value for packet size
    '''
    sw_capacity_bytes = (asics.get(asicName)[0] * 1024 * 1024 * 1024) / 8
    fw_capacity_flat = (asics.get(asicName)[1] * 1024 * 1024)
    for i in reversed(range(64,257)):
        #print('Current packet size is {}'.format(i))
        if sw_capacity_bytes / i > fw_capacity_flat:
            return '{} | Linerate if packet size is higher than {}'.format(asicName, i)
    return 'Something went wrong'
#
if __name__ == "__main__":
    print(calc('helix4_40'))
    print(calc('helix4_42'))
    print(calc('trident_plus'))
    print(calc('trident2_50'))
    print(calc('trident2_54'))
    print(calc('trident2_plus'))
    print(calc('tomahawk'))
#
#  EOF