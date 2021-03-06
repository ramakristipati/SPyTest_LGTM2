from spytest.dicts import SpyTestDict
import random

def get_unique_random_list(list_length,range_start,range_end):
    list_item = set()
    while len(list(list_item)) < list_length:
        list_item.add(random.randint(range_start,range_end))
    return list(list_item)

def get_random_sequence_list(list_length):
    start_item = random.randint(2,4000)
    list_item =[item for item in range(start_item,start_item+list_length)]
    return list_item

def convert_mac_to_dot(mac):
    mac = mac.replace(":","")
    return (mac[0:4] + '.' + mac[4:8] + '.' + mac[8:12]).lower()

data = SpyTestDict()
data.testing ='VRRP'
vrrp_sessions = 4

vlan_list = get_random_sequence_list(list_length=vrrp_sessions+8)
vlan_intf_list = ['Vlan{}'.format(vlan_id) for vlan_id in vlan_list]

vrrp_vlans = vlan_list[0:vrrp_sessions]
dut1_uplink_vlans = vlan_list[vrrp_sessions:vrrp_sessions+2]
dut2_uplink_vlans = vlan_list[vrrp_sessions+2:vrrp_sessions+4]

vrrp_vlan_intf = vlan_intf_list[0:vrrp_sessions]
dut1_uplink_vlan_intf = vlan_intf_list[vrrp_sessions:vrrp_sessions+2]
dut2_uplink_vlan_intf = vlan_intf_list[vrrp_sessions+2:vrrp_sessions+4]

dut1_vlans = vrrp_vlans + dut1_uplink_vlans
dut2_vlans = vrrp_vlans + dut2_uplink_vlans
dut3_vlans = vrrp_vlans
dut4_vlans = vlan_list[vrrp_sessions:]

dut1_vlan_intf = vrrp_vlan_intf + dut1_uplink_vlan_intf
dut2_vlan_intf = vrrp_vlan_intf + dut2_uplink_vlan_intf
dut3_vlan_intf = vrrp_vlan_intf
dut4_vlan_intf = vlan_intf_list[vrrp_sessions:]


lag_id_list = get_unique_random_list(list_length=4,range_start=1,range_end=100)
lag_intf_list = ['PortChannel{}'.format(lag_id) for lag_id in lag_id_list]


#IP params
mask = '24'
mask_v6 = '64'
dut1_4_ip_list = ['14.14.{}.1'.format(i) for i in range(1,4)]
dut4_1_ip_list = ['14.14.{}.2'.format(i) for i in range(1,4)]
dut2_4_ip_list = ['24.24.{}.1'.format(i) for i in range(1,4)]
dut4_2_ip_list = ['24.24.{}.2'.format(i) for i in range(1,4)]

## Added for IPv6 address
dut1_4_ipv6_list = ['2001::1:1', '2002::2:1', '2003::3:1']
dut4_1_ipv6_list = ['2001::1:2', '2002::2:2', '2003::3:2']
dut2_4_ipv6_list = ['3001::1:1', '3002::2:1', '3003::3:1']
dut4_2_ipv6_list = ['3001::1:2', '3002::2:2', '3003::3:2']
dut1_2_ipv6_list = ['1001::1:1', '1002::2:1', '1003::3:1', '1004::4:1']
dut2_1_ipv6_list = ['1001::1:2', '1002::2:2', '1003::3:2', '1004::4:2']


tg_src_ipv6_list = ['1001::1:5', '1002::2:5', '1003::3:5', '1004::4:5']

dut4_tg_ipv6_list = ['1234::1:2', '3421::10:2', '5120::2:10', '7512::4:3']
tg_dest_ipv6_list = ['1234::1:3', '3421::10:3', '5120::2:3', '7512::4:10']
dut4_ipv6_route_list = ['1234::', '3421::', '5120::', '7512::']

vip_ipv6_list = ['1001::1:10', '1002::2:20', '1003::3:30', '1004::4:40']
ipv6_linklocal_ip_list = ['fe80::1:2', 'fe80::1:3', 'fe80::1:30']

vrrp_sec_ipv6_list = ['1001::1:56']
#VRRP params
vrid_list = get_unique_random_list(list_length=vrrp_sessions,range_start=1,range_end=50)
vrid_ipv6_list = get_unique_random_list(list_length=vrrp_sessions,range_start=51,range_end=100)
ip_octet_list = get_unique_random_list(list_length=vrrp_sessions,range_start=25,range_end=100)

vrrp_ip_list = []
vip_list = []
vrrp_sec_ip_list =[]
vrrp_ip_nw = []
for session  in range(vrrp_sessions):
    vrrp_ip_list.append(['{}.{}.{}.{}'.format(ip_octet_list[session],ip_octet_list[session],ip_octet_list[session],i) for i in range(1,4)])
    vip_list.append('{}.{}.{}.{}'.format(ip_octet_list[session],ip_octet_list[session],ip_octet_list[session],str(random.randint(5,150))))
    vrrp_sec_ip_list.append('{}.{}.{}.{}'.format(ip_octet_list[session],ip_octet_list[session],ip_octet_list[session],str(random.randint(193,194))))
    vrrp_ip_nw.append('{}.{}.{}.0'.format(ip_octet_list[session], ip_octet_list[session], ip_octet_list[session]))


vmac_list = ['00:00:5E:00:01:{}'.format(format(vrid,'02X')) for vrid in vrid_list]
vmac_ipv6_list = ['00:00:5E:00:02:{}'.format(format(vrid,'02X')) for vrid in vrid_ipv6_list]
vmac_list_1 = [convert_mac_to_dot(vmac) for vmac in vmac_list ]
vmac_ipv6_list_2 = [convert_mac_to_dot(vmac) for vmac in vmac_ipv6_list ]
vrrp_priority_list_dut1 = get_unique_random_list(vrrp_sessions/2,101,253) + get_unique_random_list(vrrp_sessions/2,1,99)
vrrp_priority_list_dut2 = get_unique_random_list(vrrp_sessions/2,1,99) + get_unique_random_list(vrrp_sessions/2,101,253)

#BGP params
dut1_as = '100'
dut1_router_id = '1.1.1.1'
dut2_as = '200'
dut2_router_id = '2.2.2.2'
dut4_as = '400'
dut4_router_id = '4.4.4.4'
peer_v4_1 = 'peer_v4_1'
peer_v4_2 = 'peer_v4_2'


dut4_route_list  = ["100.100.{}.0".format(i) for i in range(1,vrrp_sessions+1)]
dut4_tg_ip_list = ["100.100.{}.1".format(i) for i in range(1,vrrp_sessions+1)]
tg_src_ip_list = [vrrp_ip_list[session][2] for session in range(vrrp_sessions)]
tg_dest_ip_list = ["100.100.{}.2".format(i) for i in range(1,vrrp_sessions+1)]
tg_dest_mac_list = ["00:00:00:12:22:{}".format(format(i,'02X')) for i in range(1,vrrp_sessions+1)]
tg_dest_mac_ipv6_list = ["00:01:02:11:12:{}".format(format(i,'02X')) for i in range(1,vrrp_sessions+1)]
tg_src_mac_list = ["00:00:00:11:22:{}".format(format(i,'02X')) for i in range(1,vrrp_sessions+1)]
traffic_rate = 5000
tg2_src_mac = "00:00:00:44:44:44"
frame_size_bytes = 128
rate_threshold = 5.0
vrrp_vrf ='Vrf-RED'
trigger_list = random.sample(set(['fast_boot','config_reload']),1) +['docker_restart']


