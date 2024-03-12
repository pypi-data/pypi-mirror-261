from ipaddress import IPv4Address, IPv4Network


def net_offset(parent: IPv4Network, child: IPv4Network) -> int:
    return (int(child.network_address) - int(parent.network_address)) >> (32 - child.prefixlen)


def offset_net(parent: IPv4Network, offset: int, prefix: int) -> IPv4Network:
    return IPv4Network(f"{IPv4Address(int(parent.network_address) + (offset << (32-prefix)))}/{prefix}")


def addr_offset(parent: IPv4Network, child: IPv4Address) -> int:
    return int(child) - int(parent.network_address)


def offset_addr(parent: IPv4Network, offset: int) -> IPv4Address:
    return IPv4Address(int(parent.network_address) + offset)
