# Capturing network packets

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > Capturing network packets
Capturing network packets

To troubleshoot and analyze the communication between the local production site and a primary or recovery server, you can choose to collect network packets on the VPN gateway or VPN appliance.

After collecting 32,000 network packets, or reaching time limit, capturing network packets stops, and the results are written in a .libpcap file that is added to the logs .zip archive.

The following table provides more information about the Capture network packets settings that you can configure.

Setting	Description
Network interface name	The network interface on which to capture network packets. If you want to capture network packets on all network interfaces, select Any.
Time limit (seconds)	The time limit for capturing network packets. The maximum value you can set is 1800.
Filtering

An extra filter to apply on the captured network packets.

You can enter a string containing protocols, ports, directions, and their combinations, separated by space, such as: "and", "or", "not", " ( ", " ) ", "src", "dst", "net", "host", "port", "ip", "tcp", "udp", "icmp", "arp", "esp".

If you want to use brackets, surround them with spaces. You can also enter IP addresses and network addresses, for example: "icmp or arp" and "port 67 or 68".

For more information about the values that you can enter, see the Linux tpcdump help.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.