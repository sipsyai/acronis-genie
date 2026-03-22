# Network settings

Managing the backup and recovery of workloads and files > Creating bootable media to recover operating systems > Bootable Media Builder > Network settings
Network settings

While creating bootable media, you can preconfigure the network connections that will be used by the bootable agent. The following parameters can be preconfigured:

IP address
Subnet mask
Gateway
DNS server
WINS server

After the bootable agent starts on a machine, the configuration is applied to the machine’s network interface card (NIC). If the settings have not been preconfigured, the agent uses DHCP auto configuration.

You can also configure the network settings manually when the bootable agent is running on the machine.

Preconfiguring multiple network connections

You can preconfigure TCP/IP settings for up to ten network interface cards (NICs). To ensure that each NIC will be assigned the appropriate settings, create the media on the server for which the media is customized. When you select an existing NIC in the wizard window, its settings are selected and saved on the media. The MAC address of each existing NIC is also saved on the media.

You can change the settings, except for the MAC address, or configure the settings for a non-existent NIC.

After the bootable agent starts on the server, it retrieves the list of available NICs. This list is sorted by the slots that the NICs occupy, the closest to the processor is on top.

The bootable agent assigns each known NIC the appropriate settings, and identifies the NICs by their MAC addresses. After the NICs with known MAC addresses are configured, the remaining NICs are assigned the settings that you made for non-existent NICs, starting from the upper non-assigned NIC.

You can customize the bootable media for any machine, and not only for the machine where the media is created. To do so, configure the NICs according to their slot order on that machine: NIC1 occupies the slot closest to the processor, NIC2 is in the next slot, and so on. When the bootable agent starts on that machine, it will not find the NICs with known MAC addresses and will configure the NICs in the same order as you did.

Example

The bootable agent can use one of the network adapters for communication with the management console through the production network. Automatic configuration can be done for this connection. Sizeable data for recovery can be transferred through the second NIC, included in the dedicated backup network by means of static TCP/IP settings.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.