Common Address Redundancy Protocol (**CARP**) sample


Packet format:

| field# | bits | Description |
|--------|------|-----------------|
| version | 4 | The version of the CARP protocol.This is statically defined as 2 in the header file `/usr/src/netinet/ip_carp.h`. |
|type|4|The type field defines the type of CARP packet. This value can be 0x01 (advertisement) or 0x02 (leave group), but the latter is only defined in the header file; I have not seen it being used anywhere.|
|vhid|8|Virtual host id.|
|advskew|8|Advertisement skew.|
|authlen|8|Size of Counter field + md field in 32 bit chunks.Statically defined as 7 in the header file.|
|Pad1|8|Unused, must be 0.|
|advbase|8|Advertisement interval.|
|cksum|16|Checksum for Internet Protocol family headers.|
|counter|64|Two counters used for replay detection.(not implemented yet)|
|Md|160|SHA-1 HMAC generated with the passparameter as secret key, and counter, version, type, vhid, and virtual IP address as the message digest|

read more at https://www.giac.org/paper/gsec/4031/carp-free-fail-over-protocol/106433


Configuration:

VHID: 1
Advbase: 1
Advskew: 1
Virtual IP: 192.168.88.44/24
Password: pass123


ifconfig output:
```
vtnet0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> metric 0 mtu 1500
	description: LAN
	options=800b8<VLAN_MTU,VLAN_HWTAGGING,JUMBO_MTU,VLAN_HWCSUM,LINKSTATE>
	ether d2:e4:71:c1:5e:0a
	inet6 fe80::d0e4:71ff:fec1:5e0a%vtnet0 prefixlen 64 scopeid 0x1
	inet 192.168.88.100 netmask 0xffffff00 broadcast 192.168.88.255
	inet 192.168.88.44 netmask 0xffffff00 broadcast 192.168.88.255 vhid 1
	carp: MASTER vhid 1 advbase 1 advskew 0
	media: Ethernet 10Gbase-T <full-duplex>
	status: active
	nd6 options=21<PERFORMNUD,AUTO_LINKLOCAL>
```

Wireshark:
```
Frame 1: 70 bytes on wire (560 bits), 70 bytes captured (560 bits)
Ethernet II, Src: IETF-VRRP-VRID_01 (00:00:5e:00:01:01), Dst: IPv4mcast_12 (01:00:5e:00:00:12)
Internet Protocol Version 4, Src: 192.168.88.100, Dst: 224.0.0.18
Common Address Redundancy Protocol
    Version 2, Packet type 1 (Advertisement)
    Virtual Host ID: 1
    Advertisement Skew: 0
    Auth Len: 7
    Demotion indicator: 0
    Adver Int: 1
    Checksum: 0xcf0c [correct]
    [Checksum Status: Good]
    Counter: 15630591288068578258
    HMAC: db894a44db44e04954f8bae9401eb4059db6c977
```
