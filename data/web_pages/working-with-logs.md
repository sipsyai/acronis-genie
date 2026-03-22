# Working with logs

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > Working with logs
Working with logs

Disaster Recovery collects logs for the VPN appliance and the VPN gateway. The logs are saved as .txt files, which are compressed in a .zip archive. You can download and extract the archive, and use the information for troubleshooting or monitoring purposes.

The following list describes the log files that are part of the .zip archive, and the information that they contain.

dnsmasq.config.txt - The file contains information about the configuration of the service that provides DNS and DHCP addresses.

dnsmasq.leases.txt - The file contains information about the current DHCP address leases.

dnsmasq_log.txt - The file contains logs of the dnsmasq service.

ebtables.txt - The file contains information about the firewall tables.

free.txt - The file contains information about the free memory.

ip.txt - The file contains the logs from the configuration of the network interfaces, including their names which can be used in the configuration of the Capturing network packets settings.

NetworkManager_log.txt - The file contains logs from the NetworkManager service.

NetworkManager_status.txt - The file contains information about the status of the NetworkManager service.

openvpn@p2s_log.txt - The file contains logs from the OpenVPN service.

openvpn@p2s_status.txt - The file contains information about the status of the VPN tunnels.

ps.txt - The file contains information about the currently running processes on the VPN gateway or VPN appliance.

resolf.conf.txt - The file contains information about the configuration of the DNS servers.

routes.txt - The file contains information about the networking routes.

uname.txt - The file contains information about the current version of the kernel of the operating system.

uptime.txt - The file contains information about the length of period for which the operating system has not been restarted.

vpnserver_log.txt - The file contains logs from the VPN service.

vpnserver_status.txt - The file contains information about the status of the VPN server.

For more information about log files that are specific to the IPsec VPN connectivity, see Multi-site IPSec VPN log files.

Downloading the logs of the VPN appliance

Downloading the logs of the VPN gateway

Capturing network packets

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.