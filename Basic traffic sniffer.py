# Ethernet Layer
if Ether in packet:
    eth_layer = packet[Ether]
    print(f"Ethernet: Source MAC: {eth_layer.src}, Destination MAC: {eth_layer.dst}")

# IP Layer
if IP in packet:
    ip_layer = packet[IP]
    print(f"IP: Source IP: {ip_layer.src}, Destination IP: {ip_layer.dst}")

    # ICMP Layer
    if ICMP in packet:
        icmp_layer = packet[ICMP]
        print(f"ICMP: Type: {icmp_layer.type}, Code: {icmp_layer.code}")

    # TCP Layer
    if TCP in packet:
        tcp_layer = packet[TCP]
        print(f"TCP: Source Port: {tcp_layer.sport}, Destination Port: {tcp_layer.dport}")

    # UDP Layer
    elif UDP in packet:
        udp_layer = packet[UDP]
        print(f"UDP: Source Port: {udp_layer.sport}, Destination Port: {udp_layer.dport}")

# ARP Layer
if ARP in packet:
    arp_layer = packet[ARP]
    print(f"ARP: Source IP: {arp_layer.psrc}, Destination IP: {arp_layer.pdst}, Source MAC: {arp_layer.hwsrc}, Destination MAC: {arp_layer.hwdst}")

# Print packet summary
print(packet.summary())